print("=== Digite o Valor da Compra ===")

valor = float(input("Valor da Compra: "))

valor_desc = (valor*10)/100

valor_final = valor - valor_desc

if valor > 100:
    print(f"O Valor da Compra Com 10% de Desconto é: R$ {valor_final} ")

elif valor <=100:
    print(f"O Valor da Compra é: R$ {valor} ")
    print("Valor da Compra Näo Qualifica o Desconto!!")
    