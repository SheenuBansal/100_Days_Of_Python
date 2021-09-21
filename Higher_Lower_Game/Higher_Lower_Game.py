# guessing who has highest followers between two given Persons or Apps
# Import Art Module which contains your logos
# Import game_data module which contains your list of items.

import game_data 
import random
import art


def higher_lower_game():
    score=0
    end_of_game=False
    
    while not end_of_game :
        
        print(art.logo)
        first_item=random.choice(game_data.data)
        second_item=random.choice(game_data.data)
        print(f"Compare A : {first_item['name']}, {first_item['description']}, {first_item['country']}")
        print(art.vs)
        print(f"Against B : {second_item['name']}, {second_item['description']}, {second_item['country']}")


        A=first_item['follower_count']
        B=second_item['follower_count']

        user_guess=input("Who has more followers? 'A' or 'B': ").upper()

        if (user_guess=="A" and A>B) or (user_guess=="B" and B>A) :
            score+=1
            print(f"You are right. Current score is {score}")
        else:
            end_of_game=True
        
    print(f"Sorry that's wrong. Final score is {score}")


higher_lower_game()


