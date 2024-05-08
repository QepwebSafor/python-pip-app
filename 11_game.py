import random

def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input ('Piedra, papel o tijera =>')
  user_option=user_option.lower()

  if user_option not in options:
    print('Opción no válida')
    #continue
    return None, None
  computer_option= random.choice(options)
  print('user option =>', user_option)
  print('Computer option =>', computer_option)
  return user_option, computer_option
def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user gano!')
      user_wins +=1
    else:
      print('Papel gana a piedra')
      print('computer ganó!')
      computer_wins +=1
  elif user_option == 'papel':
    if computer_option == 'tijera':
      print('tijera gana a papel')
      print('computer ganó') 
      computer_wins +=1
    else:
      print('papel gana a piedra')
      print('user ganó')
      user_wins +=1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user ganó!')
      user_wins +=1
    else:
      print('piedra gana a tijera')
      print('computer ganó')
      computer_wins +=1

  return user_wins, computer_wins
def who_wins(user_wins, computer_wins):
  if computer_wins == 2:
      return'El ganador es la computadora'
    
  if user_wins == 2:
      return 'El ganador es el usuario'
      
def run_game():
  user_wins= 0
  computer_wins=0
  rounds =1
  while True:
    print('*' *10)
    print('ROUND', rounds)
    print('*' * 10)
    print ('computer wins', computer_wins)
    print ('user wins', user_wins)
    rounds +=1
    user_options, computer_options =choose_options()    
    user_wins, computer_wins =check_rules(user_options, computer_options, user_wins, computer_wins)
    winner= who_wins(user_wins, computer_wins)
    print(winner)
run_game()
