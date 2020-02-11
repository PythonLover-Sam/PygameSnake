import pygame
from snake import *
from random import randint, choice


class Food():

    def __init__(self, positionX, positionY, type):
        self.positionX = positionX
        self.positionY = positionY
        self.rect = pygame.Rect(self.positionX, self.positionY, 25, 25)
        self.type = type  # 食物类型 “Yummy”为普通食物 增长一单位 “Speed”为加速食物，增加蛇头移动速度
        self.food_type = ['Yummy', 'Speed']

    def be_eaten(self, head, map_position):  # 食物被吃
        if self.type == "Yummy":
            head.add_length()
        elif self.type == "Speed":
            head.add_speed()
        self.refresh_food(map_position)
        if head._speed <= 45:
            self.type = choice(self.food_type)
        else:
            self.type = 'Yummy'


    def draw_food(self, screen):
        if self.type == 'Yummy':
            pygame.draw.rect(screen, (0, 100, 100, 30), self.rect)
        else:
            pygame.draw.rect(screen, (100, 255, 100, 30), self.rect)

    def check_rect(self, head, map_position):
        if self.rect.colliderect(head.rect):
            self.be_eaten(head, map_position)

    def refresh_food(self, map_position):
        x = randint(0, 399)
        self.positionX = map_position[x][0]
        self.positionY = map_position[x][1]
        self.rect = pygame.Rect(self.positionX, self.positionY, 25, 25)

