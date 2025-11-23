import re

# Patterns
email_pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
pan_pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'

email = input("Enter Email ID: ")
pan = input("Enter PAN Number: ").upper()

# Validate Email
if re.match(email_pattern, email):
    print("Valid Email ID")
else:
    print("Invalid Email ID")

# Validate PAN
if re.match(pan_pattern, pan):
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")
