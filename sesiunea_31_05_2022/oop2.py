from auto import Car


volvo = Car()
vw = Car() # aici se apeleaza constructorul automat


# print(volvo.get_gas())


# accesare atribuite

print("Volvo gas:" , volvo.get_gas())
print("VW gas:", vw.get_gas())
# print("Nivel combustibil: ", auto.get_gas(),"%")

volvo.refill_full()
vw.refill(20)
print("-" * 50)

print("Volvo gas:", volvo.get_gas())
print("VW gas:", vw.get_gas())