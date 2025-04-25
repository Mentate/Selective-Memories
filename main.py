# Example file showing a basic pygame "game loop"
import pygame
import constants
from windows import (
    SmallAppWindow,
    LargeAppWindow,
    FileAppWindow,
    OsBar
)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Selective Memories")
clock = pygame.time.Clock()
running = True

#lg_window = LargeAppWindow(0, 0)
file_window = FileAppWindow(0,0)
sm_window1 = SmallAppWindow(735, 0)
sm_window2 = SmallAppWindow(735, 372)
os_window = OsBar(0,737)


while running:
    file_window.draw(screen)
    sm_window1.draw(screen)
    sm_window2.draw(screen)
    os_window.draw(screen)

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    

    clock.tick(60)  # limits FPS to 60

pygame.quit()
