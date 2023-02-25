from time import sleep


def wait():
    sleep(1)


heroes_list = []


class Hero:
    permissions = "living"
    MAIN_STATS = ("fire", "water", "wind", "earth")
    ATTACK_STATS = ["physical", "magic", "pure"]
    energy = 0
    decision = ""
    enemy_decision = ""

    def __init__(self, name, health, attack, level=1, base_attack_stat=0,
                 rank_2_skill_info: dict = False, rank_1_skill_info: dict = False):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack = attack
        self.level = level
        self.base_attack_stat = self.ATTACK_STATS[base_attack_stat]
        self.rank_2_skill_info = rank_2_skill_info
        self.rank_1_skill_info = rank_1_skill_info
        heroes_list.append(self)

    def __str__(self):
        print(f"{self.name}, {self.permissions}, {self.health}")

    def base_attack(self, enemy):
        if self.permissions == "dead":
            print(
                "You are dead. Request assistance from another hero with the power of reviving. (SAY THE MESSAGE IN COMMENTS)")
            wait()
            return f"{self.name} tried to attack while dead."
        if enemy.permissions == "dead":
            print(f"Attacking failed. {enemy.name} is already dead!(SAY THE MESSAGE IN COMMENTS) ")
            wait()
            return f"{self.name} tried to attack a dead enemy."
        else:
            if (enemy.health - self.attack) <= 0:
                print(f"{self.name} dealt {self.attack} {self.base_attack_stat} damage to {enemy.name}! \n \
{enemy.name} is dead!")
                self.energy += 25
                enemy.permissions = "dead"
                enemy.health = 0
                wait()
                return f'{self.name} dealt {self.attack} {self.base_attack_stat} damage to {enemy.name}. {enemy.name} is dead. \n'
            else:
                print(f"{self.name} dealt {self.attack} {self.base_attack_stat} damage to {enemy.name}! \n \
{enemy.name} only has {enemy.health - self.attack} health left!")
                wait()
                enemy.health = enemy.health - self.attack
                self.energy += 20
                return f"{self.name} dealt {self.attack} {self.base_attack_stat} damage to {enemy.name}. {enemy.name}'s health is {enemy.health} \n"

    def rank_1_skill(self, enemies=None, allies=None, enemy=None, ally=None):
        if self.permissions == "dead":
            print(f"Stop it.")
            return None
        if not self.rank_1_skill_info:
            print(f"{self.name} doesn't have a Gray Skill Implemented Yet")
            return None
        if self.energy >= 150:
            self.energy -= 150
            if self.rank_1_skill_info["type"] == "all damage":
                print(f"{self.name} used their gray skill {self.rank_1_skill_info['name']} on the enemies!")
                if enemies is not None:
                    for e in enemies:
                        if (e.health - (self.attack + 500)) <= 0:
                            print(f"{e.name} is dead.")
                            e.health = 0
                        else:
                            e.health -= (self.attack + 500)
                            print(
                                f"{e.name} only has {e.health} health left.")
                else:
                    print("ERROR")
            elif self.rank_1_skill_info["type"] == "all heal":
                print(f"{self.name} used their gray skill {self.rank_1_skill_info['name']} on the enemies!")
                if allies is not None:
                    for a in allies:
                        if (a.health + (self.attack + 500)) >= a.max_health:
                            print(f"{a.name} got healed by {self.attack + 500 - a.max_health}! {a.name} is now at " 
                                  "max health.")
                            a.health = 0
                        else:
                            a.health += (self.attack + 500)
                            print(f"{a.name} got healed by {self.attack + 500}! {a.name}'s health is now at {a.health}")
                else:
                    print("ERROR")
    def rank_2_skill(self, enemy=None):
        if self.permissions == "dead":
            print(f"Stop it.")
            return None
        if not self.rank_2_skill_info:
            print(f"{self.name} doesn't have a Green Skill Implemented Yet")
            return None

        if self.energy >= 20:
            self.energy -= 20
            if self.rank_2_skill_info['type'] == "sing. damage":
                if (enemy.health - (self.attack + 300)) < 0:
                    print(
                        f"{self.name} used their green skill {self.rank_2_skill_info['name']} and dealt "
                        f"{(self.attack + 300) - enemy.health} damage to {enemy.name} \n"
                        f"{enemy.name} is dead.")
                    enemy.health = 0
                else:
                    enemy.health -= (self.attack + 300)
                    print(
                        f"{self.name} used their green skill {self.rank_2_skill_info['name']} and dealt "
                        f"{self.attack + 300} damage to {enemy.name} \n"
                        f"{enemy.name} only has {enemy.health} health left.")
            if self.rank_2_skill_info['type'] == "self heal":
                if (self.health + 350) > self.max_health:
                    print(
                        f"{self.name} used their green skill {self.rank_2_skill_info['name']} and healed themselves by "
                        f"{(self.health + 350) - self.max_health}. \n"
                        f"{self.name}'s health is now at {self.max_health}!")
                    self.health = self.max_health
                else:
                    self.health += 350
                    print(f"{self.name} used their green skill {self.rank_2_skill_info['name']} and healed by 350!" +
                          f"{self.name}'s health is now at {self.health}")
        else:
            print(f"{self.name} Does Not Enough Energy")

    def reset(self):
        self.permissions = "living"
        self.health = self.max_health
        self.energy = 0


DEBUG = False
if DEBUG:
    print("Handful of code")
