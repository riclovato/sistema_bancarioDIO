menu = """
(1) DEPOSITAR
(2) SACAR
(3) EXTRATO
(0) SAIR
"""
saldo = 0
limite = 500
extrato = ''
saque_cont = 0
saque_disponivel = 3
SAQUE_LIMITE = 3

while True:
    op = int(input(menu))

    match op:
          case 1:
               deposito = float(input("Digite o valor do depósito: "))
               if deposito > 0:
                    saldo += deposito
                    extrato += f"Depósito: R$ {deposito:.2f}\n"
               else:
                    print("Operação inválida!")

          case 2:
               print(f'{saque_disponivel} saques disponíveis! ')
               saque = float(input("Informe o valor do saque: "))

               if(saque > 0 and saque < (saldo + limite) and saque_cont < SAQUE_LIMITE):
                    saldo -= saque
                    extrato += f"Saque: R$ {saque:.2f}\n"
                    saque_cont += 1
                    saque_disponivel -= 1

               else:
                    print("Operação inválida!")
                    print(f'{saque_disponivel} saques disponíveis! ')
          case 3:
               if extrato:
                    print('=====================')
                    print(extrato)
                    print(f'saldo: {saldo:.2f}')
                    print('=====================')
               else:
                    print("Nenhuma transação registrada.")
          case 0:
               print("encerrando ...")
               break;
          case _:
                 print("Opção inválida, digite novamente: ")