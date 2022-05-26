import pygame
import random
from typing_logic import *

word_list = []
player_typing = []


def test_length(length):
    for i in range(length):
        word_list.append(random.choice(open('random_words.txt').read().split()).strip())
    return


def render_text(list):
    x_index = 50
    y_index = 30
    for i in range(len(list)):
        words = font.render(list[i], True, BLACK)
        # #words_rect = words.get_rect()
        # if x_index > 100:
        #     y_index += 100
        #     words_rect.center(x_index, y_index)
        # else:
        # words_rect.center = (x_index, y_index)
        screen.blit(words, (x_index, y_index))
        x_index += 1000/len(list)


def results():
    accuracy = font.render(get_accuracy(word_list, player_typing), True, BLACK)
    accuracy_rect = accuracy.get_rect()
    screen.blit(accuracy, accuracy_rect)


test_length(10)
print(word_list)


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
user_text = ''

# text field
text_field = pygame.Rect(200, 200, 140, 32)

active = False
started = False

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if text_field.collidepoint(event.pos):
                active = True
                started = True
            else:
                active = False

        if started:
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
                    results()
                    accuracy = get_accuracy(word_list, player_typing)
                    print(accuracy)

                else:
                    user_text += event.unicode

    screen.fill(WHITE)

    render_text(word_list)

    if active:
        color = GREEN
    else:
        color = RED

    pygame.draw.rect(screen, color, text_field)

    text_surface = font.render(user_text, True, (255, 255, 255))

    screen.blit(text_surface, (text_field.x+5, text_field.y+5))

    text_field.w = max(100, text_surface.get_width() + 10)

    pygame.display.flip()
