import pygame
import os


pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
done = False
i = 0
cur = i % 3

songs = []

path = r"C:\Users\pokam\Desktop\My education\pp2\lab7\Music"

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

with os.scandir(path) as it:
    for x in it:
        songs.append(x.name)


playing = True

while not done:

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_TAB]:
                pygame.mixer.music.load(r"C:\Users\pokam\Desktop\My education\pp2\lab7\Music\\" + songs[i])
                pygame.mixer.music.play(0)

        if pressed[pygame.K_RIGHT]:
                i += 1
                i = i % 3
                pygame.mixer.music.load(r"C:\Users\pokam\Desktop\My education\pp2\lab7\Music\\" + songs[i])
                pygame.mixer.music.play(0)

        if pressed[pygame.K_LEFT]:
                i -= 1
                i = i % 3
                pygame.mixer.music.load(r"C:\Users\pokam\Desktop\My education\pp2\lab7\Music\\" + songs[i])
                pygame.mixer.music.play(0)
        
        if pressed[pygame.K_SPACE]:
                if playing == False: 
                        pygame.mixer.music.unpause() 
                        playing = True 
                elif playing == True:
                        pygame.mixer.music.pause()
                        playing = False

                
                

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == SONG_END:
                        i += 1
                        i = i % 3
                        pygame.mixer.music.load(r"C:\Users\pokam\Desktop\My education\pp2\lab7\Music\\" + songs[i])
                        pygame.mixer.music.play(0)
        
        

        pygame.display.flip()
        clock.tick(60)
pygame.quit()