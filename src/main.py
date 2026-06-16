import pygame # pyright: ignore[reportMissingImports]
import math

pygame.init()
pygame.display.set_caption("Simple 3D Line Rendering w/ Movement using Pygame")
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 19)

pos_x = 500
pos_y = 0
pos_z = 400
heading = 0
move_mult = 10
turn = 4
rot_x = 0
rot_y = 0
zoom = 800

def coords(x, y, z):
    global pos_x, pos_y, rot_x, rot_y

    temp_x = x * math.cos(rot_y) + (y * math.sin(rot_x) + z * math.cos(rot_x)) * math.sin(rot_y)
    temp_y = y * math.cos(rot_x) - z * math.sin(rot_x)
    temp_z = -x * math.sin(rot_y) + (y * math.sin(rot_x) + z * math.cos(rot_x)) * math.cos(rot_y)
    
    factor = zoom / (-temp_z - pos_z)

    return (temp_x - pos_x) * factor, (temp_y - pos_y) * factor

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

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (pos_x, pos_z), 20)
    text = font.render("FPS: " + str(round(clock.get_fps())), True, "white")
    screen.blit(text, (1, 1))

    clock.tick(60)
    pygame.display.flip()