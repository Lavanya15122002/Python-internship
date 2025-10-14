def is_palindrome(string):
    string = string.replace(" ", "").lower()
    print(string)
    if string == string[::-1]:
        print("The string is a palindrome ")
    else:
        print("The string is not a palindrome ")
string = input("Enter a string: ")
is_palindrome(string)
