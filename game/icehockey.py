import pygame 
import os.path

pygame.init()

#Setting the window of the game in pixels (ex: 500px by 500px)
screenWidth = 800
screenHeight = 500
win = pygame.display.set_mode((screenWidth, screenHeight))

#Labels your game at the top/tab of the screen
pygame.display.set_caption("Air Hoceky Game!! By - Tyler Chang")

#Import Images (ex: background and players)
current_filepath = os.path.dirname(__file__)
image_path = os.path.join(current_filepath,'images')

background = pygame.image.load(os.path.join(image_path, 'AirHockeyBG.png'))
hockeyPuck = pygame.image.load(os.path.join(image_path, 'HockeyPuck.png'))

#Set clock
clock = pygame.time.Clock()

#Player Class for Object Oriented
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 50
        self.left = False
        self.right = False
        self.scoreCount = 0
    
    def draw(self, win):
        #Place Hockey Puck
        win.blit(hockeyPuck, (self.x, self.y))


#Backgound/Window setup
def redrawGameWindow():
    #Place background image
    win.blit(background, (0,0))
    player1.draw(win)
    pygame.display.update()

#Main loop 
player1 = player(800, 500, 64, 64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player1.x > player1.vel:
        player1.x -= player1.vel
        player1.left = True
        player1.right = False

    if keys[pygame.K_RIGHT] and player1.x < screenWidth - player1.width - player1.vel:
        player1.x += player1.vel
        player1.right = True
        player1.left = False
    # else:
    #     right = False
    #     left = True
    #     scoreCount = 0

    if keys[pygame.K_UP] and player1.y > player1.vel:
        player1.y -= player1.vel
        player1.right = False
        player1.left = False

    if keys[pygame.K_DOWN] and player1.y < screenWidth - player1.height - player1.vel:
        player1.y += player1.vel
        player1.right = False
        player1.left = False

    redrawGameWindow()

pygame.quit()