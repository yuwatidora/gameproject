####--------------------MUMMY FROGGER----------------------------------
##Description:
##
##Frogger, but you have to find three artifacts in the coffins and
##take it to the portal in the shape of an eye at the end.
##Along the way you have to avoid daggers and mummies and ride on stones.
##
##You will also have to shoot fireballs along the way to pass.
##
##press 'a' to shoot to the left
##press 's' to shoot to the right
##press 'q' to shoot to the front
##press 'z' to shoot backwards
####----------------------------------------------------------------------

import sys

import pygame

import time

import random

def start_screen(main_surface):
    done= False
    start_image = pygame.image.load("start.png").convert()

    start = start_image.get_rect()

    start.x = 0

    start.y = 0

    
    
    while True:
        
        main_surface.blit(start_image,start)

        pygame.display.flip()
        for event in pygame.event.get():
            if event .type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True
                    return
        
            

    

def playlevel(level,main_surface):

   

    hitartifact = -1

    mummyxposchange = [0,0,0,0,0,0,0,0]
    
    n=[0,0,0,0,0,1,1,1]

    coffin_choose = random.sample(n,8)
    mummyx_change1=-6 - level
    mummyx_change2=5 + level
    mummyx_change3=-5 - level
    mummyx_change4=5 + level
    mummyx_change5=5 + level
    mummyx_change6=-5 - level
    mummyx_change7=-5 - level
    mummyx_change8=-5 - level

    mummyx_change=[mummyx_change1,mummyx_change2,mummyx_change3,mummyx_change4,
                    mummyx_change5,mummyx_change6,mummyx_change7,mummyx_change8]
    
    artifactx_pos = [280,130,330,180,330,30,430,440]

    artifacty_pos = [450,400,350,300,250,450,400,250]

    carry_artifact =[]

    life = 3

    score = 0

    daggersd = 8

    daggersd1 = 5

    daggersd2 = 10

    stonesd = 5

    stonesd1 = 4

    daggersd += level

    daggersd1 += level

    daggersd2 += level

    stonesd += level

    stonesd1 += level

    
    

        

    #COLORs
    BLACK = (0,0,0)

    WHITE = (255,255,255)

    GREEN = (0,255,0)

    RED   = (255,0,0)

    BLUE = (43,143,230)

    LIGHTBLUE = (175,217,254)

    BROWN = (185,117,47)


    #Colors of blocks-----------------

    #Color of stones
    colorstone =BLUE

    #Color of daggers
    colordagger= RED
    

    #Color of coffins
    colorcoffin = BROWN

    
    #Color of mummys
    colormummy = WHITE


    #Color of frog
    colorfrog = GREEN

    #Color of artifact
    colorartifact = LIGHTBLUE

    
    #Variables-------------------------

    #background
    background_image = pygame.image.load("background.png").convert()

    background = background_image.get_rect()

    background.x = 0

    background.y = 0

    #Sound
    mummy_sound = pygame.mixer.Sound("zombie.wav")
    
    
    #frog
    #frog = pygame.rect.Rect(250,680,20,20)
    frog_image =pygame.image.load("frog.png").convert()

    frog = frog_image.get_rect()

    frog.x = 250

    frog.y = 680

    frog_image.set_colorkey(BLACK)

    
    
    #artifact
    #artifact = pygame.rect.Rect(600,250,10,10)

    egg_image = pygame.image.load("egg.jpg").convert()

    artifact = egg_image.get_rect()

    artifact.x = 600

    artifact.y = 250   
    
    #artifact1 = pygame.rect.Rect(600,250,10,10)
    wings_image = pygame.image.load("wings.png").convert()

    artifact1 = wings_image.get_rect()

    artifact1.x = 600

    artifact1.y = 250
    
    #artifact2 = pygame.rect.Rect(600,250,10,10)
    lamp_image = pygame.image.load("lamp.jpg").convert()

    artifact2 = lamp_image.get_rect()

    artifact2.x = 600

    artifact2.y = 250    
    #artifact3 = pygame.rect.Rect(600,250,10,10)
    egg_image = pygame.image.load("egg.jpg").convert()

    artifact3 = egg_image.get_rect()

    artifact3.x = 600

    artifact3.y = 250    
    #artifact4 = pygame.rect.Rect(600,250,10,10)
    wings_image = pygame.image.load("wings.png").convert()

    artifact4 = wings_image.get_rect()

    artifact4.x = 600

    artifact4.y = 250
    
    #artifact5 = pygame.rect.Rect(600,250,10,10)
    lamp_image = pygame.image.load("lamp.jpg").convert()

    artifact5 = lamp_image.get_rect()

    artifact5.x = 600

    artifact5.y = 250    
    #artifact6 = pygame.rect.Rect(600,250,10,10)
    egg_image = pygame.image.load("egg.jpg").convert()

    artifact6 = egg_image.get_rect()

    artifact6.x = 600

    artifact6.y = 250
    #artifact7 = pygame.rect.Rect(600,250,10,10)
    wings_image = pygame.image.load("wings.png").convert()

    artifact7 = wings_image.get_rect()

    artifact7.x = 600

    artifact7.y = 250

    #fire

    fire_image = pygame.image.load("fairy.png").convert()

    fire = egg_image.get_rect()

    fire.x = frog.x

    fire.y = frog.y

    fire_state = "ready"

    fire_image.set_colorkey(BLACK)
    
    #daggers
    #dagger = pygame.rect.Rect(0,640,70,20)
    dagger_image = pygame.image.load("dagger.jpg").convert()

    dagger = dagger_image.get_rect()

    dagger.x = 0

    dagger.y = 640

    dagger_image.set_colorkey(BLACK)   
    #dagger1 = pygame.rect.Rect(200,640,70,20)
    dagger_image = pygame.image.load("dagger.jpg").convert()

    dagger1 = dagger_image.get_rect()

    dagger1.x = 200

    dagger1.y = 640

    dagger_image.set_colorkey(BLACK)    
    #dagger2 = pygame.rect.Rect(400,620,70,20)
    dagger_image = pygame.image.load("dagger.jpg").convert()

    dagger2 = dagger_image.get_rect()

    dagger2.x = 400

    dagger2.y = 640

    dagger_image.set_colorkey(BLACK)    
    #dagger3 = pygame.rect.Rect(350,600,70,20)
    dagger_image1 = pygame.image.load("dagger2.jpg").convert()

    dagger3 = dagger_image.get_rect()

    dagger3.x = 350

    dagger3.y = 610

    dagger_image.set_colorkey(BLACK)    
    #dagger4 = pygame.rect.Rect(400,580,70,20)
    dagger_image = pygame.image.load("dagger.jpg").convert()

    dagger4 = dagger_image.get_rect()

    dagger4.x = 400

    dagger4.y = 580

    dagger_image.set_colorkey(BLACK)    
    #dagger5 = pygame.rect.Rect(250,580,70,20)
    dagger_image = pygame.image.load("dagger.jpg").convert()

    dagger5 = dagger_image.get_rect()

    dagger5.x = 250

    dagger5.y = 580

    dagger_image.set_colorkey(BLACK)    

    #stones---------------------------------------
    
    #stone=pygame.rect.Rect(0,60,40,40)
    stone_image =pygame.image.load("stone.png").convert()

    stone = stone_image.get_rect()

    stone.x = 0

    stone.y = 40

    stone_image.set_colorkey(BLACK)
    #stone1=pygame.rect.Rect(100,60,40,40)
    stone_image =pygame.image.load("stone.png").convert()

    stone1 = stone_image.get_rect()

    stone1.x = 100

    stone1.y = 40

    stone_image.set_colorkey(BLACK)
    
    #stone2=pygame.rect.Rect(450,60,40,40)
    stone_image =pygame.image.load("stone.png").convert()

    stone2 = stone_image.get_rect()

    stone2.x = 450

    stone2.y = 40

    stone_image.set_colorkey(BLACK)    
    #stone3=pygame.rect.Rect(300,100,40,40)
    stone_image =pygame.image.load("stone.png").convert()

    stone3 = stone_image.get_rect()

    stone3.x = 300

    stone3.y = 85

    stone_image.set_colorkey(BLACK)

    #stone4=pygame.rect.Rect(450,100,40,40)
    stone_image =pygame.image.load("stone.png").convert()

    stone4 = stone_image.get_rect()

    stone4.x = 450

    stone4.y = 85

    stone_image.set_colorkey(BLACK)
    #stone5=pygame.rect.Rect(100,100,40,40)
    stone_image =pygame.image.load("stone.png").convert()

    stone5 = stone_image.get_rect()

    stone5.x = 100

    stone5.y = 85

    stone_image.set_colorkey(BLACK)

    
    #mummys--------------------------------------
##    mummy = pygame.rect.Rect(480,450,20,50)
    mummy_image1 = pygame.image.load("mummy3.png").convert()

    mummy = mummy_image1.get_rect()

    mummy.x = 480

    mummy.y = 450



    mummy_image1.set_colorkey(BLACK)    
##    mummy1 = pygame.rect.Rect(0,400,20,50)
    mummy_image = pygame.image.load("mummy2.png").convert()

    mummy1 = mummy_image.get_rect()

    mummy1.x = 0

    mummy1.y = 400



##    mummy_image.set_colorkey(BLACK)    
##    mummy2 = pygame.rect.Rect(480,350,20,50)
    mummy_image1 = pygame.image.load("mummy3.png").convert()

    mummy2 = mummy_image1.get_rect()

    mummy2.x = 480

    mummy2.y = 350



##    mummy_image.set_colorkey(BLACK)
##    mummy3 = pygame.rect.Rect(0,300,20,50)
    mummy_image1 = pygame.image.load("mummy2.png").convert()

    mummy3 = mummy_image.get_rect()

    mummy3.x = 0

    mummy3.y = 300



##    mummy_image.set_colorkey(BLACK)    
##    mummy4 = pygame.rect.Rect(0,250,20,50)
    mummy_image = pygame.image.load("mummy2.png").convert()

    mummy4 = mummy_image.get_rect()

    mummy4.x = 0

    mummy4.y = 250



##    mummy_image.set_colorkey(BLACK)    
##    mummy5 = pygame.rect.Rect(480,450,20,50)
    mummy_image1 = pygame.image.load("mummy3.png").convert()

    mummy5 = mummy_image1.get_rect()

    mummy5.x = 480

    mummy5.y = 450



##    mummy_image.set_colorkey(BLACK)
##    mummy6 = pygame.rect.Rect(480,400,20,50)
    mummy_image1 = pygame.image.load("mummy3.png").convert()

    mummy6 = mummy_image1.get_rect()

    mummy6.x = 480

    mummy6.y = 400



##    mummy_image.set_colorkey(BLACK)
##    mummy7 = pygame.rect.Rect(480,250,20,50)
    mummy_image1 = pygame.image.load("mummy3.png").convert()

    mummy7 = mummy_image1.get_rect()

    mummy7.x = 480

    mummy7.y = 250
    

    #coffins-----------------------------------------------------
##    coffin = pygame.rect.Rect(250,450,30,50)
    coffin_image = pygame.image.load("coffin.jpg").convert()

    coffin = coffin_image.get_rect()

    coffin.x = 250

    coffin.y = 450



    coffin_image.set_colorkey(WHITE)    
##    coffin1 = pygame.rect.Rect(100 ,400,30,50)
    coffin_image = pygame.image.load("coffin.jpg").convert()

    coffin1 = coffin_image.get_rect()

    coffin1.x = 100

    coffin1.y = 400



    coffin_image.set_colorkey(WHITE)    
##    coffin2 = pygame.rect.Rect(300 ,350,30,50)
    coffin_image = pygame.image.load("coffin.jpg").convert()

    coffin2 = coffin_image.get_rect()

    coffin2.x = 300

    coffin2.y = 350



    coffin_image.set_colorkey(WHITE)    
##    coffin3 = pygame.rect.Rect(150 ,300,30,50)
    coffin_image = pygame.image.load("coffin.jpg").convert()

    coffin3 = coffin_image.get_rect()

    coffin3.x = 200

    coffin3.y = 300



    coffin_image.set_colorkey(WHITE)    
##    coffin4 = pygame.rect.Rect(300,250,30,50)
    coffin_image = pygame.image.load("coffin.jpg").convert()

    coffin4 = coffin_image.get_rect()

    coffin4.x = 300

    coffin4.y = 250

    coffin_image.set_colorkey(WHITE)
##    coffin5 = pygame.rect.Rect(0,450,30,50)
    coffin_image = pygame.image.load("coffin.jpg").convert()

    coffin5 = coffin_image.get_rect()

    coffin5.x = 0

    coffin5.y = 450

    coffin_image.set_colorkey(WHITE)
##    coffin6 = pygame.rect.Rect(400,400,30,50)
    coffin_image = pygame.image.load("coffin.jpg").convert()

    coffin6 = coffin_image.get_rect()

    coffin6.x = 400

    coffin6.y = 400



    coffin_image.set_colorkey(WHITE)   
##    coffin7 = pygame.rect.Rect(450,250,30,50)
    coffin_image = pygame.image.load("coffin.jpg").convert()

    coffin7 = coffin_image.get_rect()

    coffin7.x = 450

    coffin7.y = 250



    coffin_image.set_colorkey(WHITE)

    #Lives
    life1_image =pygame.image.load("frog.png").convert()

    life1= life1_image.get_rect()

    life1.x = 400

    life1.y = 10



    life2_image =pygame.image.load("frog.png").convert()

    life2= life2_image.get_rect()

    life2.x = 425

    life2.y = 10



    life3_image =pygame.image.load("frog.png").convert()

    life3= life3_image.get_rect()

    life3.x = 450

    life3.y = 10

    #Goal
    
    goal_image = pygame.image.load("goal.png").convert()

    goal= goal_image.get_rect()

    goal.x = 230

    goal.y = 0

    layer_image = pygame.image.load("layer.jpg").convert()

    layer = dagger_image.get_rect()

    layer.x = 0

    layer.y = 500

    #fireball

    fireball_image =pygame.image.load("fireball.png").convert()

    fireball = fireball_image.get_rect()

    fireball.x = 0

    fireball.y = 180

    fireball_image.set_colorkey(BLACK)





    fireball1_image =pygame.image.load("fireball.png").convert()

    fireball1 = fireball1_image.get_rect()

    fireball1.x = 100

    fireball1.y = 180

    fireball1_image.set_colorkey(BLACK)

    

    fireball2_image =pygame.image.load("fireball.png").convert()

    fireball2 = fireball2_image.get_rect()

    fireball2.x = 200

    fireball2.y = 180

    fireball2_image.set_colorkey(BLACK)



    fireball3_image =pygame.image.load("fireball.png").convert()

    fireball3 = fireball3_image.get_rect()

    fireball3.x = 300

    fireball3.y = 180

    fireball3_image.set_colorkey(BLACK)



    fireball4_image =pygame.image.load("fireball.png").convert()

    fireball4 = fireball4_image.get_rect()
    fireball4.x = 400 
    fireball4.y = 180
    fireball4_image.set_colorkey(BLACK)

   

    #Lists-------------------------------

    #-stone lists-
    stonelist=[stone, stone1, stone2]

    stone1list=[stone3, stone4, stone5]

    #-dagger lists-
    daggerlist=[dagger,dagger1, dagger2]

    dagger1list=[dagger3]

    dagger2list=[dagger4, dagger5]

    #artifact list-

    artifactlist = [artifact,artifact1,artifact2,artifact3,artifact4,artifact5,artifact6,artifact7]
    
    #-mummy list-
    mummylist=[mummy,mummy1,mummy2,mummy3,mummy4,mummy5,mummy6, mummy7]

    

    #coffin list-
    coffinlist=[coffin,coffin1,coffin2,coffin3,coffin4,coffin5,coffin6,coffin7]

    #fireball list-
    fireballlist =[fireball, fireball1, fireball2, fireball3, fireball4]


        

    #Game loop------------------------------
    while True:

        for event in pygame.event.get():
             if event .type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()
                 
             #Moving the frog-----------------------------------    
             if event.type == pygame.KEYDOWN:
                 
                 if event.key == pygame.K_LEFT:

                     frog.x-=20
                     fire.x-=20
                     
                     if carry_artifact != []:

                         carry_artifact[0].x -=20

                 elif event.key== pygame.K_RIGHT:

                     frog.x+=20
                     fire.x+=20

                     if carry_artifact != []:
                         
                         carry_artifact[0].x += 20

                #firing the butterfly

                 elif event.key == pygame.K_DOWN:

                     frog.y+=20
                     fire.y+=20

                     if carry_artifact != []:

                         carry_artifact[0].y += 20



                 elif event.key == pygame.K_UP:

                     frog.y-=20
                     fire.y-=20

                     if carry_artifact != []:

                         carry_artifact[0].y -= 20
                         

                 elif event.key == pygame.K_s:

                     fire.x = frog.x



                     fire_state = "fire_right"

                     main_surface.blit(fire_image, (fire.x + 16, fire.y + 10))



                 elif event.key == pygame.K_a:
                     fire.x = frog.x               

                     fire_state = "fire_left"

                     main_surface.blit(fire_image, (fire.x + 16, fire.y + 10))



                 elif event.key == pygame.K_q:
                     fire.y = frog.y               

                     fire_state = "fire_up"

                     main_surface.blit(fire_image, (fire.x + 16, fire.y + 10))



                 elif event.key == pygame.K_z:

                     fire.y = frog.y               

                     fire_state = "fire_down"

                     main_surface.blit(fire_image, (fire.x + 16, fire.y + 10))

                

                 



        #Code for collision events--------------------
        #dagger collide lists
        hitdagger=frog.collidelist(daggerlist)

        hitdagger1=frog.collidelist(dagger1list)
  
        hitdagger2= frog.collidelist(dagger2list)
        
        #stone collide lists
        hitstone=frog.collidelist(stonelist)

        hitstone1=frog.collidelist(stone1list)

        #coffin collide lists
        hitcoffin=frog.collidelist(coffinlist)

        #mummy collide list
        hitmummy=frog.collidelist(mummylist)

        #artifact collide list
        hitartifact = frog.collidelist(artifactlist)

        #goal and artifact collide list
        hitgoal= goal.collidelist(artifactlist)

        #fireball collide frog list

        hitfireball = frog.collidelist(fireballlist)

        #fire collide fireball list

        hitfire = fire.collidelist(fireballlist)
    
    
        #frog and stone

        if hitstone != -1:

            frog.x += stonesd
            fire.x += stonesd

            if carry_artifact != []:

                carry_artifact[0].x+= stonesd

        elif hitstone1 != -1:

            frog.x -= stonesd1
            fire.x -= stonesd1

            if carry_artifact != []:

                carry_artifact[0].x -= stonesd1
 
        #frog and dagger

        if hitdagger!= -1:
            
            frog.x = 250

            frog.y = 680

            fire.x = 250

            fire.y = 680

            life -= 1

            


        if hitdagger1==0:
            
            frog.x = 250

            frog.y = 680

            fire.x = 250

            fire.y = 680

            life -= 1

            

        if hitdagger2 != -1:
            
            frog.x = 250

            frog.y = 680

            fire.x = 250

            fire.y = 680

            life -= 1

            

        #frog and coffin
        
        for i in range(8):
            mummylist[i].x += mummyxposchange[i]

        if hitcoffin != -1:
            
            if coffin_choose[hitcoffin]==0:

                mummyxposchange[hitcoffin] = mummyx_change[hitcoffin]                
                mummy_sound.play()               
                
            elif coffin_choose[hitcoffin]==1:
                
                artifactlist[hitcoffin].x = artifactx_pos[hitcoffin]
                artifactlist[hitcoffin].y = artifacty_pos[hitcoffin]

                coffin_choose[hitcoffin] = 2

        #frog and artifact
                
        if hitartifact != -1 and carry_artifact == []:

            carry_artifact.append(artifactlist[hitartifact])


        #leaving artifact at the top
        if carry_artifact != []:
            if carry_artifact[0].y <= 30:
                carry_artifact[0].y = 10
                carry_artifact[0].x = 240
                
##                del carry_artifact[0]
                
            if hitgoal != -1:
                carry_artifact[0].y = 800
                del carry_artifact[0]
                score += 1
              
        #fire and fireball

        if hitfire == 0:

            fireball.y = 900

        if hitfire == 1:

            fireball1.y =900

        if hitfire == 2:

            fireball2.y =900

        if hitfire == 3:

            fireball3.y =900

        if hitfire == 4:

            fireball4.y =900



        #frog and fireball

        if hitfireball !=-1:

            frog.x = 250

            frog.y =680

            fire.x = 250
            fire.y = 680

            life-=1

            if carry_artifact != []:
     

                carry_artifact[0].x = 600

                carry_artifact[0].y = 250

                del carry_artifact[0]

                coffin_choose[hitartifact] = 1



            
        

        #frog and mummy
        if hitmummy != -1:
            frog.x = 250

            frog.y = 680

            fire.x=250
            fire.y=680

            life -= 1

            if carry_artifact != []:
                
                carry_artifact[0].x = 600
                carry_artifact[0].y = 250
                
                del carry_artifact[0]

                coffin_choose[hitartifact] = 1

                

        #frog and not going over bounderies
        if frog.x <=0 or frog.x>=500 :

            frog.x = 250

            frog.y = 680
            fire.x=250
            fire.y=680

            life -=1

            if carry_artifact != []:
                
                carry_artifact[0].x = 600
                carry_artifact[0].y = 250
                
                del carry_artifact[0]

                coffin_choose[hitartifact] = 1

                

        #frog and not going on stone
        if hitstone == -1 and hitstone1 == -1:
            
            if frog.y >35 and frog.y<110:
                frog.x = 250

                frog.y = 680
                fire.x = 250
                fire.y = 680
                life-=1

                if carry_artifact != []:

                    carry_artifact[0].x = 600
                    carry_artifact[0].y = 250
                
                    del carry_artifact[0]

                    coffin_choose[hitartifact] = 1

                
                    
        font = pygame.font.Font('freesansbold.ttf', 20)

        text = "Score:" + str(score) + " Level:" + str(level)

        text = font.render(text, True, colordagger, colorstone) 

        textRect = text.get_rect()

        textRect.center = (100,680)
       
                
                
        
        
        #for dagger restart on screen
        for block in daggerlist:        

            block.x = (block.x+daggersd)%500

        for block1 in dagger1list:           

            block1.x = (block1.x-daggersd1)%500

        for block2 in dagger2list:

            block2.x = (block2.x+daggersd2)%500

        #stone to restart screen
        for block4 in stonelist:

            block4.x = (block4.x+stonesd)%600

        for block5 in stone1list:

            block5.x = (block5.x-stonesd1)%600


        
        #mummy to restart screen
        for block6 in mummylist:

            block6.x = (block6.x)%500

        
        #speed of fireballs



        for block10 in fireballlist:

            block10.x = (block10.x+15)%500





        #firing



        if fire_state is "fire_right":

            fire.x +=20



        if fire_state is "fire_left":

            fire.x -= 20


        if fire_state is "fire_up":          

            fire.y -= 20

        if fire_state is "fire_down":        

            fire.y += 20

            

        if fire.x <= 0 or fire.x >=500:

            fire.x = frog.x

            fire.y = frog.y

            fire_state = "ready"        

        
        if fire.y<0 or fire.y >700:

            fire.y =frog.y

            fire.x = frog.x

            fire_state = "ready"

        


##        if life==0:
##            done = False
##            main()            

          
        #Redraw screen
        main_surface.blit(background_image,background)


        #Drawing codes-----------------------------------
        main_surface.blit(layer_image,layer)
        #Lives
        main_surface.blit(life1_image,life1)

        main_surface.blit(life2_image,life2)

        main_surface.blit(life3_image,life3)

        #Goal
        main_surface.blit(goal_image,goal)
        #Stones
        main_surface.blit(stone_image,stone)
        main_surface.blit(stone_image,stone1)
        main_surface.blit(stone_image,stone2)
        main_surface.blit(stone_image,stone3)
        main_surface.blit(stone_image,stone4)
        main_surface.blit(stone_image,stone5)  

        #Daggers
        main_surface.blit(dagger_image,dagger)

        main_surface.blit(dagger_image,dagger1)

        main_surface.blit(dagger_image,dagger2)

        main_surface.blit(dagger_image1,dagger3)

        main_surface.blit(dagger_image,dagger4)

        main_surface.blit(dagger_image,dagger5)

        #Mummys
        main_surface.blit(mummy_image1,mummy)

        main_surface.blit(mummy_image,mummy1)

        main_surface.blit(mummy_image1,mummy2)

        main_surface.blit(mummy_image,mummy3)

        main_surface.blit(mummy_image,mummy4)

        main_surface.blit(mummy_image1,mummy5)

        main_surface.blit(mummy_image1,mummy6)

        main_surface.blit(mummy_image1,mummy7)
        
        #Frog
        main_surface.blit(frog_image,frog)

        #fire

        main_surface.blit(fire_image,fire)

        
        #artifact
        main_surface.blit(egg_image,artifact)

        main_surface.blit(wings_image,artifact1)

        main_surface.blit(lamp_image,artifact2)

        main_surface.blit(egg_image,artifact3)

        main_surface.blit(wings_image,artifact4)

        main_surface.blit(lamp_image,artifact5)

        main_surface.blit(egg_image,artifact6)

        main_surface.blit(wings_image,artifact7)

        #Coffins?
        main_surface.blit(coffin_image,coffin)

        main_surface.blit(coffin_image,coffin1)

        main_surface.blit(coffin_image,coffin2)

        main_surface.blit(coffin_image,coffin3)

        main_surface.blit(coffin_image,coffin4)

        main_surface.blit(coffin_image,coffin5)

        main_surface.blit(coffin_image,coffin6)

        main_surface.blit(coffin_image,coffin7)


        #fireball

        main_surface.blit(fireball_image,fireball)

        main_surface.blit(fireball_image,fireball1)

        main_surface.blit(fireball_image,fireball2)

        main_surface.blit(fireball_image,fireball3)

        main_surface.blit(fireball_image,fireball4)

        



            
        #text            
        main_surface.blit(text, textRect)

        pygame.display.update()

        #flip the drawn surface onto screen
        pygame.display.flip()

        #speed
        time.sleep(0.05)

               
        if score == 3:

            return
        
        if life == 2:
            life1.y = 800

        elif life == 1:

            life2.y = 800


        elif life==0:

##            life3.y = 800

##            done = False

            playlevel(0,main_surface)        

            


        

        


def main():
    pygame.init()

    main_surface = pygame.display.set_mode((500,700))

    start_screen(main_surface)
    for i in range (0,100):
        playlevel(i,main_surface)
                

main()





##if __name__=='__main__':

##    main()
