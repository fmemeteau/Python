# Create a secret auction bid program using a dictionary. The name of the bidder shall be the key and the bid the value.

# --- My answer ---
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

from Day_9_0_Secret_Auction_Art import gavel
end_of_auction = False

print(gavel)

bid_list = {}

while end_of_auction == False:
    name = input("Please insert Bidder name: ")
    bid = input("Please insert Bid: ")
    bid = int(bid)
    bid_list[name] = bid

    other_bidder = input("Is there another bidder? Type 'yes' or 'no': ")
    clear()
    if other_bidder == 'no':
        end_of_auction = True



winner = max(bid_list, key=bid_list.get)
print(f"The winner is {winner} with a ${bid_list[winner]} bid.")




# --- Teacher's answer ---
# I added my own import of the 'os' module as well as the clear() function

import os
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

from Day_9_0_Secret_Auction_Art import gavel
print(gavel)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        clear()