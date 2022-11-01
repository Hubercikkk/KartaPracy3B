# #zad1 
#  for i in range(1,31):
#      print(i, "dni")

#zad2

# for i in range(1, 10, 2):
#     print(i**2, "no kwadraty ma sie rozumieć")

# zad3

# for i in range(1138, 9855):
#     if i %379 ==0:
#         print(i)

#zad4

# for i in range(101, 1000):
#     if i %5 ==0 and i %6 ==0 and i %11 ==0:
#         print(i)

#zad5

# a = int(input("podaj ilośc liczb: "))
# Liczby = []
# for i in range(0, a):
#     temp = int(input(f"Podaj {i+1} liczbę: "))
#     Liczby.append(temp)
# print(f"Wynik to: {sum(Liczby)}")

#   zad 6
# k = int(input())
# a = 0
# for i in range(0,2 * k,2):
#         a += i 
# print(a)

# #zad 7
# m = int(input())
# a=0
# for i in range(11, m+1, 2):
#   a+=i
# print(a)

# zad 8
# W0  = int(input("Podaj początkową wartość inwestycji."))
# L = int(input("Podaj lata inwestycji."))
# Wk = 0
# suma = Wk
# for i in range(0, L * 12):
#     Wk = suma * 0.06 * (1/12)
#     suma = suma + Wk
# print("Końcowa wartość inwestycji wynosi:")
# print(suma)

#zad 9
# n = int(input())
# suma=0
# for i in range(21,n+1,100):
#  suma+=i
# print(suma)

#zad 10
# import math
# for i in range(1,1000):
#   if i%10==math.sqrt(i):
#     print(i)
#   elif i%100==math.sqrt(i):
#     print(i)