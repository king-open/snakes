import pygame
import random

# 初始化Pygame
pygame.init()

# 游戏窗口大小和速度设置
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
SNAKE_SPEED = 10

# 定义颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 创建游戏窗口
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("贪吃蛇游戏")

# 初始化贪吃蛇位置和速度
snake_x = 50
snake_y = 50
snake_speed_x = 10
snake_speed_y = 0

# 初始化贪吃蛇身体
snake_body = [(snake_x, snake_y)]

# 初始化食物位置
food_x = random.randint(0, WINDOW_WIDTH // 10 - 1) * 10
food_y = random.randint(0, WINDOW_HEIGHT // 10 - 1) * 10

# 初始化分数
score = 0

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_speed_y == 0:
                snake_speed_x = 0
                snake_speed_y = -10
            elif event.key == pygame.K_DOWN and snake_speed_y == 0:
                snake_speed_x = 0
                snake_speed_y = 10
            elif event.key == pygame.K_LEFT and snake_speed_x == 0:
                snake_speed_x = -10
                snake_speed_y = 0
            elif event.key == pygame.K_RIGHT and snake_speed_x == 0:
                snake_speed_x = 10
                snake_speed_y = 0

    # 移动贪吃蛇
    snake_x += snake_speed_x
    snake_y += snake_speed_y

    # 判断是否吃到食物
    if snake_x == food_x and snake_y == food_y:
        score += 1
        food_x = random.randint(0, WINDOW_WIDTH // 10 - 1) * 10
        food_y = random.randint(0, WINDOW_HEIGHT // 10 - 1) * 10
    else:
        snake_body.pop(0)

    # 判断游戏是否结束
    if snake_x < 0 or snake_x >= WINDOW_WIDTH or snake_y < 0 or snake_y >= WINDOW_HEIGHT or (snake_x, snake_y) in snake_body:
        running = False

    # 更新贪吃蛇身体
    snake_body.append((snake_x, snake_y))

    # 清空窗口
    window.fill(WHITE)

    # 绘制贪吃蛇身体
    for segment in snake_body:
        pygame.draw.rect(window, GREEN, pygame.Rect(segment[0], segment[1], 10, 10))

    # 绘制食物
    pygame.draw.rect(window, RED, pygame.Rect(food_x, food_y, 10, 10))

    # 更新分数
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, GREEN)
    window.blit(score_text, (10, 10))

    # 更新窗口
    pygame.display.flip()

    # 控制游戏速度
    pygame.time.Clock().tick(SNAKE_SPEED)

# 游戏结束后关闭Pygame
pygame.quit()
