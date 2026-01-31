import random

#Inicio

print('##########################')
print('-------Bem - Vindo--------')
print('##########################')
   
while True:
    continuar = input("Você deseja continuar? (sim/não): ").lower().strip()
    if continuar in ['sim', 's', 'não', 'nao', 'n']:
        break
    print("Por favor, responda com 'sim' ou 'não'.")

if continuar in ['sim', 's']:
    print("Daremos continuidade")
else:
    print("Ok")
    exit()

#Informações

nome_do_usuario = input('Por favor, digite como deseja ser chamado:')

print('Muito bem', nome_do_usuario, 'Daremos inicio ao nosso jogo de adivinhação')
numero_certo = random.randint(1, 10)

while True:
    chute_str = input("Digite seu numero:")
    chute_int = int(chute_str)

    if chute_int == numero_certo:
         print("Voce acertou. Parabens!", nome_do_usuario)
         break
    
    elif chute_int < numero_certo:
        print('Tente um numero MAIOR')
    else:
        print('Tente um numero MENOR')






