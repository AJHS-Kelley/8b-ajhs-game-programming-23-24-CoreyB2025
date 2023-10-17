playerInventory = []

while len(playerInventory) < 10:
    item = input("What item do you want to add to the imventory?\n")
    playerInventory.append(item)

playerInventory.sort()
print(playerInventory)

when len(playerInventory) > 5:
    item = input("What item do you want to remove to the imventory?\n")
    playerInventory.renive(item)





