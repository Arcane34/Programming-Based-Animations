import pygame, sys, random, math

#initializing pygame, window and framerate clock
pygame.init()
width = (800,800)
win = pygame.display.set_mode(width)
clock = pygame.time.Clock()
f1Colour = (255,255,255)
f2Colour = (190,190,190)
topColour = (100,100,100)
offset = -10

class Bar:
    def __init__(self, x, y, start):
        self.pos = [x,y]
        self.start = start
        self.width = 20
        self.height = 30

    def draw(self):
        pygame.draw.polygon(win, f1Colour, [[self.pos[0], self.pos[1]], [self.pos[0]+self.width, self.pos[1]+offset], [self.pos[0]+self.width, self.pos[1]+self.height+offset], [self.pos[0], self.pos[1]+self.height]])
        pygame.draw.polygon(win, f2Colour, [[self.pos[0], self.pos[1]], [self.pos[0]-self.width, self.pos[1]+offset], [self.pos[0]-self.width, self.pos[1]+self.height+offset], [self.pos[0], self.pos[1]+self.height]])
        pygame.draw.polygon(win, topColour, [[self.pos[0], self.pos[1]], [self.pos[0]+self.width, self.pos[1]+offset], [self.pos[0], self.pos[1]+2*offset], [self.pos[0]-self.width, self.pos[1]+offset]])






def redrawWin():
    win.fill((0,0,0))
    bar1.draw()
    pygame.display.update()
    

bar1 = Bar(400,400,0)

run = True
while run:
    # framerate of 60 frames per second
    clock.tick(60)


    #event check if user has closed window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    #redraw window function call
    redrawWin()
        
