# Example file showing a basic pygame "game loop"
import pygame
import constants
import json
from windows import (
    ClickableAsset,
    AssetGroup
)

# fake file system json
fs_structure = {}
with open("fs.json") as fle:
    fs_structure = json.loads(fle.read())

print(fs_structure)

# pygame setup
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Selective Memories")
clock = pygame.time.Clock()
running = True


# handlers here at the top, may move to another module at some point
def dir_render(name,asset_data, event):
    #first clean the screen
    file_window.sub_assets = {}
    folders = fs_structure[name]["folders"]
    files = fs_structure[name]["files"]
    position = (100,100)
    for folder_name in folders:
        x = position[0]
        y = position[1]
        icon = ClickableAsset(asset_path="assets/folder_icon_lg.png", handler = dir_render)
        icon_text = ClickableAsset(text=folder_name,handler = dir_render)
        file_window.add_asset(folder_name,icon,True, position)
        file_window.add_asset(folder_name + "_text",icon_text,True, position)
        if x < 500:
            x = x + 75
            position = (x,y)
        else:
            x = 100
            y = y + 25
            position = (x,y)
    for file_name in folders:
        x = position[0]
        y = position[1]
        temp = ClickableAsset(asset_path="assets/file_icon.png", handler = dir_render)
        file_window.add_asset(file_name,temp,True, position)
        if x < 500:
            x = x + 75
            position = (x,y)
        else:
            x = 100
            y = y + 25
            position = (x,y)


def min_file_win(name, asset_data, event):
    if file_window.visible == True:
        file_window.visible = False
    else:
        file_window.visible = True
    print("handler 2 worked")



# create the primary assets for our asset groups
osbar_background = ClickableAsset(asset_path = "assets/bar.png", loc = (0,737))
chat_window_background = ClickableAsset(asset_path ="assets/chat_window.png", loc = (735, 0))
recovery_window_background = ClickableAsset(asset_path ="assets/recovery_window.png", loc = (735,372))
file_window_background = ClickableAsset(asset_path ="assets/byte_navigator.png",loc = (0,0))

# start building our asset groups
osbar = AssetGroup(osbar_background)
chat_window = AssetGroup(chat_window_background)
recovery_window = AssetGroup(recovery_window_background)
file_window = AssetGroup(file_window_background)

# add child assets to the groups
root_fldr = ClickableAsset(asset_path ="assets/folder_icon_lg.png", handler = dir_render)
osbar_fldr = ClickableAsset(asset_path ="assets/folder_icon.png", handler = min_file_win)
osbar.add_asset("folder",osbar_fldr,True,(90,0))
file_window.add_asset("root",root_fldr,True, (100,100))

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
