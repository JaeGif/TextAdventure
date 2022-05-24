# Author: Jae
# Version: 1
# Date Started: May 16, 22
# Date Completed:
# Main Function:
# Notes: Contains enemy classes and parameters


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


class BossEnemy:
    def __init__(self, name, enemy_type, damage, health, experience):
        self.name = name
        self.type = enemy_type
        self.damage = damage
        self.health = health
        self.experience = experience


# Human type enemies
knight = Enemy('Knight', 'Human', 8, 200, 3, 10)  # name, type, damage, health, speed, exp
inspired = Enemy('Inspired', 'Human', 10, 150, 7, 4)  # name, type, damage, health, speed, exp
uninspired = Enemy('Uninspired', 'Human', 4, 50, 3, 6)  # name, type, damage, health, speed, exp

# Creature type enemies
goblin = Enemy('Goblin', 'Creature', 2, 50, 6, 4)  # name, type, damage, health, speed, exp
orc = Enemy('Orc', 'Creature', 7, 175, 5, 6)  # name, type, damage, health, speed, exp
goomba = Enemy('Goomba', 'Creature', 2, 50, 2, 4)  # name, type, damage, health, speed, exp
bug = Enemy('Goblin', 'Creature', 2, 50, 1, 4)  # name, type, damage, health, speed, exp


# ???
questionable_flower = Enemy('Flower?', '???', 100000, 100000, 100000, 1)  # name, type, damage, health, exp


# Boss type enemies
kraken = BossEnemy('Kraken', 'Void', 60, 1000, 100)  # name, type, damage, health, exp
hydra = BossEnemy('Hydra', 'Creature', 60, 1000, 100)  # name, type, damage, health, exp
