
from pygame import *
from random import randint


class GameSprite(sprite.Sprite):
    def __init__(self,wid,hei, player_image, player_x, player_y,player_speed):
        super().__init__()
        self.wid1 = wid
        self.hei1=hei
        self.image=transform.scale(image.load(player_image), (wid,hei))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
bullets = sprite.Group()
bonusb=False
#or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall)) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5) or sprite.collide_rect(player, wall6) or sprite.collide_rect(player, wall7):
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x-= self.speed
        if keys[K_RIGHT] and self.rect.x < 600:
            self.rect.x+= self.speed
    def fire(self):
        global bonusb
        if bonusb==False:
            bullet= Bullet(15,20,'bullet.png', self.rect.centerx, self.rect.top, 4)
            bullets.add(bullet)
        else:
            bullet= Bullet(15,20,'bullet.png', self.rect.centerx, self.rect.top, 4)
            bullet2= Bullet(15,20,'bullet.png', self.rect.centerx-15, self.rect.top, 4)
            bullet3= Bullet(15,20,'bullet.png', self.rect.centerx+15, self.rect.top, 4)
            bullets.add(bullet)
            bullets.add(bullet2)
            bullets.add(bullet3)

'''
seld.rect.y += win_speed
global lost
if self.rect.y > self.win_heith:

        if keys[K_LEFT] and sprite.collide_rect(player, wall) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5) or sprite.collide_rect(player, wall6) or sprite.collide_rect(player, wall7):
            self.rect.x+= self.speed
        if keys[K_RIGHT] and sprite.collide_rect(player, wall) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5) or sprite.collide_rect(player, wall6) or sprite.collide_rect(player, wall7) :
            self.rect.x-= self.speed
        if keys[K_UP] and sprite.collide_rect(player, wall) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5) or sprite.collide_rect(player, wall6) or sprite.collide_rect(player, wall7):
            self.rect.y+= self.speed
        if keys[K_DOWN] and sprite.collide_rect(player, wall) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5) or sprite.collide_rect(player, wall6) or sprite.collide_rect(player, wall7):
            self.rect.y-= self.speed
'''
lost = 0 
score=0
class Enemy(GameSprite):
    def update(self):
        global score
        global lost
        self.rect.y += self.speed
        
        if self.rect.y > 500:
            self.rect.x = randint(80, win_width-80)
            self.rect.y = 0
            lost=lost+1
        
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x-= self.speed
        if keys[K_d] and self.rect.x < 600:
            self.rect.x+= self.speed
    def fire(self):
        if bonusb==False:
            bullet= Bullet(15,20,'bullet.png', self.rect.centerx, self.rect.top, 4)
            bullets.add(bullet)
        else:
            bullet= Bullet(15,20,'bullet.png', self.rect.centerx, self.rect.top, 4)
            bullet2= Bullet(15,20,'bullet.png', self.rect.centerx-15, self.rect.top, 4)
            bullet3= Bullet(15,20,'bullet.png', self.rect.centerx+15, self.rect.top, 4)
            bullets.add(bullet)
            bullets.add(bullet2)
            bullets.add(bullet3)
        
class Bullet(GameSprite):
    def update(self):
        self.rect.y-= self.speed
        if self.rect.y < 10:  
            self.kill()
class Bonus(GameSprite):
    def update(self):
        self.rect.y+= self.speed
        if self.rect.y > 500:  
            self.kill()


#создай окно игры
win_width=500
win_heith=700
window = display.set_mode((win_heith,win_width))
display.set_caption('Шутер')
background = transform.scale(image.load('galaxy.jpg'), (700,500))
#window.blit(background, (0,0))
#создай 2 спрайта и размести их на сцене
player = Player(70,100,'rocket.png', 320, 410, 3)

#player1 = Enemy('ufo.png', 320, 40, 4)
game = True
img='ufo.png'
img1 = 'bonus.png'
img2='bonus2.png'
img3='rocket2.png'
monsters = sprite.Group()
ll = sprite.Group()
bonuses = sprite.Group()
dif1 = 0
dif=0
dif2=0
dif3=0
clock = time.Clock()
FPS = 60
font.init()
font = font.SysFont('Arial',50)
bonusesm=sprite.Group()
bonusesr=sprite.Group()
j=True
rockets=sprite.Group()
while game:
    window.blit(background, (0,0))
    clock.tick(FPS)
    if lost == 10:
        game = False
    
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key== K_UP:
                player.fire()
                if j == False:
                    player2.fire()
        
    sprites_list=sprite.groupcollide(monsters, bullets, True,True)
    sprites_list23 = sprite.spritecollide(player,monsters, False)
    if sprite.spritecollide(player, monsters, False):
        game = False
    if sprite.spritecollide(player,bonuses, True):
        player.speed=player.speed+3

    if sprite.spritecollide(player,bonusesm, True):
        bonusb=True
    if sprite.spritecollide(player,bonusesr, True):
        player2 = Player2(70,100,'rocket.png', 100, 410, 3)
        j = False
    for c in sprites_list:
        score = score +1
    
    dif=dif+1
    dif1=dif1+1
    dif2=dif2+1
    dif3=dif3+1
    if dif == 45:
        monster = Enemy(80,60, img, randint(10,600),-40, 2 )
        monsters.add(monster)
        dif=0
    if dif1 == 300:
        bonus = Bonus(50,50,img1, randint(10,600),-40, 2 )
        bonuses.add(bonus)
        dif1 = 0
    if dif2 == 400:
        mbonus = Bonus(50,50,img2, randint(10,600),-40, 2 )
        bonusesm.add(mbonus)
        dif2 = 0
    if dif3 == 200:
        rbonus = Bonus(50,50,img3, randint(10,600),-40, 2 )
        bonusesr.add(rbonus)
    
    
    player.update()
    player.reset()

    count_lost = font.render('Пропущено: '+ str(lost), 1, (215,215,0))
    win = font.render('Ты выиграл!', 1, (215,0,0))
    count_score = font.render('Счёт: '+ str(score), 1, (215,25,0))
    if score >= 30:
        window.blit(win, (200,250))
        
        game=False
    window.blit(count_lost, (10,80))
    window.blit(count_score, (10,50))
    monsters.update()
    bonuses.update()
    bonusesr.update()
    bonusesm.update()
    bullets.update()
    if j == False:
        player2.update()
        player2.reset()

        if sprite.spritecollide(player2,monsters , True):
            print('32132')
            player2.kill()

    bullets.draw(window)
    bonuses.draw(window)
    bonusesr.draw(window)
    bonusesm.draw(window)
    monsters.draw(window)
    display.update()
  
#обработай событие «клик по кнопке "Закрыть окно"»
