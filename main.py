import art
import os

#Printing the logo
print(art.logo)
print("Welcome to the blind auction.")
#Declaring dictionary of all the auctioners
auctioners = {}  #Use a dictionary to link the bid amounts (values) to the bidders (keys)

def clear(): #Clearing the screen for a new game
  os.system('clear')

name = input("What is your name?: ")
bid = input("What's your bid?: ")
auctioners[name] = bid
highest = auctioners[name]
other_Bidders = input("Are there other bidders? Type 'yes' or 'no'. ")

if other_Bidders.lower() == "yes":
  while other_Bidders == "yes":
    clear()
    name = input("What is your name?: ")
    bid = input("What's your bid?: ")
    auctioners[name] = bid
    other_Bidders = input("Are there other bidders? Type 'yes' or 'no'. ")
    
for person in auctioners:
  if auctioners[person] > highest:
    winner = person
    highest = auctioners[person]


print(f"The winner is {winner} with their bid of $ {highest}.")

  