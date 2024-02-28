import math

precio_suscripcion = float(input("Ingrese el precio de suscripción: $"))
numero_usuarios = float(input("Ingrese el numero de usuarios: "))
gastos_totales = float(input("Ingrese el monto de gastos totales: $"))

utilidades = precio_suscripcion * numero_usuarios - gastos_totales

print(f"El monto de las utilidades obtenidas es de ${math.ceil(utilidades)} unidades monetarias")