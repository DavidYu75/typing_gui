import pygame
import random

word_list = []
player_typing = []

def test_length(length):
    for i in range(length):
        word_list.append(random.choice(open('random_words.txt').read().split()).strip())
    return

test_length(10)
print(word_list)

successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

# screen size and frames per second
screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
FPS = 60

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

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if text_field.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

    screen.fill(BLACK)

    if active:
        color = GREEN
    else:
        color = RED

    pygame.draw.rect(screen, color, text_field)

    text_surface = font.render(user_text, True, (255, 255, 255))

    screen.blit(text_surface, (text_field.x+5, text_field.y+5))

    text_field.w = max(100, text_surface.get_width() + 10)

    pygame.display.flip()