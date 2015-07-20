#customer making a purchase if stock of the item in the shopping list is >0
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(food):
    total = 0
    for item in food:
        if (stock[item]>0):
            total += prices[item]
            stock[item] = stock[item]-1
    print total
    return total

compute_bill(shopping_list)