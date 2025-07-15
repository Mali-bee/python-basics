# Sets {} - a data structure
# doesn't allow duplicates, eg; {"egg", "bacon", "cheese", "egg", "toast"} won't work, egg appears more than once

learn_sets = {"SA", "SD", "Zim", "Moz", "LST"}
print(learn_sets)
print(type(learn_sets))
print()

learn_sets.add("Nam")
print(learn_sets)
print()

learn_sets.remove("Zim")
print(learn_sets)
print()

#union
set1 = {10, 20, 30}
set2 = {30, 40, 50}

union_set = set1.union(set2)        #combines and removes the duplicate
print(union_set)
print()

#intersection
inter_set = set1.intersection(set2)     #combines and points out the duplicate value
print(inter_set)
print()

#difference
diff_set = set1.difference(set2)
print(diff_set)
# print(type(diff_set))
print()