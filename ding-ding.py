# Hello! Please don't rate my code. I wrote it really fast and for food.

try:
    import sys
    import pygame
    import random
except ImportError as e:
    exit(e)

pygame.init()
pygame.display.init()

resolution = (900, 900)
clock = pygame.time.Clock()

window = pygame.display.set_mode(resolution)
pygame.display.set_caption("Ding-Ding")
pygame.display.set_icon(pygame.image.load("img/hector.jpeg").convert())

background = pygame.image.load("img/stars.png").convert()
background = pygame.transform.scale(background, resolution)

FPS = 25
run = True

width = 300
height = 400
size = (width, height)

ding_sound = [
    pygame.mixer.Sound("sounds/ding-1.wav"),
    pygame.mixer.Sound("sounds/ding-1.wav"),
    pygame.mixer.Sound("sounds/ding-1.wav")
]

animation = [
    pygame.image.load("img/ding-1.png"),
    pygame.image.load("img/ding-2.png"),
    pygame.image.load("img/ding-3.png"),
    pygame.image.load("img/ding-4.png"),
    pygame.image.load("img/ding-5.png"),
]

animation = [pygame.transform.scale(img, size) for img in animation]
pos = (resolution[0]/2, resolution[1]/2)
rect = animation[2].get_rect(topleft=pos)

player_tick = 0
ding = False

while run:
    integer = random.randint(0, 2)
    window.blit(background, (0, 0))
    window.blit(animation[0], (resolution[0]/2-size[0]/2, resolution[1]/2-size[1]/2))

    keys = pygame.key.get_pressed()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    if player_tick == 2:
        ding_sound[integer].play()
    if keys[pygame.K_SPACE] and not ding:
        ding = True

    if player_tick < len(animation) and ding:
        window.blit(animation[player_tick], (resolution[0]/2-size[0]/2, resolution[1]/2-size[1]/2))
        player_tick += 1
    elif player_tick >= len(animation):
        ding = False
        player_tick = 0

    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
sys.exit()
