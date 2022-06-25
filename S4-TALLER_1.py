""" 
Escriba un programa que solicite al usuario la cantidad de palabras que desea ingresar. A continuación solicite las palabras creando una lista. Una vez concluido solicite la palabra que desea buscar en la lista. Presente la cantidad de veces que aparece la palabra en la lista o caso contrario indique que la palabra buscada no fue encontrada.
"""
#funcion para validar la entrada de numeros 
while True:
    try:
        numero_palabras = int(input("Dígame la cantidad de palabras que desea ingresar:  "))
    except ValueError:
        print("\33[3;31m" + "Debes ingresar un número."+"\33[0m")
        continue

    if numero_palabras <= 0:
        print("\33[3;31m"+"Debes escribir un número válido."+"\33[0m")
        continue
    else:
        break
lista = []
for i in range(numero_palabras):
    palabra_ingresada = input(f"Dígame la palabra {i + 1}: ") 
    lista += [palabra_ingresada.lower()]
#funcion para validar la entrada de palabras
palabra_buscar = " "
while not palabra_buscar.isalpha():
    palabra_buscar = input ("Escribe la palabra que deseas buscar: ")
conteo = 0
for i in lista:
    if i == palabra_buscar.lower():
        conteo += 1
if conteo == 1:
    print('La palabra -'+ palabra_buscar + '- se encuentra una vez en la lista.')
elif conteo == 0:
    print('La palabra -' + palabra_buscar +  '- no fue encontrada en la lista.')
else:
    print('La palabra -'+ palabra_buscar + '- está' + conteo + 'veces en la lista.')
