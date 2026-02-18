print("=== Calculadora de IMC ===")

altura = float(input("Digite sua Altura (m): "))
peso = float(input("Digite seu Peso (kg): "))

imc = peso / altura**2

print(f"/nSeu IMC é: {imc:.2f}")

# Classificaçäo

if imc <18.5:
    print("Classificaçäo: Abaixo do Peso!!")

elif imc <25:
    print("Classificaçäo: Peso Normal!!")

elif imc >25 <29.9:
    print("Classificaçäo: Sobrepeso!!!")

elif imc >30:
    print("Classificaçäo: Obesidade!!!")
