import pygame 
pygame.init()

#Setting the window of the game in pixels (ex: 500px by 500px)
screenWidth = 500
win = pygame.display.set_mode((screenWidth, screenWidth))

#Labels your game at the top/tab of the screen
pygame.display.set_caption("Ice Hoceky Game!!")

x = 50
y = 50
width = 40 
height = 60
vel = 25

#Backgound/Window setup
def redrawGameWindow():
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (0, 0, 255), (x , y, width, height))
    pygame.display.update()

#Main loop 
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < screenWidth - width - vel:
        y += vel

    redrawGameWindow()

pygame.quit()