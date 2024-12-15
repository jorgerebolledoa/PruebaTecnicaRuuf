def calcular_cantidad_paneles(largo_grande, ancho_grande, largo_pequeno, ancho_pequeno):
    cantidad_largo = largo_grande // largo_pequeno
    cantidad_ancho = ancho_grande // ancho_pequeno
    return cantidad_largo * cantidad_ancho

'''
largo_grande = 10
ancho_grande = 5
largo_pequeno = 3
ancho_pequeno = 12
print(calcular_cantidad_paneles(largo_grande, ancho_grande, largo_pequeno, ancho_pequeno))
'''
largo_grande = int(input("Introduce el largo del área grande: "))
ancho_grande = int(input("Introduce el ancho del área grande: "))
largo_pequeno = int(input("Introduce el largo del panel pequeño: "))
ancho_pequeno = int(input("Introduce el ancho del panel pequeño: "))
print(calcular_cantidad_paneles(largo_grande, ancho_grande, largo_pequeno, ancho_pequeno))