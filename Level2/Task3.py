def pswd_strength(pswd):
    s = "@$!%*?&#"
    upper = lower = digit = special = 0
    for char in pswd:
        upper += char.isupper()
        lower += char.islower()
        digit += char.isdigit()
        special += char in s
    if len(pswd)>=8:
        if  upper > 0 and lower > 0 and digit > 0 and special > 0:
            print("Strong password!")
        else:
            print("The password should be mix of [a-z],[A-Z],[0-9],[@$!%*?&#]")
    else:
        print("Password should greater than or equalto 8")
pswd = input("Enter a password: ")
pswd_strength(pswd)