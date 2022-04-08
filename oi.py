
valor = input().split(" ")
a, b, c = valor

max_val = max(a,b,c)
print(str(max_val) + " eh o maior")

# import math

valor = input().split(" ")
a, b, c = valor

maior = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
resultado = (int(maior) + int(c) + abs(int(maior) - int(c)))/2

print("%d eh o maior" %resultado)