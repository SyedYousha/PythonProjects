#Encryption

alphabet = 'abcdefghijklmnopqrstuvwxyz'

key = 5

newMessage = ''

message = input('Please enter a message: ')

for character in message:
    position = alphabet.find(character)
    #print(position)
    newPosition = (position + key) % 26
    #print(newPosition)
    newCharacter = alphabet[newPosition] #Makes the newCharacter = to the
    #array number of the new character. 
    #print('The new character is:', newCharacter)
    newMessage += newCharacter
    
    print('Your new message is:', newMessage)