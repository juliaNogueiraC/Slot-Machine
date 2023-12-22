import random

MAX_LINES = 5
MAX_BET = 100
MIN_BET = 1


ROWS = 3
COLS = 3

symbol_count = { # Dictionary to keep track of the number of symbols in each row
  "A": 2,
  "B": 4,
  "C": 6,
  "D": 8
}

def get_slot_machine_spin(rows, cols, symbols): # quais simbolos estarão em cada linha e coluna
  
  

def deposit(): #coletar a entrada do deposito do usuário
  while True:
    amount = input("Digite o valor do deposito: ")
    if amount.isdigit(): # checar se o amount é um numero
      amount = int(amount)
      if amount > 0: # checar se o amount é maior que 0
        break
      else:  
        print(f"{amount} é um valor inválido.")
    else:
      print("Digite apenas números.")
  return amount

#deposit()

def get_number_of_lines(): #coletar a entrada do numero de linhas do usuário
  while True:
    lines = input("Coloque o número de linhas para apostar (1-" + str(MAX_LINES) +
      ")? ")
    if lines.isdigit(): # checar se o amount é um numero
      lines = int(lines)
      if  1<= lines <= MAX_LINES: # checar se o amount é maior que 0
        break
      else:  
        print(f"{lines} é um valor inválido.")
    else:
      print("Digite apenas números.")
  return lines


def get_bet(): #coletar a entrada do aposta do usuário
  while True:
    amount = input("Digite o valor para aposta: $ ")
    if amount.isdigit(): # checar se o amount é um numero
      amount = int(amount)
      if MIN_BET <= amount <= MAX_BET: # checar se o amount é maior ou menor que o maximo e minino
        break
      else:  
        print(f"{amount} é um valor inválido. Deve ser Entre ${MIN_BET} e ${MAX_BET}.")
    else:
      print("Digite apenas números.")
  return amount


def main(): # criar o menu principal
  print("Bem vindo ao cassino Blackjack!")
  print("---------------------------------")
  balance = deposit()
  lines = get_number_of_lines()

  while True: # checar se o usuário tem saldo o sufiente para continuar jogando
    bet = get_bet()
    total_bet = bet * lines

    if total_bet >= balance:
      print("-------------------------------------------------")
      print(f"|Você não tem saldo suficiente para apostar ${total_bet}.|")
      print("-------------------------------------------------")
    else:
      break
  print("---------------------------------")
  print(f"Seu depósito é de ${balance}, em {lines} linhas, ${bet} de apostas.")
  print(f"Você esta apostando ${total_bet}.")
  

  

main()