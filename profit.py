def calculate_Profit(candyInStock):
    qty = 0
    for candy in candyInStock:
        #print(candy)
        qty += 1
    retail_total = qty * 3.00
    print(f'Total candies in the shop: {qty}')
    print(f'Total retail value: ${retail_total:.2f}')
    profit = retail_total * .25
    print(f'Total profit to be made if all candies sold: ${profit:.2f}')