#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as names:
    while names: 
        person_name = names.readline()
           
        if person_name == "":
            break
        else:
            
            input_name = person_name.split("\n")
            with open(f"./Output/ReadyToSend/letter_for_{input_name[0]}.txt","w") as dFile:
                with open("./Input/Letters/starting_letter.txt","r") as sFile:
                    texts = sFile.readlines()
                    sFile.close()

                for line in texts:
                    new_line = line.replace("[name]",input_name[0])
                    dFile.write(new_line)

                dFile.close()
    names.close()
