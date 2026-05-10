def dividir(a: float, b: float) -> float:
    """
    Retorna la división de dos números.

    Raises:
        ValueError: Si el divisor es cero.
    """
    if b == 0:
        raise ValueError("División por cero no permitida.")
    return a / b