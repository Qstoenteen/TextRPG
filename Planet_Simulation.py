
import pygame
import math
pygame.init()
speed = 0.02
#screen_Settings
width = 1200
height = 900
FPS = 60
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

pygame.display.set_caption('Planet Simulation')
angle = 0

class Planet ():

    def __init__ (self,name,centerX,centerY,radius,distance,speed,color):
        self.name = name
        self.centerX = centerX
        self.centerY = centerY
        self.radius = radius
        self.distance = distance
        self.speed = speed
        self.color = color

    def draw (self):
        x = int(self.centerX + self.distance * math.sin(angle * self.speed))
        y = int(self.centerY + self.distance * math.cos(angle * self.speed))
        pygame.draw.circle(screen,self.color,(x,y),self.radius)
        return x,y

sun = Planet('Sun', width//2, height//2, 25, 2, 0.001, (250,255,0))

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
#####################################################
    screen.fill((0, 0, 0))
    
    
    xSun,ySun = sun.draw()
    earth = Planet('Earth', xSun, ySun, 10, 100, speed*10, (0, 255, 0))
    
    
    xVenus,yVenus = sun.draw()
    venus = Planet('Venus', xSun, ySun, 8, 60, speed*12.5, (155, 155, 0))
    
    
    xMercury,yMercury = sun.draw()
    mercury = Planet('Mercury', xSun, ySun, 5, 35, speed*15, (150, 150, 150))
    
    
    xEarth,yEarth = earth.draw()
    moon = Planet('Moon', xEarth, yEarth, 3, 15, speed*20, (255, 255, 255))
    
    #========================
    mars = Planet('Mars', xSun, ySun, 15, 150, speed*8, (255,0,0))
    
   
    xMars, yMars = mars.draw()
    fobos = Planet('Fobos', xMars, yMars, 3, 20, speed*10,(255,255,255))
    
    
    demos = Planet('Demos', xMars, yMars, 2, 25, speed*15,(255,255,255))
    
    
    #========================
    pygame.draw.line(screen,(255,255,255),(xSun,ySun),(xEarth,yEarth))
    pygame.draw.line(screen,(255,255,255),(xEarth,yEarth),(xMars,yMars))
    sun.draw()
    venus.draw()
    mercury.draw()
    earth.draw()
    moon.draw()
    mars.draw()
    fobos.draw()
    demos.draw()
    
    pygame.display.update()
    angle += 0.1
    clock.tick(FPS)