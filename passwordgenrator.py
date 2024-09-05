import random
import string

def generate_password(length):
    # Define character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Get user input for the password length
length = int(input("Enter the desired length for your password: "))

# Generate the password
generated_password = generate_password(length)

# Display the generated password
print(f"Your generated password is: {generated_password}")
