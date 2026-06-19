import pygame # pyright: ignore[reportMissingImports]
import math

pygame.init()
pygame.display.set_caption("Simple 3D Line Rendering w/ Movement using Pygame WIP")
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()

background = 'white'
maincolor = 'black'
pos_x = 500
pos_y = 0
pos_z = 400
heading = 0
move_mult = 10
turn = 4
zoom = 800

def coords(x, y, z):
    # transformation stuff
    # insert math sorcery here

    return x, z # for now

def draw(surface, start, end, color=maincolor):
    pygame.draw.line(surface, color, start, end, 5)

with open('src/lines.txt', 'r') as file:
    linesraw = file.read().splitlines()
    lines = []
    excluded = [linesraw[0], linesraw[1], linesraw[2], linesraw[3], linesraw[4]] # I know this is a bad way to exclude lines but I'm lazy

    for line in linesraw: # this is DEFINITELY a slow and overcomplicated way to seperate each line into a list element
        if not line in excluded:
            coord = []
            num = ""

            for i in range(len(line)):
                if line[i] == " ":
                    coord.append(int(num))
                    num = ""
                else:
                    num += line[i]

                if len(coord) == 3:
                        lines.append(coord)
                        coord = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    true_head = -heading * math.pi/180 + math.pi

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pos_x += math.sin(true_head) * move_mult
        pos_z += math.cos(true_head) * move_mult
    if keys[pygame.K_s]:
        pos_x -= math.sin(true_head) * move_mult
        pos_z -= math.cos(true_head) * move_mult
    if keys[pygame.K_a]:
        pos_x += math.sin(true_head + math.pi/2) * move_mult
        pos_z += math.cos(true_head + math.pi/2) * move_mult
    if keys[pygame.K_d]:
        pos_x += math.sin(true_head - math.pi/2) * move_mult
        pos_z += math.cos(true_head - math.pi/2) * move_mult
    if keys[pygame.K_LEFT]:
        heading -= turn
    if keys[pygame.K_RIGHT]:
        heading += turn

    screen.fill(background)

    text = pygame.font.Font(None, 19).render("FPS: " + str(round(clock.get_fps())), True, maincolor)
    screen.blit(text, (1, 1))

    clock.tick(60)
    pygame.display.flip()