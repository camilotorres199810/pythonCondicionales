#Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si su
#promedio de tres calificaciones es mayor o igual a 70; reprueba en caso contrario.
calf1 = float(input("Digite su calificacion 1:"))
calf2 = float(input("Digite su calificacion 2:"))
calf3 = float(input("Digite su calificacion 3:"))
prom = (calf1 + calf2 + calf3)/3
if prom>=70:
    print("Alumno  aprobado",prom)
else:
    print("Alumno reprobado",prom)


