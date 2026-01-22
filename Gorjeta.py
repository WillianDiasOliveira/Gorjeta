import os

def main():
        os.system('cls')
        conta()

def conta():
        valor_conta = float(input('Digite o valor da conta: '))
        porcentagem_gorjeta = float(input('Digite a porcentagem da gorjeta: '))

        gorjeta = (porcentagem_gorjeta / 100) * valor_conta
        valor_pagar = valor_conta + gorjeta

        print(f'\nO valor da gorjeta é de R${gorjeta:.2f}')
        print(f'O valor da conta é de R${valor_conta:.2f}')
        print(f'\nO valor total a pagar é de R${valor_pagar:.2f}\n')

if __name__ == '__main__':
        main()  



'''             CONTEXTO:
        Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. 
        O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.
'''