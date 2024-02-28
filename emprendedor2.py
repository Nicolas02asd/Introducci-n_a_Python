import math

precio_suscripcion = float(input("Ingrese el precio de suscripción: $"))
numero_usuarios_normal = float(input("Ingrese el numero de usuarios con suscripción normal: "))
numero_usuarios_premium = float(input("Ingrese el numero de usuarios con suscripción premium: "))
gastos_totales = float(input("Ingrese el monto de gastos totales: $"))

utilidades = (precio_suscripcion * numero_usuarios_normal) + (precio_suscripcion*1.5*numero_usuarios_premium) - gastos_totales

print(f"El monto de las utilidades obtenidas es de ${math.ceil(utilidades)} unidades monetarias")