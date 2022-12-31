import pygame, sys, random, math

# initializing pygame, canvas, main window and framerate clock
pygame.init()
width = (800,800)
screen = pygame.display.set_mode((800,800))
win = pygame.Surface(width)
clock = pygame.time.Clock()


#particle class responsible for drawing the waves by plotting particles and moving them according to the motion implied by the wave on screen
#a collection of these points on the wave then make up the graphing of the wave which is seen on screen
class Particle:
    def __init__(self, x, y, colour,time, freq, amp):
        #amplitude of wave
        self.amp = amp
        #frequency of wave
        self.freq = freq
        #displacing the enire drawing by "adder"
        self.adder = 400
        #position function to determine x and y based on the lifespan of the particle (number of frames since it was created)
        self.pos = [-amp*math.cos(math.radians(time*freq))+self.adder,y]
        self.vel = [0,0]
        self.acc = [0, 0]
        self.colour = colour
        self.size = 1
        self.size_vel = 0
        self.time = time

    #displacing particles by velocity and changing velocity by acceleration
    # however since we manually fix every particles position to its wave-like motion when its drawn, this function does nothing in this program
    def move(self):
        for i in range(2):
            self.vel[i] += self.acc[i]
            self.pos[i] += self.vel[i]

    #drawing lines from the point of the wave to a fixed distance away, each line is 1 pixel wide and 500 pixels long, this helps to create the wave like
    #shape where the there are 2 sides to the wave, one which is blue and one which is black
    def draw2(self):
        #first two lines create black corners surrounded by water
        pygame.draw.rect(win, (100,100,255), (self.pos[0],self.pos[1],500,self.size))
        pygame.draw.rect(win, (100,100,255), (self.pos[1],self.pos[0],self.size,500))

        #these 2 lines create water corners surrounded by land
        #pygame.draw.rect(win, (0,0,0), (self.pos[0],self.pos[1],500,self.size))
        #pygame.draw.rect(win, (0,0,0), (self.pos[1],self.pos[0],self.size,500))


    #create the white border of the wave itself
    def draw(self):
        self.time += 1
        self.move()

        #size changes based on velocity variable
        if self.vel[0] > 0:
            self.size += self.size_vel
        else:
            self.size -= self.size_vel
        if self.size < 0:
            particles.remove(self)

        #updating particle position
        self.pos[0] = -self.amp*math.cos(math.radians(self.time*self.freq))+self.adder

        
        if self.pos[1]-self.adder < -self.amp*math.cos(math.radians(self.time*self.freq)):
            #border using circles
            #pygame.draw.circle(win, self.colour, (self.pos[0], self.pos[1]), self.size)
            #pygame.draw.circle(win, self.colour, (self.pos[1], self.pos[0]), self.size)

            #border using pixels
            #pygame.draw.rect(win, self.colour, (self.pos[0], self.pos[1], self.size,self.size))
            #pygame.draw.rect(win, self.colour, (self.pos[1], self.pos[0], self.size,self.size))


#redraw function for drawing all particles and objects on screen, then onto a window if any resizing is required
def redrawWin(time):
    win.fill((0,0,0))
    #win.fill((100,100,255))
    for particle in particles:
        particle.draw2()
    for particle1 in particles:
        particle1.draw()
    #lap = pygame.transform.scale(win, (1600,16000))
    """for i in range(20):
        pygame.draw.rect(win , (255,255,255), (390-i*16,390,16,16),1)
        pygame.draw.rect(win , (255,255,255), (390,390-i*16,16,16),1)"""
    #screen.blit(win,(-246,-246))
    screen.blit(win,(0,0))

    #to store screen as an image
    if time % 2 == 0:
        pygame.display.update()
        #pygame.image.save(screen, "frameNoBox"+str(time)+".png")


#initialisation of storage for all objects and loop condition
particles = []
run = True

#creating all particles
for i in range(800):
    #particles.append(Particle(400,i, (255,255,255), i, 22.5/2, 2))
    particles.append(Particle(400,i, (255,255,255), i, 5/2, 20))

#program time counter
time = 0

#game loop
while run:
    time +=1
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    
    redrawWin(time)
        
