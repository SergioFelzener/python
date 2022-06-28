name = "Sergio Felzener"
old = 40

list = ["blue", "green", "red", name, old] # colors list , name and old

print(list)

list.append("purple")
list.remove(name)
list.remove(old)
list.append("white")
list.append("black")
#loop for in list
for item in list:
    print(item)

print(list[0])
print(list[-1])

print(name[3:])

for letra in name:
    print(letra)
