logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   
from replit import clear
import random

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
 


def calculate_score(cards):
    
    if len(cards)==2 and sum(cards)==21:
        return 0
    elif 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score (user_score,computer_score):
    if user_score==0:
        return "You Won with BlackJack"
    elif computer_score==0:
        return "You lose. Opponent has black jack"
    elif user_score==computer_score:
        return "Draw"
    elif user_score>21:
        return "You lost. You went over"
    elif computer_score>21:
        return "Opponent went over. You win."
    elif user_score> computer_score:
        return "You win"
    else:
        return "You lose"

def play_game_blackjack():
    """
    Play a Black jack Game
    """
    print(logo)
    print("Welcome to Black Jack Game !!\n\n")

    user_cards = []
    computer_cards = []
    is_game_over= False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # First while loop is for user, so that user keeps playing
    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your cards: {user_cards},current score: {user_score}")
                
        print(f"Computer's first card: {computer_cards[0]}")

        # If user or comp gets Black Jack or User has score>21,game ends.
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to get another card,type 'n' to pass.")
            if user_should_deal=="y":
                user_cards.append(deal_card())
            else:
                is_game_over=True

    #Second while loop is for computer, so that computer can play when user is over.
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)


    print(compare_score(user_score,computer_score))

    print(f"Your final hand6: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand4: {computer_cards}, final score: {computer_score}")



while input('Do you want to play a black jack game? Type "y" for yes and "n" for no\n')=="y":
    clear()
    play_game_blackjack()
    

