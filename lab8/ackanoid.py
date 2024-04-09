import pygame 
import random

pygame.init()

W, H = 1100, 600
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)


pause_font = pygame.font.SysFont('comicsansms', 40)
pause_text = pause_font.render('Pause', True, (255, 255, 255))
pause_text_rect = pause_text.get_rect()
pause_text_rect.center = (W // 2, H // 2)

pause_bg_color = (0, 0, 0, 128)  # Black with 50% transparency

unbreakable_block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
                                      100, 50) for i in range(10) for j in range(1)]

block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
                           100, 50) for i in range(10) for j in range(2, 5)]
color_list = [(random.randrange(0, 255), 
               random.randrange(0, 255),  
               random.randrange(0, 255))
              for i in range(10) for j in range(4)]

losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

time_elapsed = 0
speed_increase_rate = 0.01  
paddle_shrink_rate = 0.001  

paused = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused

    if paused:
        pause_bg = pygame.Surface((W, H), pygame.SRCALPHA)
        pause_bg.fill(pause_bg_color)
        screen.blit(pause_bg, (0, 0))
        
        screen.blit(pause_text, pause_text_rect)
        
        pygame.display.flip()
        clock.tick(FPS)
        continue

    screen.fill(bg)
    
    [pygame.draw.rect(screen, (255, 0, 0), unbreakable_block) for unbreakable_block in unbreakable_block_list]

    [pygame.draw.rect(screen, color_list[color], block)
     for color, block in enumerate (block_list)]

    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50: 
        dy = -dy
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = dx, -dy

    collision_sound = pygame.mixer.Sound('catch.mp3')
    hitIndex = ball.collidelist(block_list)
    if hitIndex != -1:
        hitRect = block_list.pop(hitIndex)
        hitColor = color_list.pop(hitIndex)
        dx, dy = dx, -dy
        game_score += 1
        collision_sound.play()
