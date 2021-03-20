from pygame import *
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
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x-= self.speed
        if keys[K_RIGHT] and self.rect.x < 600:
            self.rect.x+= self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y-= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y+= self.speed

#создай окно игры
player = Player(40,40,'hero1.png', 30, 200, 1)
ost= GameSprite(130,70,'os.png', 300, 200, 4)
ost1= GameSprite(130,70,'os.png', 100, 200, 4)
window = display.set_mode((700,500))
x1=200
y1=300
x2=100
y2=200
display.set_caption('test')

background = transform.scale(image.load('images.png'), (700,500))
#window.blit(background, (0,0))

game = True
while game:
    window.blit(background, (0,0))
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    player.reset()
    ost.reset()
    ost1.reset()
    player.update()
    display.update()

#обработай событие «клик по кнопке "Закрыть окно"»
