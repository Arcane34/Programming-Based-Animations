import pygame, sys, random, math

#initializing pygame, windo and framerate clock
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


#function for creating particles with velocities based on time using wave functions to create a tentacle like movement
def tentacle(time,colour):

    #ensuring there is no division by 0
    if time + 90 // 180 != 0:
        #defines the orientation of the resulting tentacle, being the y velocity
        upDown = math.cos(math.radians(time))
        #defines the length/ size of the tentacle, being the x velocity
        reach = 1+(math.sin(math.radians(time))*math.sin(math.radians(time)))

        #creating particles and appending them
        
        particles.append(Particle(400,400, [reach,upDown], colour))
        #particles.append(Particle(400,400, [reach*-1,upDown], colour))
        #particles.append(Particle(400,400, [upDown,reach], colour))
        #particles.append(Particle(400,400, [upDown,reach*-1], colour))
        
        #particles.append(Particle(400,400, [reach,upDown*-1], colour))
        #particles.append(Particle(400,400, [reach*-1,upDown*-1], colour))
        #particles.append(Particle(400,400, [upDown*-1,reach], colour))
        #particles.append(Particle(400,400, [upDown*-1,reach*-1], colour))

        
#initialising conditions and holder of particle objects
particles = []
run = True

#program time counter for wave functions
time = 0

#game loop
while run:
    #keeping timer in degrees, and not letting number get too big so that it will not take more processing time
    time = (time+1)%360
    
    # framerate of 60 frames per second
    clock.tick(60)

    #event check if user has closed window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    for i in range(1):
        tentacle(time+i*25, (225,255,255))

    #redraw window function call
    redrawWin()
        

        



                           
