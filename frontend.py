import pygame as pg
pg.init()

#colors
red=(255,0,0)
pink=(250,100,200)
white=(255,255,255)
black=(0,0,0)
green=(0,255,0)

#variables
#w,h = pg.display.get_desktop_sizes()[0]
n,m,turn=int(input("width : ")),int(input("height : ")),0
if n<=90 and m<=47:
    w,h=20+n*21,20+m*21+5
else:
    w,h=1910,1008
bot=int(input("bot?(1/0)"))
if bot==1:
    turn=int(input("commencer a jouer?(1/0)"))

#functions
def squares(n,m):
    l=[]
    c=[]
    for xc in range(n):
        l2=[]
        c2=[]
        for yc in range(m):
            l2.append(1)
            c2.append(red)
        l.append(l2)
        c.append(c2)
    return l,c

def play(x,y,t,p):
    if x == 0 and y==0:
        print("player", str(p % 2 + 1), "lost")
    pg.time.wait(200)
    for xt in t[x:]:
        xt[y:] = [0] * len(xt[y:])
    p+=1
    return t,p

def tab(t,c,xm,ym,p,game):
    c[0][0] = green
    for x in range(len(t)):
        for y in range(len(t[x])):
            if t[x][y]==1:
                pg.draw.rect(screen,c[x][y],(10+x*21,10+y*21+5,20,20))
            else:
                pg.draw.rect(screen, black, (10 + x * 21, 10 + y * 21+5, 20, 20))
            if 10+x*21<=xm<=20+x*21+10 and 15+y*21<=ym<=10+y*21+25:
                c[x][y] = pink
                if pg.mouse.get_pressed()[0] == 1 and xm<((len(t)+1)*21)+5 and ym<((len(t[0])+1)*21)+10 and t[int(round(xm/21,0))-1][int(round((ym-5)/21,0))-1]==1:
                    t,p=play(x,y,t,p)
            else:
                c[x][y] = red
    return p,game

from random import *

def rdm(l):
    if l[0][0]!=0:
        x=randint(0,len(l)-1)
        y=randint(0,len(l[0])-1)
        if l[x][y]==0:
            return rdm(l)
        else:
            return x,y
    else:
        return 0,0



#gameloop
t,c=squares(n,m)
screen=pg.display.set_mode((w,h))
pg.display.set_caption('Chomp')
p=0
font=pg.font.Font(None,20)
clock=pg.time.Clock()

game=True
while game:
    if p % 2 == turn and bot==1:
        rx, ry = rdm(t)
        t, p = play(rx, ry, t, p)
    screen.fill(black)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            game=False
    xm, ym = pg.mouse.get_pos()
    player = font.render("p" + str(p % 2 + 1), True, white)
    screen.blit(player, (w - 15, 0))
    p,game=tab(t,c,xm,ym,p,game)
    pg.display.update()
    if t[0][0]==0:
        game=False
    clock.tick(60)