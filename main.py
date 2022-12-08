import sys

import pygame
from pygame.locals import *
from pynput import keyboard
from pynput.keyboard import Key, Listener

pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional

HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60

count = 0

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect(center=(10, 420))


class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(WIDTH / 2, HEIGHT - 10))


class Score:
    def __init__(self):
        self.count = 0
        self.listener = keyboard.Listener(
            on_press=self.update_score,
            on_release=on_release)
        self.listener.start()

    def update_score(self, key):
        self.count += 1


# def on_press(key):
#     print('{0} pressed'.format(key))


def on_release(key):
    pass
    # print('{0} release'.format(key))
    # if key == Key.esc:
    #     return False

# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()


PT1 = platform()
P1 = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

pygame.font.init()
font = pygame.font.SysFont('Arial', 24)

score = Score()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == KEYDOWN:
        #     count += 1

    count = score.count

    displaysurface.fill((255, 0, 0))

    counter_surface = font.render(str(count), False, (255, 255, 255))

    displaysurface.blit(counter_surface, (HEIGHT / 2, WIDTH / 2))

    # for entity in all_sprites:
    #     displaysurface.blit(entity.surf, entity.rect)

    pygame.display.update()
    FramePerSec.tick(FPS)
