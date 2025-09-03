def generate_email(first_name, last_name, domain):
    """
    Generates an email address in the format: first_name.last_name@domain
    All parts are lowercased.
    """
    return f"{first_name.lower()}.{last_name.lower()}@{domain.lower()}"

def validate_email(email):
    """
    Validates an email address based on the following rules:
    - Must contain @ and . characters.
    - Must not start or end with special characters.
    - Should not allow multiple @.
    Returns True if valid, False otherwise.
    """
    if not isinstance(email, str):
        return False

    # Must contain exactly one @
    if email.count('@') != 1:
        return False

    # Must contain at least one .
    if '.' not in email:
        return False

    # Must not start or end with special characters
    special_chars = {'@', '.', '-', '_', "'"}
    if email[0] in special_chars or email[-1] in special_chars:
        return False

    return True
