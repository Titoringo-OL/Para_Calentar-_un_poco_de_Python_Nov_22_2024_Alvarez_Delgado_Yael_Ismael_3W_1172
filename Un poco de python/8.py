print("Alvarez Delgado Yael Ismael 3W 1172")
print(" ")
def superposicion(lista1, lista2):
    for i in lista1:
        for j in lista2:
            if i == j:
                return True
    return False

# Ejemplo:
print(superposicion([1, 2, 3], [4, 5, 6]))  
print(superposicion([1, 2, 3], [3, 4, 5])) 
