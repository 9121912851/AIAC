import csv
import string
from datetime import datetime

# Define stopwords (a small sample, you can expand this)
STOPWORDS = set([
    'the', 'is', 'at', 'which', 'on', 'and', 'a', 'an', 'to', 'in', 'for', 'of', 'with', 'by', 'from', 'it', 'this', 'that'
])

def clean_text(text):
    # Remove punctuation and special symbols
    text = ''.join(ch for ch in text if ch.isalnum() or ch.isspace())
    # Remove stopwords
    words = text.lower().split()
    words = [w for w in words if w not in STOPWORDS]
    return ' '.join(words)

def parse_datetime(timestamp):
    # Extract hour and weekday from timestamp using datetime module
    try:
        dt = datetime.strptime(timestamp.strip(), '%Y-%m-%d %H:%M:%S')
        return dt.hour, dt.weekday()  # 0 = Monday, 6 = Sunday
    except Exception:
        return None, None

def is_spam(post_text):
    # Simple spam detection: repeated words or excessive length
    words = post_text.lower().split()
    total_words = len(words)
    unique_words = len(set(words))

    if total_words > 100:
        return True
    if total_words > 0 and unique_words / total_words < 0.5:
        return True
    return False

def read_and_clean_csv(filename):
    cleaned_data = []
    seen_posts = set()

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            post_text = row.get('post_text', '').strip()
            likes = row.get('likes', '').strip()
            shares = row.get('shares', '').strip()
            timestamp = row.get('timestamp', '').strip()

            # Handle missing values
            likes = int(likes) if likes.isdigit() else 0
            shares = int(shares) if shares.isdigit() else 0

            # Clean post text
            cleaned_post = clean_text(post_text)

            # Remove spam/duplicates
            post_key = cleaned_post
            if post_key in seen_posts or is_spam(cleaned_post):
                continue
            seen_posts.add(post_key)

            # Extract datetime features
            hour, weekday = parse_datetime(timestamp)

            cleaned_data.append({
                'post_text': cleaned_post,
                'likes': likes,
                'shares': shares,
                'hour': hour,
                'weekday': weekday
            })

    return cleaned_data

def main():
    filename = input("Enter CSV filename: ")
    cleaned = read_and_clean_csv(filename)

    # Output cleaned data
    output_file = 'cleaned_' + filename
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['post_text', 'likes', 'shares', 'hour', 'weekday']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in cleaned:
            writer.writerow(row)

    print(f"✅ Cleaned data written to: {output_file}")

if __name__ == "__main__":
    main()
