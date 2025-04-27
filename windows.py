import pygame
import constants


class ClickableAsset:
    def __init__(self,text = None,asset_path=None, loc=(0,0),handler=None):
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        if asset_path:
            self.surf = pygame.image.load(asset_path).convert_alpha()
        elif text:
            self.surf = my_font.render(text, False, (0, 0, 0))

        self.x = loc[0]
        self.y = loc[1]
        self.handler = handler


    def draw(self,screen):
        size = self.surf.get_size()
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])
        self.rect.topleft = (self.x, self.y)
        screen.blit(self.surf, (self.x,self.y))

    def clicked(self,event):
        return self.rect.collidepoint(event.pos)


class AssetGroup:
    def __init__(self,primary_asset:ClickableAsset):
        self.primary_asset = primary_asset
        self.sub_assets = {}
        self.visible = True

    def clicked(self,event):
        for asset_name in self.sub_assets:
            asset_data = self.sub_assets[asset_name]
            asset_obj = asset_data["asset_obj"]
            if asset_data["visible"] == True and asset_obj.clicked(event) and asset_obj.handler:
                    asset_obj.handler(asset_name, asset_data, event) # call the handler
                    return asset_name

    def add_asset(self, name:str, asset_obj:ClickableAsset, visible:bool, relative_loc:tuple,meta=None):
        self.sub_assets[name] = {
            'asset_obj':asset_obj,
            'visible':visible,
            'relative_loc':relative_loc,
            'meta':meta
        }

    def draw(self,screen):
        # draw the primary first
        if self.visible == True:
            self.primary_asset.draw(screen)
            pri_x = self.primary_asset.x
            pri_y = self.primary_asset.y

            # iterate through sub assets and draw them
            for item in self.sub_assets:
                # our dict stores relative location, that is x and y relative to the top left of the primary
                # asset. we need to update the absolute locations of each asset before we draw it
                asset_data = self.sub_assets[item]
                asset_obj = asset_data["asset_obj"]
                if asset_data["visible"] == True:
                    asset_obj.x = asset_data["relative_loc"][0] + pri_x
                    asset_obj.y = asset_data["relative_loc"][1] + pri_y
                    asset_obj.draw(screen)
