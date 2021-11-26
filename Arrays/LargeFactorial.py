def factorial(n):
        sum = 1
        for i in range(1,n+1):
            sum*=i
        return [sum]


res = factorial(10)
print(res)