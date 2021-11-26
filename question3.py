def sumnum(num1, num2, k):
    sum = 0
    for i in range(num1,num2+1):
        sum += pow(i, k)
    return sum

print(sumnum(6,8,2))

def mainsum():
    a = 50
    b = 150
    k = 2
print("Sum of %d power of numbers from %d to %d" (k, a, b,sumnum(a, b, k)))

mainsum()
