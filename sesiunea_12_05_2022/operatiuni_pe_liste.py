user_id = [33, 455, 3, 32 ,34, 12, 90, 234]
leader_board = ['Alex', 'Zeorge', 'Ionut']
print(user_id)

# Lungimea listei

print("Lungimea listei:", len(user_id))

# Maximul listei
print("Maximul listei:", max(user_id))
print(max(leader_board))

# Minimul listei
print("Minimul listei:", min(user_id))
print(min(leader_board))

print("-" * 30)


# adaugare element nou - append
user_id.append(100)
print(user_id)
print("lungimea listei:" , len(user_id))

# stergere element
user_id.remove(3)
print("Dupa remove")
print(user_id)


# verificare daca valoare face parte din lista
# value_to_remove = int(input("Remove value:"))

# if value_to_remove in user_id:
#     user_id.remove(value_to_remove)
# else:
#     print("Valoarea nu exista in lista.")


# numarul de aparitii al unui element
print("elementul 33 apare de" , user_id.count(33), "ori")

# insert la index 
user_id.insert(1, 0)
user_id.insert(-1, 0)

print("Dupa insert 0")
print(user_id)


# gasesti indexul unei valori
index_magic = user_id.index(32)
user_id.insert(index_magic +1 , "x")

print("Dupa index magic")
print(user_id)

# reversul listei !! opereaza pe lista


# list sliceing

#list copy


print("END")