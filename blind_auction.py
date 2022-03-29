from replit import clear
from art import logo

print(logo)
auction_live = True
bidders = {}

while auction_live:
  name = input("Enter your name : ")
  bid = int(input("Enter your bid : $") )

  
  bidders[name] = bid
  # print(bidders)
  another_bidder = input("Are there any other bidders 'Yes' or 'No' ? ").lower()

  if another_bidder == 'yes':
    clear()
  elif another_bidder == 'no':
    auction_live = False
 
print(bidders)
highest_bid = 0
winner = ""
  # bidding_record = {"Nick": 123, "James": 321}
for bidder in bidders:
  bid_amount = bidders[bidder]
  if bid_amount > highest_bid: 
    highest_bid = bid_amount
    winner = bidder
print(f"The winner is {winner} with a bid of ${highest_bid}")