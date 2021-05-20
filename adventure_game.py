# imports
import time
import random


# print message to screen
def print_pause(message, pause=1):
    print(message)
    time.sleep(pause)


# prompt user for input and validate
def valid_input(message, option1, option2):
    while True:
        # get the user input
        response = input(message)
        # validate
        if response == option1 or response == option2:
            break
        else:
            print('(Please enter 1 or 2)')
    # return response
    return response


# print the intro
def intro(weapon):
    print_pause('You find yourself standing in an open field,'
                'filled with grass and wheat as tall as yourself on '
                'a summer\'s day right before dark.')
    print_pause('There is a rumor there is a monster is somewhere around here,'
                'and has been terrifying the nearby town at night.')
    print_pause('You hear something growling in the field.....', 2)
    print_pause('To the right is a cave.')
    print_pause('To the left is an old farm house just on the '
                'outskirts of town.')
    print_pause(f'In your hand you hold your trusty '
                '(but not very effective) {weapon}.')


# handle the cave story
def cave(game_status, monster, user_weapon, farmers_weapon):
    # Print outcome of cave
    print_pause('Upon entering the cave you find a nest with the '
                f'{monster} and it\'s babies.')
    print_pause('The monster is guarding it\'s nest ready to attack.')

    # prompt for user action
    action = valid_input('Enter 1 to fight back as you think your '
                         f'{user_weapon} stands a chance.\n'
                         'Enter 2 to to run out of the cave.\n', '1', '2')

    # Display a message and set game status based on user action
    if action == '1':
        print_pause(f'The {monster} is to powerful and defeats you easily.')
        print_pause('You become food for the monster\'s babies.')
        game_status = 'lost'
    elif action == '2':
        print_pause(f'As you are running away , you realize the {monster} '
                    'just wants to protect '
                    'it\'s babies and leaves you alone.')
        print_pause(f'You find shelter in the nearby town for the night.')
        game_status = 'won'

    # return game status
    return game_status


# handle the farm house story
def farm_house(game_status, monster, user_weapon, farmers_weapon):
    game_status = 'playing'

    # Print the outcome of the farm house
    print_pause('The farmer lets you in.'
                'He closes and locks the door behind you.')
    print_pause(f'The farmer goes to attack you with his {farmers_weapon}.')

    # Prompt for user action
    action = valid_input('Enter 1 to fight back as you think your '
                         f'{user_weapon} stands a chance.\n'
                         'Enter 2 to to run through the back door.\n',
                         '1', '2')

    # Display a message and set game status based on user action
    if action == '1':
        print_pause('You were right, the farmer and his '
                    f'{farmers_weapon} were no match for you.')
        print_pause('You stay the night and continue on your journey.')
        game_status = 'won'
    elif action == '2':
        print_pause('As you are running away from the farmers house,'
                    'you hear him shout to the monster.')
        print_pause('Turns out the monster was just the farmer\'s '
                    f'pet {monster} and is hungry.')
        game_status = 'lost'

    # return game status
    return game_status


# play the adventure game
def play_game():
    # hold the random monsters
    monsters = ['dragon', 'werewolf']
    # hold random weapons
    weapons = ['sword', 'dagger', 'axe', 'bow']
    # get the monster
    monster = random.choice(monsters)
    # get the user user and farmers weapon
    user_weapon = random.choice(weapons)
    farmers_weapon = random.choice(weapons)
    # status of game
    game_status = 'playing'

    # display the intro
    intro(user_weapon)

    # prompt user for input
    choice = valid_input('Enter 1 to knock on the farm house door.\n'
                         'Enter 2 to enter the cave.\n', '1', '2')

    # Show story based on user choice
    if choice == '1':
        game_status = farm_house(game_status, monster,
                                 user_weapon, farmers_weapon)
    elif choice == '2':
        game_status = cave(game_status, monster,
                           user_weapon, farmers_weapon)

    # Handle end of game message
    if game_status == 'won':
        print_pause('Congradulations!You made it through the night.')
    elif game_status == 'lost':
        print_pause('You did not survive the night.Better luck next time!')

    # prompt user to play again
    play_again = valid_input('Enter 1 to play again.\n'
                             'Enter 2 to quit.\n', '1', '2')

    # Handle if user plays again or not
    if play_again == '1':
        play_game()
    elif play_again == '2':
        print_pause('Thank you for playing!')


"""
You'll sometimes see variables in Python that have double underscores in the name, such as __name__ and __main__. 
These are also sometimes called "dunder" variables—with "dunder" being short for "double underscore".

Notice that these names have double underscores at both the beginning and the end.
When you see this, it's a signal that it's a special name that is reserved for use by Python. 

Although you don't always see it in the code, every script has its own copy of the __name__ variable. 
Before running the code in a program, Python assigns a value to this variable. 
The value it assigns depends on whether the script is being imported or getting directly executed.

If we directly run my_script.py, then __name__ gets set to '__main__'.
If we import my_script,py, then __name__ gets set to 'my_script'.

When you import a module, the code in that module gets run.
To avoid code from running upon import, we can wrap the code in an if block testing the __name__ variable
If __name__ is __main__, the script is ran directly so we can execute the code
"""
if '__name__' == '__main__':
    # start the game
    play_game()
