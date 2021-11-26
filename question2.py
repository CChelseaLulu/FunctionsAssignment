def sumnum(num1, num2):
    sum = 0
    for i in range(num1,num2+1):
        sum +=i
    return sum
print(sumnum(6,8))


def mainsum():
    a = 50
    b = 150
    print("Sum of numbers from %d to %d" ,(a, b,sumnum(a, b)))

mainsum()
