def calificaciones(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3)/3
    return promedio

#uso de la funcion 
nota1= 10
nota2= 9
nota3= 3
resultado = calificaciones(nota1, nota2, nota3)

print("----Nota----")
print("Nota1:", nota1)
print("Nota2", nota2)
print("Nota3", nota3)
print("El resultado es: ", resultado)
