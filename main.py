# Example file showing a basic pygame "game loop"
import pygame
import constants
from windows import (
    ClickableAsset,
    AssetGroup
)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Selective Memories")
clock = pygame.time.Clock()
running = True


# handlers here at the top, may move to another module at some point
def test_handler1(event):
    print("handler 1 worked")

def min_file_win(name, asset_data, event):
    if file_window.visible == True:
        file_window.visible = False
    else:
        file_window.visible = True
    print("handler 2 worked")



# create the primary assets for our asset groups
osbar_background = ClickableAsset("assets/bar.png", (0,737),test_handler1)
chat_window_background = ClickableAsset("assets/chat_window.png",(735, 0),test_handler1)
recovery_window_background = ClickableAsset("assets/recovery_window.png", (735,372), test_handler1)
file_window_background = ClickableAsset("assets/byte_navigator.png",(0,0),test_handler1)

# start building our asset groups
osbar = AssetGroup(osbar_background)
chat_window = AssetGroup(chat_window_background)
recovery_window = AssetGroup(recovery_window_background)
file_window = AssetGroup(file_window_background)

# add child assets to the groups
osbar_fldr = ClickableAsset("assets/folder_icon.png",(0,0),min_file_win)
osbar.add_asset("folder",osbar_fldr,True,(90,0))

# add them to a dict
asset_groups = {
    "osbar":osbar,
    "file_win":file_window,
    "chat_window":chat_window,
    "recovery_window":recovery_window
}


while running:
    screen.fill((0,0,0))
    for group in asset_groups:
        asset_groups[group].draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for group in asset_groups:
                asset_name = asset_groups[group].clicked(event)
                if asset_name:
                    print(f"{asset_name} was clicked")


    pygame.display.flip()
    clock.tick(30)  # limits FPS to 60

pygame.quit()


            # left_click = pygame.mouse.get_pressed()[0]
            # middle_click = pygame.mouse.get_pressed()[1]
            # right_click = pygame.mouse.get_pressed()[2]
