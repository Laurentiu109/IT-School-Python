# algoritm numere prime


n = 29
prim = True

for i in range(2, n):
    if n % i == 0:
        prim = False
        break

if prim:
    print("Numar prim")
else:
    print("Numarul nu este prim")