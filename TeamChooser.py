#Team chooser from codeclubprojects.org

from random import choice 

players = [] #Listing all the players
file = open('players.txt', 'r') #Python opens this file in the background
players = file.read().splitlines() #Reads the player list from here
#Splitlines means that every line is a new item for the players list. 
print('Player List:', players)

teamA = [] #Empty list for Team A
teamB = []

while len(players) > 0: #Runs code until player list runs out. 
    playerA = choice(players) #Assigns the attribute of PlayerA to the
    #randonly selected player and then prints it out 
    print('TeamA selects:', playerA)
    teamA.append(playerA) #Append will add playerA to the teamA list
    players.remove(playerA) #Removes playerA from being selected again

    playerB = choice(players)
    print('TeamB selects:', playerB)
    teamB.append(playerB)
    players.remove(playerB)

print('Team A: ', teamA)
print('Team B: ', teamB)