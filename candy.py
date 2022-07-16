from inventory import *


def main():
    candyInStockArray = [{"Candy Type": "Candy Bar", "Flavor": "Chocolate"},
                         {"Candy Type": "Gummie", "Flavor": "Orange"}]
    allowedCandyList = ("Candy Bar", "Gummie", "Popsicle")
    allowedCandyListMaxSize = [{'Candy Type': "Candy Bar", 'Max Amt': 3},
                               {'Candy Type': "Gummie", 'Max Amt': 4},
                               {'Candy Type': "Popsicle", 'Max Amt': 5}]

    while True:
        selection = input(
            "\nEnter \n1 - to add candy \n2 - to remove last candy from inventory \n3 - to remove one candy from "
            "inventory \n4 - to list inventory \n5 - to clear inventory \n0 - to exit:\n")
        if selection == '1':
            candyInStockArray = add_Candy(candyInStockArray, allowedCandyList, allowedCandyListMaxSize)
        elif selection == '2':
            candyInStockArray = remove_last_candy_added(candyInStockArray)
        elif selection == '3':
            candyInStockArray = remove_Candy(candyInStockArray)
        elif selection == '4':
            show_Inventory(candyInStockArray)
        elif selection == '5':
            clear_Inventory(candyInStockArray)
        elif selection == '0':
            print("Session ended\n")
            quit()


main()
