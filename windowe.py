import pygame

pygame.init()

WIDTH, HEIGHT = 400, 300

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My first game screen")

WHITE = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 7. Drawing/Rendering (fill the background color)
    screen.fill(WHITE)

    # 8. Update the display to make changes visible
    pygame.display.flip() # or pygame.display.update()

# 9. Quit Pygame and the program when the loop ends
pygame.quit()