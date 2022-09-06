from datetime import datetime
from time import time
import time

# debug decorator
# def cube_volume(edge):

#     # 1 m3 = 1000 litri
#     return edge ** 3 * 1000

# def reverse(n):
#     rev = 0
#     while n != 0:
#         c = n % 10 # rest
#         n = n // 10 # cat
#         rev = rev * 10 + c

#     return rev

    

l = 29

# print("S-a apelat functia cube_volume la ora", datetime.now() , "pentru edge = ", l)

# start = time.time()
# cube_volume(l)
# stop = time.time()

# print("Apelul a durat x secunde", stop - start)


def debuger(f):
    def inner(*args):
        print("S-a apelat functia xxx la ora", datetime.now(), "pentru argumentele", args)
        start = time.time()
        print("Rezultatul apeului", f(*args))
        stop = time.time()
        print("Apelul a durat x secunde", stop - start)
        f(*args)

    return inner

@debuger
def cube_volume(edge):
    return edge ** 3 * 1000

@debuger
def reverse(n):
    rev = 0
    while n != 0:
        c = n % 10 # rest
        n = n // 10 # cat
        rev = rev * 10 + c

    return rev

cube_volume(10) # debuger(cube_volume(10))

# inner(10)
reverse(234)