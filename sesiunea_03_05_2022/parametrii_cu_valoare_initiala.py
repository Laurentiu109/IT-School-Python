"""

def hello(name="Guest"):
    print("Hello and welcome", name)

hello()
hello("Laurentiu")

"""

def b_range(stop, sep="+", sep_c=10):
    for i in range(stop):
        print(i, end="")
        print(sep * sep_c)

# b_range(10, "*", 10)

# b_range(10, "=", 10)
# b_range(5, "=", 10)
# b_range(20, "=", 10)

b_range(5, sep_c=20)