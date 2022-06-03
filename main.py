import pygame
import random
from typing_logic import *
import time

word_list = []
player_typing = []
time_spent = 0


def test_length(length):
    for i in range(length):
        word_list.append(random.choice(open('random_words.txt').read().split()).strip())
    return


def render_text(list):
    x_index = 50
    y_index = 30
    for i in range(len(list)):
        words = font.render(list[i], True, BLACK)
        words_rect = words.get_rect(center=(x_index, y_index))
        screen.blit(words, words_rect)
        x_index += 1000/10
        if x_index > 950:
            x_index = 50
            y_index += 50


def results():
    accuracy = font.render('Accuracy: ' + get_accuracy(word_list, player_typing) + '%', True, BLACK)
    accuracy_rect = accuracy.get_rect(center=(500, 325))
    screen.blit(accuracy, accuracy_rect)

    time = font.render('Time Spent: ' + str(time_spent) + ' seconds', True, BLACK)
    time_rect = time.get_rect(center=(500, 350))
    screen.blit(time, time_rect)

    wpm = font.render("WPM: " + get_wpm(time_spent, player_typing), True, BLACK)
    wpm_rect = wpm.get_rect(center=(500, 375))
    screen.blit(wpm, wpm_rect)


def countdown(seconds):
    count = seconds
    for i in range(seconds):
        countdown = font.render(str(count - i) + "...", True, BLACK)
        countdown_rect = countdown.get_rect(center=(500, 250))
        screen.blit(countdown, countdown_rect)
        time.sleep(1)
        if count - i == 1:
            start = font.render("Go!", True, BLACK)
            start_rect = start.get_rect(center=(500, 250))
            screen.blit(start, start_rect)


successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))
pygame.key.set_repeat(500, 20)
pygame.display.set_caption('Monkeytype')

# screen size and frames per second
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()
FPS = 60

counter, text = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
color = RED

# font
font = pygame.font.Font(None, 32)
title = pygame.font.Font(None, 128)
user_text = ''

# text field
text_field = pygame.Rect(425, 275, 150, 32)

# buttons
one_line_button = pygame.Rect(425, 275, 150, 32)
two_line_button = pygame.Rect(425, 350, 150, 32)
three_line_button = pygame.Rect(425, 425, 150, 32)
exit_button = pygame.Rect(425, 500, 150, 32)
retry_button = pygame.Rect(450, 400, 50, 32)

title_text = title.render("MonkeyType", True, BLACK)
one_line = font.render("One Line", True, WHITE)
two_line = font.render("Two Line", True, WHITE)
three_line = font.render("Three Line", True, WHITE)
exit = font.render("Exit", True, WHITE)

active = False
started = False
selected = False
finished = False

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if not finished:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_field.collidepoint(event.pos):
                    active = True
                    starting_time = time.time()
                else:
                    active = False

        if not selected:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if one_line_button.collidepoint(event.pos):
                    started = True
                    selected = True
                    test_length(10)
                elif two_line_button.collidepoint(event.pos):
                    started = True
                    selected = True
                    test_length(20)
                elif three_line_button.collidepoint(event.pos):
                    started = True
                    selected = True
                    test_length(30)
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()

        if active:
            if event.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else 'Go!'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_SPACE:
                    player_typing.append(user_text)
                    user_text = ''
                elif event.key == pygame.K_RETURN:
                    player_typing.append(user_text)
                    user_text = ''
                    finished = True
                    ending_time = time.time()
                    active = False
                else:
                    user_text += event.unicode

    screen.fill(WHITE)

    start_text = font.render('Start', True, BLACK)
    screen.blit(start_text, one_line_button)

    pygame.draw.rect(screen, RED, one_line_button)
    pygame.draw.rect(screen, RED, two_line_button)
    pygame.draw.rect(screen, RED, three_line_button)
    pygame.draw.rect(screen, RED, exit_button)

    screen.blit(title_text, (250, 100))
    screen.blit(one_line, one_line_button)
    screen.blit(two_line, two_line_button)
    screen.blit(three_line, three_line_button)
    screen.blit(exit, exit_button)

    if started:
        pygame.draw.rect(screen, WHITE, one_line_button)
        pygame.draw.rect(screen,WHITE, two_line_button)
        pygame.draw.rect(screen, WHITE, three_line_button)
        pygame.draw.rect(screen, WHITE, exit_button)
        title_text = title.render('', True, WHITE)

        render_text(word_list)

        if active:
            color = GREEN
        else:
            color = RED

        pygame.draw.rect(screen, color, text_field)

        text_surface = font.render(user_text, True, (255, 255, 255))

        screen.blit(text_surface, (text_field.x+5, text_field.y+5))

        text_field.w = max(100, text_surface.get_width() + 10)

        pygame.draw.rect(screen, RED, retry_button)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if retry_button.collidepoint(event.pos):
                active = False
                started = False
                selected = False
                finished = False
                word_list.clear()
                player_typing.clear()
                time_spent = 0

        if finished:
            time_spent = round(ending_time - starting_time)
            results()

    pygame.display.flip()
