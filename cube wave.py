import pygame, sys, random, math

#initializing pygame, window and framerate clock
pygame.init()
width = (800,800)
win = pygame.display.set_mode(width)
clock = pygame.time.Clock()
topColour = (255,255,255)
f1Colour = (190,190,190)
f2Colour = (100,100,100)
offset = -7
height = 14*9
width = 14

class Bar:
    def __init__(self, x, y, start):
        self.pos = [x,y]
        self.addedHeight = 0
        self.time = start

    def draw(self):
        self.time = (self.time + 2) %360
        self.addedHeight = math.sin(math.radians(self.time))*(height/3)
        pygame.draw.polygon(win, f1Colour, [[self.pos[0], self.pos[1]-self.addedHeight], [self.pos[0]+width, self.pos[1]+offset-self.addedHeight], [self.pos[0]+width, self.pos[1]+height+offset+self.addedHeight], [self.pos[0], self.pos[1]+height+self.addedHeight]])
        pygame.draw.polygon(win, f2Colour, [[self.pos[0], self.pos[1]-self.addedHeight], [self.pos[0]-width, self.pos[1]+offset-self.addedHeight], [self.pos[0]-width, self.pos[1]+height+offset+self.addedHeight], [self.pos[0], self.pos[1]+height+self.addedHeight]])
        pygame.draw.polygon(win, topColour, [[self.pos[0], self.pos[1]-self.addedHeight], [self.pos[0]+width, self.pos[1]+offset-self.addedHeight], [self.pos[0], self.pos[1]+2*offset-self.addedHeight], [self.pos[0]-width, self.pos[1]+offset-self.addedHeight]])






def redrawWin():
    win.fill((0,0,0))
    
    for bar in cube:
        bar.draw()
    pygame.draw.circle(win,(255,0,0),(400,400),5)
    pygame.display.update()
    

cube = []
n = 20
yMove = 280
xMove = 400
for i in range(n):
    for j in range(i+1):
        offsetX = j*(width*2) - (i*width)
        cube.append(Bar(xMove+offsetX,yMove+i*(offset*-1),0))

for i in range(n-1):
    for j in range((n-1)-i):
        offsetX = j*(width*2) - (((n-1)-i)*width) + width
        cube.append(Bar(xMove+offsetX,yMove+((n-1)*offset*-1)+i*(offset*-1)-offset,0))


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
        
