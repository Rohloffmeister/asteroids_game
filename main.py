import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable,drawable)
    Shot.containers = (updatable,drawable,shoots)
    
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            
        for object in updatable:
            object.update(dt)
        
        for object in asteroids:
            if player.check_collision(object):
                print("Game over!")
                return
            
        for asteroid in asteroids:
            
            for shoot in shoots:
                if asteroid.check_collision(shoot):
                    shoot.kill()
                    asteroid.split()
        
        screen.fill(pygame.Color(0,0,0))
 
        for object in drawable:
            object.draw(screen)
            
        
            

        
        
        
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    
if __name__ == "__main__":
    main()