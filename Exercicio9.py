print("=== Sistema de Login ===")

usuario_correto = "admin"
senha_correta = "1234"

while 1 == 1:
        usuario = input("Digite o Usuario: ")
        senha = input("Digite a Senha: ")
        if senha == senha_correta and usuario == usuario_correto:
                print("Acesso Liberado!!!")
                break
        else:
                print("Tente Novamente!!!")
