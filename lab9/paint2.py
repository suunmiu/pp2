import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    points = []
    
    drawing = False
    erasing = False
    rectangle_mode = False
    circle_mode = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                    rectangle_mode = False
                    circle_mode = False
                    erasing = False
                elif event.key == pygame.K_g:
                    mode = 'green'
                    rectangle_mode = False
                    circle_mode = False
                    erasing = False
                elif event.key == pygame.K_b:
                    mode = 'blue'
                    rectangle_mode = False
                    circle_mode = False
                    erasing = False
                elif event.key == pygame.K_e:
                    erasing = not erasing
                    rectangle_mode = False
                    circle_mode = False
                elif event.key == pygame.K_a:
                    rectangle_mode = True
                    circle_mode = False
                    erasing = False
                elif event.key == pygame.K_c:
                    circle_mode = True
                    rectangle_mode = False
                    erasing = False
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rectangle_mode or circle_mode:
                        x1, y1 = event.pos
                        drawing = True
                    else:
                        radius = min(200, radius + 1)
                elif event.button == 3:
                    if rectangle_mode or circle_mode:
                        drawing = False
                    else:
                        radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if rectangle_mode or circle_mode:
                        x2, y2 = event.pos
                        if rectangle_mode:
                            pygame.draw.rect(screen, pygame.Color(mode), (x1, y1, x2-x1, y2-y1), 0)
                        elif circle_mode:
                            pygame.draw.circle(screen, pygame.Color(mode), (x1, y1), max(abs(x2-x1), abs(y2-y1)), 0)
                        drawing = False
            
            if event.type == pygame.MOUSEMOTION:
                if drawing and (rectangle_mode or circle_mode):
                    screen.fill((0, 0, 0))
                    if rectangle_mode:
                        pygame.draw.rect(screen, pygame.Color(mode), (x1, y1, event.pos[0]-x1, event.pos[1]-y1), 0)
                    elif circle_mode:
                        pygame.draw.circle(screen, pygame.Color(mode), (x1, y1), max(abs(event.pos[0]-x1), abs(event.pos[1]-y1)), 0)
                elif erasing and event.buttons[0]:
                    position = event.pos
                    pygame.draw.circle(screen, (0, 0, 0), position, radius)
                elif not erasing:
                    position = event.pos
                    points.append(position)
                    points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
