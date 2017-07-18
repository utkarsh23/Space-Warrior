import pygame, random

def Main():
    pygame.init()

    displaysurface=pygame.display.set_mode((900,600))
    pygame.display.set_caption("Space Warrior")
    clock=pygame.time.Clock()

    ORANGE=(255,88,0)
    VIOLET=(111,45,168)
    YELLOW=(204,204,0)
    DARK_SLATE_GREY=(119,136,153)
    WHITE=(255,255,255)
    BLACK=(0,0,0)
    BLUE=(0,35,185)

    meteox1,meteoy1=random.randint(25,875),0
    meteox2,meteoy2=random.randint(25,875),0
    meteox3,meteoy3=random.randint(25,875),0
    meteox4,meteoy4=random.randint(25,875),0
    meteo1=0
    meteo2=0
    meteo3=0
    meteo4=0
    meteo5=0

    xcoors={}
    for i in range(32):
        xcoors["xcoor"+str(i+1)]=random.randint(2,898)
    ycoors={}
    for j in range(32):
        ycoors["ycoor"+str(j+1)]=19*(j+1)

    X,Y=355,573
    movex=0
    loops=0
    firsttime=True
    exit_it=False

    face=pygame.font.SysFont('georgia',25)

    while True:
        loops+=1
        displaysurface.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                pygame.quit()
                exit_it=True
            else:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        movex=25
                    elif event.key==pygame.K_LEFT:
                        movex=-25
                elif event.type==pygame.KEYUP:
                    movex=0
        if exit_it:
            break

        if meteoy1>600:
            meteox1,meteoy1=random.randint(10,790),0
        if meteoy2>600:
            meteox2,meteoy2=random.randint(10,790),0
        if meteoy3>600:
            meteox3,meteoy3=random.randint(10,790),0
        if meteoy4>600:
            meteox4,meteoy4=random.randint(10,790),0

        if loops>100 or not(firsttime):
            pygame.draw.circle(displaysurface,ORANGE,(meteox1,meteoy1),10)
            meteoy1+=15
        if loops>400 or not(firsttime):
            pygame.draw.circle(displaysurface,VIOLET,(meteox2,meteoy2),20)
            meteoy2+=20
        if loops>800 or not(firsttime):
            pygame.draw.circle(displaysurface,YELLOW,(meteox3,meteoy3),17)
            meteoy3+=30
        if loops>1200 or not(firsttime):
            pygame.draw.circle(displaysurface,DARK_SLATE_GREY,(meteox4,meteoy4),13)
            meteoy4+=35
            firsttime=False

        for m in range(32):
            if ycoors["ycoor"+str(m+1)]>600:
                ycoors["ycoor"+str(m+1)]=2
            pygame.draw.circle(displaysurface,WHITE,(xcoors["xcoor"+str(m+1)],ycoors["ycoor"+str(m+1)]),3)
            ycoors["ycoor"+str(m+1)]+=2

        X+=movex
        if X>1100:
            X=-195
        elif X<-195:
            X=1100
        pygame.draw.rect(displaysurface,BLUE,(X,Y,190,23))

        if meteoy1>=Y and meteox1 in range(X,X+191):
            meteox1,meteoy1=random.randint(25,875),0
            meteox2,meteoy2=random.randint(25,875),0
            meteox3,meteoy3=random.randint(25,875),0
            meteox4,meteoy4=random.randint(25,875),0

            meteo1+=1
            loops=0
            firsttime=True
            X,Y=355,573
        if meteoy2>=Y and meteox2 in range(X,X+191):
            meteox1,meteoy1=random.randint(25,875),0
            meteox2,meteoy2=random.randint(25,875),0
            meteox3,meteoy3=random.randint(25,875),0
            meteox4,meteoy4=random.randint(25,875),0

            meteo2+=1
            loops=0
            firsttime=True
            X,Y=355,573
        if meteoy3>=Y and meteox3 in range(X,X+191):
            meteox1,meteoy1=random.randint(25,875),0
            meteox2,meteoy2=random.randint(25,875),0
            meteox3,meteoy3=random.randint(25,875),0
            meteox4,meteoy4=random.randint(25,875),0

            meteo3+=1
            loops=0
            firsttime=True
            X,Y=355,573
        if meteoy4>=Y and meteox4 in range(X,X+191):
            meteox1,meteoy1=random.randint(25,875),0
            meteox2,meteoy2=random.randint(25,875),0
            meteox3,meteoy3=random.randint(25,875),0
            meteox4,meteoy4=random.randint(25,875),0

            meteo4+=1
            loops=0
            firsttime=True
            X,Y=355,573

        pygame.draw.circle(displaysurface,ORANGE,(840,20),10)
        pygame.draw.circle(displaysurface,VIOLET,(840,55),20)
        pygame.draw.circle(displaysurface,YELLOW,(840,98),17)
        pygame.draw.circle(displaysurface,DARK_SLATE_GREY,(840,134),13)

        sc1=face.render(str(meteo1),1,WHITE)
        pos1=sc1.get_rect()
        pos1.center=(875,20)
        sc2=face.render(str(meteo2),1,WHITE)
        pos2=sc2.get_rect()
        pos2.center=(875,55)
        sc3=face.render(str(meteo3),1,WHITE)
        pos3=sc3.get_rect()
        pos3.center=(875,98)
        sc4=face.render(str(meteo4),1,WHITE)
        pos4=sc4.get_rect()
        pos4.center=(875,134)

        displaysurface.blit(sc1,pos1)
        displaysurface.blit(sc2,pos2)
        displaysurface.blit(sc3,pos3)
        displaysurface.blit(sc4,pos4)
            
        clock.tick(30)
        pygame.display.update()
Main()
