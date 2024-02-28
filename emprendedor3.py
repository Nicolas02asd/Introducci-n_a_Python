import math

precio_suscripcion = float(input("Ingrese el precio de suscripción: $"))
numero_usuarios = float(input("Ingrese el numero de usuarios: "))
gastos_totales = float(input("Ingrese el monto de gastos totales: $"))
utilidades_año_anterior = float(input("Ingrese utilidades del año anterior: $"))

utilidades_actuales = precio_suscripcion * numero_usuarios - gastos_totales
razon_utilidades = utilidades_actuales / utilidades_año_anterior

print(f"El monto de las utilidades actuales obtenidas es de ${math.ceil(utilidades_actuales)} unidades monetarias")
print(f"Las utilidades actuales corresponden a {razon_utilidades:.2f} veces las del año anterior")