# Lesson 5 - List Variables II

## Recap 1: Favourite Food List
# **Recap 1a**:
# Create a list of 5 foods that you like to eat

# **Recap 1b**:
# You no longer like to eat the 3rd item on your list,
# delete it

# **Recap 1c**:
# Add 1 more item into your list

# **Recap 1d**:
# Write a for loop to say all the food items in your list

favouriteFood=["dino minosaur","wanton mee","chicken rice with wasabi","fishball noodles","fried rice"]
# favouriteFood.pop(2)
# favouriteFood.append("sushi")
# favouriteFood.remove("chicken rice with wasabi")
del(favouriteFood[2])
favouriteFood.insert(4,"sushi")
for food in favouriteFood:
    print(food)


