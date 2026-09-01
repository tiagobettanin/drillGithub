"""Realiza uma operação matemática simples entre dois números."""


try:
    primeiro_numero = float(input("Digite o primeiro número: "))
    operador = input("Digite a operação (+, -, * ou /): ").strip()
    segundo_numero = float(input("Digite o segundo número: "))

    if operador == "+":
        resultado = primeiro_numero + segundo_numero
    elif operador == "-":
        resultado = primeiro_numero - segundo_numero
    elif operador == "*":
        resultado = primeiro_numero * segundo_numero
    elif operador == "/":
        if segundo_numero == 0:
            raise ZeroDivisionError
        resultado = primeiro_numero / segundo_numero
    else:
        resultado = None
        print("Operação inválida. Use +, -, * ou /.")

    if resultado is not None:
        print(f"Resultado: {resultado:g}")
except ValueError:
    print("Entrada inválida. Digite apenas números válidos.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
