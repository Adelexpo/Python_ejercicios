import Operaciones as op

def main():
    resSuma = op.Suma(2, 3)
    resResta = op.Resta(6, 2)
    resMultiplicar = op.Multiplicar(9, 3)
    resDividir = op.Dividir(12, 2)
    print("El resultado de las operaciones son: ", resSuma, resResta, resMultiplicar, resDividir)



if __name__ == '__main__':
    main()