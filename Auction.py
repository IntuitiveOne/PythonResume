
auctionbidsdict = {}

bidding = "y"

while bidding == "y": #replayability of adding auction key value pairs if auctions still ongoing

    ok = "" #declaring variables to use in while loops which are enforcing correct user inputs are only accepted
    name = "123"
    bidamount = "notnumber"
    bidding = ""

    while name.isalpha() == False:
        name = input("\n\nWhat is your name?\n\n")
    while bidamount.isnumeric() == False:   
        bidamount = input("\n\nHow much is your bid?\n\n$")
    while ok != 1: 
        bidding = input("\n\nIs the bidding still ongoing for this auction? y/n\n\n").lower()
        if bidding == "y" or bidding == "n":
            ok = 1
    

bidamount = int(bidamount) #integer conversion to use comparative operator at the end of the bidding process
auctionbidsdict[name] = bidamount #adding the key value pairs to the dictionary

if bidding == "n":
    highest_bid = 0
    winner = ""   
    for i in auctionbidsdict:
        bid_amount = auctionbidsdict[i]
        if bid_amount > highest_bid: 
            highest_bid = bid_amount
            winner = i.capitalize()
            print(f"\n\nThe winner is {winner} with a bid of ${highest_bid}\n\n")





    