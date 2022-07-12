from inventory import add_Candy, remove_Candy, show_Inventory
from profit import calculate_Profit


def main():
    candyInStock = [{"Candy Type": "Candy Bar", "Flavor": "Chocolate"},
                    {"Candy Type": "Gummie", "Flavor": "Orange"}]
    allowedCandy = ["Candy Bar", "Gummie", "Popsicle"]
    allowedCandyListMaxSize = [{'Candy Type': "Candy Bar", 'Max Amt': 3},
                               {'Candy Type': "Gummie", 'Max Amt': 4},
                               {'Candy Type': "Popsicle", 'Max Amt': 5}]

    while True:
        selection = input(
            "\nEnter 1 to add candy, 2 to remove candy, 3 to list candy, 4 to calculate cost of all candy, 0 to exit: ")
        if selection == '1':
            candyInStock = add_Candy(candyInStock, allowedCandy, allowedCandyListMaxSize)
        elif selection == '2':
            candyInStock = remove_Candy(candyInStock)
        elif selection == '3':
            show_Inventory(candyInStock)
        elif selection == '4':
            calculate_Profit(candyInStock)
        elif selection == '0':
            print("Session ended\n")
            quit()


main()

