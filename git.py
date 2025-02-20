def menu():
    print("Bienvenido, selecciona la operación que deseas realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Salir")

def suma():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")

def main():
    while True:
        menu()
        opcion = input("Ingresa el número de la operación que deseas realizar: ")

        if opcion == '6':
            print("Saliendo de la calculadora...")
            break
        elif opcion == '1':
            suma()
        elif opcion == '2':
            print("Aquí iría la lógica de la resta.")
        elif opcion == '3':
            print("Aquí iría la lógica de la multiplicación.")
        elif opcion == '4':
            print("Aquí iría la lógica de la división.")
        elif opcion == '5':
            print("Aquí iría la lógica de la potencia.")
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")

if __name__ == "__main__":
    main()