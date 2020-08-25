#Un hombre desea saber cuanto dinero se genera por concepto de intereses sobre la
#cantidad que tiene en inversión en el banco. El decidirá reinvertir los intereses siempre y
#cuando estos excedan a $7000, y en ese caso desea saber cuanto dinero tendrá finalmente
#en su cuenta.
p_int = float(input("Digite la cantidad de intereses:"))
cap = float(input("Digite su cantidad a invertir:"))
int = cap * p_int
capf = cap + int
if int > 7000:
    print(f" Puede reinvertir sus intereses: {capf}")
    print(f"")
else:
    print(f" no invierta: {capf}")
