#learning strings in python
#in Python you don't have to state the data type when declaring vairables

message = " Hello World, nice to meet you. Mali here learning Python "

print(message) #to display what's in the variable
"""""""""
print(message[0]) #to pull and display the character at the index which is index 0
print(message[6])

print(message[-1]) # to pull and display from the last character in the variable
"""""""""
print(len(message)) #to pull the amount of characters (how long) the string is inlcuding white space

print(message.strip()) #remove leaving and trailing whitespace
print(message.lower()) #convert all characters to lowercase
print(message.split('.')) #split the string into a list based on the comma or full stop
print(message.upper()) #convert all characters to uppercase
print(message.replace('Mali','Thando')) #replace one character(s) with another

#OPERATORS WITH STRINGS
msg_one = "Yebo"
msg_two = "South"
msg_three = "Africa!!"
print(msg_one+ " " +msg_two+ " " +msg_three)
print(msg_three* 5)