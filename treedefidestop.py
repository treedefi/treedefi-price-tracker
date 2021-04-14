import pygame
import requests
import re
import time

pygame.init()

white = (255, 255, 255)
green = (59, 183, 143)
blue = (255, 255, 255)

X = 400
Y = 400

display_surface = pygame.display.set_mode((X, Y))

pygame.display.set_caption('Price Tracker')

font = pygame.font.Font('freesansbold.ttf', 52)

text = font.render('TreeDefi.com', True, green, blue)
textRect = text.get_rect()
textRect.center = (X // 2, Y // 2)

display_surface.blit(text, textRect)
pygame.display.update()

while True:


    display_surface.fill(white)

    bg = pygame.image.load("tree.png")
    display_surface.blit(bg, (0, 0))


    treeweb=requests.get("https://bscscan.com/token/0xf0fcd737fce18f95621cc7841ebe0ea6efccf77e")
    seedweb=requests.get("https://bscscan.com/token/0x40B34cC972908060D6d527276e17c105d224559d")
    p=re.compile("[$][0-9]{1,4}\.[0-9]{1,4}")
    result1=p.search(treeweb.text)
    result2=p.search(seedweb.text)
    print(result1.group(0),result2.group(0))
    text = font.render("TREE: "+result1.group(0), True, green, blue)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    text2 = font.render("SEED: "+result2.group(0), True, green, blue)
    textRect2 = text2.get_rect()
    textRect2.center = (X // 2, Y // 2 + 52)


    display_surface.blit(text, textRect)
    display_surface.blit(text2, textRect2)
    time.sleep(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
