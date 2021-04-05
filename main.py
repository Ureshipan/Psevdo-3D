import math
import pygame
from random import randint
import pickle
import os
import sys
from data import pygame_textinput
import importlib

lines = [[[-20, 300, 20], [20, 300, 20], [-20, 300, 20], [20, 300, 20], 0, 0, 0, 0, (255, 0, 0)],
              [[-20, 300, -20],[20, 300, -20], [-20, 300, -20], [20, 300, -20], 0, 0, 0, 0, (255, 0, 0)],
              [[-20, 300, 20], [-20, 300, -20], [-20, 300, 20], [-20, 300, -20], 0, 0, 0, 0, (255, 0, 0)],
              [[20, 300, 20], [20, 300, -20], [20, 300, 20], [20, 300, -20], 0, 0, 0, 0, (255, 0, 0)],
              [[-20, 340, 20], [20, 340, 20], [-20, 340, 20], [20, 340, 20], 0, 0, 0, 0, (255, 0, 0)],
              [[-20, 340, -20], [20, 340, -20], [-20, 340, -20], [20, 340, -20], 0, 0, 0, 0, (255, 0, 0)],
              [[-20, 340, 20], [-20, 340, -20], [-20, 340, 20], [-20, 340, -20], 0, 0, 0, 0, (255, 0, 0)],
              [[20, 340, 20], [20, 340, -20], [20, 340, 20], [20, 340, -20], 0, 0, 0, 0, (255, 0, 0)],
              [[-20, 300, 20], [-20, 340, 20], [-20, 300, 20], [-20, 340, 20], 0, 0, 0, 0, (255, 0, 0)],
              [[20, 300, 20], [20, 340, 20], [20, 300, 20], [20, 340, 20], 0, 0, 0, 0, (255, 0, 0)],
              [[-20, 300, -20], [-20, 340, -20], [-20, 300, -20], [-20, 340, -20], 0, 0, 0, 0, (255, 0, 0)],
              [[20, 300, -20], [20, 340, -20], [20, 300, -20], [20, 340, -20], 0, 0, 0, 0, (255, 0, 0)]]


menu_lines = [[[-20, 300, 20], [20, 300, 20], [-20, 300, 20], [20, 300, 20], 0, 0, 0, 0, (255, 0, 0)],
              [[-20, 300, -20],[20, 300, -20], [-20, 300, -20], [20, 300, -20], 0, 0, 0, 0, (255, 0, 0)],
              [[-20, 300, 20], [-20, 300, -20], [-20, 300, 20], [-20, 300, -20], 0, 0, 0, 0, (255, 0, 0)],
              [[20, 300, 20], [20, 300, -20], [20, 300, 20], [20, 300, -20], 0, 0, 0, 0, (255, 0, 0)],
              [[-20, 340, 20], [20, 340, 20], [-20, 340, 20], [20, 340, 20], 0, 0, 0, 0, (255, 0, 0)],
              [[-20, 340, -20], [20, 340, -20], [-20, 340, -20], [20, 340, -20], 0, 0, 0, 0, (255, 0, 0)],
              [[-20, 340, 20], [-20, 340, -20], [-20, 340, 20], [-20, 340, -20], 0, 0, 0, 0, (255, 0, 0)],
              [[20, 340, 20], [20, 340, -20], [20, 340, 20], [20, 340, -20], 0, 0, 0, 0, (255, 0, 0)],
              [[-20, 300, 20], [-20, 340, 20], [-20, 300, 20], [-20, 340, 20], 0, 0, 0, 0, (255, 0, 0)],
              [[20, 300, 20], [20, 340, 20], [20, 300, 20], [20, 340, 20], 0, 0, 0, 0, (255, 0, 0)],
              [[-20, 300, -20], [-20, 340, -20], [-20, 300, -20], [-20, 340, -20], 0, 0, 0, 0, (255, 0, 0)],
              [[20, 300, -20], [20, 340, -20], [20, 300, -20], [20, 340, -20], 0, 0, 0, 0, (255, 0, 0)]]
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Linear Engine')
running = True
turn_grad = math.radians(0.4)
hor = 1000
vertical_point = 300
vertical_turn = 0.0
god_mod = True
points = 0
new_points = []
modificated = False
mod = None

pygame.mixer.init()


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удалось загрузить изображение:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


def terminate():
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()


def start_screen():
    fon = load_image('images/Menu.jpg')
    buttons = load_image('images/buttons0.png')
    screen.blit(fon, (0, 0))
    screen.blit(buttons, (0, 0))
    d = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 290 <= event.pos[0] <= 510 and 430 <= event.pos[1] <= 510:
                    enter_name()
                elif 50 <= event.pos[0] <= 270 and 430 <= event.pos[1] <= 510:
                    main('')
                elif 530 <= event.pos[0] <= 750 and 430 <= event.pos[1] <= 510:
                    pass
        for line in menu_lines:
            line[0][1] -= 320
            line[1][1] -= 320
            line[2][1] -= 320
            line[3][1] -= 320
        turn_right(menu_lines)
        #if d:
            #turn_down(menu_lines)
            #d = False
        #else:
            #d = True
        for line in menu_lines:
            line[0][1] += 320
            line[1][1] += 320
            line[2][1] += 320
            line[3][1] += 320
        screen.blit(fon, (0, 0))
        render(menu_lines, 1800, 8, False)
        screen.blit(buttons, (0, 0))
        pygame.display.flip()
        clock.tick(60)


def enter_name():
    fon = load_image('images/Input.jpg')
    textinput = pygame_textinput.TextInput()
    while True:
        screen.blit(fon, (0, 0))

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    filename = textinput.get_text()
                    main(filename)
        textinput.update(events)
        screen.blit(textinput.get_surface(), (50, 230))

        pygame.display.flip()
        clock.tick(30)


def save_as(filename):
    global lines
    fon = load_image('images/Save_map.jpg')
    textinput = pygame_textinput.TextInput()
    textinput.input_string = filename
    while True:
        screen.blit(fon, (0, 0))

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    filename = textinput.get_text()
                    map_file = open('data/maps/' + filename + '.coords_map', 'wb')
                    pickle.dump(lines, map_file)
                    map_file.close()
                    main(filename)

        textinput.update(events)
        screen.blit(textinput.get_surface(), (50, 230))

        pygame.display.flip()
        clock.tick(30)


def render(lines, hor, width, need_circle):
    global mod
    try:
        mod.render(screen, lines, hor, vertical_point)
    except:
        for line in lines:
            if 1000 > line[0][1] > 0 and 1000 > line[1][1] > 0:
                r = int(line[-1][0] * (255 / ((line[0][1] + line[1][1]) / 2)))
                if r > 255:
                    r = 255

                g = int(line[-1][1] * (255 / ((line[0][1] + line[1][1]) / 2)))
                if g > 255:
                    g = 255

                b = int(line[-1][2] * (255 / ((line[0][1] + line[1][1]) / 2)))
                if b > 255:
                    b = 255
                pygame.draw.line(screen, pygame.Color(r, g, b),
                                 [line[0][0] * (hor / line[0][1]) + 400,
                                  line[0][2] * (hor / line[0][1]) + vertical_point],
                                 [line[1][0] * (hor / line[1][1]) + 400,
                                  line[1][2] * (hor / line[1][1]) + vertical_point],
                                 width)
                if need_circle:
                    for tr in lines[:lines.index(line)]:
                        if 1000 > tr[0][1] > 0 and 1000 > tr[1][1] > 0:
                            x, y = line_intersection(
                                ((line[0][0] * (hor / line[0][1]) + 400, line[0][2] * (hor / line[0][1]) +
                                  vertical_point),
                                 (line[1][0] * (hor / line[1][1]) + 400, line[1][2] * (hor / line[1][1]) +
                                  vertical_point)),
                                ((tr[0][0] * (hor / tr[0][1]) + 400, tr[0][2] * (hor / tr[0][1]) +
                                  vertical_point),
                                 (tr[1][0] * (hor / tr[1][1]) + 400, tr[1][2] * (hor / tr[1][1]) +
                                  vertical_point)))
                            pygame.draw.circle(screen, 'black', (x, y), 5, 0)
                    for tr in lines[lines.index(line) + 1:]:
                        if 1000 > tr[0][1] > 0 and 1000 > tr[1][1] > 0:
                            x, y = line_intersection(
                                ((line[0][0] * (hor / line[0][1]) + 400, line[0][2] * (hor / line[0][1]) +
                                  vertical_point),
                                 (line[1][0] * (hor / line[1][1]) + 400, line[1][2] * (hor / line[1][1]) +
                                  vertical_point)),
                                ((tr[0][0] * (hor / tr[0][1]) + 400, tr[0][2] * (hor / tr[0][1]) +
                                  vertical_point),
                                 (tr[1][0] * (hor / tr[1][1]) + 400, tr[1][2] * (hor / tr[1][1]) +
                                  vertical_point)))
                            pygame.draw.circle(screen, 'black', (x, y), 5, 0)
        if len(new_points) == 1 and new_points[0][1] > 0 and god_mod:
            g = int(255 * (255 / new_points[0][1]))
            if g > 255:
                g = 255
            pygame.draw.circle(screen, pygame.Color(0, g, 0),
                               (new_points[0][0] * (hor / new_points[0][1]) + 400, new_points[0][2] *
                                (hor / new_points[0][1]) + vertical_point),
                               1 * (hor / new_points[0][1]), 0)


def move_forward(lines):
    global new_points
    if len(new_points) == 1:
        new_points[0][1] -= 1
    for i in range(len(lines)):
        if lines[i][2][0] != 0:
            ug00 = math.atan(lines[i][2][1] / lines[i][2][0])
        else:
            ug00 = 0

        if lines[i][3][0] != 0:
            ug01 = math.atan(lines[i][3][1] / lines[i][3][0])
        else:
            ug01 = 0

        lines[i][0][1] -= 1
        lines[i][1][1] -= 1
        lines[i][2][1] -= 1
        lines[i][3][1] -= 1
        if lines[i][2][0] != 0:
            ug10 = math.atan(lines[i][2][1] / lines[i][2][0])
        else:
            ug10 = 0

        if lines[i][3][0] != 0:
            ug11 = math.atan(lines[i][3][1] / lines[i][3][0])
        else:
            ug11 = 0

        lines[i][4] += ug00 - ug01
        lines[i][6] += ug10 - ug11
        #print(ug10)
        #print(ug11)

        #print(lines[0])


def move_back(lines):
    global new_points
    if len(new_points) == 1:
        new_points[0][1] += 1
    for i in range(len(lines)):
        lines[i][0][1] += 1
        lines[i][1][1] += 1
        lines[i][2][1] += 1
        lines[i][3][1] += 1


def move_right(lines):
    global new_points
    if len(new_points) == 1:
        new_points[0][0] -= 1
    for i in range(len(lines)):
        lines[i][0][0] -= 1
        lines[i][1][0] -= 1
        lines[i][2][0] -= 1
        lines[i][3][0] -= 1


def move_left(lines):
    global new_points
    if len(new_points) == 1:
        new_points[0][0] += 1
    for i in range(len(lines)):
        lines[i][0][0] += 1
        lines[i][1][0] += 1
        lines[i][2][0] += 1
        lines[i][3][0] += 1


def move_up(lines):
    global new_points
    if god_mod:
        if len(new_points) == 1:
            new_points[0][2] += 1
        for i in range(len(lines)):
            lines[i][0][2] += 1
            lines[i][1][2] += 1


def move_down(lines):
    global new_points
    if god_mod:
        if len(new_points) == 1:
            new_points[0][2] -= 1
        for i in range(len(lines)):
            lines[i][0][2] -= 1
            lines[i][1][2] -= 1


def turn_right(lines):
    global new_points
    #if len(new_points) == 1:
        #new_points[0][0] = new_points[0][0] * cos - new_points[0][1] * sin
        #new_points[0][1] = new_points[0][0] * sin + new_points[0][1] * cos
    for i in range(len(lines)):
        lines[i][4] += turn_grad
        if lines[i][4] > math.pi * 2:
            lines[i][4] -= math.pi * 2
        if lines[i][4] < 0:
            lines[i][4] += math.pi * 2
        lines[i][6] += turn_grad
        if lines[i][6] > math.pi * 2:
            lines[i][6] -= math.pi * 2
        if lines[i][6] < 0:
            lines[i][6] += math.pi * 2
        lines[i][0][0] = lines[i][2][0] * math.cos(lines[i][4]) - lines[i][2][1] * math.sin(lines[i][4])
        lines[i][0][1] = lines[i][2][0] * math.sin(lines[i][4]) + lines[i][2][1] * math.cos(lines[i][4])
        lines[i][1][0] = lines[i][3][0] * math.cos(lines[i][6]) - lines[i][3][1] * math.sin(lines[i][6])
        lines[i][1][1] = lines[i][3][0] * math.sin(lines[i][6]) + lines[i][3][1] * math.cos(lines[i][6])



def turn_left(lines):
    global new_points
    #if len(new_points) == 1:
        #new_points[0][0] = new_points[0][0] * math.cos(math.radians(-turn_grad)) - new_points[0][1] * math.sin(
            #math.radians(-turn_grad))
       # new_points[0][1] = new_points[0][0] * math.sin(math.radians(-turn_grad)) + new_points[0][1] * math.cos(
           # math.radians(-turn_grad))
    for i in range(len(lines)):
        lines[i][4] -= turn_grad
        if lines[i][4] > math.pi * 2:
            lines[i][4] -= math.pi * 2
        if lines[i][4] < 0:
            lines[i][4] += math.pi * 2
        lines[i][6] -= turn_grad
        if lines[i][6] > math.pi * 2:
            lines[i][6] -= math.pi * 2
        if lines[i][6] < 0:
            lines[i][6] += math.pi * 2
        lines[i][0][0] = lines[i][2][0] * math.cos(lines[i][4]) - lines[i][2][1] * math.sin(lines[i][4])
        lines[i][0][1] = lines[i][2][0] * math.sin(lines[i][4]) + lines[i][2][1] * math.cos(lines[i][4])
        lines[i][1][0] = lines[i][3][0] * math.cos(lines[i][6]) - lines[i][3][1] * math.sin(lines[i][6])
        lines[i][1][1] = lines[i][3][0] * math.sin(lines[i][6]) + lines[i][3][1] * math.cos(lines[i][6])



def turn_up(lines):
    global vertical_turn, new_points

    if god_mod and vertical_turn <= 85:
        if len(new_points) == 1:
            new_points[0][1] = new_points[0][1] * math.cos(math.radians(turn_grad)) - new_points[0][2] * math.sin(
                math.radians(turn_grad))
            new_points[0][2] = new_points[0][1] * math.sin(math.radians(turn_grad)) + new_points[0][2] * math.cos(
                math.radians(turn_grad))
        for i in range(len(lines)):
            lines[i][0][1] = lines[i][0][1] * math.cos(math.radians(turn_grad)) - lines[i][0][2] * math.sin(
                math.radians(turn_grad))
            lines[i][0][2] = lines[i][0][1] * math.sin(math.radians(turn_grad)) + lines[i][0][2] * math.cos(
                math.radians(turn_grad))
            lines[i][1][1] = lines[i][1][1] * math.cos(math.radians(turn_grad)) - lines[i][1][2] * math.sin(
                math.radians(turn_grad))
            lines[i][1][2] = lines[i][1][1] * math.sin(math.radians(turn_grad)) + lines[i][1][2] * math.cos(
                math.radians(turn_grad))
        vertical_turn += turn_grad


def turn_down(lines):
    global vertical_turn, new_points

    if god_mod and vertical_turn <= 85:
        if len(new_points) == 1:
            new_points[0][1] = new_points[0][1] * math.cos(math.radians(-turn_grad)) - new_points[0][2] * math.sin(
                math.radians(-turn_grad))
            new_points[0][2] = new_points[0][1] * math.sin(math.radians(-turn_grad)) + new_points[0][2] * math.cos(
                math.radians(-turn_grad))
        for i in range(len(lines)):
            lines[i][0][1] = lines[i][0][1] * math.cos(math.radians(-turn_grad)) - lines[i][0][2] * math.sin(
                math.radians(-turn_grad))
            lines[i][0][2] = lines[i][0][1] * math.sin(math.radians(-turn_grad)) + lines[i][0][2] * math.cos(
                math.radians(-turn_grad))
            lines[i][1][1] = lines[i][1][1] * math.cos(math.radians(-turn_grad)) - lines[i][1][2] * math.sin(
                math.radians(-turn_grad))
            lines[i][1][2] = lines[i][1][1] * math.sin(math.radians(-turn_grad)) + lines[i][1][2] * math.cos(
                math.radians(-turn_grad))
        vertical_turn -= turn_grad


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])  # Typo was here

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return 0, 0

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    if min(line1[0][0], line1[1][0]) <= x <= max(line1[0][0], line1[1][0]):
        if min(line1[0][1], line1[1][1]) <= y <= max(line1[0][1], line1[1][1]):
            if min(line2[0][0], line2[1][0]) <= x <= max(line2[0][0], line2[1][0]):
                if min(line2[0][1], line2[1][1]) <= y <= max(line2[0][1], line2[1][1]):
                    return x, y
                else:
                    return 0, 0
            else:
                return 0, 0
        else:
            return 0, 0
    else:
        return 0, 0


def add_point():
    global lines, points, new_points

    if len(new_points) == 0:
        new_points.append([0, 50, 0])
    else:
        lines.append(
            [new_points[0], [0, 50, 0], (randint(0, 255), randint(0, 255), randint(0, 255))])
        new_points = []


def main(filename):
    global lines, god_mod, modificated, mod
    if filename != '':
        if '/' not in filename:
            modificated = False
            try:
                map_file = open('data/maps/' + filename + '.coords_map', 'rb')
                lines = pickle.load(map_file)
                map_file.close()
            except FileNotFoundError:
                map_file = open('data/maps/' + filename + '.coords_map', 'wb')
                pickle.dump(lines, map_file)
                map_file.close()
        else:
            modificated = True
            map_file = open('data/maps/' + filename + 'map.coords_map', 'rb')
            lines = pickle.load(map_file)
            map_file.close()
            filename = filename[:-1] + '.'
            mod = importlib.import_module('data.maps.' + filename + 'mod')
    else:
        i = 0
        x = True
        while x:
            try:
                map_file = open('data/maps/new_map_' + str(i) + '.coords_map', 'rb')
                map_file.close()
                i += 1

            except FileNotFoundError:
                map_file = open('data/maps/new_map_' + str(i) + '.coords_map', 'wb')
                pickle.dump(lines, map_file)
                map_file.close()
                filename = 'new_map_' + str(i)
                x = False

    run = True
    while run:
        screen.fill(pygame.Color('black'))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                add_point()
        if pygame.key.get_pressed()[pygame.K_w]:
            move_forward(lines)
        if pygame.key.get_pressed()[pygame.K_s]:
            move_back(lines)
        if pygame.key.get_pressed()[pygame.K_a]:
            move_left(lines)
        if pygame.key.get_pressed()[pygame.K_d]:
            move_right(lines)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            turn_right(lines)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            turn_left(lines)
        if pygame.key.get_pressed()[pygame.K_UP]:
            turn_up(lines)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            turn_down(lines)
        if pygame.key.get_pressed()[pygame.K_LSHIFT]:
            move_up(lines)
        if pygame.key.get_pressed()[pygame.K_LCTRL]:
            move_down(lines)
        if pygame.key.get_pressed()[pygame.K_m]:
            save_as(filename)
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            test_map_file = open('data/maps/' + filename + '.coords_map', 'wb')
            pickle.dump(lines, test_map_file)
            test_map_file.close()
            start_screen()

        render(lines, hor, 4, True)

        pygame.display.flip()
        clock.tick(30)
    test_map_file = open('data/maps/' + filename + '.coords_map', 'wb')
    pickle.dump(lines, test_map_file)
    test_map_file.close()
    terminate()


track = randint(0, 3)
music = 'data/music/' + str(track) + '.mp3'
pygame.mixer.music.load(music)
#pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
start_screen()
