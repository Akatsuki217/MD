def IndMat(n: int):
    if n >= 0:
        resultado = int( (n * (n + 1) * ((2*n)+1)) / 6 ) 
        print(f"({n} * ({n} + 1) * ((2*{n})+1)) / 6", resultado)
        return
    print("Sin resultado")
