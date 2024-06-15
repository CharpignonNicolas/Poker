# Definition of the Pot class
class Pot:
    def __init__(self):
        self.amount = 0

    def add(self, amount):
        self.amount += amount
        print(f"\n{amount} ajoutés au pot.")
        print (f"Total Pot: {self.amount}\n")

    def reset(self):
        self.amount = 0

    def __repr__(self):
        return f"Pot: {self.amount}"