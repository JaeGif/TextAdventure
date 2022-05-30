# Author: Jae
# Version: 2
# Date Started: May 18th, 22
# Date Completed: NA
# Notes: This file contains most methods and functions for the text-adventure2 project. There is no ascribed main() here
# just the library for basic functions

import pickle
import random
inventory = ['Inventory']
# class constructions for enemies, player and weapons


class Enemy:
    def __init__(self, name, enemy_type, damage, health, speed, experience):
        self.name = name
        self.type = enemy_type
        self.damage = damage
        self.health = health
        self.speed = speed
        self.experience = experience

    def damage_type(self):
        """This method selects the damage multiplier for enemy and player units based on their unique types"""
        # Creature > Human > Void > Creature > ... cyclically
        if 'Creature' in self.type and 'Human' in player.faction:  # damage increased based on type
            self.damage *= 1.5
            return self.damage, print('The {} is buffed against you!'.format(self.name))
        elif 'Void' in self.type and 'Creature' in player.faction:
            self.damage *= 1.5
            return self.damage, print('The {} is buffed against you!'.format(self.name))
        elif 'Human' in self.type and 'Void' in player.faction:
            self.damage *= 1.5
            return self.damage, print('The {} is buffed against you!'.format(self.name))

        elif 'Human' in self.type and 'Creature' in player.faction:  # damage decreased based on type
            self.damage *= .75
            return self.damage, print('The {} is debuffed against you!'.format(self.name))
        elif 'Creature' in self.type and 'Void' in player.faction:
            self.damage *= .75
            return self.damage, print('The {} is debuffed against you!'.format(self.name))
        elif 'Void' in self.type and 'Human' in player.faction:
            self.damage *= .75
            return self.damage, print('The {} is debuffed against you!'.format(self.name))

        elif self.type == player.faction:  # same faction increases damage slightly
            self.damage *= 1.1
            return self.damage, print('The {} is slightly buffed against you!'.format(self.name))

        else:  # no type interaction just in case, or the ??? type
            return self.damage, print('There seems to be some kind of problem ...')

    def enemy_lose_hp(self, inc_damage):  # lose hp function based on incoming damage variable, returns players health
        self.health = self.health - inc_damage
        return self.health

    def fight(self):
        """This method generally encapsulates most instances of turn-based combat, looping through HP of both
        the enemy unit and the player until one of them dies. The function returns the experience values if the enemy
        dies and the players remaining health."""
        player_damage = player.player_damage(bow, inventory)
        # enemy unit's damage is subject to a multiplier based on the players chosen faction when they begin the run
        unit_damage, weakness = self.damage_type()
        # begin general combat looping if the enemy unit is still alive
        while self.health > 0:
            print('{} health:'.format(self.name), self.health)
            # starts the turn based combat, looping until 'run_from_enemy' is successful, or player/enemy death
            while player_fight_choice(self):
                # units speed determines who strikes first
                if self.speed >= player.speed:
                    player.player_lose_hp(unit_damage)
                    self.enemy_lose_hp(player_damage)
                elif self.speed < player.speed:
                    self.enemy_lose_hp(player_damage)
                    player.player_lose_hp(unit_damage)

                # player dies first
                if player.health <= 0:
                    print('You died to a {}!'.format(self.name))
                    break

                # enemy dies first
                elif self.health <= 0:
                    print('You defeated a {}!'.format(self.name))
                    print('Remaining Health: {}'.format(player.health))
                    break

        return


class Player:
    def __init__(self, name, damage, health, faction, speed, level=1):
        self.name = name
        self.damage = damage
        self.health = health
        self.faction = faction
        self.speed = speed
        self.experience = 0
        self.level = level

    def player_damage(self, item, inv):
        """Class method, that returns the players damage based on the item in their inventory"""
        item_dmg = call_item_damage(inv, item)
        player_dmg = self.damage
        return item_dmg + player_dmg

    def player_lose_hp(self, inc_damage):  # lose hp function based on incoming damage variable, returns players health
        """returns an updated metric of the player's health after an instance of damage, from any source"""
        self.health = self.health - inc_damage
        return self.health

    def player_get_hp(self, inc_health):  # gain hp function based on certain amount of health input (integer type)
        """method is used to update an increase to the players HP"""
        self.health = self.health + inc_health
        return self.health

    def exp_gain(self, exp):
        self.experience += exp
        if self.experience >= 100:
            self.level += 1
            self.experience -= 100
            save_player()
            return self.level, self.experience


class Weapons:
    def __init__(self, name, damage, size):
        self.name = name
        self.damage = damage
        self.size = size

    def pick_up_weapon(self, inv):
        """This method is used to add an item to the inventory of the player, it checks to see if the players
        inventory is full, and if not the item is successfully added"""
        if inv is None:
            inv = ['Inventory']
        inv.append(self.name)
        if self.inventory_space_check(inv):
            save_player()
            save_inventory(inv)
            print('You picked up the {}'.format(self.name))
        else:
            return print('Your inventory is full!')
        return inv

    def inventory_space_check(self, inv):
        """method that evaluates whether the players inventory is full, if an item is picked up but the inventory
        is already full or cannot fit the item, then the item is removed from the inventory and a full inventory
        message is displayed"""
        max_inventory_size = 20
        inventory_weight = 0
        if self.name in inv:
            for i in range(len(inv[1:])):
                inventory_weight += self.size
        else:
            inventory_weight = 0
        if inventory_weight == max_inventory_size:
            return True
        elif inventory_weight < max_inventory_size:
            return True
        elif inventory_weight > max_inventory_size:
            inv.pop(-1)
            inventory_weight -= self.size
            print('Used inventory space: ', inventory_weight)
            return False


def save_player():
    """This function saves the player name and faction information to be referenced later as the game is played"""
    name_write = player.name
    faction_write = player.faction
    level_write = player.level
    with open('save', 'w+') as f:
        f.write(str(name_write.strip()) + '\n' + str(faction_write.strip()) + '\n' + str(level_write).strip())
        f.close()


def load_player():
    """This function reads the save file created by save_player and returns the new player class object
    based on the information in the save file"""
    with open('save', 'r') as f:
        lines = f.readlines()
        if not lines:
            player_c = player_customization()
            return player_c
        else:
            save_name = lines[0]
            save_faction = lines[1]
            save_level = int(lines[2])
        if 'Void' in save_faction:
            player_c = Player(save_name, 30, 50, 'Void', 7, save_level)
        elif 'Creature' in save_faction:
            player_c = Player(save_name, 30, 50, 'Creature', 7, save_level)
        elif 'Human' in save_faction:
            player_c = Player(save_name, 30, 50, 'Human', 7, save_level)
        else:
            print('Error: save data corrupted.')
            return False

    return player_c


def player_customization():
    """This is the initial player customization function that is only called once, at the very beginning of a new
    save file, it accepts a name and faction input from the player to create the new player obj"""
    player_name = str(input('Name?: '))
    accepted_input = 'Void' or 'Creature' or 'Human'
    player_class = input('What faction do you want to represent?\nPlease enter Human, Creature, or Void: ')
    if player_class == accepted_input:
        if player_class == 'Void':
            # player (name, damage, health, faction, speed)
            player_c = Player(player_name, 30, 50, 'Void', 7, 1)
            return player_c
        elif player_class == 'Human':
            # player (name, damage, health, faction, speed)
            player_c = Player(player_name, 30, 50, 'Human', 7, 1)
            return player_c
        elif player_class == 'Creature':
            # player (name, damage, health, faction, speed)
            player_c = Player(player_name, 30, 50, 'Creature', 7, 1)
            return player_c
    else:
        print('Bad input, try again')
        player_c = player_customization()
        return player_c


def load_inventory():
    """loads the inventory list data using pickle so the list information can be accessed with minimal manipulation"""
    with open('inventory.pickle', 'rb') as f:
        inv = pickle.load(f)
    return inv


def save_inventory(inv):
    """saves the inventory list using pickle to retain the list structure"""
    with open('inventory.pickle', 'wb') as f:
        pickle.dump(inv, f, pickle.HIGHEST_PROTOCOL)


def call_item_damage(inv, weapons):
    """checks the weapon damage to be added to the player's damage in combat, returns the damage value or a message
    stating that you don't have the weapon you tried to reference"""
    if weapons.name in inv:
        damage = weapons.damage
        return damage
    else:
        print('You don\'t have that weapon!')
        return 0


def run_from_fight(enemy):
    """an option to run from a fight if the players speed is greater than that of the enemy, randomly selects whether
    you can run based on your speed vs, the enemy unit's speed"""
    mode_enemy_favor = enemy.speed / player.speed
    mode_player_favor = player.speed / enemy.speed
    speed_avg = abs(enemy.speed + player.speed) / 2
    if enemy.speed >= player.speed:  # enemy faster than player
        mode = mode_enemy_favor * speed_avg
        escape_chance = random.triangular(player.speed, enemy.speed, mode)
        if escape_chance < speed_avg:
            print('You\'ve escaped!')
            return True
        elif escape_chance == speed_avg:  # if the speed of player and enemy is the same escape chance is 50/50
            if random.choice([0, 1]) is 1:
                print('You\'ve escaped!')
                return True
            else:
                print('You\'re not fast enough!')
                return False
        else:
            print('You\'re not fast enough!')
            return False
    else:  # player faster than enemy
        mode = mode_player_favor * speed_avg
        escape_chance = random.triangular(enemy.speed, player.speed, mode)
        if escape_chance >= speed_avg:
            print('You\'ve escaped!')
            return True
        else:
            print('You\'re not fast enough!')
            return False


def enemy_encounter(enemy):
    """checks to see if the player wants to fight or run when they encounter a new enemy"""
    print('You\'ve encountered a {}\n'.format(enemy.name))
    player_choice = input('Run or fight?\n')
    if player_choice == 'run':
        if not run_from_fight(enemy):
            enemy.fight()
    elif player_choice == 'fight':
        enemy.fight()
    else:
        print('Invalid input, try again. (input: run/fight only)')


def player_fight_choice(enemy):
    """used during combat to repeatedly wait for player input in case the player wants to run, continue fighting or
    use an item to influence the outcome"""
    choice = input('Fight or run? (enter to keep fighting, anything else to run!)')
    if choice == '':
        return True
    else:
        run_from_fight(enemy)


# initialized objects of weapons for testing
knife = Weapons('knife', 5, 2)
sword = Weapons('sword', 8, 2)
bow = Weapons('bow', 10, 5)

# initialize test enemies
knight = Enemy('Knight', 'Human', 8, 200, 3, 10)  # name, type, damage, health, speed, exp
inspired = Enemy('Inspired', 'Void', 10, 150, 7, 4)
uninspired = Enemy('Uninspired', 'Human', 4, 50, 3, 6)
goblin = Enemy('Goblin', 'Creature', 2, 50, 6, 4)
orc = Enemy('Orc', 'Creature', 7, 175, 5, 6)
goomba = Enemy('Goomba', 'Creature', 2, 50, 2, 4)
bug = Enemy('Bug', 'Creature', 2, 50, 1, 4)
questionable_flower = Enemy('Flower?', '???', 100000, 100000, 100000, 1)


# workflow area and check functionality
player = load_player()
inventory = bow.pick_up_weapon(inventory)

# enemy encounter
# enemy_encounter(inspired)
# run_from_fight(inspired)
print(player.level)
