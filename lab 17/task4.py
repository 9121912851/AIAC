import csv
import re
from statistics import median

# 1. Remove HTML tags
def remove_html(text):
    clean = re.sub(r'<.*?>', '', text)
    return clean

# 2. Text standardization: lowercase + remove HTML
def clean_text(text):
    if text is None:
        return ''
    text = remove_html(text)
    return text.lower().strip()

# 3. Handle missing ratings: fill with median
def fill_missing_ratings(data):
    ratings = [float(d['rating']) for d in data if d['rating'] != '' and d['rating'] is not None]
    med = median(ratings) if ratings else 5.0  # default median if empty

    for d in data:
        if d['rating'] == '' or d['rating'] is None:
            d['rating'] = med
        else:
            d['rating'] = float(d['rating'])

# 4. Normalize ratings 0-10 to 0-1
def normalize_ratings(data):
    for d in data:
        d['rating'] = d['rating'] / 10.0

# 5. Tokenize using TF-IDF vectorizer
# As no external libraries allowed, implement simple word count vectorizer
def tokenize(data):
    from collections import Counter
    for d in data:
        words = d['review_text'].split()
        d['tokens'] = Counter(words)

def read_csv(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append({
                'review_text': row.get('review_text', '').strip(),
                'rating': row.get('rating', '').strip()
            })
    return data

def write_csv(data, filename):
    fieldnames = ['review_text', 'rating']
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for d in data:
            writer.writerow({'review_text': d['review_text'], 'rating': round(d['rating'], 3)})

def main():
    input_file = input("Enter movie reviews CSV filename: ")
    output_file = 'cleaned_' + input_file

    data = read_csv(input_file)

    # Clean texts
    for d in data:
        d['review_text'] = clean_text(d['review_text'])

    # Fill missing ratings
    fill_missing_ratings(data)

    # Normalize ratings
    normalize_ratings(data)

    # Tokenize (just simple count here)
    tokenize(data)

    write_csv(data, output_file)

    print(f"✅ Cleaned data written to {output_file}")

if __name__ == "__main__":
    main()

def test_remove_html():
    assert remove_html("<b>Bold</b> Text") == "Bold Text"
    assert remove_html("<div>Test</div>") == "Test"
    assert remove_html("No tags") == "No tags"

def test_fill_missing_ratings():
    data = [{'rating': '8'}, {'rating': ''}, {'rating': '6'}, {'rating': None}]
    fill_missing_ratings(data)
    expected_median = 7  # median of [8,6] = 7
    assert data[1]['rating'] == expected_median
    assert data[3]['rating'] == expected_median

def test_normalize_ratings():
    data = [{'rating': 10}, {'rating': 5}, {'rating': 0}]
    normalize_ratings(data)
    assert data[0]['rating'] == 1.0
    assert data[1]['rating'] == 0.5
    assert data[2]['rating'] == 0.0

