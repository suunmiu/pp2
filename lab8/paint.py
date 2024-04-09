import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    circle_color = 'blue'
    square_color = 'red'
    mode = 'circle'
    points = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    circle_color = 'red'
                    square_color = 'red'
                elif event.key == pygame.K_g:
                    circle_color = 'green'
                    square_color = 'green'
                elif event.key == pygame.K_b:
                    circle_color = 'blue'
                    square_color = 'blue'
                elif event.key == pygame.K_y:
                    circle_color = 'yellow'
                    square_color = 'yellow'
                elif event.key == pygame.K_d:
                  main()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                  position = event.pos
                  if mode == 'circle':
                    points.append((position, 'circle', circle_color))
                  elif mode == 'rectangle':
                    points.append((position, 'rectangle', square_color))
                elif event.button == 3:  # Right click
                    if mode == 'circle':
                        mode = 'rectangle'
                    elif mode == 'rectangle':
                        mode = 'circle'
                  

        screen.fill((0, 0, 0))

        for point, drawing_mode, color in points:
            if drawing_mode == 'circle':
                pygame.draw.circle(screen, getColor(color), point, radius)
            elif drawing_mode == 'rectangle':
                pygame.draw.rect(screen, getColor(color), pygame.Rect(point[0] - radius, point[1] - radius, 2 * radius, 2 * radius))
            

        pygame.display.flip()
        clock.tick(60)

def getColor(color_mode):
    if color_mode == 'blue':
        return (0, 0, 255)
    elif color_mode == 'red':
        return (255, 0, 0)
    elif color_mode == 'green':
        return (0, 255, 0)
    elif color_mode == 'yellow':
        return (255, 255, 0)

main()