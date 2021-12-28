import random


class Game:
    def __init__(self, steps, player):
        self.steps = steps
        self.player = player
        self.survived = 0

    def p_survived(self):
        self.survived += 1

    def step(self):
        self.step -= 1

    def simulate(self):
        for p in self.player:
            while not p.is_dead():
                self.steps -= 1
                if p.jump(self.steps) or self.steps < 0:
                    self.survived += 1
                    break

    def get_survived(self):
        return self.survived


class Player:
    def __init__(self, name):
        self.name = name
        self.p_steps = 0
        self.dead = False

    def jump(self, steps):
        choice = random.randint(0, 1)
        if choice == 0 and steps > 0:
            self.dead = True
        elif steps == 0:
            return True
        else:
            self.p_steps += 1
            return False

    def is_dead(self):
        return self.dead

    def get_p_steps(self):
        return self.p_steps


if __name__ == '__main__':
    RUNS = 100_000
    STEPS = 18
    result = 0

    for i in range(RUNS):
        p1 = Player('456')
        p2 = Player('067')
        p3 = Player('218')
        p4 = Player('054')
        p5 = Player('002')
        p6 = Player('007')
        p7 = Player('123')
        p8 = Player('110')
        p9 = Player('112')
        p10 = Player('119')
        p11 = Player('020')
        p12 = Player('033')
        p13 = Player('109')
        p14 = Player('111')
        p15 = Player('116')
        p16 = Player('122')
        game = Game(STEPS, [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16])
        game.simulate()
        result += game.get_survived()

    print(round(result / RUNS, 0))