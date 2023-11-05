
import pygame, random, time, sys
pygame.init()
m = 20
Imgbody = pygame.transform.scale(pygame.image.load('body.png'),(m,m)) 
Imghead = pygame.transform.scale(pygame.image.load('Head.png'),(m,m))
Imgfood = pygame.transform.scale(pygame.image.load('food.png'),(m,m)) 
gameSurface = pygame.display.set_mode((735,475))
pygame.display.set_caption('Snack by Kryous Ngo')

#==== Thiết lập màu sắc =====
red = pygame.Color(255,0,0)
blue = pygame.Color(65,105,255)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
gray = pygame.Color(128,128,128)

snackpos = [100,60]
snackbody = [[100,60],[80,60],[60,60]]
foodx = random.randrange(1,71)
foody = random.randrange(1,45)
if foodx%2 != 0: 
    foodx +=1
if foody%2 != 0: 
    foody += 1
foodpos = [foodx * 10,foody * 10]
foodflat = True
direction = 'Right'
changeto = direction
score = 0
# hàm gameover
def game_over():
    gfont = pygame.font.SysFont('consolas', 40)
    gsurf = gfont.render('Game Over!', True, red)
    grect = gsurf.get_rect()
    grect.midtop = (360,150)
    gameSurface.blit(gsurf,grect)
    show_score(0)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

#hàm tính điểm
def show_score(choice = 1)   :
    sfont = pygame.font.SysFont('consolas', 20)
    ssurf = sfont.render('Score: {0}'.format(score), True, black)
    srect = ssurf.get_rect()
    if choice == 1:
        srect.midtop = (70,20)
    else:
        srect.midtop = (360,230)
    gameSurface.blit(ssurf,srect)
    

while True:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_RIGHT):
                changeto = 'RIGHT'
            if (event.key == pygame.K_LEFT):
                changeto = 'LEFT'
            if (event.key == pygame.K_UP):
                changeto = 'UP'
            if (event.key == pygame.K_DOWN):
                changeto = 'DOWN'
            if (event.key == pygame.K_ESCAPE):
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'    
    
    #cập nhật vị trí
    if direction == 'RIGHT':
        snackpos[0] += m
    if direction == 'LEFT':
        snackpos[0] -= m
    if direction == 'UP':
        snackpos[1] -= m
    if direction == 'DOWN':
        snackpos[1] += m
        
    #cập nhật chiều dài
    snackbody.insert(0,list(snackpos))
    if snackpos[0] == foodpos[0] and snackpos[1] == foodpos[1]:
        score += 1
        foodflat = False
    else:
        snackbody.pop()
    # tạo mồi
    if foodflat == False:
        foodx = random.randrange(1,71)
        foody = random.randrange(1,45)
        if foodx%2 != 0: 
            foodx +=1
        if foody%2 != 0: 
            foody += 1
        foodpos = [foodx * 10,foody * 10]
        foodflat = True
    # hiển thị lên màn hình
    gameSurface.fill(white)
    for pos in snackbody:
        gameSurface.blit(Imgbody, pygame.Rect(pos[0],pos[1], m, m))
        gameSurface.blit(Imghead, pygame.Rect(snackbody[0][0], snackbody[0][1],m ,m ))
        gameSurface.blit(Imgfood, pygame.Rect(foodpos[0], foodpos[1],m,m))

    #Xử lý đụng biên
    if snackpos[0] > 710 or snackpos[0] < 10:
        game_over()
    if snackpos[1] > 450 or snackpos[1] < 10:
        game_over() 
        
#   #Ăn chính mình
#   for b in snackbody[1:]:
#        if (snackpos[0] == b[0] and snackpos[1] == b[1]):
#            game_over()
    
    
    #Viền
    pygame.draw.rect(gameSurface,gray,(10,10,715,455), 2)
    show_score()
    pygame.display.flip()
