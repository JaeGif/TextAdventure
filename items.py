# Author: Jae
# Version: 1
# Date Started: May 12, 22
# Date Completed:
# Notes: Item definitions


# Weapons
# 'damage': int
# 'weight': int
# 'damage_type': str
# 'inventory_space': int

knife_properties = {
    'damage': 5,
    'weight': 2,
    'damage_type': 'sharp',
    'inventory_space': 1
}
knife = {
    'name': 'knife',
    'properties': knife_properties
}
sword_properties = {
    'damage': 8,
    'weight': 5,
    'damage_type': 'sharp',
    'inventory_space': 2
}
sword = {
    'name': 'sword',
    'properties': sword_properties
}
bow_properties = {
    'damage': 5,
    'weight': 1,
    'damage_type': 'pierce',
    'inventory_space': 2
}
bow = {
    'name': 'bow',
    'properties': bow_properties
}
mace_properties = {
    'damage': 10,
    'weight': 10,
    'damage_type': 'blunt',
    'inventory_space': 5
}
mace = {
    'name': 'mace',
    'properties': mace_properties
}
h2h_properties = {
    'damage': 2,
    'weight': 0,
    'damage_type': 'blunt',
    'inventory_space': 0
}
h2h = {
    'name': 'hand to hand',
    'properties': h2h_properties
}
flail_properties = {
    'damage': 9,
    'weight': 8,
    'damage_type': 'sharp',
    'inventory_space': 3
}
flail = {
    'name': 'flail',
    'properties': flail_properties
}

# all weapons
weapons = [knife,
           sword,
           bow,
           h2h,
           flail,
           mace
           ]

# Key Items Class
small_key_properties = {
    'use': 'unlock_small',
    'inventory_space': 1
}
forest_key_properties = {
    'use': 'unlock_forest',
    'inventory_space': 1
}
water_key_properties = {
    'use': 'unlock_water',
    'inventory_space': 1
}
mountain_key_properties = {
    'use': 'unlock_mountain',
    'inventory_space': 1
}
sky_key_properties = {
    'use': 'unlock_sky',
    'inventory_space': 1
}

# Currency properties
gold_properties = {
    'value': 10,
    'pouch_space': 1
}
gold = {
    'name': 'gold',
    'properties': gold_properties
}
silver_properties = {
    'value': 5,
    'pouch_space': 1
}
silver = {
    'name': 'silver',
    'properties': silver_properties
}
copper_properties = {
    'value': 1,
    'pouch_space': 1
}
copper = {
    'name': 'copper',
    'properties': copper_properties
}

# Important items properties
money_pouch_properties = {
    'inventory_space': 1
}

# Inventory


# Item with information about the item
mountain_key = {
    'name': 'Mountain Key',
    'properties': mountain_key_properties
}
sky_key = {
    'name': 'Sky Key',
    'properties': sky_key_properties
}
water_key = {
    'name': 'Water Key',
    'properties': water_key_properties
}
forest_key = {
    'name': 'Forest Key',
    'properties': forest_key_properties
}
