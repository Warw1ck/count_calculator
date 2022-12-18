import pygame
from sys import exit


def num(n):
    number_surface = my_font.render(f'{number}', False, (0, 0, 0))
    screen.blit(number_surface, (240, 0))


pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Countdown calculator')
clock = pygame.time.Clock()
number = 0
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 150)

plus_surface = my_font.render(f'+', False, (0, 0, 0))
button_1 = pygame.image.load('rectagle-grey.png')
button_1_rect = button_1.get_rect(center=(300, 270))
button_2 = pygame.image.load('rectagle-grey.png')
button_2_rect = button_2.get_rect(center=(300, 420))
negative_surface = my_font.render(f'-', False, (0, 0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_1_rect.collidepoint(event.pos):
                number += 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_2_rect.collidepoint(event.pos):
                number -= 1
    screen.fill((255, 255, 255))
    screen.blit(button_1, button_1_rect)
    screen.blit(plus_surface, (250, 150))
    screen.blit(button_2, button_2_rect)
    screen.blit(negative_surface, (250, 280))
    num(number)

    pygame.display.update()
    clock.tick(60)
