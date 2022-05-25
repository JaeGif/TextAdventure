# Author: Jae
# Version: 1
# Date Started: May 16, 22
# Date Completed:
# Main Function:
# Notes: functions related to enemies

import enemies
import player_save


def run_from_fight(enemy):
    if player_save.player_customized.speed > enemy.speed:
        print('You\'ve escaped!')
        return True
    else:
        print('You\'re not fast enough!')
        return False


def fight_enemy(enemy):

    unit_health = enemy.health
    player_health = player_save.player_customized.health
    player_damage = player_save.player_customized.damage  # + items.sword['properties']['damage']
    while unit_health > 0:
        unit_health -= player_damage
        if unit_health <= 0:
            break

        player_health -= enemy.damage
        if player_health <= 0:
            print('You Died')
            print('Enemy remaining Health: {}'.format(unit_health))
            return False

    print('You defeated a {}!'.format(enemy.name))
    print('Remaining Health: {}'.format(player_health))
    return True, enemy.experience, player_health


def enemy_encounter(enemy):
    print('You\'ve encountered a {}\n'.format(enemy.name))
    player_choice = input('Run or fight?\n')
    if player_choice == 'run':
        if not run_from_fight(enemy):
            fight_enemy(enemy)
    elif player_choice == 'fight':
        fight_enemy(enemy)


enemy_encounter(enemies.knight)
