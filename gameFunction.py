import pygame
from pygame.locals import *
from sys import exit
from time import time

global delta_time
delta_time = 0

def high_score_reload():
    file = open('score.txt', 'w')
    file.write('0')
    file_test = open('D:\\Windows', 'w')
    file_test.write('0')
# 贪吃蛇移动刷新
def refresh_snake(snake_head):
    global delta_time
    """if 0 <= pygame.time.get_ticks() % (500-10*(snake_head._speed-1)) <= 4 and snake_head.canMove is True:
        snake_head.update_position()
        snake_head.canMove = False

    elif 0 <= pygame.time.get_ticks() % (500-10*(snake_head._speed-1)) <= 7 and snake_head.canMove is False:
        snake_head.canMove = True"""
    if int(time()*100) % 1000000 % (50 - 1 * (snake_head._speed - 1)) == 0 and snake_head.canMove is True and (int(time()*100) % 1000000) - delta_time > 10:
        snake_head.update_position()
        snake_head.canMove = False
        delta_time = int(time()*100) % 1000000

    elif int(time()*100) % 1000000 % (50 - 1 * (snake_head._speed - 1)) != 0 and snake_head.canMove is False:
        snake_head.canMove = True




# 游戏按键控制
def key_input(snake_head, highscore):
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                snake_head.change_direction('UP')

            if event.key == K_DOWN:
                snake_head.change_direction('DOWN')

            if event.key == K_LEFT:
                snake_head.change_direction('LEFT')

            if event.key == K_RIGHT:
                snake_head.change_direction('RIGHT')

            if event.key == K_SPACE:
                snake_head.add_length()
            if highscore == '请勿作弊！':
                high_score_reload()


# 贪吃蛇死亡初始化
def restart_game(snake_head):
    snake_head._last = None
    snake_head._length = 1
    snake_head.canMove = True  # 蛇移动控制信号
    snake_head._direction = 'STOP'  # 蛇移动方向变量
    snake_head._speed = 1  # 蛇移动速度变量
    snake_head._state = 'ALIVE'  # 蛇是否存活状态变量
    snake_head._positionX = 26
    snake_head._positionY = 76



# 创建地图
def add_map(list, list2):
    x_position, y_position = 0, 0
    delta_add = 26
    for i in range(20):
        x_position = 0
        y_position += delta_add
        for j in range(20):
            x_position += delta_add
            list2.append((x_position, 50+y_position))
            list.append(pygame.Rect(x_position, 50+y_position, 25, 25))


# 绘制地图
def draw_map(screen, list):
    for rect in list:
        pygame.draw.rect(screen, (185, 185, 185), rect)

