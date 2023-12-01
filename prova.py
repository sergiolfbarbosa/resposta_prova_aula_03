#   [LP-A03] Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número 
#   inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja
#   ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#   Tabuada de 5:
#   
#   5 X 1 = 5
#   
#   5 X 2 = 10
#   
#   ...
#   
#   5 X 10 = 50

numero = int(input("Digite um número de 1 à 10: "))
resultado = 0
if numero < 1 or numero > 10:
    print(f"O valor {numero} é inválido!")
    print(f"Por favor, informe um número de 1 à 10.")
else:
    for i in range(1,11):
        resultado = numero * i
        print (f"{numero} x {i} = {resultado}")