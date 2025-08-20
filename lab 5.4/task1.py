# Script to collect user data: name, age, and email

# Collect user data
name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")

# Display collected data
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Email: {email}")

# --- Data Protection and Anonymization Comments ---
# 1. Avoid storing raw personal data unless necessary.
# 2. Use hashing (e.g., hashlib) to anonymize sensitive fields like email.
# 3. Store data securely (e.g., encrypted files or databases).
# 4. Limit access to personal data to authorized personnel only.
# 5. Remove or mask identifiers before sharing or analyzing data.
# Example anonymization:
# import hashlib
# anonymized_email = hashlib.sha256(email.encode()).hexdigest()