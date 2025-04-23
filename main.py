# Example file showing a basic pygame "game loop"
import pygame
import constants
from windows import (
    SmallAppWindow,
    LargeAppWindow,
)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Selective Memories")
clock = pygame.time.Clock()
running = True

lg_window = LargeAppWindow(0, 0)
sm_window1 = SmallAppWindow(735, 0)
sm_window2 = SmallAppWindow(735, 372)



while running:
    lg_window.draw(screen)
    sm_window1.draw(screen)
    sm_window2.draw(screen)

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        # left_click = pygame.mouse.get_pressed()[0]
        # middle_click = pygame.mouse.get_pressed()[1]
        # right_click = pygame.mouse.get_pressed()[2]
        x, y = pygame.mouse.get_pos()
        if lg_window.clicked(event):
            print("LG Window Clicked")
        if sm_window1.clicked(event):
            print("SM Windows 1 Clicked")
        if sm_window2.clicked(event):
            print("SM Window 2 Clicked")
            
        # if lg_window.rect.collidepoint(x, y):
        #     print("LG Window Clicked")
        # if left_click:
        #     print(f"left mouse click at {pygame.mouse.get_pos()}")
        # elif middle_click:
        #     print(f"middle mouse click at {pygame.mouse.get_pos()}")
        # elif right_click:
        #     print(f"right mouse click at {pygame.mouse.get_pos()}")

    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    

    clock.tick(175)  # limits FPS to 60

pygame.quit()