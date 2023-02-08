from SingleOrder import SingleOrder


def order():
    order = SingleOrder()
    print("Hello welcome to Lia's Restaurant's takeout page!")
    print("1. Brussel Sprouts\n2. Pepperoni Pizza\n3. Chicken Bella\n4. Rigatoni Carbonara")
    item_num = int(input("Please choose the number item that you would like to order: "))
    if order.setItemNum(item_num) == -1:
        return -1
    delivery = input("Would you like it delivered (y/n): ")
    order.setDelivery(delivery == 'y')
    tip = input("Would you like to tip (y/n): ")
    if tip == 'y':
        tip_amount = float(input("Enter tip amount (0.00 to 0.40): "))
        if order.setTip(tip_amount) == -1:
            return -1
    total_cost = order.calcTotalCost()
    print("Total cost of your order: $%.2f" % total_cost)
    return total_cost

order()