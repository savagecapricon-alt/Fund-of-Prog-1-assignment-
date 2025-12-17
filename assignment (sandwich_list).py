#7-8 list of sandwitch orders
sandwich_orders = ['BLT','Classic club','Grilled cheese','Panini','Brochette']
finished_sandwiches=[]
print(sandwich_orders)

#Messsage for placing orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich!!!")
finished_sandwiches.append(current_sandwich)

#List of each sandwich made
print("\nSandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)

#7-9 Pastrami appearing in list at list 3 times
sandwich_orders=['Pastrami','BLT','Classic club', 'Pastrami','Panini','Brochette', 'Pastrami']
finished_sandwiches=[]
print("Sorry, the deli has run out of pastrami.\n")

#Removing all occurences of pastrami
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

#Making the rest of the sandwiches
while sandwich_orders:
    current_sandwich =sandwich_orders.pop(0)
    print(f"Your {current_sandwich} sandwich is ready!!!")
finished_sandwiches.append(current_sandwich)

#The final list
print("\nSandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)
