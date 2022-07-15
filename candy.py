from inventory import *


def main():
    candyInStock = [{"Candy Type": "Candy Bar", "Flavor": "Chocolate"},
                    {"Candy Type": "Gummie", "Flavor": "Orange"}]
    allowedCandy = ["Candy Bar", "Gummie", "Popsicle"]
    allowedCandyListMaxSize = [{'Candy Type': "Candy Bar", 'Max Amt': 3},
                               {'Candy Type': "Gummie", 'Max Amt': 4},
                               {'Candy Type': "Popsicle", 'Max Amt': 5}]

    while True:
        selection = input(
            "\nEnter 1 to add candy, \n2 to remove last candy from inventory, \n3 to remove one candy from inventory, \n4 to list inventory, \n5 to clear inventory, \n0 to exit: ")
        if selection == '1':
            candyInStock = add_Candy(candyInStock, allowedCandy, allowedCandyListMaxSize)
        elif selection == '2':
            candyInStock = remove_last_candy_added(candyInStock)
        elif selection == '3':
            candyInStock = remove_Candy(remove_Candy(candyInStock))
        elif selection == '4':
            show_Inventory(candyInStock)
        elif selection == '5':
            clear_Inventory(candyInStock)
        elif selection == '0':
            print("Session ended\n")
            quit()


main()


