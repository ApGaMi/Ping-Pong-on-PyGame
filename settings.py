from pygame import *
init()

WIDTH = 700
HEIGHT = 500
FPS = 60
x = 350
y = 250
speed = 5
p_speed = 8
radius = 25
dx = 1
dy = -1
h = 140
w = 20
p1x = 0
p1y = HEIGHT//2 - h//2
p2x = WIDTH - w
p2y = HEIGHT//2 - h//2
Arial = font.SysFont('arial', 150)
lose_f = font.SysFont('arial', 100)
lose_t = lose_f.render("Lose!", True, (200, 200, 100))