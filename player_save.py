# Author: Jae
# Version: 1
# Date Started: May 18th, 22
# Date Completed:
# Notes: Ascribes player attributes

import item_functions
import items
import pickle


def save_player():
    # this function saves the player information and returns none for a save file to be later accessed. Arg is inventory
    name_write = player_customized.name
    faction_write = player_customized.faction

    with open('save', 'w+') as f:
        f.write(str(name_write.strip()) + '\n' + str(faction_write.strip()) + '\n')
        f.close()


def load_player():
    class Player:
        def __init__(self, name, damage, health, faction, speed):
            self.name = name
            self.damage = damage
            self.health = health
            self.faction = faction
            self.speed = speed

    with open('save', 'r') as f:
        lines = f.readlines()
        if not lines:
            player = player_customization()
            return player
        else:
            save_name = lines[0]
            save_faction = lines[1]
        if 'Void' in save_faction:
            player = Player(save_name, 30, 50, 'Void', 7)
        elif 'Creature' in save_faction:
            player = Player(save_name, 30, 50, 'Creature', 7)
        elif 'Human' in save_faction:
            player = Player(save_name, 30, 50, 'Human', 7)
        else:
            print('Error: save data corrupted.')
            return False

    return player


def player_customization():
    player_name = str(input('Name?: '))
    accepted_input = 'Void' or 'Creature' or 'Human'
    player_class = input('What faction do you want to represent?\nPlease enter Human, Creature, or Void: ')
    if player_class == accepted_input:
        class Player:
            def __init__(self, name, damage, health, faction, speed):
                self.name = name
                self.damage = damage
                self.health = health
                self.faction = faction
                self.speed = speed

        if player_class == 'Void':
            # player (name, damage, health, faction, speed)
            player = Player(player_name, 30, 50, 'Void', 7)
            return player
        elif player_class == 'Human':
            # player (name, damage, health, faction, speed)
            player = Player(player_name, 30, 50, 'Human', 7)
            return player
        elif player_class == 'Creature':
            # player (name, damage, health, faction, speed)
            player = Player(player_name, 30, 50, 'Creature', 7)
            return player
    else:
        print('Bad input, try again')
        player = player_customization()
        return player


def pick_up_item(item, inv):
    inv.append(item)
    if item_functions.inventory_space_check(inv):
        save_player()
    return inv


def load_inventory():
    with open('inventory.pickle', 'rb') as f:
        inv = pickle.load(f)
    return inv


def save_inventory(inv):
    with open('inventory.pickle', 'wb') as f:
        pickle.dump(inv, f, pickle.HIGHEST_PROTOCOL)


inventory = ['Inventory:']
player_customized = load_player()
inventory = pick_up_item(items.sword, inventory)
save_player()
save_inventory(inventory)
print(load_inventory())
