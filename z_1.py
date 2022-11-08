import math

d = input('Введите степень округления 10^(-1) ≤ d ≤10^(-10): ')
d = d[2:len(d)]
print(round(math.pi,len(d)))