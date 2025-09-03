def is_sentence_palindrome(sentence):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(
        c.lower() for c in sentence if c.isalnum()
    )
    return cleaned == cleaned[::-1]
