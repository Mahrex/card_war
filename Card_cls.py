# Creating a card class -> Suit,Rank & Value will be needed

# Creating values of cards and respective numbers 
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

# Creating suits and ranks tuples for usage
suits = ('Clubs', 'Spades', 'Hearts', 'Diamond')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank.capitalize()] # Getting the rank from 'values' dictionary
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"