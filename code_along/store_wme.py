
from category_wme import Category

class Store:
  def __init__(self, name, categories=[], address=None, established=None):
    self.name = name
    self.categories = categories
    self.address = address
    self.established = established

  def __str__(self):
    output = ''
    output += f'Welcome to {self.name} \n'
    for index, category in enumerate(self.categories):
      output += f'{index+1}. {category.name} \n'

    output += f'{len(self.categories) + 1}. Exit'
    
    return output

  def __repr__(self):
    return f'this was called as: Store({self.name}, {self.categories})'

running_category = Category('running', 'shoes and other gear', 'F2')
basketball_category = Category('basketball', 'hoops and balls', 'F1')
baseball_category = Category('baseball', 'bats and bases', 'F3')

sports_store = Store(
  'Lambda Sports',
  categories=[running_category, basketball_category, baseball_category]
)
print(sports_store)

# REPL (Read, evaluate, print, loop)
# READ
selection = 0
# LOOP
while selection != len(sports_store.categories) + 1:
  selection = input("Select the number of a department: ")
  try:
    # EVALUATE
    selection = int(selection)
    # PRINT
    if selection == len(sports_store.categories) + 1:
      print("Thank you for shopping!")
    elif selection <= 0 or selection > len(sports_store.categories) + 1:
      print("Error, please enter a valid number")
    else:
      print(f'the user selected: \n{sports_store.categories[selection - 1]}')
  except ValueError:
    print("Error, input was not a number")
