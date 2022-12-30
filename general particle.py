import pygame, sys, random, math

pygame.init()
width = (800,800)
win = pygame.display.set_mode(width)
clock = pygame.time.Clock()



class Particle:
    def __init__(self, x, y, vel, colour):
        self.pos = [x,y]
        self.vel = vel
        self.acc = [0,0]
        self.colour = colour
        self.size = 10
        self.size_vel = 0.1
        self.time = 0


        


    def move(self):
        for i in range(2):
            self.vel[i] += self.acc[i]
            self.pos[i] += self.vel[i]

    def draw(self):
        self.time += 1
        self.move()
        self.size -= self.size_vel
        if self.size < 0:
            particles.remove(self)
        pygame.draw.circle(win, self.colour, (self.pos[0], self.pos[1]), self.size)


def redrawWin():
    win.fill((0,0,0))
    for particle in particles:
        particle.draw()
    pygame.display.update()


particles = []
run = True
while run:

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    
    redrawWin()
        
