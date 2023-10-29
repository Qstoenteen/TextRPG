import pygame
import random as r
import sys
pygame.init()

window_width, window_height = 800, 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("MyVisualTextGame")
clock = pygame.time.Clock()
answer = 0
class Text ():
    def __init__(self, text, size, x, y):
        self.text = text
        self.size = size
        self.x = x
        self.y = y
    def print(self):
        text_surface, rect = font.render(self.text, (0, 0, 0))
        screen.blit(text_surface, (self.x, self.y))
class Button():
    def __init__(self, buttonColor, buttonX, buttonY, buttonWidth, buttonHeight, buttonText):
        self.buttonColor = buttonColor
        self.buttonX = buttonX
        self.buttonY = buttonY
        self.buttonWidth = buttonWidth
        self.buttonHeight = buttonHeight
        self.buttonText = buttonText

    def drawButton(self):
        pygame.draw.rect(screen, self.buttonColor, (self.buttonX, self.buttonY, self.buttonWidth, self.buttonHeight))
        text = font.render(self.buttonText, True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.buttonX + (self.buttonWidth // 2), self.buttonY + (self.buttonHeight // 2)))
        screen.blit(text, text_rect)

def click():
    if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button1.buttonX < mouse_x <button1.buttonX + button1.buttonWidth and button1.buttonY < mouse_y < button1.buttonY + button1.buttonHeight:
                #draw_text(event(), 25, 200, 20)
                print("КНОПКА ДА НАЖАТА\b")
                answer = 1
                answer = 0
                print(answer)
            if button2.buttonX < mouse_x <button2.buttonX + button1.buttonWidth and button2.buttonY < mouse_y < button2.buttonY + button2.buttonHeight:
                print("КНОПКА НЕТ НАЖАТА") 
                answer = 2
                answer = 0
                print(answer)

enemy = 'null'


def meetMonster():
    global hp
    global coins
    global damage
    global enemy
    monsterLvl = r.randint(1,4)
    monsterHp = monsterLvl * 5
    monsterDamage = monsterHp // 2
    monsters = ['Вепрь','Хрусталиск','Мурлок','Марсюган','Софиньон']
    monsterStatus = ['Отравленный','Просоленный','Гневный','Разгневанный']
    monster = r.choice(monsters)
    draw_text(('Ваш противник: '+ str(monster)),30,10,70)
    enemy = monster
        
    

def draw_text(text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (x, y))

# Create a font object
font = pygame.font.Font(None, 30)

# Create a button instance
hp = 100
damage = 10
damageprint = str(damage)
hpprint = str(hp)




button1 = Button((255, 150, 150), 150, 300, 100, 50, 'Да')
button2 = Button((255, 150, 150), 300, 300, 100, 50, 'Нет')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if hp < 0:
            break
        click()
        meetMonster()
            
    screen.fill((50, 50, 50))
    
    # Draw the button
    button1.drawButton()
    button2.drawButton()
    draw_text(('Урон: '+ str(damage)),30,10,30)
    draw_text(('Здоровье: '+ str(hp)),30,10,10)
    draw_text(('Здоровье: '+ str(enemy)),30,50,30)
    #print(hp)
    #event()
    meetMonster()
    pygame.display.flip()
    clock.tick(10)

pygame.quit()