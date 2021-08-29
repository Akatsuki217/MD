def Identidad(val_a, val_b):
    valor = 0
    multiplo = HallarMaximo(val_a, val_b)
    faltante = 0

    while valor <= val_a:
        faltante += 1
        valor = val_b * multiplo + faltante
        if valor == val_a:
            print(f"{val_a} = {val_b} * {multiplo} + {faltante}")
            break

    return val_b, faltante, multiplo


def HallarMaximo(a, b):
    multiplo = 0

    while True:
        valor = b * multiplo
        if valor >= a:
            break
        multiplo += 1
        
    return multiplo - 1


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
    a, b, m = Identidad(valor_a, valor_b)
    try:
        while m > 0:
            a, b, m = Identidad(a, b)
    except ZeroDivisionError:
        pass
