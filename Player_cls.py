from Card_cls import *
from Deck_cls import *

# Creating a player class

class Player():
    
    def __init__(self,name):
        self.name = name
        self.card_in_hand = [] 
        
    # Serving the first/top card from cards in hand
    def play_first(self):
        return self.card_in_hand.pop(0)
    
    # Adding card(s) to cards in hand
    def add_cards(self,new_cards):
        # Adding a list of card to hand
        if type(new_cards) == type([]):
            self.card_in_hand.extend(new_cards)
        # Adding only a single card to hand
        else:
            self.card_in_hand.append(new_cards)
            
    def __str__(self):
        return f"{self.name} has {len(self.card_in_hand)} cards in hand!"