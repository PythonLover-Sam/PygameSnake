"""贪吃蛇实现"""
import pygame
from gameFunction import *


class YummySnakeBody():  # 贪吃蛇身体类
    def __init__(self, positionX, positionY, next):
        self._last = None  # 上一段身体
        self._next = next  # 下一段身体
        self._positionX = positionX  # 此段身体的X位置
        self._positionY = positionY  # 此段身体的Y位置
        self._lastPositionX = 0  # 此段身体上一时刻的X位置
        self._lastPositionY = 0  # 此段身体上一时刻的Y位置
        self.rect = pygame.Rect(self._positionX, self._positionY, 25, 25)  # 此段身体的碰撞块

    def update_position(self):  # 蛇身体位置更新方法

        self._lastPositionX = self._positionX
        self._lastPositionY = self._positionY
        self._positionX = self._next._lastPositionX
        self._positionY = self._next._lastPositionY
        self.rect = pygame.Rect(self._positionX, self._positionY, 25, 25)
        if self._last is not None:
            self._last.update_position()
        else:
            pass

    def check_rect(self, head):  # 递归调用碰撞检测

        if(head.rect.colliderect(self.rect)):
            head.death()
        elif self._last is not None:
            self._last.check_rect(head)

    def add_length(self):  # 增加蛇身体长度方法
        if self._last is None:
            self._last = YummySnakeBody(self._lastPositionX, self._lastPositionY, self)
        else:
            self._last.add_length()

    def draw_snake(self, screen):  # 绘制身体方法

        pygame.draw.rect(screen, (100, 20, 10, 20), (self._positionX, self._positionY, 25, 25))
        if self._last is not None:
            self._last.draw_snake(screen)


class YummySnakeHead(YummySnakeBody):  # 蛇头类

    def __init__(self, positionX, positionY):
        super(YummySnakeBody, self).__init__()
        self.canMove = True  # 蛇移动控制信号
        self._length = 1  # 蛇长度计数器
        self._direction = 'STOP'  # 蛇移动方向变量
        self._speed = 1  # 蛇移动速度变量
        self._state = 'ALIVE'  # 蛇是否存活状态变量
        self._last = None
        self._next = None
        self._positionX = positionX
        self._positionY = positionY
        self.rect = pygame.Rect(self._positionX, self._positionY, 25, 25)

    def add_speed(self):
        if self._speed < 45:
            self._speed += 1

    def getX(self):  # 返回蛇头X坐标
        return self._positionX

    def getY(self):  # 返回蛇头Y坐标
        return self._positionY

    def add_length(self):

        self._length += 1
        if self._last is None:
            self._last = YummySnakeBody(self._lastPositionX, self._lastPositionY, self)
        else:
            self._last.add_length()

    def change_direction(self, direction):
        if self._last is not None:
            if direction == 'UP' and self._last._positionY >= self._positionY:
                self._direction = 'UP'
            if direction == 'DOWN' and self._last._positionY <= self._positionY:
                self._direction = 'DOWN'
            if direction == 'LEFT' and self._last._positionX >= self._positionX:
                self._direction = 'LEFT'
            if direction == 'RIGHT' and self._last._positionX <= self._positionX:
                self._direction = 'RIGHT'
        else:
            if direction == 'UP':
                self._direction = 'UP'
            if direction == 'DOWN':
                self._direction = 'DOWN'
            if direction == 'LEFT':
                self._direction = 'LEFT'
            if direction == 'RIGHT':
                self._direction = 'RIGHT'

    def death(self):  # 蛇死亡方法
        self._state = 'DEAD'
        restart_game(self)
        return True

    def draw_snake(self, screen):
        pygame.draw.rect(screen, (160, 70, 80, 255), (self._positionX, self._positionY, 25, 25))
        if self._last is not None:
            self._last.draw_snake(screen)

    def check_rect(self):
        if self._last is not None:
            if(self.rect.colliderect(self._last.rect)):
                self.death()

            else:
                self._last.check_rect(self)

    def update_position(self):
        self.check_rect()

        if (self._positionY > 590 or self._positionY <70) or (self._positionX < 25 or self._positionX >520) :
            self.death()

        self._lastPositionX = self._positionX
        self._lastPositionY = self._positionY
        if self._last is None:
            if self._direction == 'UP':
                self._positionY -= 26

            if self._direction == 'DOWN':
                self._positionY += 26

            if self._direction == 'LEFT':
                self._positionX -= 26

            if self._direction == 'RIGHT':
                self._positionX += 26
        else:
            if self._direction == 'UP':
                self._positionY -= 26

            if self._direction == 'DOWN':
                self._positionY += 26

            if self._direction == 'LEFT':
                self._positionX -= 26

            if self._direction == 'RIGHT':
                self._positionX += 26

            self._last.update_position()
        self.rect = pygame.Rect(self._positionX, self._positionY, 25, 25)
