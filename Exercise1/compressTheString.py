a = str(input())
c=0
b=""
for i in range(0, len(a)):
    for k in range(i, len(a)):
        if a[i] == a[k]:
            c+=1
        else:
            break
    if len(b) >=3:
        if b[len(b) - 3] != a[i]:
            b += "(" + str(c) + ", " + a[i] + ") "
    else:
        b += "(" + str(c) + ", " + a[i] + ") "
    c = 0

print(b)