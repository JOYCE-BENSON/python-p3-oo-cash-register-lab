#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0
        self.last_transaction_items = 0
    
    def add_item(self, title, price, quantity=1):
        transaction_amount = price * quantity
        self.total += transaction_amount
        
        # Add the item to the items list, repeating for quantity
        for _ in range(quantity):
            self.items.append(title)
            
        # Store last transaction details
        self.last_transaction_amount = transaction_amount
        self.last_transaction_items = quantity
    
    def apply_discount(self):
        if self.discount > 0:
            discount_amount = int(self.total * (self.discount / 100))
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        # Subtract the last transaction amount from the total
        self.total -= self.last_transaction_amount
        
        # Remove the last added items from the items list
        for _ in range(self.last_transaction_items):
            if self.items:
                self.items.pop()
        
        # Reset the last transaction tracking
        self.last_transaction_amount = 0
        self.last_transaction_items = 0

