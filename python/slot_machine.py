import random

def play():
  symbols = ['🍒', '🍇', '🍉', '7️⃣']
  results = f"{random.choices(symbols)[0]} | {random.choices(symbols)[0]} | {random.choices(symbols)[0]}"

  if results == f"{symbols[3]} | {symbols[3]} | {symbols[3]}":
    print(results)
    print('Jackpot!')
  else:
    print(results)
    print('Better luck next time!')
retry = True
while retry:
  play()
  print('Would you like to try again?')
  play_again = input('Y/N')
  if play_again in ['Y', 'y']:
    continue
  else:
    retry = False