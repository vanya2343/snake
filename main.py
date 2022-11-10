import pygame
import time
import random
size = [600, 400]
color = (189, 183, 107)
color1 = (0, 183, 107)
snake_blok = 10
x1 = size[0]/2
y1 = size[1]/2
snake_list=[]
snake_len=1
foodx=round(random.randrange(0,size[0]-snake_blok)/10.0)*10.0
foody=round(random.randrange(0,size[1]-snake_blok)/10.0)*10.0
delta = [0, 0]
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Змейка за фруктами")
font_style=pygame.font.SysFont(None,50)
point_style=pygame.font.SysFont(None,20)

def key_down(event):
    global delta
    if event.key == pygame.K_LEFT and delta[0]!=snake_blok:
        delta = [-snake_blok, 0]
    if event.key == pygame.K_RIGHT and delta[0]!=-snake_blok:
        delta = [snake_blok, 0]
    if event.key == pygame.K_UP and delta[1]!=snake_blok:
        delta = [0, -snake_blok]
    if event.key == pygame.K_DOWN and delta[1]!=-snake_blok:
        delta = [0, snake_blok]
    return delta

def messag(text,color):
    mess=font_style.render(text,True,color)
    screen.blit(mess,[size[0]/2,size[1]/2])

def point(text,color):
    mess=point_style.render(text,True,color)
    screen.blit(mess,[5,5])

def print_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, color, [x[0], x[1], snake_blok, snake_blok])

def save(point):
    a=open('point.txt','r')
    max_point=0
    for line in a:
        max_point=line
    a.close()
    if point>int(max_point):
        a=open('point.txt','w')
        a.write(str(point))
        a.close()

def top_point(text,color):
    mess=point_style.render(text,True,color)
    screen.blit(mess, [400, 250])

game_over=False

while game_over==False:
    c=pygame.event.get()
    if len(c)!=0:
        event=c[0]
    if event.type == pygame.QUIT:
        pygame.quit()
    if event.type == pygame.KEYDOWN:
        delta = key_down(event)
    if x1>=size[0] or x1 < 0 or y1>=size[1] or y1 < 0:
        game_over=True
    x1+=delta[0]
    y1+=delta[1]
    screen.fill((0,0,0))
    #спавн змейки
    #pygame.draw.rect(screen, color, [x1, y1, snake_blok, snake_blok])
    #спавн еды
    pygame.draw.rect(screen,(255, 0, 0),[foodx,foody,snake_blok,snake_blok])
    snake_head=(x1,y1)
    snake_list.append(snake_head)
    if len(snake_list)>snake_len:
        del snake_list[0]
    set_snake=set(snake_list)
    if len(snake_list)>len(set_snake):
        game_over=True
    print_snake(snake_list)
    point(str(snake_len), (220, 20, 60))
    pygame.draw.rect(screen, color1, [x1, y1, snake_blok, snake_blok])
    count=0

    # for x in snake_list:
    #     if x1 == x[0] and y1 == x[1]:
    #         count+=1
    #         if count >= 2:
    #             game_over=True
    pygame.display.update()

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, size[0] - snake_blok) / 10.0) * 10.0
        foody = round(random.randrange(0, size[1] - snake_blok) / 10.0) * 10.0
        snake_len=snake_len+1

        save(snake_len)


    clock.tick(10)
messag("Поражение",(220, 20, 60))
max=open('point.txt','r')
max_point=0
for line in max:
    max_point=line
top_point("рекорд: "+max_point,(220, 20, 60))
pygame.display.update()
time.sleep(5)
pygame.quit()
quit()