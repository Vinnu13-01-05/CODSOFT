import random
import string

def generate_password(length):
    if not isinstance(length, int) or length < 4:
        return "Error: Password length should be an integer of at least 4 characters."
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

# Example test cases
print("Generated Password (length 8):", generate_password(8))  # Expected: Random 8-character password
print("Generated Password (length 12):", generate_password(12))  # Expected: Random 12-character password
print("Generated Password (length 3):", generate_password(3))  # Expected: Error message
print("Generated Password (length 'ten'):", generate_password("ten"))  # Expected: Error message