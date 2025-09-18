import re
import string

def extract_mentions_hashtags(text):
    # Find all @mentions and #hashtags
    mentions = re.findall(r'@\w+', text)
    hashtags = re.findall(r'#\w+', text)
    
    # Helper to strip punctuation and convert to lowercase
    def clean(items):
        return [item.strip(string.punctuation).lower() for item in items]
    
    return clean(mentions), clean(hashtags)

# Test cases
test_cases = [
    ("Hello @alice check #AI and #Python with @Bob", (['@alice', '@bob'], ['#ai', '#python'])),
    ("@John! #Hello, @Jane. #World?", (['@john', '@jane'], ['#hello', '#world'])),
    ("No mentions or hashtags here.", ([], [])),
    ("Multiple @Mentions @Test #Hash #Tag", (['@mentions', '@test'], ['#hash', '#tag'])),
]

for i, (text, expected) in enumerate(test_cases, 1):
    mentions, hashtags = extract_mentions_hashtags(text)
    print(f"Test case {i}:")
    print(f"Mentions: {mentions} (Expected: {expected[0]})")
    print(f"Hashtags: {hashtags} (Expected: {expected[1]})")
    print("---")