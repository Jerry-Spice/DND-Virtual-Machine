import mouse
import pygame
from Fog import *
from Vector2 import *
import time

counter = 0
cur_fog = None
id = 0

def process_click():
    global pos, result, counter, cur_fog, id
    pos = pygame.mouse.get_pos()
    result, pos = True, Vector2(pos[0], pos[1])
    if counter == 1:
        cur_fog = Fog(cur_fog.x, cur_fog.y, pos.x-cur_fog.x,pos.y-cur_fog.y, id)
        fogs.append(cur_fog)
        id+=1
        counter = 0
    else:
        cur_fog = Fog(pos.x, pos.y, 0,0, id)
        counter+=1

def finish_recording(filename):
    global coords
    print(coords)
    with open(filename[:-4]+"Fog.txt","w") as f:
        for i in range(len(coords)):
            f.write(str(coords[i].x)+","+str(coords[i].y)+"\n")
        f.close()
    quit()  

if __name__ == '__main__':
    filename = input("file to record:")

    screen = pygame.display.set_mode((700,700))

    background_image = pygame.transform.scale(pygame.image.load(filename), (700,700))

    pos = None
    coords = []
    result = False
    fogs = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
        if pygame.mouse.get_pressed(3)[0]:
            process_click()
            time.sleep(0.5)
        if pygame.mouse.get_pressed(3)[2]:
            finish_recording(filename)
        if result:
            coords.append(pos)
            result = False
        


        screen.fill((200,200,200))
        screen.blit(background_image, (0,0))

        for fog in fogs:
            fog.display_fog(screen)
        
        pygame.display.update()
    

