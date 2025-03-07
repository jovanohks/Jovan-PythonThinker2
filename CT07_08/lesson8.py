print("Hello from lesson 8")


#Q1
order = []
userwant=""
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