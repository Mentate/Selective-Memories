# Example file showing a basic pygame "game loop"
import pygame
import constants
from windows import (
    ClickableAsset
)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Selective Memories")
clock = pygame.time.Clock()
running = True


active_assets = {
    "file_window":ClickableAsset("assets/byte_navigator.png",0,0),
    "chat_wndow":ClickableAsset("assets/chat_window.png",735, 0),
    "recovery_window":ClickableAsset("assets/recovery_window.png", 735, 372),
    "taskbar":ClickableAsset("assets/bar.png", 0,737),
    "tbar_fldr":ClickableAsset("assets/folder_icon.png",100,737)
}



while running:
    for asset in active_assets:
        active_assets[asset].draw(screen)

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
            for asset in active_assets:
                if active_assets[asset].clicked(event):
                    print(f"{asset} was clicked")


    pygame.display.flip()
    clock.tick(30)  # limits FPS to 60

pygame.quit()
