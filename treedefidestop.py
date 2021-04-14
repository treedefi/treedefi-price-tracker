
# import pygame module in this program
import pygame
import requests
import re
import time
# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# define the RGB value for white,
# green, blue colour .
white = (255, 255, 255)
green = (59, 183, 143)
blue = (255, 255, 255)

# assigning values to X and Y variable
X = 600
Y = 600

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Price Tracker')

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 52)

# create a text suface object,
# on which text is drawn on it.
text = font.render('TreeDefi.com', True, green, blue)

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (X // 2, Y // 2)
display_surface.blit(text, textRect)
pygame.display.update()
# infinite loop
while True:


    # completely fill the surface object
    # with white color
    display_surface.fill(white)
    bg = pygame.image.load("tree.png")

    #INSIDE OF THE GAME LOOP
    display_surface.blit(bg, (0, 0))


    # copying the text surface object
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
    # to the display surface object
    # at the center coordinate.


    display_surface.blit(text, textRect)
    display_surface.blit(text2, textRect2)
    time.sleep(5)
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:

            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()

        # Draws the surface object to the screen.
        pygame.display.update()
