"""

"""
lista = [1,2,3,4,5,6,7,8,9]
for indice, valor in enumerate(lista):
    print(indice,valor)

# Python program to illustrate
# enumerate function
l1 = ["eat","sleep","repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Return type:",type(obj1))
print(list(enumerate(l1)))

# changing start index to 2 from 0
print(list(enumerate(s1,2)))