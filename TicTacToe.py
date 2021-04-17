
import pygame

pygame.init()

def rematch():
    global XO
    XO = [[None, None, None],
          [None, None ,None],
          [None, None, None]]

def text_renderer(surface, font, msg, color, x=None, y=None):
    text = font.render(msg, True, color)
    rect = text.get_rect()
    if x != None:
        print(rect.width, rect.height, msg)
        rect.x = x
        rect.y = y
    else:
        rect.x = 150-(rect.width//2)
        rect.y = 150-(rect.height//2)
    surface.blit(text, rect)
    rematch()
        

def checker():
    global XO
    global quitt
    global msg
    
    for i in range(3):
        if XO[0][i] == 'x' and XO[1][i] == 'x' and XO[2][i] == 'x':
            msg = "X WON"
        
        elif XO[i][0] == 'x' and XO[i][1] == 'x' and XO[i][2] == 'x':
            msg = "X WON"
            
        elif XO[i][0] == 'o' and XO[i][1] == 'o' and XO[i][2] == 'o':
            msg = "X WON"
            
        elif XO[0][i] == 'o' and XO[1][i] == 'o' and XO[2][i] == 'o':
            msg = "O WON"
            
        for j in range(3):
            if XO[i][j] == None:
                quitt = False
    if XO[0][0] == 'x' and XO[1][1] == 'x' and XO[2][2] == 'x':
        msg = "X WON"
        
    elif XO[0][2] == 'x' and XO[1][1] == 'x' and XO[2][0] == 'x':
        msg = "X WON"
        
    elif XO[0][0] == 'o' and XO[1][1] == 'o' and XO[2][2] == 'o':
        msg = "O WON"
        
    elif XO[0][2] == 'o' and XO[1][1] == 'o' and XO[2][0] == 'o':
        msg = "O WON"
        
    if quitt == True:
        msg =  'DRAW'
        
    else:
        quitt = True
    

## constant variables
WIDTH = 300
FPS = 60
T = 1

## Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

## hash tag coords
board_line_cords = [[(110, 30), (110, 270)], [(190, 30), (190, 270)],
                    [(30, 110), (270, 110)], [(30, 190), (270, 190)]]

XO = [[None, None, None],
      [None, None ,None],
      [None, None, None]]

turn = 'x'
## pygame display intialization
surface = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Tic Tac Toe")

## clock for pygame
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 64)
gameLoop = True
quitt = True
msg = None
## Game Loop

while gameLoop == True:
    clock.tick(FPS)

    checker()

    ## event listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_r and msg != None:
                msg = None
                XO = [[None, None, None],
                      [None, None ,None],
                      [None, None, None]]

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
                if 30 < x < 270 and 30 < y < 270:
                    i2 = (x-30)//80
                    j2 = (y-30)//80
                    if XO[i2][j2] == None:
                        if turn == 'x':
                            XO[i2][j2] = 'x'
                            turn = 'o'
                        elif turn == 'o':
                            XO[i2][j2] = 'o'
                            turn = 'x'
    
    ## updating screen
    surface.fill(BLACK)

    ## tic tac toe board
    for i,j in board_line_cords:
        pygame.draw.line(surface, WHITE, i, j, T)

    for i,k in enumerate(XO):
        for j,l in enumerate(k):
            if l == 'x':
                pygame.draw.line(surface, WHITE, (40+(80*i), 40+(80*j)), (100+(80*i), 100+(80*j)))
                pygame.draw.line(surface, WHITE, (40+(80*i), 100+(80*j)), (100+(80*i), 40+(80*j)))
            elif l == 'o':
                pygame.draw.circle(surface, WHITE, ((70+(80*i)), (70+(80*j))), 30, 1)
    if msg:
        text_renderer(surface, font, msg, WHITE)
    
    pygame.display.flip()

## quiting everything
pygame.quit()
quit()
