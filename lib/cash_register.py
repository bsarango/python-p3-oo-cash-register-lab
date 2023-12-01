#!/usr/bin/env python3

class CashRegister:
    
    #if the variables are set outside, the values will 
    def __init__(self,discount=0):
        self.discount = discount
        self.total = 0  #must initialize instance variable inside of __init__ for it to 'reset' on each instance
        self.items = []
    
    def add_item(self,item,price,quantity=1):
        self.total += (price * quantity)
        for i in range(quantity):
            (self.items).append(item)
            self.most_recent_item = {"price":price,"quantity":quantity}
    
    def apply_discount(self):
        if self.discount != 0:
            amount_discount = int((self.total) * ((self.discount)/ 100))
            self.total -= amount_discount 
            print(f"After the discount, the total comes to ${(self.total)}.")
        else:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        for i in range (self.most_recent_item["quantity"]):
            (self.items).pop()
            self.total -= self.most_recent_item["price"]