from heros import *
from time import sleep as wait
from AI import AI



DEBUG = True
if DEBUG:
    Froggy = Hero("Froggy", 2, 1000, 250, level=1, base_attack_stat=1,
                  green_skill_info={"name": "Whirlpool", "type": "damage"})

    Sludge = Hero("Sludge", 2, 1000, 250, level=1, base_attack_stat=2,
                  green_skill_info={"name": "Flower of the Earth", "type": "self heal"})
    Froggladior = Hero("Froggladior", 2, 1500, 250, level=1, green_skill_info={"name": "Downfall", "type": "self heal"})
    Frogglar = Hero("asdf", 2, 1500, 250, level=1, green_skill_info={"name": "Downfall", "type": "damage"})

class Battle:
    def __init__(self, heros , enemies):
        self.heros = heros
        self.enemies = enemies

    def battle(self):
        over = False
        MAIN_AI = AI(self.heros, self.heros[1])

        def battle_over(over_var, hero_list, enemy_list):
            # Checking that all heros are dead:
            if all(hero.permissions == "dead" for hero in heroes_list):
                print("You Lose. All Heros Are Dead")
                over_var = True
                return "You Lose."
            elif all(enemy.permissions == "dead" for enemy in enemy_list):
                over_var = True
                print("You Win!")
                return "You Win."
            else:
                return


        # Making Sure that All Lists are full.
        if len(self.heros) > 5:
            return

        while not over:
            for hero in self.heros:
                if hero.health <= 0:
                    continue
                else:
                    hero.decision = ""
                    hero.enemy_decision: str = ""
                    while hero.decision != "":
                        enemy_number = 0
                        print(f"Choose one action for {hero.name}:")
                        print("\n")
                        wait(1)
                        print("(1): Base Attack")
                        wait(0.5)
                        print("(2): Green Skill")
                        wait(0.5)
                        print("(3): Pass")
                        wait(0.5)
                        hero.decision = input("Choose: ")
                        if hero.decision == "1":
                            print("Which Enemy Are You Going To Attack?")
                            wait(1)

                            for index, enemy in enumerate(self.enemies, start=1):
                                if enemy is not None:
                                    print(f"({index}): {enemy.name}")
                                else:
                                    continue
                            while hero.enemy_decision != "":
                                if hero.enemy_decision == "1" and not (
                                        int(hero.enemy_decision) > len(self.enemies)) and not (
                                        enemy.health <= 0):
                                    hero.green_skill(self.enemies[0])
                                elif hero.enemy_decision == "2" and not (
                                        int(hero.enemy_decision) > len(self.enemies)) and not (
                                        enemy.health <= 0):
                                    hero.green_skill(self.enemies[1])
                                elif hero.enemy_decision == "3" and not (
                                        int(hero.enemy_decision) > len(self.enemies)) and not (
                                        enemy.health <= 0):
                                    hero.green_skill(self.enemies[2])
                                elif hero.enemy_decision == "4" and not (
                                        int(hero.enemy_decision) > len(self.enemies) and not (enemy.health <= 0)):
                                    hero.green_skill(self.enemies[3])
                                elif hero.enemy_decision == "5" and not (
                                        int(hero.enemy_decision) > len(self.enemies)) and not (
                                        enemy.health <= 0):
                                    hero.green_skill(self.enemies[4])
                                else:
                                    hero.enemy_decision = ""
                                    print("Retry. Unknown String Typed")
                                    wait(1)
                            hero.enemy_decision = ""
                            hero.decision = ""

                            # BASE ATTACK
                        elif hero.decision == "2":
                            type = hero.green_skill_info["type"]
                            if type == "damage":
                                for index, enemy in enumerate(self.enemies):
                                    if enemy is not None and not (enemy.health <= 0):
                                        enemy_number += 1
                                        print(f"({index + 1}): {enemy.name}")
                                    else:
                                        continue
                                hero.enemy_decision = input("Choose: ")
                                while hero.enemy_decision != "":
                                    if hero.enemy_decision == "1" and not (
                                            int(hero.enemy_decision) > len(self.enemies)) and not (enemy.health <= 0):
                                        hero.green_skill(self.enemies[0])
                                    elif hero.enemy_decision == "2" and not (
                                            int(hero.enemy_decision) > len(self.enemies)) and not (enemy.health <= 0):
                                        hero.green_skill(self.enemies[1])
                                    elif hero.enemy_decision == "3" and not (
                                            int(hero.enemy_decision) > len(self.enemies)) and not (enemy.health <= 0):
                                        hero.green_skill(self.enemies[2])
                                    elif hero.enemy_decision == "4" and not (
                                            int(hero.enemy_decision) > len(self.enemies) and not (enemy.health <= 0)):
                                        hero.green_skill(self.enemies[3])
                                    elif hero.enemy_decision == "5" and not (
                                            int(hero.enemy_decision) > len(self.enemies)) and not (enemy.health <= 0):
                                        hero.green_skill(self.enemies[4])
                                    else:
                                        hero.enemy_decision = ""
                                        print("retry. unknown string typed")
                                        wait(1)
                                hero.enemy_decision = ""
                                hero.decision = ""
                            elif type == "self heal":
                                hero.green_skill(enemy)
                                hero.enemy_decision = ""
                                hero.decision = ""
                        elif hero.decision == "3":
                            print("Passing to the next hero. . .")
                            wait(1)
                            hero.enemy_decision = ""
                            hero.decision = ""
                            break
                        else:
                            hero.decision = ""
                            print("Try again")
                battle_over(over, self.heros, self.enemies)
            for enemy in self.enemies:
                if enemy.health <= 0:
                    continue
                else:
                    MAIN_AI.hero = enemy
                    MAIN_AI.decide()

    def reset(self):
        for hero in self.heros:
            hero.reset()
        for enemy in self.enemies:
            enemy.reset()

def battle(heros, enemy_set1, enemy_set2, enemy_set3):
    battle = Battle(heros, enemy_set1)
    battle.battle()
    battle.enemies = enemy_set2
    battle.battle()
    battle.enemies = enemy_set3
    battle.battle()