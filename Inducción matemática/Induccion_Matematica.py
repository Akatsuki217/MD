# Sumatoria total
def IndMat(n: int):
    if n >= 0:
        resultado = int((n+1)*(n/2))
        print(resultado)
        return
    print("Sin resultado")

if __name__=="__main__":
    IndMat(4)
