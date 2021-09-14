alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo ='''

 ####    ##   ######  ####    ##   #####  
#    #  #  #  #      #       #  #  #    # 
#      #    # #####   ####  #    # #    # 
#      ###### #           # ###### #####  
#    # #    # #      #    # #    # #   #  
 ####  #    # ######  ####  #    # #    # 
                                          
                                     
 ####  # #####  #    # ###### #####  
#    # # #    # #    # #      #    # 
#      # #    # ###### #####  #    # 
#      # #####  #    # #      #####  
#    # # #      #    # #      #   #  
 ####  # #      #    # ###### #    # 
'''
print(logo)

def caesar(direction):
    text = input("Type your message:\n").lower()
    shift = input("Type the shift number:\n")

    try :

        shift=int(shift)
    except ValueError:
        print("You entered wrong value.") 
        exit()

    old_index=0
    new_index=0
    cipher_text=""
    for i in text:
        if i not in alphabet:
            cipher_text+=i
        else:
            old_index=alphabet.index(i)

            if direction=="encode":
                new_index=old_index+shift
                if new_index>25:
                    new_index-=26
                

            elif direction=="decode":
                new_index=old_index-shift
                if new_index<0:
                    new_index+=26
            cipher_text+=alphabet[new_index]

    print(f"The {direction}d text is {cipher_text}")
    
    user_will(will=input("Type 'Yes' to play again. Otherwise type 'No' to exit\n").lower())

def user_will(will):    
    if will=="yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
        if direction=="encode" or direction=="decode":
            caesar(direction)
        elif direction=="exit":
            print("Good Bye !!")
        else:
            user_will(will)
    elif will=="no":
        print("Good Bye")
    else:
        print("oops!! you did not enter correct input")
        user_will(will)

user_will("yes")
