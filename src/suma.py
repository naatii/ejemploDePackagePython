def suma (numeroUno:int, numeroDos:int)->int:
    return  numeroUno + numeroDos 

def salida(resultado:int)-> int:
    return "El resultado de la suma es ", resultado

if __name__=="__main__":
    # Ejercicio 1
    numeroUnoSuma = int(input("Introduce el primer número: "))
    numeroDosSuma = int(input("Introduce el primer número: "))
    print(salida(suma(numeroUnoSuma,numeroDosSuma)))