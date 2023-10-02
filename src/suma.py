def suma (numeroUno:int, numeroDos:int)->str:
    return  (f"El resultado de la suma es: {numeroUno+numeroDos}")
def multiplicacion(numeroUno: int, numeroDos:int)->str:
    return  (f"El resultado de la multiplicacion es: {numeroUno*numeroDos}")

if __name__=="__main__":
    # Ejercicio 1
    numeroUnoSuma = int(input("Introduce el primer número: "))
    numeroDosSuma = int(input("Introduce el primer número: "))
    print(suma(numeroUnoSuma, numeroDosSuma))
    
    
    # Ejercicio 2
    numeroDosMultiplicacion = int(input("Introduce el primer número: "))
    numeroUnoMultiplicacion = int(input("Introduce el primer número: "))
    print(multiplicacion(numeroUnoMultiplicacion, numeroDosMultiplicacion))