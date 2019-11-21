from category import Category

class Store:
    def __init__(self, name, categories=[], address=None, established=None):
        self.name = name
        self.categories = categories
        self.address = address
        self.established = established

    # so that we can print it
    def __str__(self):
        output = ''
        output += f'Welcome to {self.name} \n'
        i = 1
        for category in self.categories:
            output += f'{i}. {category.name} \n'    
            i += 1
        output += f'{i}. Exit'
        return output
    
    def __repr__(self):
        return f'this was called as: Store({self.name}, {self.categories})'
    

# create several categories
running_category = Category('running', 'shoes and other gear', 'F2')
basketball_category = Category('basketball', 'hoops and balls', 'F1')
baseball_category = Category('baseball', 'bats and bases', 'F3')

# create an instance of our store
sports_store = Store(
    'Lambda Sports', 
    categories=[running_category, basketball_category, baseball_category]
)
# get me the __str__ function of the instance
# print essentially calls sports_store.__str__()
print(sports_store)

# REPL (Read, evaluate, print, loop)
selection = 0
# LOOP
while selection != len(sports_store.categories) + 1:
    # READ
    selection = input("Select the number of a department: ")
    # Evaluate
    try:
        selection = int(selection)
        if selection == len(sports_store.categories) + 1:
            # print
            print("Thank you for shopping!")
        elif selection <= 0 or selection > len(sports_store.categories):
            # print
            print("Error, please enter a valid number")
        else: 
            # print
            print(sports_store.categories[selection - 1])
    except ValueError:
            # print
        print("Error, input was not a number")