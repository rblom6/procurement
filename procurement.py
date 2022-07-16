from ActionsPrompt import ActionsPrompt
from Owner import Owner

def main():
    """ First calls create_db to create a local database containing a
    table called Inventory and populates it with the contents of the csv file.
    Allows the user to create as many owners as they want to. The user can select any owner at any point, 
    and call the various functions on them.

    When the "What would you like to do next?" prompt appears, the user can either
    "create owner", "buy inventory", "sell inventory", "check net worth", or "quit".
    """
    Owner.create_db("items.csv")
    actionsPrompt = ActionsPrompt()
    print("Hello! Welcome to the procurement simulation.")
    next = True
    while(next == True):
        try:
            next = actionsPrompt.ask_action()
        except:
            print("Something went wrong")
            break
    Owner.drop_db()



if __name__ == "__main__":
    main()
