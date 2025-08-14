import re

def extract_email(text):
    # Regular expression for matching email addresses
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    emails = re.findall(pattern, text)
    return emails

if __name__ == "__main__":
    user_input = input("Enter text: ")
    emails = extract_email(user_input)
    if emails:
        print("Email address(es) found:", ', '.join(emails))
    else:
        print("No email address found.")