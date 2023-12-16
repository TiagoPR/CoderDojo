from time import sleep
import time
import pygame
import random
from pygame import Vector2
from enum import Enum
from random import randint

def apple_draw(pos):
    pygame.draw.rect(screen, "red", pygame.Rect(pos, (step, step)))

def snake_draw(snake):
    for p in snake:
        pygame.draw.rect(screen, (1, randint(50,200), 1), pygame.Rect(p, (step,step)))

def snake_incr(snake, direction, grow):
    if not grow:
        snake.pop()

    snake.insert(0, Vector2(snake[0].x, snake[0].y))

    match direction:
        case Direction.UP:
            snake[0].y -= step
            if snake[0].y < 0:
                snake[0].y = screen.get_height() - step
        case Direction.DOWN:
            snake[0].y += step
            if snake[0].y >= screen.get_height():
                snake[0].y = 0
        case Direction.LEFT:
            snake[0].x -= step
            if snake[0].x < 0:
                snake[0].x = screen.get_width() - step
        case Direction.RIGHT:
            snake[0].x += step
            if snake[0].x >= screen.get_width():
                snake[0].x = 0

def text_draw(points, font, text_col, x, y):
    img = font.render("SCORE: " + points, True, text_col)
    screen.blit(img, (x,y))

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
dt = 0
step = 36
Direction = Enum('Direction', ['UP', 'DOWN', 'LEFT', 'RIGHT'])
text_font = pygame.font.SysFont("Consola", 40)
boardLength = 20
cnt = 0
size = 36

dir = Direction.RIGHT

snake_arr = []
snake_arr.append(Vector2(screen.get_width() / 2, screen.get_height() / 2))
snake_arr.append(Vector2((screen.get_width() / 2) - step, screen.get_height() / 2))
print(snake_arr)

apple_pos = Vector2(random.randint(1,19) * step, random.randint(1,19) * step)

snake_draw(snake_arr)

pygame.display.flip()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((170,215,81))

    for i in range(-1,boardLength+1):
        for z in range(-1,boardLength+1):
            if cnt % 2 == 0:
                pass#pygame.draw.rect(screen, (170,215,81) ,[size*z,size*i,size,size])
            else:
                pygame.draw.rect(screen, (162,209,73) , [size*z,size*i,size,size])
            cnt +=1
        #since theres an even number of squares go back one value
        cnt-=1

    pygame.display.update()

    a = str(len(snake_arr) - 2)
    text_draw(a, text_font, "black", 20, screen.get_height() - 30)

    snake_draw(snake_arr)
    apple_draw(apple_pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        dir = Direction.UP
        #player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        dir = Direction.DOWN
       # player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        dir = Direction.LEFT
        #player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        dir = Direction.RIGHT
       # player_pos.x += 300 * dt

    if snake_arr[0] in snake_arr[1:]:
        break       

    grow = snake_arr[0] == apple_pos

    if grow:
        apple_pos = Vector2(random.randint(1,19) * step, random.randint(1,19) * step)
        while apple_pos in snake_arr:
            apple_pos = Vector2(random.randint(1,19) * step, random.randint(1,19) * step)

    snake_incr(snake_arr, dir, grow)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(7) / 1000

pygame.quit()