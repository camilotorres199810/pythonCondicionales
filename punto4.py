#Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig. manera:
#Si trabaja 40 horas o menos se le paga $16 por hora
#Si trabaja mas de 40 horas se le paga $16 por cada una de las primeras 40 horas y
#$20 por cada hora extra.
ht = int(input("Digite el numero de horas:"))
if ht > 40:
    he = ht -40
    ss = he * 20 + 40 * 16
    print(f"su salario por horas trabajadas sera de :{ss}")
else:
    ss = ht * 16
    print(f"su salario por horas trabajadas sera de :{ss}")