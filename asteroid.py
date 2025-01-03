from constants import *
from circleshape import CircleShape
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        
    
    def draw(self,screen):
        pygame.draw.circle(screen,pygame.Color(255,255,255),self.position,self.radius,2)
        
        
    def update(self,dt):
        self.position +=  self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            
            first_new_asteroid = Asteroid(self.position.x,self.position.y,new_radius)
            second_new_asteroid = Asteroid(self.position.x,self.position.y,new_radius)
            
            
            first_new_asteroid.velocity = self.velocity.rotate(angle) * 1.2
            first_new_asteroid.velocity.rotate(angle)
            
            
            second_new_asteroid.velocity = self.velocity.rotate(-angle) * 1.2
            second_new_asteroid.velocity.rotate(-angle)