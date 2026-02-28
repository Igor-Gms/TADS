print("=== Sistema de Média Dos Alunos ===")

nota1 = float(input("Digite a Primeira Nota: "))
nota2 = float(input("Digite a Segunda Nota: "))

média = (nota1+nota2)/2

if média >5<6.9:
    print(f"Nota => {média:.1f} Classificaçäo: Recuperaçäo!!!!")

elif média >=7:
    print(f"Nota => {média:.1f} Classificaçäo: Aprovado!!!")

elif média <5:
    print(f"Nota => {média:.1f} Classificaçäo: Reprovado!!!")
