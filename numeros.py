numero1 = float(input("introduce el primer numero: "))
numero2 = float(input("introduce el segundo numero: "))

print (f"Numero 1: {numero1}")
print (f"Numero 2: {numero2}")
if numero2 != 0:
    cociente1 = numero1 / numero2 
    print(f"cociente de {numero1} / {numero2} = {cociente1}") 
else:
    print("No se puede dividir por cero.")

if numero1 != 0:
   cociente2 = numero2 / numero1 
   print(f"cociente de {numero2} / {numero1} = {cociente2}")
else:
    print("No se puede dividir por cero.")
    
