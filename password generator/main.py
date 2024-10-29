import random
import string

def generate_random_password(length=12):
    # Define the character sets for each type of password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Combine all the character sets into one
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    
    # Generate a random password by selecting characters from each character set
    password = []
    for _ in range(length):
        character_set = random.choice([lowercase_letters, uppercase_letters, digits, special_characters])
        password.append(random.choice(character_set))
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)
    
    # Convert the password list into a string
    password_str = ''.join(password)
    
    return password_str

# Generate a random password
random_password = generate_random_password()
print(random_password)
