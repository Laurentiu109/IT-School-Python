class Ticket:
    
    
    def __init__(self, price):
        # Atribute de instanta
        self.price = price

    # Metode de instanta
    def get_price_w_taxes(self):
        return self.price + self.price * 0.19

    # definire metoda statica
    @staticmethod
    def get_tva_ratio(): # metodele statice nu au nevoie de self
        return 0.19

    @staticmethod
    def stm():
        print("TVA:", Ticket.get_tva_ratio())


# instantiere
tk = Ticket()

# tk = obiect = instanta
# tk.get_price_w_taxes()
tk.stm()
Ticket.stm()

# print(Ticket.get_tva_ratio())