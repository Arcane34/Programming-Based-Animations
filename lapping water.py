import pygame, sys, random, math

pygame.init()
width = (800,800)
screen = pygame.display.set_mode((160,160))
win = pygame.Surface(width)
clock = pygame.time.Clock()



class Particle:
    def __init__(self, x, y, colour,time, freq, amp):
        self.amp = amp
        self.freq = freq
        self.adder = 400
        self.pos = [-amp*math.cos(math.radians(time*freq))+self.adder,y]
        self.vel = [0,0]
        self.acc = [0, 0]
        self.colour = colour
        self.size = 1
        self.size_vel = 0
        self.time = time

    def move(self):
        for i in range(2):
            self.vel[i] += self.acc[i]
            self.pos[i] += self.vel[i]


    def draw2(self):
        pygame.draw.rect(win, (100,100,255), (self.pos[0],self.pos[1],500,self.size))
        pygame.draw.rect(win, (100,100,255), (self.pos[1],self.pos[0],self.size,500))
        #pygame.draw.rect(win, (0,0,0), (self.pos[0],self.pos[1],500,self.size))
        #pygame.draw.rect(win, (0,0,0), (self.pos[1],self.pos[0],self.size,500))

    def draw(self):
        self.time += 1
        self.move()
        if self.vel[0] > 0:
            self.size += self.size_vel
        else:
            self.size -= self.size_vel
        if self.size < 0:
            particles.remove(self)
        self.pos[0] = -self.amp*math.cos(math.radians(self.time*self.freq))+self.adder
        if self.pos[1]-self.adder < -self.amp*math.cos(math.radians(self.time*self.freq)):
            #pygame.draw.circle(win, self.colour, (self.pos[0], self.pos[1]), self.size)
            #pygame.draw.circle(win, self.colour, (self.pos[1], self.pos[0]), self.size)
            pygame.draw.rect(win, self.colour, (self.pos[0], self.pos[1], self.size,self.size))
            pygame.draw.rect(win, self.colour, (self.pos[1], self.pos[0], self.size,self.size))


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
    screen.blit(win,(0-246,-246))
    
    if time % 2 == 0:
        pygame.display.update()
        #pygame.image.save(screen, "frameNoBox"+str(time)+".png")


particles = []
run = True

for i in range(800):
    particles.append(Particle(400,i, (255,255,255), i, 22.5/2, 2))
time = 0
while run:
    time +=1
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    
    redrawWin(time)
        
