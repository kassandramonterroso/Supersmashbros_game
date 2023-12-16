import random

class SuperSmashBros():
    def __init__(self):
        self.health = 250
        self.characters = [Pikachu(), Kirby(), Yoshi()]

        self.fighter = self.select_fighter()
        self.fighter2 = random.choice(self.characters)
        self.beginfight(self.fighter, self.fighter2)

    def select_fighter(self):
        selected_fighter = input('''You are in a Super Smash Bros 
        competition, choose your fighter... Kirby, Pikachu, Yoshi ''')
        if selected_fighter == "Pikachu":
            return Pikachu()
        elif selected_fighter == "Kirby":
            return Kirby()
        elif selected_fighter == "Yoshi":
            return Yoshi()

    def beginfight(self, fighter, fighter2):
        print("You chose " + fighter.name + " as your fighter")
        print("Your competitor is ..." + fighter2.name + "!")
        hit_chance = 0.5  # 80% chance to hit

        while fighter.health > 0 and fighter2.health > 0:
            fighter_move = fighter.choosemove()
            print(fighter.name + " used " + fighter_move)

            if random.random() < hit_chance:
                fighter2.health -= fighter.moveset.get(fighter_move, 0)
                if fighter2.health <= 0:
                    print(fighter2.name + " was defeated. YOU WIN!")
                    break
            else:
                print(fighter2.name + " dodged the attack!")

            fighter2_move = fighter2.randommove()
            print(fighter2.name + " used " + fighter2_move)

            if random.random() < hit_chance:
                fighter.health -= fighter2.moveset.get(fighter2_move, 0)
                if fighter.health <= 0:
                    print("You were defeated by " + fighter2.name + ".")
                    break
            else:
                print("You dodged the attack!")

            print(fighter.name + "'s health:", fighter.health)
            print(fighter2.name + "'s health:", fighter2.health)


class Kirby(SuperSmashBros):
    def __init__(self):
        self.name = "Kirby"
        self.health = 100

    @property
    def moveset(self):
        return {"inhale": 20, "hammer": 37}

    def choosemove(self):
        print("Choose your character's move")
        for move in self.moveset:
            print(move)
        choice = input("Enter your desired move: ")
        return choice

    def randommove(self):
        return random.choice(list(self.moveset.keys()))


class Pikachu(SuperSmashBros):
    def __init__(self):
        self.name = "Pikachu"
        self.health = 100

    @property
    def moveset(self):
        return {"thunder": 50, "quickattack": 37}

    def choosemove(self):
        print("Choose your character's move")
        for move in self.moveset:
            print(move)
        choice = input("Enter your desired move: ")
        return choice

    def randommove(self):
        return random.choice(list(self.moveset.keys()))


class Yoshi(SuperSmashBros):
    def __init__(self):
        self.name = "Yoshi"
        self.health = 100

    @property
    def moveset(self):
        return {"eggthrow": 35, "superdragon": 60}

    def choosemove(self):
        print("Choose your character's move")
        for move in self.moveset:
            print(move)
        choice = input("Enter your desired move: ")
        return choice

    def randommove(self):
        return random.choice(list(self.moveset.keys()))


SuperSmashBros()