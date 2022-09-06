# scrieti o clasa Shape

# care are o metoda arie




# scrieti o clasa Circle care mosteneste Shape si suprascrie metoda arie

# scrieti o clasa Square care mosteneste Shape si suprascrie metoda arie


from cmath import pi


class Shape:

    def aria(self):
        pass

class Circle(Shape):
    
    def aria(self, r):
        return 3.14 * r ** 2

class Square(Shape):

    def aria(self, l):
        return l ** 2


patrat = Square()

cerc = Circle()


print(patrat.aria(10))

print(cerc.aria(14))


