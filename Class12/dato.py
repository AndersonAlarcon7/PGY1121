# Ejemplo de uso de repositorio
 
print("Datos Personales")
print("==========================\n")
Vnom = input("Ingrese su nombre: ")
while True:
    try:
        Vedad =int(input("Ingrese su edad :"))
        break
    except:
        print("Valor No Coreresponde")    
print("==========================='")
print(f"Su nombre es:{Vnom}")
print(f"Su edad es:{Vedad}")

print("Programa finalzado...")