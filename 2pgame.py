import pygame
pygame.init()
win=pygame.display.set_mode([956,500])
pygame.display.set_caption("2pg")
clock=pygame.time.Clock()
game_run=True
class background(object):
    def __init__(self):
        self.bg_surface=pygame.image.load("bg.png").convert()
        self.rect_bg=self.bg_surface.get_rect()
        self.bg_x=0
    def update(self):
        self.bg_x-=1
        if self.bg_x<= (-self.rect_bg.topright[0]):
            self.bg_x=0    
    def render(self):
        win.blit(self.bg_surface,(self.bg_x,0))
        win.blit(self.bg_surface,(self.bg_x+self.rect_bg.topright[0],0))
class player():
    def __init__(self,x,y):
        self.walk_right = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
        self.walk_left = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
        self.rect_player=self.walk_right[0].get_rect()
        self.isJump=False
        self.jump_count=10
        self.left=False
        self.right=False
        self.walk_count=0
        self.x=x
        self.y=y
        self.vel=2
        self.standing=True
    def draw(self): 
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if not(self.standing):
            if self.left:  
                win.blit(self.walk_left[self.walk_count//3], (self.x,self.y))
                self.walk_count += 1                          
            elif self.right:
                win.blit(self.walk_right[self.walk_count//3], (self.x,self.y))
                self.walk_count += 1
        else:
            if self.right:
                win.blit(self.walk_right[0],(self.x,self.y))
            else:
                win.blit(self.walk_left[0],(self.x,self.y))  
        if self.isJump:
            if self.jump_count>= -10:
                neg=1
                if self.jump_count<0:
                    neg=-1
                self.y-=(self.jump_count**2)*0.50* neg
                self.jump_count-=1   
            else:
                self.isJump=False
                self.jump_count=10                      

bg_1=background()
p1=player(300,410)
p2=player(400,410)
print(p1.rect_player.bottom)
while True:
    bg_1.update()
    bg_1.render()
    if p1.rect_player.bottom-p2.rect_player.top==0:

        print("hai")
    else:
        print("hahahahahah")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys=pygame.key.get_pressed()    
    if keys[pygame.K_LEFT] :
        p1.x-=p1.vel
        p1.left=True
        p1.right=False
        p1.standing=False
    elif keys[pygame.K_RIGHT] :
        p1.x+=p1.vel
        p1.left=False
        p1.right=True
        p1.standing=False    
    else:
        p1.standing=True
        p1.walk_count=0  
    if keys[pygame.K_UP]:
        p1.isJump=True
    if keys[pygame.K_a] :
        p2.x-=p2.vel
        p2.left=True
        p2.right=False
        p2.standing=False
    elif keys[pygame.K_d] :
        p2.x+=p2.vel
        p2.left=False
        p2.right=True
        p2.standing=False    
    else:
        p2.standing=True
        p2.walk_count=0  
    if keys[pygame.K_w]:
        p2.isJump=True 
    p1.draw()                                 
    p2.draw()
    # pygame.draw.rect(win,p1.rect_player, 2)
    pygame.display.update()        
    clock.tick(50)
    