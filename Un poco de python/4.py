print("Alvarez Delgado Yael Ismael 3W 1172")
print(" ")
# Asegura que sea solo un carácter
def es_vocal(c):
    if len(c) != 1:  
        return False
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return c in vocales

# Una deberia ser true y otra false
print(es_vocal("a"))  
print(es_vocal("b"))  
