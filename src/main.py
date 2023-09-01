import pygame
import random

# 初始化
pygame.init()

# 游戏界面的宽和高
width = 640
height = 480

# 颜色定义
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# 创建游戏窗口
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇游戏")

# 蛇的初始位置和速度
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_speed = 15

# 食物的初始位置
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
food_spawn = True

# 方向设置：上、下、左、右
up = False
down = False
left = False
right = False

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # 键盘事件处理
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_LEFT]:
                left = True
                right = False
                up = False
                down = False
            if keys[pygame.K_RIGHT]:
                left = False
                right = True
                up = False
                down = False
            if keys[pygame.K_UP]:
                left = False
                right = False
                up = True
                down = False
            if keys[pygame.K_DOWN]:
                left = False
                right = False
                up = False
                down = True
    
    # 移动蛇头
    if left:
        snake_pos[0] -= 10
    if right:
        snake_pos[0] += 10
    if up:
        snake_pos[1] -= 10
    if down:
        snake_pos[1] += 10
    
    # 增加蛇的长度
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False
    else:
        snake_body.pop()
    
    if not food_spawn:
        food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
    food_spawn = True
    
    # 绘制蛇和食物
    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
    
    pygame.draw.rect(screen, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    
    pygame.display.flip()
    
    # 游戏结束条件
    if snake_pos[0] >= width or snake_pos[0] <= 0 or snake_pos[1] >= height or snake_pos[1] <= 0:
        pygame.quit()
        quit()
    
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            pygame.quit()
            quit()
    
    pygame.time.Clock().tick(snake_speed)
