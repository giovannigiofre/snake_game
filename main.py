import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

from cube import cube
from snake import snake

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        # loop per disegnare le griglie bianche
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redrawWindow(surface):
    global rows, width, s, snack, score
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        # nel caso in cui la random position sia sul serpente, viene ricalcolata
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)


#def message_box(subject, content):
#    root = tk.Tk()
 #   root.attributes("-topmost", True)
  #  root.withdraw()
   # tk.messagebox.showinfo(subject, content)
  #  try:
   #     root.destroy()
  #  except:
   #     pass

def show_message_box(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Message", message)

def main():
    global width, rows, s, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255, 0, 0), (10, 10))
    snack = cube(randomSnack(rows, s), color=(255, 0, 0))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        # velocità di gioco
        pygame.time.delay(50)
        clock.tick(10)
        s.move()

        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(255, 0, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                print('Score: ', len(s.body))
                message = 'Score: ',str(len(s.body))
                show_message_box(message)
                #message_box('You Lost!', 'Play again...')
                s.reset((10, 10))
                break

        redrawWindow(win)

    pass

main()

