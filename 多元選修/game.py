import pygame
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 400),0,32)  # �]�w�C������
pygame.display.set_caption('Hello World!')  # �]�w�C�����D
clock = pygame.time.Clock()  # �Ыؤ@�Ӯ�����H
game_over = False
flwImg = pygame.image.load('A.png')
fstartx = 10
fstarty = 10
DISPLAYSURF.blit(flwImg, (fstartx, fstarty))

def move():
    global fstartx, fstarty
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        fstarty = fstarty + 5
        if fstarty > 380:
            fstarty = 380
    if keys[pygame.K_UP]:
        fstarty = fstarty - 5
        if fstarty < 0:
            fstarty = 0
    if keys[pygame.K_LEFT]:
        fstartx = fstartx - 5
        if fstartx < 0:
            fstartx = 0
    if keys[pygame.K_RIGHT]:
        fstartx = fstartx + 5
        if fstartx > 480:
            fstartx = 480
    DISPLAYSURF.fill((0, 0, 0))
    DISPLAYSURF.blit(flwImg, (fstartx, fstarty))
    pygame.display.update()

while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_over = True
    move()
    clock.tick(10)  # ����C���t�׬��C��10�V
pygame.quit()
