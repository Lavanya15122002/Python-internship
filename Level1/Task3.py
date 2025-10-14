def validate_email():
    email = input("Enter your email: ")
    if email.count("@") != 1:
        print("Invalid Email")
        return
    username, domain = email.split("@")    
    if not username:
        print("Invalid Email")
        return
    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        print("Invalid Email")
        return
    print("Valid Email")
validate_email()