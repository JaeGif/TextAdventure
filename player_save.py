# Author: Jae
# Version: 1
# Date Started: May 18th, 22
# Date Completed:
# Notes: Ascribes player attributes

# import initialize
# import items
# import item_functions


def save_player():
    name_write = player_customized.name
    faction_write = player_customized.faction
    print(name_write.strip(), faction_write)

    with open('save', 'w+') as f:
        f.write(str(name_write.strip()) + '\n' + str(faction_write.strip()))
    f.close()


def load_player():
    with open('save', 'r') as f:
        lines = f.readlines()
        if not lines:
            f.close()
            player = player_customization()
            return player
        else:
            save_name = lines[0]
            save_faction = lines[1]

        if 'Void' in save_faction:
            class PlayerVoid:
                def __init__(self, name, damage, health, speed):
                    self.name = name
                    self.damage = damage
                    self.health = health
                    self.faction = 'Void'
                    self.speed = speed
            player = PlayerVoid(save_name, 30, 50, 7)
            f.close()
        elif 'Creature' in save_faction:
            class PlayerCreature:
                def __init__(self, name, damage, health, speed):
                    self.name = name
                    self.damage = damage
                    self.health = health
                    self.faction = 'Creature'
                    self.speed = speed
            player = PlayerCreature(save_name, 2, 200, 10)
        elif 'Human' in save_faction:
            class PlayerHuman:
                def __init__(self, name, damage, health, speed):
                    self.name = name
                    self.damage = damage
                    self.health = health
                    self.faction = 'Human'
                    self.speed = speed
            player = PlayerHuman(save_name, 3, 100, 4)
        else:
            print('Error: save data corrupted.')
        f.close()

    return player


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


def player_dict():
    stats_properties = {
        'faction': player_customized.faction,
        'attack': player_customized.damage,
        'health': player_customized.health,
        'name': player_customized.name,  # insert player_name variable later
        'speed': player_customized.speed,
        'inventory_space': 0
    }

    stats_check = {
        'name': 'Player Attributes: ',
        'properties': stats_properties
    }

    return stats_check


player_customized = load_player()
save_player()
