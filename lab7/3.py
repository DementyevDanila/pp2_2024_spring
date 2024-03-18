import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
done = False
x = 400
y = 300
y_upper_boarder = 25 
x_upper_boarder = 25
y_lower_boarder = 575
x_lower_boarder = 775
alpha = 0
while not done:
        
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
            if (y - 20 >= y_upper_boarder):
                y -= 20
            if (y - 20 < y_upper_boarder):
                alpha = y - y_upper_boarder
                y -= alpha
        if pressed[pygame.K_DOWN]:
            if (y + 20 <= y_lower_boarder):
                y += 20
            if (y + 20 > y_lower_boarder):
                alpha = y_lower_boarder - y
                y += alpha
        if pressed[pygame.K_LEFT]: 
            if (x - 20 >= x_upper_boarder):
                x -= 20
            if (x - 20 < y_upper_boarder):
                alpha = x - x_upper_boarder
                x -= alpha
        if pressed[pygame.K_RIGHT]:
            if (x + 20 <= x_lower_boarder):
                x += 20
            if (x + 20 > x_lower_boarder):
                alpha = x_lower_boarder - x
                x += alpha
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, 'Red', (x, y), 25)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()
        clock.tick(60)
pygame.quit()