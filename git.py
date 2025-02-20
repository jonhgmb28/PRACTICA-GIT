
from root_square import get_sqrt
from multiply import get_multy

def resta(a, b):
    return a - b


def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b



def menu():
    print("Bienvenido, selecciona la operación que deseas realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Raíz cuadrada")
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

        if opcion == '1':
            print("Aquí iría la lógica de la suma.")
        elif opcion == '2':
            n = float(input('Ingrese un número: '))
            m = float(input('Ingrese otro número: '))

            print(resta(n, m))  # Se usa la función de resta definida en el mismo archivo
            print(resta(n, m))

        elif opcion == '3':
            n = float(input('Ingrese un número: '))
            m = float(input('Ingrese otro número: '))
            print(get_multy(n, m))
        elif opcion == '4':
            n = float(input('Ingrese un número: '))
            m = float(input('Ingrese otro número: '))
            print(division(n, m))
        elif opcion == '5':
            n = float(input('Ingrese un número: '))
            print(get_sqrt(n))

            n = float(input('Ingrese un número: '))
            m = float(input('Ingrese otro número: '))
            print(division(n, m))
       



        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")

if __name__ == "__main__":
    main()
