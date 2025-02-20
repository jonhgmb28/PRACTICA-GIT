from root_square import get_sqrt
from multiply import get_multy

def resta(a, b):
    return a - b

def menu():
    print("Bienvenido, selecciona la operación que deseas realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Raíz cuadrada")
    print("6. Salir")

def main():
    while True:
        menu()
        opcion = input("Ingresa el número de la operación que deseas realizar: ")

        if opcion == '6':
            print("Saliendo de la calculadora...")
            break        

        if opcion == '1':
            print("Aquí iría la lógica de la suma.")
        elif opcion == '2':
            n = float(input('Ingrese un número: '))
            m = float(input('Ingrese otro número: '))
            print(resta(n, m))  # Se usa la función de resta definida en el mismo archivo
        elif opcion == '3':
            n = float(input('Ingrese un número: '))
            m = float(input('Ingrese otro número: '))
            print(get_multy(n, m))
        elif opcion == '4':
            print("Aquí iría la lógica de la división.")
        elif opcion == '5':
            n = float(input('Ingrese un número: '))
            print(get_sqrt(n))
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")

if __name__ == "__main__":
    main()
