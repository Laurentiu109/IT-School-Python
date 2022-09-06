from math import pi
from datetime import datetime
from typing import Type

def circle_area(radius):
    """" Calculeaza aria cercului, doar pentru numere pozitive.

    Args:
        * radius int or float : Raza cercului.
        

    Returns : 
        float: Aria cercului.

    Raises:
        * ValueError : Daca radius este numar negativ.
        * TypeError : Daca radius nu este numar.
    """
    if isinstance(radius, float) or isinstance(radius, int):
        if radius < 0:
            raise ValueError("Nu pot calcula aria pentru un numar negativ.")
        
        return pi * radius ** 2
            
    else:
        raise TypeError("Nu pot calcula aria pentru parametru introdus.")   # se creeaza un obj nou de tip exceptie


def cylinder_volume(radius, height):
    return circle_area(radius) * height

# height = int(input("Intaltime: "))
# radius = int(input("Raza: "))
# print(f"Volum cilindru : {cylinder_volume(radius, height)}")
    

# circle_area(None)

try:
    print(circle_area("str"))
    print(circle_area(10)) # nu se executa daca ai exceptie
except (ValueError, TypeError) as err:
    print(f"{datetime.now()} [ERROR] {err}")


print(circle_area(2))

l1 = [2.3, "re", None, 4, 10, -2, 33]

for i in l1:
    try: 
        print(circle_area(i))
    except (TypeError, ValueError) as err:
        print(f"{datetime.now()} [ERROR] {err}")


# print(circle_area({}))
# print(circle_area([]))
# print(circle_area("dkjsakdsa"))
# print(circle_area(2))
# print(circle_area(-3))
# print(circle_area)
# print(circle_area)
# print(circle_area)