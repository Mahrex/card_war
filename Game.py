from Card_cls import *
from Deck_cls import *
from Player_cls import *

# GAME SETUP
# Creating the two players (both computers)
player_one = Player('Dell')
player_two = Player('Lenovo')

# Creating a new deck and then shuffling them
new_deck = Deck()
new_deck.shuffle_cards()

# Dividing the cards deck into two halves and giving the players, 26 cards each
for i in range(26):
    player_one.add_cards(new_deck.deal_one_card())
    player_two.add_cards(new_deck.deal_one_card())
    
# Starting actual game

current_round = 1
game_on = True

while game_on:
    
    # Printing currently which round is playing
    print(f"Currently at round {current_round}")
    current_round += 1
    
    # Checking if any of the players has lost!
    if len(player_one.card_in_hand) == 0:
        print(f"{player_one.name} is out of cards! {player_two.name} won the game!")
        game_on = False
        break
    
    if len(player_two.card_in_hand) == 0:
        print(f"{player_two.name} is out of cards! {player_one.name} won the game!")
        game_on = False
        break
    
    # Starting a NEW ROUND (card on the table!)
    player_one_cards_in_table = []
    player_one_cards_in_table.append(player_one.play_first())
    
    player_two_cards_in_table = []
    player_two_cards_in_table.append(player_two.play_first())
    
    
    # Executing the main game logic 
    # Starting at_war = True
    at_war = True
    
    while at_war:
        
        # Checking if player 1 has won that particular round
        if player_one_cards_in_table[-1].value > player_two_cards_in_table[-1].value:
            
            # Adding cards from both players to winner of this round
            player_one.add_cards(player_one_cards_in_table)
            player_one.add_cards(player_two_cards_in_table)
            
            # No war in this round 
            at_war = False
            
        # Checking if player 2 has won that particular round
        elif player_one_cards_in_table[-1].value < player_two_cards_in_table[-1].value:
            
            # Adding cards from both players to winner of this round
            player_two.add_cards(player_one_cards_in_table)
            player_two.add_cards(player_two_cards_in_table)
            
            # No war in this round 
            at_war = False
            
        # Game at war!
        elif player_one_cards_in_table[-1].value == player_two_cards_in_table[-1].value:
            print('GAME AT WAR!')
            
            # Checking if any player is in short of cards so they loose
            if len(player_one.card_in_hand) < 3:
                print(f"{player_one.name} is unable to declare war.")
                print(f"{player_two.name} won the game!")
                game_on = False # Breaking out of main game
                break # Breaking out of current at_war loop
            
            elif len(player_two.card_in_hand) < 3:
                print(f"{player_two.name} is unable to declare war.")
                print(f"{player_one.name} won the game!")
                game_on = False # Breaking out of main game
                break # Breaking out of current at_war loop
            
            
            # Both can declare war and add (3) cards in table
            else:
                for i in range(3):
                    player_one_cards_in_table.append(player_one.play_first())
                    player_two_cards_in_table.append(player_two.play_first())