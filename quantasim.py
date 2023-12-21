import pygame
import pymunk
import pymunk.pygame_util
import math
import sys

pygame.init()

WIDTH, HEIGHT = 700,700
window = pygame.display.set_mode((WIDTH,HEIGHT))

def draw(space, window, draw_options):
    window.fill("white")
    space.debug_draw(draw_options)
    pygame.display.update()

def create_boundaries(space, width, height):
    rects = [
        [(width/2,height-10), (width, 20)],
        [(width/2, 10), (width, 20)],
        [(10, height/2), (20, height)],
        [(width-10, height/2), (20, height)]
    ]

    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        space.add(body,shape)
        return shape

def create_ball(space, radius, mass, s):
    body = pymunk.Body()
    if s<0.4:
        s = s+0.4
    body.position = (200,HEIGHT - 20 - 75*s)
    shape = pymunk.Circle(body,radius)
    shape.mass = mass
    shape.color = (255,0,0,100)
    space.add(body, shape)
    return shape

def run(window, width, height):
    run = True
    clock = pygame.time.Clock()
    fps=60
    dt = 1/fps
    g = float(input("Enter Gravitational Constant value: "))
    if g<=0:
        sys.exit("0 or negative values aren't accepted.")
    r = 30
    m = 10
    s = float(input("Enter height of ball above the ground: "))
    if s<0:
        sys.exit("Invalid height.")
    space = pymunk.Space()
    space.gravity = (0, g*100)
    t = math.sqrt(2*s/g)
    print("Time of free fall(t)=",t)

    ball = create_ball(space,r,m,s)
    create_boundaries(space, width, height)

    draw_options = pymunk.pygame_util.DrawOptions(window)


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(space, window, draw_options)
        space.step(dt)
        clock.tick(fps)
    pygame.quit()

if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)
