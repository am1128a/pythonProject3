class SingleOrder:
    def __init__(self):
        self.item_num = 0
        self.delivery = False
        self.tip = 0.0
        self.menu = {1: 1.99, 2: 2.99, 3: 3.99, 4: 4.99}

    def setItemNum(self, item_num):
        if item_num in self.menu:
            self.item_num = item_num
        else:
            return -1

    def setDelivery(self, delivery):
        self.delivery = delivery

    def setTip(self, tip):
        if 0.00 <= tip <= 0.40:
            self.tip = tip
        else:
            return -1

    def calcTotalCost(self):
        base_price = self.menu[self.item_num]
        delivery_fee = 5.99 if self.delivery else 0
        tip_amount = base_price * self.tip
        tax = (base_price + delivery_fee) * 0.10
        total_cost = base_price + delivery_fee + tip_amount + tax
        return total_cost
