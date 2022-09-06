class Pen:

    #atribut de clasa
    brand = 'Noki'

    def __init__(self, color) -> None:
        self.color = color
        self.is_empty = False


pen = Pen("red")
pen2 = Pen("black")

print(pen.color)
print(pen2.color)

pen2.brand = "pen2-brand"

# pen2.owner = "Mihai"  # creeaza un atribut de instanta

# print(pen2.owner)

print(Pen.brand)

print(pen2.brand)