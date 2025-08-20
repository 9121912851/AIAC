import re

def sentiment_analysis(text):
    # Basic bias handling: remove gendered and racial terms (example list)
    bias_terms = ['he', 'she', 'him', 'her', 'black', 'white', 'asian', 'latino']
    pattern = re.compile(r'\b(' + '|'.join(bias_terms) + r')\b', re.IGNORECASE)
    cleaned_text = pattern.sub('', text)

    # Simple sentiment analysis using keywords
    positive_words = ['good', 'great', 'excellent', 'happy', 'love', 'wonderful']
    negative_words = ['bad', 'terrible', 'sad', 'hate', 'awful', 'poor']

    pos_count = sum(word in cleaned_text.lower() for word in positive_words)
    neg_count = sum(word in cleaned_text.lower() for word in negative_words)

    if pos_count > neg_count:
        sentiment = 'Positive'
    elif neg_count > pos_count:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment

if __name__ == "__main__":
    user_input = input("Enter text for sentiment analysis: ")
    result = sentiment_analysis(user_input)
    print(f"Sentiment: {result}")