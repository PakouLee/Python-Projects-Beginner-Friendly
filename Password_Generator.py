"""
 Create a python script generates a random strong password with a default length of # characters.
 Make sure that you can change the "#" of characters that you want the password to return.

secrets: Used for securely generating random choices (safer than random for passwords).
string: Provides character sets (letters, digits, punctuation).
digits from encodings.punycode: This is redundant and unused in the code.

"""

import secrets
import string


#Defines a function to generate a password.
def create_pw(pw_length =15):
    letters = string.ascii_letters              # uses both Uppercase + lowercase letters.
    digits = string.digits                      # Uppercase + lowercase letters
    special_chars = string.punctuation          # Special characters like @!#$

    alphabet =  letters + digits + special_chars
    pwd = ''
    pw_strong = False

    while not pw_strong:                        # The script loops until a strong password is generated. Initially, pw_strong = False, so it will force the loop to run at least once.
        pwd = ''                                # Before generating a new password, pwd is reset to an empty string. This ensures that every iteration starts with a fresh password.
        for i in range(pw_length):              # This loop runs pw_length times to meet the "#" of character requirement is meet. In this case it is 15.
            pwd += ''.join(secrets.choice(alphabet)) #In each iteration, python will randomly pick one character from the combined pool and then adds that character to "pwd".


        if  (any(char in special_chars for char in pwd) and             # This statement checks if the password meets two conditions: At least one special character and at least two digits
                sum(char in digits for char in pwd) >= 2):              # Uses sum() to count how many characters in pwd are digits. If the count is 2 or more, this condition is satisfied.
            pw_strong = True                                            # If both conditions are met, pw_strong = True, which exits the while loop.
                                                                        # If not, the loop runs again, generating a new password until a valid one is found.
    return pwd                                                          # If all conditions are met, then  return the pwd.

if __name__ == '__main__':

    print(create_pw())