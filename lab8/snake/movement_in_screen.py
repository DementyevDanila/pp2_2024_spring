import pygame
import random

def create_background(width, height):
        colors = [(152, 251, 152), (52, 201, 36)]
        background = pygame.Surface((width, height))
        tile_width = 20
        y = 0
        while y < height:
                x = 0
                while x < width:
                        row = y // tile_width
                        col = x // tile_width
                        pygame.draw.rect(
                                background, 
                                colors[(row + col) % 2],
                                pygame.Rect(x, y, tile_width, tile_width))
                        x += tile_width
                y += tile_width
        return background

pygame.init()

width = 800
height = 600

start_x = 160
start_y = 280
size = 20
cur_x = start_x
cur_y = start_y

y_upper_boarder = -20
x_upper_boarder = -20
y_lower_boarder = 600
x_lower_boarder = 800

food_x = random.randint(0, 39) * 20
food_y = random.randint(0, 29) * 20

score = 1
pos_x = [160]
pos_y = [280]

def draw_snake(x, y):
        pygame.draw.rect(screen, "Red", (x, y, 20, 20))

for i in range(score):
        p = 1 + i
        if (food_x == pos_x[-p] and food_y == pos_y[-p]):
                food_x = random.randint(0, 39) * 20
                food_y = random.randint(0, 29) * 20 
        
screen = pygame.display.set_mode((width, height))
background = create_background(width, height)
clock = pygame.time.Clock()

screen.blit(background, (0, 0))

done = False
UpMoving = False
DownMoving = False
LeftMoving = False
RightMoving = False
Restart = False
Playing = True

while not done:

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_r]:
            Restart = True
            UpMoving = False
            DownMoving = False
            LeftMoving = False
            RightMoving = False
            Playing = True

            cur_x = start_x
            cur_y = start_y
            score = 1
            pos_x = [160]
            pos_y = [280]

            screen.blit(background, (0, 0))
            draw_snake(start_x, start_y)


        if pressed[pygame.K_UP]: 
            UpMoving = True
            DownMoving = False
            LeftMoving = False
            RightMoving = False
            Restart = False
            
        if pressed[pygame.K_DOWN]:
            UpMoving = False
            DownMoving = True
            LeftMoving = False
            RightMoving = False
            Restart = False
        
        if pressed[pygame.K_LEFT]:    
            UpMoving = False
            DownMoving = False
            LeftMoving = True
            RightMoving = False
            Restart = False
        
        if pressed[pygame.K_RIGHT]:
            UpMoving = False
            DownMoving = False
            LeftMoving = False
            RightMoving = True
            Restart = False
        

        if (UpMoving == True and Playing == True):
            cur_y -= 20
            pos_x.append(cur_x)
            pos_y.append(cur_y)
            if(cur_y - 20 < y_upper_boarder):
                Playing = False
                cur_y += 20
                screen.blit(background, (0, 0))
                draw_snake(cur_x, cur_y)
                print("Your score is amazing:", score - 1)


        if (DownMoving == True and Playing == True):
            cur_y += 20
            pos_x.append(cur_x)
            pos_y.append(cur_y)
            if(cur_y + 20 > y_lower_boarder):
                Playing = False
                cur_y -= 20
                screen.blit(background, (0, 0))
                draw_snake(cur_x, cur_y)
                print("Your score is amazing:", score - 1)

        if (LeftMoving == True and Playing == True):
            cur_x -= 20
            pos_x.append(cur_x)
            pos_y.append(cur_y)
            if(cur_x - 20 < x_upper_boarder):
                Playing = False
                cur_x += 20
                screen.blit(background, (0, 0))
                draw_snake(cur_x, cur_y)
                print("Your score is amazing:", score - 1)

        if (RightMoving == True and Playing == True):
            cur_x += 20
            pos_x.append(cur_x)
            pos_y.append(cur_y) 
            if(cur_x + 20 > x_lower_boarder):
                Playing = False
                cur_x -= 20
                screen.blit(background, (0, 0))
                draw_snake(cur_x, cur_y)
                print("Your score is amazing:", score - 1)

      
        if (Restart == False):
            screen.blit(background, (0, 0))
            if(score == 1):
                draw_snake(cur_x, cur_y)
            else:
                for i in range(score):
                        p = 1 + i
                        draw_snake(pos_x[-p], pos_y[-p])
            pygame.draw.rect(screen, 'Blue', (food_x, food_y, size, size))

        if (cur_x == food_x and cur_y == food_y):
                score += 1
                for i in range(score):
                        p = 1 + i
                        if (food_x == pos_x[-p] and food_y == pos_y[-p]):
                                food_x = random.randint(0, 39) * 20
                                food_y = random.randint(0, 29) * 20 
                pygame.draw.rect(screen, 'Blue', (food_x, food_y, size, size))
                

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()
        clock.tick(8)
pygame.quit()