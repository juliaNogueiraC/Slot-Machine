MAX_LINES = 5

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

def main(): # criar o menu principal
  balance = deposit()
  lines = get_number_of_lines()
  print(balance, lines)
  

main()