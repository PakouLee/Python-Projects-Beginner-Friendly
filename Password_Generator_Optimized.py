"""
Generates a secure random password with at least `min_digits` and `min_special` characters.

:param pw_length: Length of the password (default: 12)
:param min_digits: Minimum number of digits required (default: 2)
:param min_special: Minimum number of special characters required (default: 1)
:return: Secure password as a string
"""


import secrets
import string


def create_pw(pw_length=12, min_digits=2, min_special=1):

    # Define character sets
    letters = string.ascii_letters  # A-Z, a-z
    digits = string.digits  # 0-9
    special_chars = string.punctuation  # Special characters like @, #, etc.

    # Full character pool
    alphabet = letters + digits + special_chars

    # Generate a strong password
    while True:
        # Create a password of specified length
        pwd = ''.join(secrets.choice(alphabet) for _ in range(pw_length))

        # Validate password strength
        if (sum(char in digits for char in pwd) >= min_digits and
                sum(char in special_chars for char in pwd) >= min_special):
            return pwd


# Run the password generator if the script is executed directly
if __name__ == '__main__':

    print(create_pw())