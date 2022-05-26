# Author: Jae
# Version: 2
# Date Started: May 18th, 22
# Date Completed:
# Notes: This file contains most methods and functions for the text-adventure2 project. There is no ascribed main() here
# just the library for basic functions


import enemies
import item_functions
import pickle

inventory = ['Inventory:']  # initialize 1st inventory global instance


class Enemy:
    def __init__(self, name, enemy_type, damage, health, speed, experience):
        self.name = name
        self.type = enemy_type
        self.damage = damage
        self.health = health
        self.speed = speed
        self.experience = experience

    def damage_type(self):
        if 'Creature' in self.type:
            self.damage *= 1.5
            return self.damage
        elif '???' in self.type:
            self.damage *= 500
            return self.damage
        elif 'Void' in self.type:
            self.damage *= 2
            return self.damage


class Player:
    def __init__(self, name, damage, health, faction, speed):
        self.name = name
        self.damage = damage
        self.health = health
        self.faction = faction
        self.speed = speed
        self.experience = 0
        self.level = 1

    def player_damage(self, item):
        item_dmg = call_item_damage(inventory, item)
        player_dmg = self.damage
        return item_dmg + player_dmg

    def player_lose_hp(self, inc_damage):
        player_customized.health = self.health - inc_damage
        return player_customized.health

    def player_get_hp(self, health):
        player_customized.health = self.health + health
        return player_customized.health


class Weapons:
    def __init__(self, name, damage, size):
        self.name = name
        self.damage = damage
        self.size = size

    def pick_up_weapon(self, inv):
        inv.append(self.name)
        if item_functions.inventory_space_check(inv):
            save_player()
            save_inventory(inv)
        return inv


def save_player():
    # this function saves the player information and returns none for a save file to be later accessed. Arg is inventory
    name_write = player_customized.name
    faction_write = player_customized.faction

    with open('save', 'w+') as f:
        f.write(str(name_write.strip()) + '\n' + str(faction_write.strip()) + '\n')
        f.close()


def load_player():
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


def call_item_damage(inv, weapons):
    if weapons.name in inv:
        damage = weapons.damage
        return damage
    else:
        print('You don\'t have that weapon!')
        return 0


def inventory_space_check(inv):
    inventory_weight = 0
    max_inventory_size = 20

    if inventory_weight == max_inventory_size:
        return inventory_weight, max_inventory_size
    elif inventory_weight < max_inventory_size:
        return inventory_weight, max_inventory_size
    elif inventory_weight > max_inventory_size:
        inv.pop(-1)
        print('You cant fit that!')
        print('Used inventory space: ', inventory_weight)
        return inventory_weight, max_inventory_size


def check_inventory(inv):
    inventory_weight, max_inventory_size = inventory_space_check(inv)
    inventory_str = ''
    for i in inv[1:]:  # excluding the player stat check
        inventory_weight += i['properties']['inventory_space']
        inventory_str += i['name'] + ' ' + '|' + ' '
    if inventory_weight == max_inventory_size:
        print('Inventory is full!')
    elif inventory_weight < max_inventory_size:
        print('Remaining inventory space: ', max_inventory_size - inventory_weight)

    print('Inventory: ', inventory_str)


# initialized objects of weapons, and enemies
knife = Weapons('knife', 5, 2)
sword = Weapons('sword', 8, 2)
bow = Weapons('bow', 10, 5)

# workflow area and check functionality
player_customized = load_player()
bow.pick_up_weapon(inventory)
knife.pick_up_weapon(inventory)
print(player_customized.player_damage(knife))
incdamage = enemies.bug.damage
print('enemy dmg: ', incdamage)
print('player health pre-damage:', player_customized.health)
print(player_customized.player_lose_hp(incdamage))
print('player health after-damage:', player_customized.health)
