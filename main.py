import pygame
import random
import sys
from pygame.locals import *

BG_COLOR = (8, 217, 214)
WHITE = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
mainClock = pygame.time.Clock()
pygame.init()
pygame.font.init()
pygame.display.set_caption("Basic Math Game")
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 64)
font = pygame.font.SysFont("Sans", 32)
font_number = pygame.font.SysFont("Sans", 180)
image = pygame.image.load('zehraoyun.png')
image2 = pygame.image.load('addition-sign.png')
image3 = pygame.image.load('minus-sign.png')
image4 = pygame.image.load('equal.png')
image5 = pygame.image.load('gameover.png')
image6 = pygame.image.load('check.png')


def draw_text(text, fonts, color, surface, x, y):
    text_obj = fonts.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


def draw_number(text, fonts, color, surface, x, y):
    text_obj = fonts.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


def main_menu():
    click = False
    while True:
        screen.fill(BG_COLOR)
        draw_text("By Utku Faruk Şen", font, (255, 255, 255), screen, 560, 540)
        screen.blit(image, (200, 30))
        mx, my = pygame.mouse.get_pos()
        button1 = pygame.Rect(300, 275, 200, 50)
        if button1.collidepoint((mx, my)):
            if click:
                game()
        pygame.draw.ellipse(screen, (249, 166, 246), button1)
        draw_text("Play", font, (255, 255, 255), screen, 375, 290)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)


def game():
    running = True
    click = False
    while running:
        level = 0
        screen.fill(BG_COLOR)
        mx, my = pygame.mouse.get_pos()
        button2 = pygame.Rect(300, 135, 200, 50)
        button3 = pygame.Rect(300, 275, 200, 50)
        if button2.collidepoint((mx, my)):
            if click:
                addition(level)
        if button3.collidepoint((mx, my)):
            if click:
                subtraction(level)

        pygame.draw.ellipse(screen, (249, 166, 246), button2)
        pygame.draw.ellipse(screen, (249, 166, 246), button3)
        draw_text("Addition", font, (255, 255, 255), screen, 355, 150)
        draw_text("Subtraction", font, (255, 255, 255), screen, 350, 290)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)


def addition(level):
    running = True
    click = False
    inputnumbers = ""
    counter, text = 30, '30'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clock = pygame.time.Clock()
    screen.fill(BG_COLOR)
    draw_text("Addition", font, (255, 255, 255), screen, 20, 20)
    screen.blit(image2, (170, 150))
    screen.blit(image4, (460, 150))
    pygame.draw.rect(screen, (255, 255, 255), (0, 400, 800, 10))  # üst
    pygame.draw.rect(screen, (255, 255, 255), (400, 400, 10, 200))  # mid
    screen.blit(image6, (600, 500))
    draw_text("Countdown", font, (255, 255, 255), screen, 120, 415)
    number_1 = random.randint(0, 20)
    number_2 = random.randint(0, 20)
    sum_of_numbers = number_1 + number_2
    draw_number(str(number_1), font_number, (255, 255, 255), screen, 10, 120)
    draw_number(str(number_2), font_number, (255, 255, 255), screen, 290, 120)
    draw_text(str(level), font, (255, 255, 255), screen, 400, 50)
    while running:

        mx, my = pygame.mouse.get_pos()
        button4 = pygame.Rect(600, 500, 50, 50)
        if button4.collidepoint((mx, my)):
            if click:
                if str(sum_of_numbers) == inputnumbers:
                    draw_text("Correct Answer", font, (255, 255, 255), screen, 600, 50)
                    level = level + 1
                    addition(level)
                else:
                    draw_text("Wrong Answer", font, (255, 255, 255), screen, 600, 50)
                    gameover(level)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
                    running = False
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_0]:
                    inputnumbers += "0"
                elif pressed[pygame.K_1]:
                    inputnumbers += "1"
                elif pressed[pygame.K_2]:
                    inputnumbers += "2"
                elif pressed[pygame.K_3]:
                    inputnumbers += "3"
                elif pressed[pygame.K_4]:
                    inputnumbers += "4"
                elif pressed[pygame.K_5]:
                    inputnumbers += "5"
                elif pressed[pygame.K_6]:
                    inputnumbers += "6"
                elif pressed[pygame.K_7]:
                    inputnumbers += "7"
                elif pressed[pygame.K_8]:
                    inputnumbers += "8"
                elif pressed[pygame.K_9]:
                    inputnumbers += "9"
            draw_number(inputnumbers, font_number, (255, 255, 255), screen, 600, 120)
            if event.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else 'Time Is Up'
                if counter == 0:
                    gameover(level)
            if event.type == pygame.QUIT:
                break
        else:
            screen.fill(BG_COLOR, (155, 445, 165, 455))
            screen.blit(font.render(text, True, (255, 0, 0)), (160, 450))
            pygame.display.flip()
            clock.tick(60)
            continue
        pygame.display.update()
        mainClock.tick(60)


def subtraction(level):
    running = True
    click = False
    inputnumbers = ""
    counter, text = 30, '30'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clock = pygame.time.Clock()
    screen.fill(BG_COLOR)
    draw_text("Subtraction", font, (255, 255, 255), screen, 20, 20)
    screen.blit(image3, (170, 150))
    screen.blit(image4, (460, 150))
    pygame.draw.rect(screen, (255, 255, 255), (0, 400, 800, 10))  # üst
    pygame.draw.rect(screen, (255, 255, 255), (400, 400, 10, 200))  # mid
    screen.blit(image6, (600, 500))
    draw_text("Countdown", font, (255, 255, 255), screen, 120, 420)
    number_1 = random.randint(10, 20)
    number_2 = random.randint(0, 10)
    dif_of_numbers = number_1 - number_2
    draw_number(str(number_1), font_number, (255, 255, 255), screen, 10, 120)
    draw_number(str(number_2), font_number, (255, 255, 255), screen, 290, 120)
    draw_text(str(level), font, (255, 255, 255), screen, 400, 50)
    while running:

        mx, my = pygame.mouse.get_pos()
        button4 = pygame.Rect(600, 500, 50, 50)
        if button4.collidepoint((mx, my)):
            if click:
                if str(dif_of_numbers) == inputnumbers:
                    draw_text("Correct Answer", font, (255, 255, 255), screen, 600, 50)
                    level = level + 1
                    subtraction(level)
                else:
                    draw_text("Wrong Answer", font, (255, 255, 255), screen, 600, 50)
                    gameover(level)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
                    running = False
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_0]:
                    inputnumbers += "0"
                elif pressed[pygame.K_1]:
                    inputnumbers += "1"
                elif pressed[pygame.K_2]:
                    inputnumbers += "2"
                elif pressed[pygame.K_3]:
                    inputnumbers += "3"
                elif pressed[pygame.K_4]:
                    inputnumbers += "4"
                elif pressed[pygame.K_5]:
                    inputnumbers += "5"
                elif pressed[pygame.K_6]:
                    inputnumbers += "6"
                elif pressed[pygame.K_7]:
                    inputnumbers += "7"
                elif pressed[pygame.K_8]:
                    inputnumbers += "8"
                elif pressed[pygame.K_9]:
                    inputnumbers += "9"
            draw_number(inputnumbers, font_number, (255, 255, 255), screen, 600, 120)
            if event.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else 'Time Is Up'
                if counter == 0:
                    gameover(level)
            if event.type == pygame.QUIT:
                break
        else:
            screen.fill(BG_COLOR, (155, 445, 165, 455))
            screen.blit(font.render(text, True, (255, 0, 0)), (160, 450))
            pygame.display.flip()
            clock.tick(60)
            continue
        pygame.display.update()
        mainClock.tick(60)


def gameover(level):
    click = False
    running = True
    while running:
        screen.fill(BG_COLOR)
        screen.blit(image5, (150, 30))
        mx, my = pygame.mouse.get_pos()

        button5 = pygame.Rect(300, 145, 200, 50)
        button6 = pygame.Rect(300, 275, 200, 50)
        pygame.draw.ellipse(screen, (249, 166, 246), button5)
        pygame.draw.ellipse(screen, (249, 166, 246), button6)
        draw_text("Play Again", font, (255, 255, 255), screen, 350, 155)
        draw_text("Quit", font, (255, 255, 255), screen, 365, 290)
        draw_text("Your Score : ", font, (255, 255, 255), screen, 350, 350)
        draw_text(str(level), font, (255, 255, 255), screen, 500, 350)

        if button5.collidepoint((mx, my)):
            if click:
                game()
        if button6.collidepoint((mx, my)):
            if click:
                quit()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    main_menu()

        pygame.display.update()
        mainClock.tick(60)


main_menu()
