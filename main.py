import pygame
import time
#import sys
import random
#from pygame.locals import QUIT
from pong_ball import Ball
from pong_paddle import Paddle

# defining screen
colour = (1, 1, 255)
pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 500))
DISPLAYSURF.fill(colour)
white = (255, 255, 255)
font = pygame.font.SysFont('Times New Roman', 20)
# menu
in_menu = True
rectangle1 = pygame.Rect(200, 300, 100, 40)
pygame.draw.rect(DISPLAYSURF, white, rectangle1)
text = font.render("Infinate pong", False, white)
DISPLAYSURF.blit(text, (200, 50))
text = font.render("start", False, colour)
DISPLAYSURF.blit(text, (230, 310))

while in_menu:
    time.sleep(0.01)
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 200 <= mouse[0] <= 300 and 300 <= mouse[1] <= 340:
                in_menu = False

                break
    pygame.display.update()

# setting up game variables
ball = Ball()

paddle_1 = Paddle()
paddle_1.rect.x = 10
paddle_1.rect.y = 245
paddle_1_y = 245
paddle_2_y = 245
paddle_2 = Paddle()
paddle_2.rect.x = 480
paddle_2.rect.y = 245
paddle_1_vel_y = 0
paddle_2_vel_y = 0
ball_x = 245
ball_y = 245
ball_vel_x = 2.5
ball_vel_y = random.randint(-5, 5)
paddle_1_score = 0
paddle_2_score = 0

Running = True
all_sprites = pygame.sprite.Group()
all_sprites.add(ball, paddle_1, paddle_2)
outcome = 0

delay = 0.025
Running = True


def draw_game_objects():
    DISPLAYSURF.fill(colour)

    text = font.render(str(paddle_1_score) + "                                          " + str(paddle_2_score), False,
                       white)
    text_rect = text.get_rect()
    text_rect = (100, 50)

    pygame.draw.lines(DISPLAYSURF, (0, 0, 0), closed=True, points=[(250, 0), (250, 500)], width=2)

    DISPLAYSURF.blit(text, text_rect)

    all_sprites.draw(DISPLAYSURF)
    pygame.display.update()


def get_predicted_outcome():
    Y_outcome = ((480 - ball_x) / ball_vel_x) * ball_vel_y + ball_y

    while Y_outcome < 0 or Y_outcome >= 500:
        if Y_outcome < 0:
            Y_outcome = -Y_outcome
        elif Y_outcome >= 500:
            Y_outcome = 1000 - Y_outcome
    return Y_outcome


def alline_variables():
    ball.rect.x = ball_x
    ball.rect.y = ball_y
    paddle_1.rect.y = paddle_1_y
    paddle_2.rect.y = paddle_2_y


collide_paddle_1 = pygame.sprite.collide_rect(ball, paddle_1)
collide_paddle_2 = pygame.sprite.collide_rect(ball, paddle_2)
outcome = get_predicted_outcome()
while Running:
    alline_variables()

    for event in pygame.event.get():
        None

    if ball_x < 100 or ball_x > 400:

        if ball_x < 0:
            paddle_2_score += 1
            ball_x = 245
            ball_y = 245
            ball_vel_x = 2.5
            ball_vel_y = random.randint(-5, 5)
            outcome = get_predicted_outcome()
            paddle_2_y = 200
            paddle_1_y = 200
            delay = 0.025

        if ball_x >= 500:
            paddle_1_score += 1
            ball_x = 245
            ball_y = 245
            ball_vel_x = -2.5
            ball_vel_y = random.randint(-5, 5)
            paddle_1_y = 200
            paddle_2_y = 200
            delay = 0.025
        # check if ball hit paddles
        collide_paddle_1 = pygame.sprite.collide_rect(ball, paddle_1)
        collide_paddle_2 = pygame.sprite.collide_rect(ball, paddle_2)
        if collide_paddle_1:
            ball_vel_x *= -1.1
            ball_vel_y = (ball_vel_y) + (0.5 * paddle_1_vel_y)

            outcome = get_predicted_outcome()

        elif collide_paddle_2:
            ball_vel_x *= -1.1
            ball_vel_y = (ball_vel_y) + (0.5 * paddle_2_vel_y)

    if outcome >= paddle_2_y + 45:
        paddle_2_vel_y += 0.6 if paddle_2_score - paddle_1_score < 2 else 0.55

    elif outcome <= paddle_2_y + 45:
        paddle_2_vel_y -= 0.6 if paddle_2_score - paddle_1_score < 2 else 0.55

    ball_x += ball_vel_x
    ball_y += ball_vel_y

    if ball_y > 490 or ball_y <= 0:

        ball_vel_y *= -1
        if ball_y > 490:
            ball_y = 490
        else:
            ball_y = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle_1_vel_y -= 1
    elif keys[pygame.K_DOWN]:
        paddle_1_vel_y += 1

    paddle_1_y += paddle_1_vel_y
    if paddle_1_vel_y >= 0.5:
        paddle_1_vel_y -= 0.5
    elif paddle_1_vel_y <= -0.5:
        paddle_1_vel_y += 0.5
    else:
        paddle_1_vel_y = 0

    if paddle_1_vel_y > 5:
        paddle_1_vel_y = 5
    elif paddle_1_vel_y < -5:
        paddle_1_vel_y = -5

    if paddle_1_y > 400:
        paddle_1_y = 400
        paddle_1_vel_y = 0
    elif paddle_1_y < 0:
        paddle_1_y = 0
        paddle_1_vel_y = 0

    paddle_2_y += paddle_2_vel_y
    if paddle_2_vel_y >= 0.5:
        paddle_2_vel_y -= 0.5
    elif paddle_2_vel_y <= -0.5:
        paddle_2_vel_y += 0.5
    else:
        paddle_2_vel_y = 0

    if paddle_2_vel_y > 5:
        paddle_2_vel_y = 5
    elif paddle_2_vel_y < -5:
        paddle_2_vel_y = -5

    if paddle_2_y > 400:
        paddle_2_y = 400
        paddle_2_vel_y = 0
    elif paddle_2_y < 0:
        paddle_2_y = 0
        paddle_2_vel_y = 0

    # alline_variables()
    time.sleep(delay)
    draw_game_objects()

pygame.quit()