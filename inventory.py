def add_Candy(candyInStock, allowedCandy, allowedCandyListMaxSize):
    candyType = input("What type of candy are you trying to add? Choose Candy Bar, Gummie, or Popsicle: ")
    candyFlavor = input("What flavor of candy is it? ")

    candy = {"Candy Type": candyType,
             "Flavor": candyFlavor}

    if candy in candyInStock:
        print("We have that candy in stock already")
    elif candy["Candy Type"] not in allowedCandy:
        print("We do not stock that type of candy")
    else:
        count = 0
        for x in candyInStock:
            if x["Candy Type"] == candy["Candy Type"]:
                count += 1
        for y in allowedCandyListMaxSize:
            if y["Candy Type"] == candy["Candy Type"]:
                maxAmt = y["Max Amt"]
        if count >= maxAmt:
            print("We have enough of that candy in stock")
        else:
            candyInStock.append(candy)
            print(candy["Candy Type"] + " " + candy["Flavor"] + " added to inventory.")
            return candyInStock
    return candyInStock


def remove_last_candy_added(candyInStock):
    print("Oops!")
    candyInStock.pop()
    return show_Inventory(candyInStock)



def remove_Candy(candyInStock):
    candyType = input("What type of candy is being removed?: ")
    candyFlavor = input("What flavor of candy is it?: ")

    candyToRemove = {"Candy Type": candyType,
                     "Flavor": candyFlavor}
    if candyToRemove not in candyInStock:
        print("We do not have that candy in stock")
    else:
        if candyToRemove in candyInStock:
            candyInStock.remove(candyToRemove)
            print("Candy removed.")
            return candyInStock


def show_Inventory(candyInStock):
    print("Candies in stock: ")
    count = 0
    for candy in candyInStock:
        print(candy)
        count += 1
    print(f'Total number: ', count)


def clear_Inventory(candyInStock):
    candyInStock.clear()
    print("Inventory cleared")
    print(f'Amount of candies in stock: ', len(candyInStock))


candyInStock = []
allowedCandy = ["Candy Bar", "Popscicle", "Gummie"]
