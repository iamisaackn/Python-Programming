num_cards_per_suit = 13

total_cards = 13

def probability(num_cards_in_suit):
    return num_cards_in_suit/total_cards

def main():
    
    user_suit = input("Enter the suit (Hearts, Diamonds, Clubs, Spades): ").lower()

    if user_suit in ["hearts", "diamonds", "clubs", "spades"]:

        if user_suit == "heads":
            num_cards_in_suit = num_cards_per_suit

        else:
            num_cards_in_suit = num_cards_per_suit * 3

    else: print("Invalid suit. Please enter Hearts, Diamonds, Clubs, or Spades.")

if __name__ == "__main__":
    main()

