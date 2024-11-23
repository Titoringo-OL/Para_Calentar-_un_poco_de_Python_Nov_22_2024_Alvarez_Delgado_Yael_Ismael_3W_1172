print("Alvarez Delgado Yael Ismael 3W 1172")
print(" ")
def max_de_tres(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# Se imprime el valor maximo
print(max_de_tres(43, 99, 65))  