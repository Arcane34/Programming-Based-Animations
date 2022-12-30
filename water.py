import pygame, sys, random, math

pygame.init()
width = (800,800)
win = pygame.display.set_mode(width)
clock = pygame.time.Clock()



class Particle:
    def __init__(self, x, y, vel, colour, size):
        self.pos = [x,y]
        self.vel = vel
        self.acc = [0,0]
        self.colour = colour
        self.size = size
        self.size_vel = 0.1
        self.time = 0


    def move(self):
        for i in range(2):
            self.vel[i] += self.acc[i]
            self.pos[i] += self.vel[i]

    def draw(self):
        self.time += 1
        self.move()
        r = self.colour[0]
        g = self.colour[1]
        b = self.colour[2]
        #if self.time % 2 == 0:
        r -= 1
        g -= 1
        self.colour = (r, g, b)
        pygame.draw.rect(win, self.colour, (self.pos[0], self.pos[1], self.size[0], self.size[1]))


def redrawWin():
    win.fill((100,100,255))
    for particle in particles:
        particle.draw()
    for part in particles1:
            part.draw()
            if part.colour[0] < 100:
                particles1.remove(part)
    pygame.display.update()

class waterEmitter:
    def __init__(self, x, y, time):
        self.x= x
        self.y  = y
        self.time = time
        self.particles = []

    def draw(self):
        self.time -= 1
        if random.randint(0,50) == 1:
            particles1.append(Particle(self.x + 2*(random.randint(0,20)-10),self.y + 2*(random.randint(0,20)-10),[0,0], (255,255,255), [random.randint(2,5)*2,2]))
        
            
        if self.time < 0:
            particles.remove(self)
        

particles = []
particles1 = []
run = True
while run:

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    if random.randint(0,100) == 1:
        particles.append(waterEmitter(random.randint(0,800),random.randint(0,800),400))
    redrawWin()
        
