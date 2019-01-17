########################################
############### GAME START #############
########################################

import os
import random


class Game:
    is_run = True
    map = []
    warrior = None
    monsters = []
    current = None
    opt = ''

    def __init__(self):
        self.warrior = Warrior(0, 100, 10)
        for i in range(2000):
            self.map.append(0)
        for i in range(100):
            self.monsters.append(Monster(random.randint(10, 2000), 80, 2))

    def run(self):
        self.update()
        self.show_info()
        while self.is_run:
            self.input()
            os.system('clear')
            self.update()
            self.show_info()
        print("Game Over")

    def update(self):
        for i in range(len(self.map)):
            self.map[i] = 0

        for m in self.monsters:
            if m.hp <= 0:
                self.monsters.remove(m)

        for i in range(len(self.map)):
            if self.warrior.pos == i:
                self.map[i] = 1

            for w in self.monsters:
                if w.pos == i:
                    self.map[i] = 2

        self.map_str = ''
        for i in range(len(self.map)):
            if self.map[i] == 1:
                self.map_str = self.map_str + "🧜‍♂️_"
            elif self.map[i] == 2:
                self.map_str = self.map_str + "👻_"
            else:
                self.map_str = self.map_str + "_"

    def show_info(self):
        print(self.map_str)
        print("Warrior   HP:%d  FP:%d POS:%d" %
              (self.warrior.hp, self.warrior.fp, self.warrior.pos))
        if self.current:
            print("Monster   HP:%d  FP:%d POS:%d" %
                  (self.current.hp, self.current.fp, self.current.pos))

    def input(self):
        x = input()
        if x == 'a' or x == 'd':
            self.warrior.move(x)

        if x == 'q':
            self.is_run = False

        if x == 'f':
            for m in self.monsters:
                if self.warrior.pos+1 == m.pos:
                    self.current = m
                    m.hp = m.hp - self.warrior.fp
                    self.warrior.hp = self.warrior.hp - m.fp


class Actor:
    def __init__(self, pos, hp, fp):
        self.pos = pos
        self.hp = hp
        self.fp = fp

    def fire(self, obj):
        obj.hp = obj.hp - obj.fp


class Warrior(Actor):
    def move(self, dir):
        if dir == 'a':
            self.pos = self.pos - 1
        elif dir == 'd':
            self.pos = self.pos + 1


class Monster(Actor):
    pass


game = Game()
game.run()

########################################
########################################
