from heros import *
from time import sleep as wait
from AI import AI

DEBUG = True  # Don't mess with this
if DEBUG:
    Froggy = Hero("Froggy", 2, 1000, 250, level=1, base_attack_stat=1,
                  rank_2_skill_info={"name": "Whirlpool", "type": "damage"})

    Sludge = Hero("Sludge", 2, 1000, 250, level=1, base_attack_stat=2,
                  rank_2_skill_info={"name": "Flower of the Earth", "type": "self heal"})
    Froggladior = Hero("Froggladior", 2, 1500, 350, level=1,
                       rank_2_skill_info={"name": "Downfall", "type": "self heal"})
    Frogglar = Hero("asdf", 2, 1500, 250, level=1, rank_2_skill_info={"name": "Downfall", "type": "damage"})

    h = [Froggy, Froggladior]
    e = [Sludge, Frogglar]


class Battle:
    def __init__(self, watchers, enemies):
        self.heros = watchers
        self.enemies = enemies

    def battle(self):
        over = 0
        MAIN_AI = AI(self.heros, self.heros[1])

        def battle_over(over_var, hero_list, enemy_list):
            # Checking that all heros are dead:
            if all(hero.permissions == "dead" for hero in heroes_list):
                print("You Lose. All Watchers Are Dead")
                over_var += 1
            elif all(enemy.permissions == "dead" for enemy in enemy_list):
                over_var = True
                print("You Win!")
                over_var += 1
            else:
                return False

        # Making Sure that All Lists are not over 5
        if len(self.heros) > 5:
            print("Go to feedback and report \"Battle Failed\"")

        while not over:
            for hero in self.heros:
                if hero.health <= 0:
                    continue
                else:
                    hero.decision = ""
                    hero.enemy_decision: str = ""
                    while hero.decision == "":
                        enemy_number = 0
                        print(f"Choose one action for {hero.name}:")
                        print("\n")
                        wait(1)
                        print("(1): Base Attack")
                        wait(0.5)
                        print("(2): Rank 2 Skill")
                        wait(0.5)
                        print("(3): Pass")
                        wait(0.5)
                        hero.decision = input("Choose: ")
                        if hero.decision == "1":
                            print("Which Enemy Are You Going To Attack?")
                            wait(1)

                            for index, enemy in enumerate(self.enemies, start=1):
                                if enemy.health > 0:
                                    print(f"({index}): {enemy.name}")
                                else:
                                    continue
                            hero.enemy_decision = input("Choice: ")
                            moved = 0
                            while moved == 0:
                                if hero.enemy_decision.isdigit() and int(hero.enemy_decision) <= len(
                                        self.enemies) and not self.enemies[int(hero.enemy_decision) - 1].health <= 0:
                                    hero.base_attack(self.enemies[int(hero.enemy_decision) - 1])
                                    moved += 1
                                else:
                                    hero.enemy_decision = ""
                                    print("Retry. Unknown String Typed")
                                    hero.enemy_decision = input("Choice: ")
                                    wait(1)

                            # Green Skill
                        elif hero.decision == "2":
                            type = hero.green_skill_info["type"]
                            if hero.energy >= 20:
                                if type == "damage":
                                    for index, enemy in enumerate(self.enemies):
                                        if enemy is not None and not (enemy.health <= 0):
                                            enemy_number += 1
                                            print(f"({index + 1}): {enemy.name}")
                                        else:
                                            continue
                                    hero.enemy_decision = input("Choose: ")
                                    while moved == 0:
                                        if hero.enemy_decision.isdigit() and int(hero.enemy_decision) <= len(
                                                self.enemies) and not self.enemies[
                                                                          int(hero.enemy_decision) - 1].health <= 0:
                                            hero.base_attack(self.enemies[int(hero.enemy_decision) - 1])
                                            moved += 1
                                        else:
                                            hero.enemy_decision = ""
                                            print("Retry. Unknown String Typed")
                                            hero.enemy_decision = input("Choice: ")
                                            wait(1)

                                elif type == "self heal":
                                    hero.rank_2_skill()
                                    hero.decision = ""
                                    hero.enemy_decision = ""
                                    break
                            else:
                                hero.decision = ""
                                print("Not enough energy.")
                        elif hero.decision == "3":
                            print("Passing to the next hero. . .")
                            hero.energy += 30
                            wait(1)
                            break
                        else:
                            hero.decision = ""
                            print("Try again")
                    hero.enemy_decision = ""
                    hero.decision = ""
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


def standard_battle(heros, enemy_set1, enemy_set2, enemy_set3):
    battle = Battle(heros, enemy_set1)
    battle.battle()
    battle.enemies = enemy_set2
    battle.battle()
    battle.enemies = enemy_set3
    battle.battle()
    battle.reset()


def sing_round_battle(heros, enemies):
    battle = Battle(heros, enemies)
    battle.battle()
    battle.reset()
