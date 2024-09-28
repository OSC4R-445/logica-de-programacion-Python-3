cantidad=input("Cuántos productos va a llevar?\n")
precio=random.randint(1000,50000)
subtotal=precio*cantidad
porc=0
if subtotal>50000:
        porc=0.05
else:   
        porc=0.02
#montodescuento
#total a pagar

#salidas
print(f"El precio del producto es:{precio}")
print(f"El subtotal de la compra es : {subtotal}")
print(f"EL procentaje de descuento es: {porc}") 