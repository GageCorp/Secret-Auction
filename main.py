from art import logo
import os

bids = []

print(logo)
print("Welcome to the secret auction.")


while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bids.append({
        "Name": name,
        "Bid" : bid
    })
    more_bidders = input("Are there any other biders? Type \'yes\' or \'no\': ")
    os.system('cls')
    if more_bidders == "no":
        break
    
