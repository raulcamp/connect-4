from connect4 import Connect4
import pygame
from pygame.locals import *

def drawBoard(window, font):
    """Draws the initial game board"""
    window.fill((255,255,255)) # white background
    pygame.draw.rect(window, (0, 100, 200), [0, 100, 50, 700]) # left board column
    pygame.draw.circle(window, (0, 100, 200), (50,100), 50) # left round corner
    pygame.draw.rect(window, (0, 100, 200), [750, 100, 50, 700]) # right board column
    pygame.draw.circle(window, (0, 100, 200), (750,100), 50) # right round corner
    pygame.draw.rect(window, (15, 110, 230), [50,100,700,700]) #board
    pygame.draw.rect(window, (0, 100, 200), [50,100,700,15]) # top board row
    pygame.draw.rect(window, (255,255,255), [50, 0, 700, 100]) # top white background
    pygame.draw.rect(window, (210,210,210), [100, 25, 200, 50]) # left button
    text = font.render("Human", 1, (0,0,0))
    window.blit(text, (125, 30))
    pygame.draw.rect(window, (210,210,210), [500, 25, 200, 50]) # right button
    text = font.render("AI", 1, (0,0,0))
    window.blit(text, (575, 30))
    for r in range(100, 800, 100):
        for c in range(175, 700, 100):
            pygame.draw.circle(window, (255,255,255), (r,c), 40) # white discs
    pygame.display.update()

def drawDisc(window, player, color, coords):
    if coords:
        r, c = coords
        pygame.draw.circle(window, color, ((c+1)*100, (r+1)*100 + 75), 40)
        return 2 if player == 1 else 1
    return player

def run():
    """Initializes and runs the game"""
    pygame.init()
    pygame.display.set_caption("Connect 4")
    font = pygame.font.SysFont("Arial", 60)
    screen = pygame.display.set_mode((800,725))
    C4 = Connect4()
    opponent = None
    drawBoard(screen, font)
    # choose to play against human or AI
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                if (mouse_x >= 100 and mouse_x <= 300 and 
                    mouse_y >= 25 and mouse_y <= 75):
                    pygame.draw.rect(screen, (175,175,175), [100, 25, 200, 50])
                else:
                    pygame.draw.rect(screen, (210,210,210), [100, 25, 200, 50])
                
                text = font.render("Human", 1, (0,0,0))
                screen.blit(text, (125, 30))
                
                if (mouse_x >= 500 and mouse_x <= 700 and 
                    mouse_y >= 25 and mouse_y <= 75):
                    pygame.draw.rect(screen, (175,175,175), [500, 25, 200, 50])
                else:
                    pygame.draw.rect(screen, (210,210,210), [500, 25, 200, 50])
                text = font.render("AI", 1, (0,0,0))
                screen.blit(text, (575, 30))
                pygame.display.update()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if (mouse_x >= 100 and mouse_x <= 300 and 
                    mouse_y >= 25 and mouse_y <= 75):
                    opponent = "Human"
                
                if (mouse_x >= 500 and mouse_x <= 700 and 
                    mouse_y >= 25 and mouse_y <= 75):
                    opponent = "AI"
                pygame.draw.rect(screen, (255,255,255), [50, 0, 700, 100])
                pygame.display.update()
                running = False
    
    print(opponent)
    # start and play the game
    while not C4.is_over():
        for event in pygame.event.get():
            player = C4.get_player()
            color = (230, 65, 40) if player == 1 else (240, 220, 75)
            
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, (255,255,255), [50, 0, 700, 100])
                mouse_x = event.pos[0]
                x = 100 if mouse_x <= 100 else 700 if mouse_x >= 700 else mouse_x
                pygame.draw.circle(screen, color, (x, 50), 40)
                pygame.display.update()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0]
                column = 1 if mouse_x <= 100 else 7 if mouse_x >= 700 else int(round(mouse_x/100))
                coords = C4.place_disc(player, column)
                C4.player = drawDisc(screen, player, color, coords)
                color = (230, 65, 40) if C4.get_player() == 1 else (240, 220, 75)
                pygame.draw.circle(screen, color, (mouse_x, 50), 40)
                pygame.display.update()
                
    # game is over
    pygame.draw.rect(screen, (255,255,255), [50, 0, 700, 100])
    result = C4.is_over()
    if result == 1:
        s = "Red won! Thanks for playing!"
    elif result == 2:
        s = "Yellow won! Thanks for playing!"
    else:
        s = "There was a tie..."
    
    text = font.render(s, 1, (0,0,0))
    screen.blit(text, (75,25))
    pygame.display.update()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                    
if __name__ == "__main__":
    run()