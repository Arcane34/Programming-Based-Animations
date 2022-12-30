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


def tentacle(time,colour):
    if time + 90 // 180 != 0:
        upDown = math.cos(math.radians(time))
        reach = 1+(math.sin(math.radians(time))*math.sin(math.radians(time)))
        particles.append(Particle(400,400, [reach,upDown], colour))
        #particles.append(Particle(400,400, [reach*-1,upDown], colour))
        #particles.append(Particle(400,400, [upDown,reach], colour))
        #particles.append(Particle(400,400, [upDown,reach*-1], colour))
        
        #particles.append(Particle(400,400, [reach,upDown*-1], colour))
        #particles.append(Particle(400,400, [reach*-1,upDown*-1], colour))
        #particles.append(Particle(400,400, [upDown*-1,reach], colour))
        #particles.append(Particle(400,400, [upDown*-1,reach*-1], colour))

class Tentacle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        

particles = []
run = True
time = 0
while run:
    time = (time+1)%360
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    for i in range(1):
        tentacle(time+i*25, (225,255,255))
    
    redrawWin()
        

        



                           
