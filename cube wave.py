import pygame, sys, random, math

#initializing pygame, window, colours, constant values for dimensions and framerate clock
pygame.init()
width = (800,800)
win = pygame.display.set_mode(width)
clock = pygame.time.Clock()
topColour = (255,255,255)
f1Colour = (190,190,190)
f2Colour = (100,100,100)
offset = -10
wide = offset*-2
height = wide*9


class Bar:
    #initialising the bar starting coordinates, the added height they will have added on which will be used to display motion and time which is used to move that height every frame
    def __init__(self, x, y, start, column, row):
        self.pos = [x,y]
        self.addedHeight = 0
        self.time = start
        self.column = column
        self.row = row
        self.scale = wide*3

    # the draw function draws 3 polygon faces that represent the 3 visible faces of each bar, the time of each bar is incremented to function as an angle and the added height is adjusted appropriately
    def draw(self):
        self.time = (self.time + 2) %360
        self.addedHeight = math.cos(math.radians(self.time))*(self.scale)
        
        pygame.draw.polygon(win, f1Colour, [[self.pos[0], self.pos[1]-self.addedHeight], [self.pos[0]+wide, self.pos[1]+offset-self.addedHeight], [self.pos[0]+wide, self.pos[1]+height+offset+self.addedHeight], [self.pos[0], self.pos[1]+height+self.addedHeight]])
        pygame.draw.polygon(win, f2Colour, [[self.pos[0], self.pos[1]-self.addedHeight], [self.pos[0]-wide, self.pos[1]+offset-self.addedHeight], [self.pos[0]-wide, self.pos[1]+height+offset+self.addedHeight], [self.pos[0], self.pos[1]+height+self.addedHeight]])
        pygame.draw.polygon(win, topColour, [[self.pos[0], self.pos[1]-self.addedHeight], [self.pos[0]+wide, self.pos[1]+offset-self.addedHeight], [self.pos[0], self.pos[1]+2*offset-self.addedHeight], [self.pos[0]-wide, self.pos[1]+offset-self.addedHeight]])

        #pygame.draw.circle(win, (0,255,0), self.pos,3) #debug





# redraw window function that redraws every bar object onto the screen
def redrawWin():
    win.fill((0,0,0))
    
    for section in cube:
        for bar in section:
            bar.draw()

    #pygame.draw.circle(win, (255,0,0), (400-wide,280+wide*(n/2)),1) #debug
    pygame.display.update()
    

cube = []
n = 20
yOr = 180
yMove = yOr
xOr = 420
xMove = xOr

time = 0

# for i in range(n):
#     temp = []
#     xMove -= wide          #change the sign of this operation and xPos operation to generate from right to left or vice versa
#     yMove -= offset         #change the sign of this operation and yPos operation to generate from bottom to top or vice versa
#     for j in range(n):
#         xPos = xMove + wide*(j)
#         yPos = yMove - j*(offset)
#         temp.append(Bar(xPos, yPos, time+j+i, i, j))
#     cube.append(temp)

for i in range(n):
    temp = []
    xMove -= wide          #change the sign of this operation and xPos operation to generate from right to left or vice versa
    yMove -= offset         #change the sign of this operation and yPos operation to generate from bottom to top or vice versa
    for j in range(n):
        xPos = xMove + wide*(j)
        yPos = yMove - j*(offset)
        temp.append(Bar(xPos, yPos, -math.dist((xPos,yPos),(xOr-wide,yOr+wide*(n/2))), i, j))
    cube.append(temp)


# for i in range(n):

#     for j in range(i+1):
#         # timeOffset = 20*(i-j)  #weird half sine, half inphase wave motion
#         # timeOffset = i #sine motion bottom to top
#         timeOffset = i

#         offsetX = j*(width*2) - (i*width)
#         cube.append(Bar(xMove+offsetX,yMove+i*(offset*-1),timeOffset*20))

# for i in range(n-1):
    

#     for j in range((n-1)-i):
#         timeOffset = 20+i


#         offsetX = j*(width*2) - (((n-1)-i)*width) + width
#         cube.append(Bar(xMove+offsetX,yMove+((n-1)*offset*-1)+i*(offset*-1)-offset,timeOffset*20))


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
        
