from art import logo
import os

bids = []

print(logo)
print("Welcome to the secret auction.")

bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bids.append({
        "Name": name,
        "Bid" : bid
    })
    more_bidders = input("Are there any other biders? Type \'yes\' or \'no\': ")
    os.system('cls')
    if more_bidders == "no":
        bidding_finished = True



def highest_bidder(bids):
    highest_bid = 0
    winner = ''
    for bid in bids:
        bid_amount = bids[bid]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            