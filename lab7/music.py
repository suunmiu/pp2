import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Music player")

music_files = ["music/Beatles.mp3", "music/heaven.mp3", "music/Maria.mp3"]
current_track = 0

pygame.mixer.music.load(music_files[current_track])

def play():
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    play()

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop()
                else:
                    play()
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                previous_track()

    screen.fill((255, 255, 255))

    font = pygame.font.SysFont(None, 24)
    text = font.render("Current Track: " + music_files[current_track], True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.update()

pygame.quit()


    window.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
