import re

def is_valid_email(email: str) -> bool:
    regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return bool(re.match(regex, email))

# Test the function
print(is_valid_email("user@example.com"))  # True
print(is_valid_email("user.name@example.com"))  # True
print(is_valid_email("user@subdomain.example.com"))  # True
print(is_valid_email("username@example.com"))  # True
print(is_valid_email("user@example.co.uk"))  # True
print(is_valid_email("invalid_email"))  # False
