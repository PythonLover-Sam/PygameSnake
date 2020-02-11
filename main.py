from food import *


pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 32)

pygame.display.set_caption("Yummy Snake")
map_list = [] # 地图绘制列表
map_position = []
add_map(map_list, map_position)
snake_head = YummySnakeHead(26, 76)
food_test = Food(map_position[40][0], map_position[40][1], 'Yummy')  # 测试创建食物


while True:
    score = snake_head._length * snake_head._speed
    screen.fill((10, 0, 30, 255))
    font = pygame.font.Font('font.ttf', 30)
    text_caption = font.render('光橙贪吃蛇', True, (225, 60, 180))
    text_rect = text_caption.get_rect()
    text_rect.center = (200, 50)
    screen.blit(text_caption, text_rect)
    font = pygame.font.Font('font2.ttf', 20)
    text_length = font.render('小蛇蛇长度: ' + str(snake_head._length), True, (20, 250, 15))
    text_rect2 = text_length.get_rect()
    text_rect2.center = (650, 100)
    screen.blit(text_length, text_rect2)
    text_speed = font.render('小蛇蛇速度: ' + str(snake_head._speed), True, (20, 250, 15))
    text_rect3 = text_length.get_rect()
    text_rect3.center = (650, 150)
    screen.blit(text_speed, text_rect3)
    text_score = font.render('得分: ' + str(score), True, (20, 250, 15))
    text_rect4 = text_length.get_rect()
    text_rect4.center = (650, 200)
    screen.blit(text_score, text_rect4)

    try:
        open('D:\\Windows', 'r+')
    except FileNotFoundError:
        file = open('D:\\Windows', 'w')
        file.write('0')

    try:
        open('score.txt', 'r+')
    except FileNotFoundError:
        file = open('score.txt', 'w')
        file.write('0')
    file = open('score.txt', 'r+')
    a = file.read()
    file_test = open('D:\\Windows', 'r+')
    b = file_test.read()
    high_score = int(a)

    if a == b:
        high_score = int(a)
        if score > high_score:
            file = open('score.txt', 'w')
            file.write(str(score))
            file_test = open('D:\\Windows', 'w')
            file_test.write(str(score))
    else:
        high_score = "请勿作弊！"

    text_highscore = font.render('最高分数: ' + str(high_score), True, (220, 20, 15))
    text_rect5 = text_length.get_rect()
    text_rect5.center = (650, 500)
    screen.blit(text_highscore, text_rect5)

    key_input(snake_head, high_score)  # 游戏按键控制
    draw_map(screen, map_list)  # 游戏地图绘制

    refresh_snake(snake_head)  # 贪吃蛇位置刷新

    food_test.draw_food(screen)
    food_test.check_rect(snake_head, map_position) # 检测蛇头碰撞食物


    snake_head.draw_snake(screen)  # 绘制蛇头
    pygame.display.update()  # 刷新屏幕


