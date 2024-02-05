def fibonacci(n):
    terms_list = [0]
    variable1 = 0
    variable2 = 1
    while n > 0:
        variable3 = variable1 + variable2
        variable1 = variable2
        variable2 = variable3
        terms_list.append(variable1)
        n = n - 1
    return terms_list

def fibosum(n , terms_list):
    summatory = 0
    count = 0
    for i in terms_list:
        if count <= n:
            summatory += i
            count += 1

    return summatory
n = int(input("Number of terms:"))
terms_list = fibonacci(n)
summatory = fibosum(n, terms_list)
print("Sum of the First 5 terms of the Fibonacci series:", summatory)
n = int(input("Number of terms:"))
terms_list = fibonacci(n)
summatory = fibosum(n, terms_list)
print("Sum of the First 10 terms of the Fibonacci series:", summatory)
