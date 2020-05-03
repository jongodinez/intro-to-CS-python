#Program takes 2 inputs, encapsulates a password (rudimentarily) and prints a formatted string.

username = input("what's your username?")
passwordInput = input("what's your password?")

password =(len(passwordInput)) * "*"

passwordLength = len(passwordInput)

print(f"Hi {username}, your password is {password}. It has {passwordLength} characters.")