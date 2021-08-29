def Algoritmo(val_a: int, val_b: int):
    paso_1 = round(val_a / val_b)
    print(f"{val_a} / {val_b} = {paso_1}")
    paso_2 = val_b * paso_1
    print(f"{val_b} * {paso_1} = {paso_2}")
    paso_3 = val_a - paso_2
    print(f"{val_a} - {paso_2} = {paso_3}")

    print("#######")
    return val_b, paso_3


def Ordenar(val_a, val_b):
    if val_a < val_b:
        val_c = val_a
        val_a = val_b
        val_b = val_c
    return val_a, val_b


if __name__ == "__main__":
    valor_a = int(input("Ingrese numero A:"))
    valor_b = int(input("Ingrese numero B:"))

    valor_a, valor_b = Ordenar(valor_a, valor_b)
    b, p_3 = Algoritmo(valor_a, valor_b)
    try:
        while p_3 >= 0:
            b, p_3 = Algoritmo(b, p_3)
    except ZeroDivisionError:
        pass
