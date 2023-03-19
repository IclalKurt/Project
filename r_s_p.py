import random

def win (player,opponent):
    if (player == 'r'and opponent =='s') or (player == 'p' and opponent == 'r') or \
    (player == 's' and opponent == 'p'):
        return True
    
user = input('chose your move!\nr-rock, p-paper,s-scissors\n')
game = ['r','p','s']
computer = random.choice(game)

if user == computer:
    print('its a tie')

elif win(user,computer):
    print('you won!')
    
elif win(computer,user):
    print('you lost..')


