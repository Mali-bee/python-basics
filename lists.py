# Lists [] - a python data structure
# lists are ordered (new itemsplaced at the end of the list), change-able, update-able, and allow duplicates

heroes = ["Batman", "Stom", "Static Shock", "Incinvible", "Wonder Woman"]
print(heroes)
print(type(heroes))
print()

print(heroes[4])                #print the value of this index
print()

heroes[3] = "Queen Maeve"       #replace the value at the selected index with a new value
print(heroes)
print()

heroes.append("All Might")      #add a new value to the list
print(heroes)
print()

heroes.insert(2, "Ichigo")      #insert new value at the selected index
print(heroes)
print()

heroes.remove("Queen Maeve")    #deletes teh value at the selected index
print(heroes)
print()

heroes.sort()                   #organises the lists
print(heroes)
heroes.sort(reverse=True)       #organises the list in reverse order   
print(heroes)
print()