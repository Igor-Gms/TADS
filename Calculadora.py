print("=====Calculadora=====")

num1 = float(input("Escolha o Primeiro Número: "))
num2 = float(input("Escolha o Segundo Número: "))

print("\nEscolha a operaçäo: ")

print("1 - Soma")
print("2 - Subtraçäo")
print("3 - Multiplicaçäo")
print("4- Divisäo")

opçäo = input("Digite a opçäo 1/2/3/4: ")

if opçäo == "1":
    resultado = num1 + num2 
    print("Resultado da Soma: ", resultado)
    
elif opçäo == "2":
    resultado = num1 - num2
    print("Resultado da Subtraçäo: ", resultado)

elif opçäo == "3":
    resultado = num1 * num2
    print("Resultado da Multiplicaçäo: ", resultado)

elif  opçäo == "4":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado da Divisäo: ", resultado)

    else: print("Erro: Divisäo por Zero!")

else: print("Operaçäo Inválida!")

