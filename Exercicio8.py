print("=== Contador de Números Pares ===")

contador = int(input("Digite um valor: "))

if contador % 2 != 0:
    print(f"Nota: {contador} é um Número Ímpar. Começando do número par anterior...")
    contador -= 1

while contador >= 0:
    print(f"{contador} é um Número Par")
    
    if contador == 0:
        print("Fim da Contagem!!")
        break
    
    contador -= 2
