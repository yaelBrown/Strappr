open = True
selection = 0

def menu():
  print("Select an option")
  print("1 New App")
  print("2 App from Config")
  print("3 Setup")
  print("4 About")
  print("5 Exit")
  selection = input("input option here: ")

  def menuSelection(selection):
    if type(selection) != int:
      selection = input("Invalid menu option. Try again")
      return menuSelection(selection)

    def exit():
      open = False
      return print("Exit")

    switcher = {
      1: print("New App!"),
      2: print("App from config"),
      3: print("Setup"),
      4: print("About"),
      5: exit()
    }


    if selection in switcher.keys():
      return switcher.get(selection, 0)
    else:
      switcher = 0
      menu()

  menuSelection(selection)


while open == True:
  menu()



# input is coming in as string and needs to be catched.
# need to add try catch for line 13/14 ish