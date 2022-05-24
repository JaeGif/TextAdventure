# Author: 
# Version: 
# Date Started: 
# Date Completed:
# Main Function:
# Notes:


def player_customization():
    player_name = input('Name?: ')
    player_class = input('What faction do you want to represent?\nPlease enter Human, Creature, or Void: ')

    class PlayerHuman:
        def __init__(self, name, damage, health, speed):
            self.name = name
            self.damage = damage
            self.health = health
            self.faction = 'Human'
            self.speed = speed

    class PlayerCreature:
        def __init__(self, name, damage, health, speed):
            self.name = name
            self.damage = damage
            self.health = health
            self.faction = 'Creature'
            self.speed = speed

    class PlayerVoid:
        def __init__(self, name, damage, health, speed):
            self.name = name
            self.damage = damage
            self.health = health
            self.faction = 'Void'
            self.speed = speed

    if player_class == 'Void':
        player = PlayerVoid(player_name, 30, 50, 7)

        return player
    elif player_class == 'Human':
        player = PlayerHuman(player_name, 3, 100, 4)

        return player
    elif player_class == 'Creature':
        player = PlayerCreature(player_name, 2, 200, 10)

        return player
    else:
        print('Invalid Entry, try again.')
        player_customization()


# player_customized = player_customization()
# inventory = [player_dict()]
