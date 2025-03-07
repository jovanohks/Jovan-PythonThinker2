print("Hello from lesson 8")


#Q1
order = [] # list  to store food user wants
userwant="" #a variable to store the
while True:
    userwant= input("What would you like to order? ") #ask user for what food to add to order
    if userwant == "end":
        break #if user type end, end the program
    else:
        order.append(userwant) #append what user has ordered to the stuff that user want
print("You have ordered the following:")
for items in order:
    print(str(order.index(items)+1)+". "+items) #print the index of items plus 1 , and tell user what he has ordered







#Q2