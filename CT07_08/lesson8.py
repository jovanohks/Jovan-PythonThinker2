print("Hello from lesson 8")


#Q1
order = [] # list  to store food user wants
userwant="" #a variable to store the
while True:
    userwant= input("What would you like to order? ")
    if userwant == "end":
        break
    else:
        order.append(userwant)
print("You have ordered the following:")
for items in order:
    print(str(order.index(items)+1)+". "+items)







#Q2