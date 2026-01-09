pw=input("Enter a password: ")

def validate_password(pw):
    if len(pw) < 8:
        return "Password must be at least 8 characters long."
    if not any(char.isdigit() for char in pw):
        return "Password must contain at least one digit."
    if not any(char.isupper() for char in pw):
        return "Password must contain at least one uppercase letter."
    if not any(char.islower() for char in pw):
        return "Password must contain at least one lowercase letter."
    if not any(char in "!@#$%^&*()-_+=" for char in pw):
        return "Password must contain at least one special character (!@#$%^&*()-_+=)."
    return "Password is valid."

result = validate_password(pw)
print(result)