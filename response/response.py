from validator_collection import checkers

check_email = input("What's your email address? ")

is_email_address = checkers.is_email(check_email)

if is_email_address:
    print("Valid")
else:
    print("Invalid")
