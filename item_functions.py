# Author: Jae
# Version: 1
# Date Started: May 16, 22
# Date Completed:
# Main Function:
# Notes: functions for items inventory needs to be defined globally as there is no main function

import items
# Inventory is a list of item dictionaries
# Default weight is 0, weight is to change as items are added and removed
import player_save


def pick_up_item(item, inventory):
    inventory.append(item)
    inventory_weight = inventory_space_check(inventory)
    inventory_write(inventory)
    return inventory, inventory_weight


def inventory_space_check(inventory):
    inventory_weight = 0
    max_inventory_size = 20

    if inventory_weight == max_inventory_size:
        return inventory_weight, max_inventory_size
    elif inventory_weight < max_inventory_size:
        return inventory_weight, max_inventory_size
    elif inventory_weight > max_inventory_size:
        inventory.pop(-1)
        print('You cant fit that!')
        print('Used inventory space: ', inventory_weight)
        return inventory_weight, max_inventory_size


def check_inventory(inventory):
    inventory_weight, max_inventory_size = inventory_space_check(inventory)
    inventory_str = ''
    for i in inventory[1:]:  # excluding the player stat check
        inventory_weight += i['properties']['inventory_space']
        inventory_str += i['name'] + ' ' + '|' + ' '
    if inventory_weight == max_inventory_size:
        print('Inventory is full!')
    elif inventory_weight < max_inventory_size:
        print('Remaining inventory space: ', max_inventory_size - inventory_weight)

    print('Inventory: ', inventory_str)


def player_stat_check(inventory):
    print(inventory[0]['name'],
          'Strength:', inventory[0]['properties']['attack'], '\n\t\t\t\t\t'
                                                             'Health:', inventory[0]['properties']['health']
          )


def weapon_stat_check(item, inventory):  # weapons have the structure name

    if item in inventory:
        item_index = inventory.index(item)
        print('Weapon:', inventory[item_index]['name'], '\n'
              'Damage:', inventory[item_index]['properties']['damage'], '\n'
              'Type:',
              inventory[item_index]['properties']['damage_type'], '\n'
              'Weight:',
              inventory[item_index]['properties']['weight'], '\n'
              'Inventory Space:',
              inventory[item_index]['properties']['inventory_space']
              )
    else:
        print('You don\'t have that')


def weapons_chart(weapons):  # outputs the values of all in-game weapons added to items.weapons
    print(weapons)
    for i in range(0, len(weapons) - 1):
        print('Weapon:', weapons[i]['name'], '\n'
              'Damage:', weapons[i]['properties']['damage'], '\n'
              'Type:', weapons[i]['properties']['damage_type'], '\n'
              'Weight:', weapons[i]['properties']['weight'], '\n'
              )


def inventory_write(inventory):                          # writes full inventory to a .txt
    inventory_w = str(inventory[1:])
    with open('inventory', 'w+') as f:
        read_inv = f.read()
        for i in inventory_w:
            if i not in read_inv:
                f.write(i)
    f.close()


inventory = player_save.inventory
# pick_up_item(items.h2h, inventory)
