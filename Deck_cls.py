from Card_cls import *
import random

# Creating a new deck class for creating new decks

class Deck():
    
    def __init__(self):
    
        # Constructing a new deck as a form of list of cards
        self.all_cards = []
        
        # Looping through all cards (52 round)
        for suit in suits:
            for rank in ranks:
                
                # Creating all unique cars and adding in the deck
                card = Card(suit,rank)
                self.all_cards.append(card)

    # Shuffling all cards
    def shuffle_cards(self):
        random.shuffle(self.all_cards)
        
    # Dealing only one card from deck (Generally the last card)
    def deal_one_card(self):
        return self.all_cards.pop()

# new_deck = Deck()

# new_deck.shuffle_cards()