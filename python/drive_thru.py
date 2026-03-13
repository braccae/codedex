# Write code below 💖

def get_item(x):
  menu = [
    'Taco',
    'Burg',
    'Brug supreme',
    'Pizza',
    'Corn Doggo',
    'Ocean water'
  ]
  return menu[x - 1]

def welcome():
  print("""
  Welcome to AU sonic, Here is our menu

  1.) Taco
  2.) Burg
  3.) Brug supreme
  4.) Pizza
  5.) Corn Doggo
  6.) Ocean water
  """)

welcome()

while True:
  order = int(input("Please place your order from the menu: "))
  if order > 6 or order < 1:
    print("Invalid order, please pick from the menu.")
  else:
    print(f"You have ordered [{get_item(order)}]")
    break