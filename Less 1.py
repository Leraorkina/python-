# 3
text = str(input())
l = len(text)
count = 1
for i in range (l):
    if i == l - 1:
        print(text[i]+str(count))
    else:
        if text[i] == text [i+1]:
            count = count +1
        else:
            print(text[i] + str(count))
            count = 1
#с выводом беда беда




