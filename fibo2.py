def fibo(n):
    num1 = 0
    num2 = 1
    result = 1
    i = 0
    while i < n:
        if i == 0: result = 0
        if i == 1: result = 1
        result = num1 + num2
        print(result)
        num1 = num2
        num2 = result 
        i += 1
    return result
fibo(10)

