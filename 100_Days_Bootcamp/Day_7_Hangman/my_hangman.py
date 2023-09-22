stages = [ 
    """
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    """,

    """
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    """,

    """
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    """,

    """
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    """,

    """
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    """,
    
    """
    _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    """,

"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """

]

import random

list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(list)
word_length = len(chosen_word)
display = []

for char in chosen_word:
    display += "_"

end_of_game = False
lives = 6

while not end_of_game:
    print(stages[lives])
    print(display)

    guess = input("Guess a letter: ")
    
    if guess in chosen_word:
        for position in range(word_length): 
            if guess == chosen_word[position]:
                display[position] = guess
    else:
        lives -= 1
    

    if "_" not in display:
        end_of_game = True
        print(stages[lives])
        print("You win !")
    elif lives == 0:
        end_of_game = True
        print(stages[lives])
        print("You lose.")

    

    




