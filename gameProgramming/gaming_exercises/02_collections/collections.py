playerInventory = []

while len(playerInventory) < 10:
    item = input("What item do you want to ad to the imventory?\n")
    playerInventory.append(item)

playerInventory.sort()
print(playerInventory)







