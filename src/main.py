from operations import sumar, restar, multiplicar, dividir

def ejecutar_demo() -> None:
    print("=== Calculadora App ===\n")
    print(f"  Suma:          2 + 3  = {sumar(2, 3)}")
    print(f"  Resta:        10 - 4  = {restar(10, 4)}")
    print(f"  Multiplicar:   3 x 4  = {multiplicar(3, 4)}")
    print(f"  Dividir:      10 / 2  = {dividir(10, 2)}")

    print("\n--- Manejo de errores ---")
    try:
        dividir(5, 0)
    except ValueError as e:
        print(f"  Error capturado: {e}")

if __name__ == "__main__":
    ejecutar_demo()        