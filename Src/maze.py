#create a Maze game!
from pygame import *
#create game window
window_width = 1400
window_height = 700
window = display.set_mode( (window_width, window_height) )
#set scene background
bg = transform.scale( image.load('background.jpg'),  (window_width, window_height) )

class Character():
    def __init__(self, filename, size_x, size_y, pos_x, pos_y, speed):
        self.image = transform.scale( image.load(filename),  (size_x, size_y) )
        self.size_x = size_x
        self.size_y = size_y
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def draw(self):
        draw.rect(window, ( 102, 255, 122 ), self.rect)
        window.blit(self.image, (self.rect.x, self.rect.y))
class Wall(Character):
    def __init__(self, size_x, size_y, pos_x, pos_y):
        self.image = Surface( (size_x, size_y) )
        self.image.fill( (13, 222, 191) )
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
wall_list = []
wall_list.append( Wall(10, 150, 100, 000) )
wall_list.append( Wall(10, 900, 100, 250) )
wall_list.append( Wall(10, 150, 300, 000) )
wall_list.append( Wall(10, 150, 300, 250) )
wall_list.append( Wall(10, 150, 600, 000) )
wall_list.append( Wall(300, 10, 305, 250) )
wall_list.append( Wall(10, 250, 600, 250) )
wall_list.append( Wall(10, 400, 750, 100) )
wall_list.append( Wall(320, 10, 600, 500) )
wall_list.append( Wall(10, 250, 920, 260) )
wall_list.append( Wall(10, 215, 920, 000) )
wall_list.append( Wall(10, 150 , 450, 100) )
wall_list.append( Wall(10, 300, 300, 475) )
wall_list.append( Wall(100, 10, 300, 475) )
wall_list.append( Wall(10, 150, 400, 335) )
wall_list.append( Wall(125, 10, 400, 335) )
wall_list.append( Wall(10, 250, 523, 335) )
wall_list.append( Wall(550, 10, 523, 585) )
wall_list.append( Wall(10, 300, 1072, 295) )
wall_list.append( Wall(10, 250, 920, 260) )
wall_list.append( Wall(10, 215, 920, 000) )
wall_list.append( Wall(10, 150 , 450, 100) )
wall_list.append( Wall(10, 300, 300, 475) )
wall_list.append( Wall(100, 10, 300, 475) )
wall_list.append( Wall(10, 150, 400, 335) )
wall_list.append( Wall(125, 10, 400, 335) )
wall_list.append( Wall(10, 250, 523, 335) )


player1 = Character('naruto.png', 50, 50, 200, 35, 4)
player2 = Character('madara.png', 50, 50, 600, 200, 4 )
route_list = [ (100, 150), (300, 500)]
ok_x = False
ok_y = False
route_id = 0
player3 = Character('kurama.png', 50, 50, 1200, 100, 4)

fps = 60
clock = time.Clock()
game = True
finish = False

font.init()
style = font.SysFont(None, 60)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            print(e.pos)


    for wall in wall_list:
        wall.draw()


    if finish == False:
        lastplayer1_x = player1.rect.x
        lastplayer1_y = player1.rect.y
        keys = key.get_pressed()

        if (keys[K_d] and player1.rect.x < window_width-player1.size_x):        
            player1.rect.x += player1.speed

        if (keys[K_a] and player1.rect.x > 0):
            player1.rect.x -= player1.speed

        if (keys[K_w] and player1.rect.y > 0):
            player1.rect.y -= player1.speed

        if (keys[K_s]and player1.rect.y < window_height-player1.size_y):
            player1.rect.y += player1.speed

        target_x, target_y = route_list[route_id]
        if (player2.rect.x < target_x): # right
            dist = target_x - player2.rect.x
            player2.rect.x += min(player2.speed, dist)
        elif (player2.rect.x > target_x):
            dist = player2.rect.x - target_x
            player2.rect.x -= min(player2.speed, dist)
        else:
            ok_x = True
            
        if (player2.rect.y < target_y): 
            dist = target_y - player2.rect.y
            player2.rect.y += min(player2.speed, dist)
        elif (player2.rect.y > target_y):
            dist = player2.rect.y - target_y
            player2.rect.y -= min(player2.speed, dist)
        else:
            ok_y = True
        
        if ok_x == True and ok_y == True:
            route_id += 1
            if route_id == len(route_list):
                route_id = 0
            ok_x = False
            ok_y = False
        
        isCollide = sprite.collide_rect(player1, player2)
        if isCollide == True:
            print('You Lose!')
            finish = True
            
        isCollide = sprite.collide_rect(player1, player3)
        if isCollide == True:
            finish = True  



        for wall in wall_list:
            isCollide = sprite.collide_rect(player1, wall)
            if isCollide:
                player1.rect.x = lastplayer1_x
                player1.rect.y = lastplayer1_y



    else:
        collide = sprite.collide_rect(player1, player3)
        if collide == True:
            text = style.render("You Win!", True, (58, 232, 96))
            window.blit(text, (650, 350) )
        else:
            text = style.render("You Lose!", True, (209, 33, 27))
            window.blit(text, (650, 350) )




    display.update()
    clock.tick(fps)
    window.blit(bg, (0, 0))
    player1.draw()
    player2.draw()
    player3.draw()