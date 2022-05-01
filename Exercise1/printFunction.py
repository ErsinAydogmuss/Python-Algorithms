a = int (input())
b = ""
if a <= 150 and a >= 1:
    for sayi in range(1,a+1):
        b += str (sayi)
print(b)