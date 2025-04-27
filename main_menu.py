import pygame, sys

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('game test')
screen = pygame.display.set_mode((500, 500), 0, 32)
font = pygame.font.SysFont(None, 20)
click = False

# text rendering helper function
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    
# Main game loop
def main_menu():
    while True:
        screen.fill((0,0,0))
        draw_text("Main Menu", font, (255,255,255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button1 = pygame.Rect(50, 100, 200, 50)
        button2 = pygame.Rect(50, 200, 200, 50)
        
        # Call Sub game loop on click
        if button1.collidepoint((mx, my)):
            if click:
                game()
        # Call Sub game loop on click
        if button2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255,0,0), button1)
        pygame.draw.rect(screen, (255,0,0), button2)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        mainClock.tick(60)

def game():
    running = True
    while running:
        # Reset screen to black
        screen.fill((0,0,0))
        draw_text("game", font, (255,255,255), screen, 20, 20)
        
        # Exit or ESC back to main parent loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)
        
def options():
    running = True
    while running:
        # Reset screen to black
        screen.fill((0,0,0))
        draw_text("options", font, (255,255,255), screen, 20, 20)
        
        # Exit or ESC back to main parent loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)
main_menu()