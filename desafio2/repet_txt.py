"""Repete um texto pela quantidade de vezes informada pelo usuário."""


texto = input("Digite o texto que deseja repetir: ")

try:
    quantidade = int(input("Digite a quantidade de repetições: "))

    if quantidade < 0:
        print("A quantidade de repetições não pode ser negativa.")
    else:
        print(f"Texto repetido: {texto * quantidade}")
except ValueError:
    print("Quantidade inválida. Digite um número inteiro.")
