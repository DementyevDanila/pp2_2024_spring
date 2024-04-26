import pygame
import random
import sys
import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    dbname = 'postgres',
    user = 'postgres',
    password = 'hhhohoh'
)

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS snake_users (
            nickname VARCHAR(20) PRIMARY KEY,
            score INT
);
""")
conn.commit()

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

clock = pygame.time.Clock()

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

food2_x = random.randint(0, 39) * 20
food2_y = random.randint(0, 29) * 20

food3_x = random.randint(0, 39) * 20
food3_y = random.randint(0, 29) * 20

loaded_level = 0
score = 1
pos_x = [160]
pos_y = [280]
defeat_cnt = 0

TEXT = ""
FPS = 8
big_font = pygame.font.SysFont("Verdana", 40)
font = pygame.font.SysFont("comicsansms", 30)
txt = str("Score: " + str(score - 1))
text = font.render(txt, True, "Brown")

FOOD_RESPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(FOOD_RESPAWN_EVENT, 3000)

FOOD2_SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(FOOD2_SPAWN_EVENT, 6000)

FOOD3_SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(FOOD3_SPAWN_EVENT, 9000)

fps = (FPS + score // 5)
def draw_snake(x, y):
        pygame.draw.rect(screen, "Red", (x, y, 20, 20))

def defeat_screen():
        screen.fill((255, 0, 0))
        background.fill((255, 0, 0))
        pygame.display.flip()
        screen.blit(pygame.font.SysFont("Verdana", 60).render("Game over", True, "Black"), (130, 250))
        screen.blit(font.render("Your total score: " + str(score), True, "Black"), (150, 350))
        screen.blit(font.render("Your current speed is: " + str(fps), True, "Black"), (150, 380))
        screen.blit(font.render("Press P to reduce your speed to normal", True, "Black"), (150, 410))
        screen.blit(font.render("Press R to restart", True, "Black"), (150, 440))
        screen.blit(font.render("Press ESC to see mtnu", True, "Black"), (150, 470))
        pygame.display.flip()
        cur.execute(f"""UPDATE snake_users
                SET level = '{fps}'
                WHERE nickname = '{TEXT}'
                """)
        conn.commit()
        """sleep(2)
        pygame.quit()
        sys.exit()"""

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
Greating = True

def menu():
    doone = False
    f = 0
    txt = False
    men = ["Resume", "Save", "Exit"]
    while not doone:
        screen.fill((100, 34, 134))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    doone = True
                elif event.key == pygame.K_DOWN:
                    f += 1
                    if f > 2: f = 2
                elif event.key == pygame.K_UP:
                    f -= 1
                    if f < 0: f = 0
                if event.key == pygame.K_RETURN:
                    if f == 0: doone = True
                    if f == 1:
                        cur.execute(f"""UPDATE snake_users
                        SET level = '{fps}'
                        WHERE nickname = '{TEXT}'
                        """)
                        conn.commit()
                        txt = True
                    if f == 2:
                        pygame.quit()
                        sys.exit()
        
        
        for i in range(3):
            if f == i:
                screen.blit(big_font.render('>' + men[i], True, "White"), (100, 60 + 60*i))
            else:
                screen.blit(big_font.render(men[i], True, "White"), (100, 60 + 60*i))
        if txt: screen.blit(big_font.render("Saved", True, "White"), (450,550))
        
        pygame.display.flip()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                                TEXT = TEXT[:-1]
                        elif event.key == pygame.K_RETURN:
                                done = True
                        else:
                                TEXT += event.unicode
                                TEXT = TEXT[:20]
        screen.fill((100, 34, 134))
        pygame.draw.rect(screen, "White", pygame.Rect(100, 275, 400, 50))
        screen.blit(big_font.render("Enter your nickname", True, "White"), (95,200))
        screen.blit(font.render(TEXT, True, "Black"), (120,285))
    
        pygame.display.flip()
        
cur.execute(f"SELECT * FROM snake_users WHERE nickname  = '{TEXT}'")
found = cur.fetchone()
if found:
    FPS = found[1]
    
else:
    cur.execute(f"""INSERT INTO snake_users (nickname, level) VALUES
                ('{TEXT}', 0);
            """)
    conn.commit()
                
done = False
while not done:
        fps = (FPS + score // 5)
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_r]:
            Restart = True
            UpMoving = False
            DownMoving = False
            LeftMoving = False
            RightMoving = False
            Playing = True
            Greating = False

            cur_x = start_x
            cur_y = start_y
            score = 1
            defeat_cnt = 0
            pos_x = [160]
            pos_y = [280]
            fps = (FPS + score // 5)
            screen = pygame.display.set_mode((width, height))
            background = create_background(width, height)

            txt = str("Score: " + str(score - 1))
            text = font.render(txt, True, "Brown")

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
        
        if pressed[pygame.K_ESCAPE]:
                menu()

        if pressed[pygame.K_p]:
                FPS = 8
        
        if (UpMoving == True and Playing == True):
            cur_y -= 20
            pos_x.append(cur_x)
            pos_y.append(cur_y)
            if(cur_y - 20 < y_upper_boarder):
                Playing = False
                


        if (DownMoving == True and Playing == True):
            cur_y += 20
            pos_x.append(cur_x)
            pos_y.append(cur_y)
            if(cur_y + 20 > y_lower_boarder):
                Playing = False
                

        if (LeftMoving == True and Playing == True):
            cur_x -= 20
            pos_x.append(cur_x)
            pos_y.append(cur_y)
            if(cur_x - 20 < x_upper_boarder):
                Playing = False
                

        if (RightMoving == True and Playing == True):
            cur_x += 20
            pos_x.append(cur_x)
            pos_y.append(cur_y) 
            if(cur_x + 20 > x_lower_boarder):
                Playing = False
     
        if (Playing == False and defeat_cnt == 0):
                defeat_screen()
                defeat_cnt += 1

        

        if (Restart == False and Playing == True):
                screen.blit(background, (0, 0))
                if(score == 1):
                        draw_snake(cur_x, cur_y)
                else:
                        for i in range(score):
                                p = 1 + i
                                draw_snake(pos_x[-p], pos_y[-p])
                for i in range(score):
                        if(score == 1):
                                continue
                        g = 2 + i
                        if(cur_x == pos_x[-g] and cur_y == pos_y[-g]):
                                Playing = False
                pygame.draw.rect(screen, 'Blue', (food_x, food_y, size, size))
                pygame.draw.rect(screen, 'Magenta', (food2_x, food2_y, size, size))
                pygame.draw.rect(screen, 'Orange', (food3_x, food3_y, size, size))


                if (cur_x == food_x and cur_y == food_y):
                        pygame.time.set_timer(FOOD_RESPAWN_EVENT, 3000)
                        score += 1
                        txt = str("Score: " + str(score - 1))
                        text = font.render(txt, True, "Brown")
                        for i in range(score):
                                p = 1 + i
                                if (food_x == pos_x[-p] and food_y == pos_y[-p]):
                                        food_x = random.randint(0, 39) * 20
                                        food_y = random.randint(0, 29) * 20 
                        pygame.draw.rect(screen, 'Blue', (food_x, food_y, size, size))

                if (cur_x == food2_x and cur_y == food2_y):
                        pygame.time.set_timer(FOOD2_SPAWN_EVENT, 6000)
                        score += 2
                        txt = str("Score: " + str(score - 1))
                        text = font.render(txt, True, "Brown")
                        for i in range(score):
                                p = 1 + i
                                if (food2_x == pos_x[-p] and food2_y == pos_y[-p]):
                                        food2_x = random.randint(0, 39) * 20
                                        food2_y = random.randint(0, 29) * 20 
                        pygame.draw.rect(screen, 'Magenta', (food2_x, food2_y, size, size))

                if (cur_x == food3_x and cur_y == food3_y):
                        pygame.time.set_timer(FOOD3_SPAWN_EVENT, 9000)
                        score += 3
                        txt = str("Score: " + str(score - 1))
                        text = font.render(txt, True, "Brown")
                        for i in range(score):
                                p = 1 + i
                                if (food3_x == pos_x[-p] and food3_y == pos_y[-p]):
                                        food3_x = random.randint(0, 39) * 20
                                        food3_y = random.randint(0, 29) * 20 
                        pygame.draw.rect(screen, 'Orange', (food3_x, food3_y, size, size))

                screen.blit(text, (330, 10))
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == FOOD_RESPAWN_EVENT:  
                        food_x = random.randint(0, 39) * 20
                        food_y = random.randint(0, 29) * 20
                if event.type == FOOD2_SPAWN_EVENT:  
                        food2_x = random.randint(0, 39) * 20
                        food2_y = random.randint(0, 29) * 20
                if event.type == FOOD3_SPAWN_EVENT:  
                        food3_x = random.randint(0, 39) * 20
                        food3_y = random.randint(0, 29) * 20
                
        pygame.display.flip()
        clock.tick(fps)
pygame.quit()