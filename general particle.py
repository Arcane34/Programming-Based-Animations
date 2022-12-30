import pygame, sys, random, math

#initializing pygame, window and framerate clock
pygame.init()
width = (800,800)
win = pygame.display.set_mode(width)
clock = pygame.time.Clock()


#particle class that hold particle data, such as velocity, colour and position
class Particle:
    def __init__(self, x, y, vel, colour):
        self.pos = [x,y]
        self.vel = vel
        self.acc = [0,0]
        self.colour = colour
        self.size = 10
        #size_vel is the shrink rate of a particle establishing how much a particle's radius will decrease every frame
        self.size_vel = 0.1
        #counter to hold lifespan of particle object in number of frames
        self.time = 0


        

    #move function that displaces particle according to velocity, changes velocity according to acceleration
    def move(self):
        for i in range(2):
            self.vel[i] += self.acc[i]
            self.pos[i] += self.vel[i]

    #draw function that adds to lifespan counter, calls the move function of the object, decreases the particle's size by size_vel and finally draws the particle onto the pygame window
    def draw(self):
        self.time += 1
        self.move()
        self.size -= self.size_vel
        if self.size < 0:
            particles.remove(self)
        pygame.draw.circle(win, self.colour, (self.pos[0], self.pos[1]), self.size)


#redraw function that handles the drawing of the entire window every frame along with all of its contents
def redrawWin():
    win.fill((0,0,0))
    for particle in particles:
        particle.draw()
    pygame.display.update()


#initialising conditions and holder of particle objects
particles = []
run = True

#game loop
while run:
    # framerate of 60 frames per second
    clock.tick(60)
    #particle generation at 400,400 with random velocity and the colour white
    particles.append(Particle(400,400,[(random.randint(0,20)/10)-1,(random.randint(0,20)/10)-1],(255,255,255)))

    #event check if user has closed window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    #redraw window function call
    redrawWin()
        
