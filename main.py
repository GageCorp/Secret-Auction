from art import logo
import os

bids = []
all_bids_entered = False

print(logo)
print("Welcome to the secret auction.")


while all_bids_entered == False:
    name = input("What is your name?:")
    bid = int(input("What is your bid?: "))
    bids.append({
        "Name": name,
        "Bid" : bid
    })
    more_bidders = input("Are there any other biders? Type \'yes\' or \'no\' ")
