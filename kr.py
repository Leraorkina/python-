#2
num1 = int(input())
num2 = int(input())
multiply = num1 * num2
for i in range(max(num1,num2), multiply + 1):
    if i % num1 == 0 and i % num2 == 0:
        print(i)
        break





