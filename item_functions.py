# Author: Jae
# Version: 1
# Date Started: May 16, 22
# Date Completed:
# Main Function:
# Notes: functions for items inventory needs to be defined globally as there is no main function

# Inventory is a list of item dictionaries
# Default weight is 0, weight is to change as items are added and removed


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

