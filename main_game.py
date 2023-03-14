from pygame import *
from settings import *
from menu import Menu
import sys

init()

kf = -1

game = False



screen = display.set_mode((WIDTH, HEIGHT), RESIZABLE)
display.set_caption("Ping-Pong")
clock = time.Clock()  

menu = Menu()
menu.append_option('Play', lambda: print('Play'))
menu.append_option('Exit', quit)
lose = False

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()
    keys = key.get_pressed()        
    if not lose:
        if game == False:
            screen.fill((0, 0 ,0))
            menu.draw(screen, 200, 100, 180)
            if keys[K_w]:
                menu.switch(-1)
                kf = -1
            elif keys[K_s]:
                menu.switch(1)
                kf = 1
        if keys[K_SPACE] and kf == -1:
            game = True
        elif keys[K_SPACE] and kf == 1:
            quit()
            sys.exit()
        if game == True:
            screen.fill((0, 0, 0))
            ball = draw.circle(screen, (255, 180, 180), (x, y), radius)
            player1 = draw.rect(screen, (255, 255, 255), (p1x, p1y, w, h))
            player2 = draw.rect(screen, (255, 255, 255), (p2x, p2y, w, h))
            x += speed * dx
            y += speed * dy
            if y < radius or y > HEIGHT - radius:
                dy = - dy
            if ball.colliderect(player2) and dx > 0:
                dx = - dx
            if ball.colliderect(player1) and dx < 0:
                dx = - dx
            if keys[K_w] and p1y >= 0:
                p1y -= p_speed
            if keys[K_s] and p1y <= HEIGHT - h:
                p1y += p_speed
            if keys[K_UP] and p2y >= 0:
                p2y -= p_speed
            if keys[K_DOWN] and p2y <= HEIGHT - h:
                p2y += p_speed
            if x > WIDTH + radius//2 or x < 0 - radius:
                lose = True
                game = False
                screen.blit(lose_t, (220, 30))
    elif lose:
        lose_t.blit(screen, (180, 180))
  
        

    display.update()
    clock.tick(FPS)



