
def pedir_numero(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("No puedes ingresar un espacio vacío.")
            continue
        try:
            return int(texto)
        except ValueError:
            print("Ingrese un número válido.")


while True:
    print("***Operaciones básicas*** \n" \
        "1. Suma \n" \
        "2. Resta \n" \
        "3: Multiplicación \n" \
        "4. División \n" \
        "5. Salir")
    
    opcion_str = input("Ingrese una opción: ").strip()

    if opcion_str == "":
        print("No puedes dejar un espacio vacío.")
        continue
    try:
        opcion = int(opcion_str)

    except ValueError:
        print("Debes ingreasar una opción válida.")
        continue

    #Suma
    if opcion == 1:
        print("**Suma**")
            
        #Operación
        num1 = pedir_numero("Ingrese el primer número: ")
        num2 = pedir_numero("Ingrese el segundo número: ")

        suma = num1 + num2
        print(f"El resultado de {num1} + {num2} = {suma}")

    #Resta
    elif opcion == 2:
        print("**Resta**")

        #Operación
        num1 = pedir_numero("Ingrese el primer número: ")
        num2 = pedir_numero("Ingrese el segundo número: ")

        resta = num1 - num2
        print(f"El resultado de {num1} - {num2} = {resta}")

    #Multiplicación
    elif opcion == 3:
        print("**Multiplicación**")

        #Operación
        num1 = pedir_numero("Ingrese el primer número: ")
        num2 = pedir_numero("Ingrese el segundo número: ")

        mult = num1 * num2
        print(f"El resultado de {num1} x {num2} = {mult}")

    #División
    elif opcion == 4:
        print("**División**")
        
        #Operación
        num1 = pedir_numero("Ingrese el primer número: ")
        num2 = pedir_numero("Ingrese el segundo número: ")

        try:
            div = num1 / num2
            print(f"El resultado de {num1} ÷ {num2} = {div}")
        except ZeroDivisionError:
            print("No puedes dividir para 0.")
            
    #Salir
    elif opcion == 5:
        print("Saliendo...")
        break

    else:
        print("Ingrese una opción válida del 1 al 5.")