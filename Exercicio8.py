print("=== Contador de Numeros Pares ===")

contador = int(input("Digite um valor: "))
if contador != 0:
   print(f"Nota:{contador} é um Número Ímpar. Começando do Número Anterior...")

   contador-1
   
while 0 < contador:
   contador -= 2

   print(f"{contador} é um Número Par")
   
   if contador == 0:
      print("Fim da Contagem!!")
      break
   