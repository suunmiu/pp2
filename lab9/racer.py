import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

blue  = (0, 0, 255)
red   = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

w = 400
h = 600
speed = 5
score = 0
coins_collected = 0


font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)

background = pygame.image.load("PygameTutorial_3_0/AnimatedStreet.png")

screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("racer")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("PygameTutorial_3_0/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w-40), 0)  

      def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.top > 600):
            global score
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, w - 40), 0)


class Coin(pygame.sprite.Sprite):
  def __init__(self):
      super().__init__()
      self.image = pygame.image.load("PygameTutorial_3_0/coin.png")
      self.rect = self.image.get_rect()
      self.rect.center = (random.randint(40, w - 40), 0)

  def move(self):
      global coins_collected
      self.rect.move_ip(0, speed)
      if self.rect.top > h:
          self.rect.top = 0
          self.rect.center = (random.randint(40, w - 40), 0)

      # Check for collision with player
      if self.rect.colliderect(P1.rect):
          coins_collected += 1
          self.rect.top = 0
          self.rect.center = (random.randint(40, w - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("PygameTutorial_3_0/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
      pressed_keys = pygame.key.get_pressed()

      if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
      if self.rect.right < w:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
coin = Coin()


#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
coins = pygame.sprite.Group()
all_sprites.add(coin)


#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:

    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              speed += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0,0))
    scores = font_small.render(f"Score:{score}", True, black)
    coin_text = font_small.render(f"Coins: {coins_collected}", True, black)
    screen.blit(scores, (10,10))
    screen.blit(coin_text, (w - 100, 10))


    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('PygameTutorial_3_0/crash.wav').play()
          time.sleep(0.5)

          screen.fill(red)
          screen.blit(game_over, (30,250))

    pygame.display.update()
    FramePerSec.tick(FPS)


pygame.quit()