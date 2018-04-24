def calculadora():
    operacion = str(input("Digite operacion: "))
    n1 = int(input("Digite primer numero:"))
    n2 = int(input("Digite segundo numero:"))
    if operacion == '+' :
        resultado = n1 + n2
        return resultado
    if operacion == '-' :
        resultado = n1 - n2
        return resultado
    if operacion == "*" :
        resultado = n1*n2
        return resultado
print(calculadora())