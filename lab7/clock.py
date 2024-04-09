import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((850, 850))
pygame.display.set_caption("Mickey Clock")

#images 
mickey_left = pygame.image.load('image/lefthand.png')
mickey_right = pygame.image.load('image/righthand.png')
mickey = pygame.image.load('image/clock.png')

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36) 
white = (255, 255, 255)

hand_width, hand_height = mickey_left.get_width(), mickey_left.get_height()
center_x, center_y = 850 // 2, 850 // 2

def rotate_image(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=image.get_rect().center)
    return rotated_image, rotated_rect


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    current_time = pygame.time.get_ticks() // 1000  
    minutes = current_time // 60
    seconds = current_time % 60

    # Calculate angles for Mickey's hands
    seconds_angle = 360 - seconds * 6 
    minutes_angle = 360 - minutes * 6  

    screen.blit(mickey, (0, 0)) 


    # Rotate the images of Mickey's hands
    rotated_left, left_rect = rotate_image(mickey_left, minutes_angle)
    rotated_right, right_rect = rotate_image(mickey_right, seconds_angle)

    left_rect.center = (center_x, center_y)
    right_rect.center = (center_x, center_y)
  
    # clock hands
    screen.blit(rotated_left, left_rect.topleft)
    screen.blit(rotated_right, right_rect.topleft)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()
