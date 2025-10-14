def fibonacci_sequence(terms):
    li = []
    a, b = 0, 1  
    li.append(a)
    li.append(b)
    for i in range(0,terms-2):
        a,b=b,a+b
        li.append(b)
    return li   
terms= int(input("Enter the number of terms for Fibonacci sequence: "))
print(fibonacci_sequence(terms))