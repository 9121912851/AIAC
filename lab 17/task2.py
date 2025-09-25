import csv
import string
from datetime import datetime

# Stopwords (basic set)
STOPWORDS = set([
    'the', 'is', 'at', 'which', 'on', 'and', 'a', 'an', 'to',
    'in', 'for', 'of', 'with', 'by', 'from', 'it', 'this', 'that'
])

# Clean review text
def clean_text(text):
    text = ''.join(ch for ch in text if ch.isalnum() or ch.isspace())
    words = text.lower().split()
    return ' '.join(w for w in words if w not in STOPWORDS)

# Parse timestamp into hour and weekday
def parse_timestamp(ts):
    try:
        dt = datetime.strptime(ts, '%Y-%m-%d %H:%M:%S')
        return dt.hour, dt.weekday()  # 0 = Monday
    except:
        return None, None

# Read and process the CSV
def read_and_process(filename):
    data = []
    ratings = []

    # First pass: read, clean, collect ratings
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            review = row.get('review_text', '').strip()
            timestamp = row.get('timestamp', '').strip()
            rating_str = row.get('rating', '').strip()

            # Convert rating to float
            try:
                rating = float(rating_str)
                ratings.append(rating)
            except:
                rating = None

            cleaned_review = clean_text(review)
            hour, weekday = parse_timestamp(timestamp)

            data.append({
                'cleaned_review': cleaned_review,
                'hour': hour,
                'weekday': weekday,
                'rating': rating,
            })

    # Compute average rating for missing values
    avg_rating = sum(ratings) / len(ratings) if ratings else 3.0

    # Second pass: fill missing ratings and flag sentiment
    for row in data:
        if row['rating'] is None:
            row['rating'] = avg_rating
        row['sentiment'] = 'positive' if row['rating'] >= 3 else 'negative'

    return data

# Write to output CSV
def write_csv(data, output_file):
    fieldnames = ['cleaned_review', 'hour', 'weekday', 'rating', 'sentiment']
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Main function
def main():
    input_file = input("Enter movie review CSV filename: ").strip()
    output_file = 'processed_' + input_file

    try:
        data = read_and_process(input_file)
        write_csv(data, output_file)
        print(f"✅ Processed data written to: {output_file}")
    except FileNotFoundError:
        print(f"❌ File '{input_file}' not found.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
