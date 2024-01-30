import pygame, sys, random, math, colorsys

#initializing pygame, window and framerate clock
pygame.init()
width = (800,800)
win = pygame.display.set_mode(width)
clock = pygame.time.Clock()
sandCol = pygame.Color(255,255,255)
sandCol.hsva = (0, 100, 100, 10)
colVal = 0


def redrawWin(board):
    win.fill((0,0,0))
    # for i in range(len(board)):
    #     for j in range(len(board[0])):
    #         if board[i][j] == 1:
    #             pygame.draw.rect(win, (255,255,255), (j*sizeOfPixel, i*sizeOfPixel,sizeOfPixel,sizeOfPixel))
    board = boardUpdate(board)
    pygame.display.update()
    return(board)


#initialising conditions of board
sizeOfPixel = 5
board = [[[0,sandCol] for i in range(width[0]//sizeOfPixel)] for j in range(width[1]//sizeOfPixel)]




def boardUpdate(board):
    tempBoard = [[[0,sandCol] for i in range(width[0]//sizeOfPixel)] for j in range(width[1]//sizeOfPixel)]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j][0] == 1:
                if i != len(board)-1 :
                    direction = 1
                    if random.random() < 0.5:
                        direction *= -1
                    boardA = board[i+1][(j-direction)%len(board)][0]
                    boardB = board[i+1][(j+direction)%len(board)][0]
                    boardD = board[i+1][j][0]
                    if boardD == 0:
                        tempBoard[i+1][j] = [1, board[i][j][1]]
                        sandCol.hsva = board[i][j][1]
                        pygame.draw.rect(win, sandCol, (j*sizeOfPixel, (i+1)*sizeOfPixel,sizeOfPixel,sizeOfPixel))
                    elif boardA == 0:
                        tempBoard[i+1][(j-direction)%len(board)] = [1, board[i][j][1]]
                        sandCol.hsva = board[i][j][1]
                        pygame.draw.rect(win, sandCol, (((j-direction)%len(board))*sizeOfPixel, (i+1)*sizeOfPixel,sizeOfPixel,sizeOfPixel))
                    elif boardB == 0:
                        tempBoard[i+1][(j+direction)%len(board)] = [1, board[i][j][1]]
                        sandCol.hsva = board[i][j][1]
                        pygame.draw.rect(win, sandCol, (((j+direction)%len(board))*sizeOfPixel, (i+1)*sizeOfPixel,sizeOfPixel,sizeOfPixel))
                    else:
                        tempBoard[i][j] = [1, board[i][j][1]]
                        sandCol.hsva = board[i][j][1]
                        pygame.draw.rect(win, sandCol, (j*sizeOfPixel, i*sizeOfPixel,sizeOfPixel,sizeOfPixel))
                else:
                    tempBoard[i][j] = [1, board[i][j][1]]
                    sandCol.hsva = board[i][j][1]
                    pygame.draw.rect(win, sandCol, (j*sizeOfPixel, i*sizeOfPixel,sizeOfPixel,sizeOfPixel))
    
    return tempBoard



run = True
brushSize = 5
#game loop
while run:
    
    
    
    # framerate of 60 frames per second
    clock.tick(60)

    #event check if user has closed window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    
    click = pygame.mouse.get_pressed()
    if click[0]:
        mouse = pygame.mouse.get_pos()
        if 0 < mouse[1]//20 < len(board) and 0 < mouse[0]//20 < len(board[0]):
            colVal += 1
            col = ((colVal%360), 100, 100, 10)
            coords = [mouse[1]//sizeOfPixel,mouse[0]//sizeOfPixel]
            for k in range(brushSize*2):
                for l in range(brushSize*2):
                    if 0 < coords[0]-brushSize + k < len(board)-1 and 0 < coords[1]-brushSize + l < len(board[0])-1:
                        if board[coords[0]-brushSize + k][coords[1]-brushSize + l][0] == 0:
                            board[coords[0]-brushSize + k][coords[1]-brushSize + l] = [1, col]

    #redraw window function call
    board = redrawWin(board)
        
