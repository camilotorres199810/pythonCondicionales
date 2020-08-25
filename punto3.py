#En un almacén se hace un 20% de descuento a los clientes cuya compra supere los $1000
#¿ Cual será la cantidad que pagara una persona por su compra?
compra = float(input("Digite el valor de la compra:"))
if compra > 1000:
    desc = compra * 0.20
else:
    desc = 0

tot_pag = compra - desc

print(f"el total a pagar por su compra es de:{tot_pag}")