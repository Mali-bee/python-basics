#Shopping cart project - by Malibongwe Makhubo

print()

food_stock = []                         #declaring lists to store the multiple values
price_stock = []
total = 0
print("Type EXIT or QUIT when finished entering values...")

while True:                             #use while loops so that it keeps running until we tell it to stop
    food_name = input("Enter name of food: ")
    if food_name == "exit":
        break
    elif food_name == "quit":
        break
    
    else:
        prices = float(input(f"Enter price of {food_name}: "))
        food_stock.append(food_name)
        price_stock.append(prices)

total = sum(price_stock)                #to add up the prices of the products
food_stock.sort()                       #to sort the list in alphabetical order
print()

#print(food_stock, price_stock, total)
print("--------CART-------")
for f_list in food_stock:
    print(f_list, end= " | ")
    
for p_list in price_stock:
    print(p_list)

print("\n")    
print(f"Total: R{total}")
print()
