#print("Hello  World")

#Control Statements
"""""""""
num_age = int(input("Enter your age: ")) #to get user input, and then convert to integer

if num_age >= 18:
    print(num_age, "years old. You are legal and can have a drink.")
elif num_age < 18:
    print(num_age, "years old. You are a minor.")
else:
    print("error, invalid entry")
"""""""""    

#===============================================================
#LOOPS
#for loops

fruits = ["apple", "banana", "strawberry", "mango", "lime"]

for itemListed in fruits:
    print(itemListed)
    
print()
"""""""""
for m in fruits:
    if m == "strawberry":
        break               #exists the loop if strawberry is found
    print(m)
    
print()

for q in fruits:
    if q == "strawberry":
        continue            #skips and moves to the next iteration
    print(q)
  
print()

for ama in fruits:
    if ama == "strawberry":
        pass                #placeholder, no sction needed for strawberry. Used for editing the list, saying skip this one,don't edit anything here
    print(ama)   
 
print()   

numbers = [18, 28, 1997, 44, 9]

for numbersListed in numbers:
    print(numbersListed)
"""""""""  


#while loops
count = 0           #using a while loop to count from one to another

while count <= 5:
    print(count)
    count = count + 1   #increment the counts
    if count == 3:
        break           #exists the loop when the count is found
    
