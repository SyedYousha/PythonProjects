#rock, paper, scissors

from random import randint #to import random numbers


user = input('rock (r), paper (p), scissors (s)?') #Let's the user input something and assigns
    #it to whatever option it picked. So the next line, user will show as r, p, or s. 

print(user, 'against') #Just prints out the user input and the string against.

random = randint (1,3) #Sets the range of the random integer to all numbers between
    #1 and 3, which also includes 1 and 3.

if random == 1:
    computerChoice = 'rock' #Assigning the random integers to a specific string.

elif random == 2:
    computerChoice = 'paper' 

else:
    computerChoice = 'scissors'

#     """COMMENT: The reason why else doesn't have a option like else random == 3:
#         is because else is used when it has to evaluate EVERYTHING else that is left, if you want
#         to make this    user = input('rock (r), paper (p), scissors (s)?') #Let's the user input something and assigns
#         it to whatever option it picked. So the next line, user will show as r, p, or s.""" 



# """COMMENT: The reason why else doesn't have a option like else random == 3:
#         is because else is used when it has to evaluate EVERYTHING else that is left, if you want
#         to make this more restrictive, then just use another elif statement."""

print(computerChoice)

if user == computerChoice: #So it can output if something is a draw. 
    print('Draw!')

elif user == 'rock' and computerChoice == 'scissors': #The colon at the end is important because
    print('You won!')

elif user == 'rock' and computerChoice == 'paper':
    print('You lost!')

elif user == 'paper' and computerChoice == 'rock':
    print('You won!')

elif user == 'paper' and computerChoice == 'scissors':
    print('You lost!')

elif user == 'scissors' and computerChoice == 'paper':
    print('You won!')

elif user == 'scissors' and computerChoice == 'rock':
    print('You lost!')

    # """COMMENT: The code above consists of If and else statements that makes sure to include all
    # possible outcomes of this game, Since there are not that many outcomes, this works but
    # eventually there should be an easier way of doing this because you cannot just keep writing
    # IF and ELIF statements for several hundred outcomes.
    # The colon at the end of the statements is important because you are executing something.
    # """
