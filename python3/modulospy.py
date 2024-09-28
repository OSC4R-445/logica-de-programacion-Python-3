def aloo():
    nombre = input("dime tu nombre")
    print ("hola", nombre)

def bye():
    print("nos vemos")

def notas():
    nota1=int(input("cual es tu nota 1"))
    nota2=int(input("cual es tu nota 2"))
    nota3=int(input("cual es tu nota 3"))
    promedio=nota1+nota2+nota3
    print(f"todas tus notas{nota1,nota2,nota3}")
    print(f"tu promedio: {promedio/3}")

#CUERPO PRINCIPAL
aloo()
notas()
bye()
