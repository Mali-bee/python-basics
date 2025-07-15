# Dictionary - 
# indexed by key (of any data type)
# orderd, changeable, does not allow duplicates

learn_the_dictionary = {
    "ID" : 18,
    "hero" : "Batman",
    "year" : 1939,
    "color" : "black",
    "active" : True
}

print()
print(learn_the_dictionary)
print(learn_the_dictionary.keys())              # to print the keys of the array
print(type(learn_the_dictionary))
print()

print(learn_the_dictionary["hero"])
print()

learn_the_dictionary["hero"] = "Black Panther"
learn_the_dictionary["year"] = 1969
print(learn_the_dictionary)
print()