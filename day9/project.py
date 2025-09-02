continue_bidding = True
bid_information = {}

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""

    for name in bidding_dictionary:
        if bidding_dictionary[name] > highest_bid:
            highest_bid = bidding_dictionary[name]
            winner = name
            
    print(f"The winnder is {winner} with a bid of ${highest_bid}.")

while continue_bidding:
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    bid_information[name] = bid
    
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    
    if should_continue == 'yes':
        print('\n' * 100)
    else:
        continue_bidding = False
        find_highest_bidder(bid_information)
