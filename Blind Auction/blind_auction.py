import auction_art
print(auction_art.logo)

bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid

    other_bids = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if other_bids == "no":
        continue_bidding = False
    elif other_bids == "yes":
        print("\n" * 20)

winner = max(bids, key=bids.get)
print(f"The winner is {winner} with a bid of ${bids[winner]}")