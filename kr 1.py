# 1
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
def print_multiplic_table(num1,num2,num3,num4):
    for i in range(num1, num2 +1):
        for j in range(num3, num4 + 1):
            print(i*j, end="\t")
        print()
print_multiplic_table(num1, num2, num3, num4)
#я честно долго думала, как сделать красивый вывод, но как то не судьба(((
