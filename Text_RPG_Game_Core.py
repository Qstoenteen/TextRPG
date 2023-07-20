import random as r
import time
hp = 0
coins = 0
damage = 0


def event():
    event = r.randint(1,13)
    if event == 1:
        print('')
        input('Вокруг сгущаются тучи, в воздухе чувствуется запах озона, продолжаю двигаться дальше...')
    if event == 2:
        print('')
        input('Вдалеке виднеются тени, нужно быть настороже. Двигаюсь дальше...')
    if event >= 3:
        print('')
        input('Ничего не происходит, блуждаю...')

def printParameters(): # Функция параметров
    print('==')
    print('Сейчас у тебя {0} HP, {1} золотых и {2} урона' .format(hp, coins, damage))
    print('')
def printHp ():
    print('У тебя', hp, 'Здоровья')
def printCoins():
    print('У тебя', coins, 'монет')
def printDamage():
    print('У тебя', damage, 'урона')

def meetChest():
    global hp
    global coins
    global damage
    print('')
    while input('Ты обнаружил сокровище, попытаешься его достать?(Да/Нет)\n') .lower() == 'да':
        chest = r.randint(1,3)
        if chest == 1:
            damage += 1
            print('Ты раскопал ценный артефакт, он придаёт тебе сил! + 1 урона')
            printDamage()
            print('Путешествие продолжается...')
            break
        if chest == 2:
            hp -= 1
            print('Ты попал в ловушку, острые зубья скользнули по твоей плоти, ты получаешь -- 1 урона',)
            printHp()
            print('Путешествие продолжается...')
            break
        if chest == 3:
            print('Тайник оказался разграбленным, ничего ценного не осталось')
            print('Путешествие продолжается...')
            break
def meetShop():
    global hp
    global coins
    global damage 

    def buy (cost):
        global coins
        if coins >= cost:
            coins -= cost
            # printCoins() Временно отключил
            return True
        print('')
        print('У тебя маловато монет')
        return False

    weaponLvl = r.randint(1, 3)
    weaponDamage = r.randint(2,3)* weaponLvl
    weapons = ['Меч','Лук','Посох','Топор','Кинжал']
    weaponRarities = [ 'Обычный', 'Редкий', 'Легендарный']
    weaponRarity = weaponRarities[weaponLvl-1]
    weaponCost = r.randint (3,4)* weaponLvl + 5
    weapon = r.choice(weapons)

    oneHpCost = 5
    threeHpCost = 12
    print('')
    print('')
    print('==============')
    print('На пути тебе встретился торговец!')
    printParameters()
    print('==============')
    time.sleep(1)
    while input('Начать торговлю?(да/нет)\n') .lower() == "да":
        print('')
        print('Торговец приветливо показывает свой товар:')
        print('1)Эликсир здоровья(1HP) ', oneHpCost,' монет')
        print('2)Большой эликсир здоровья(3HP) ', threeHpCost,' монет')
        print('3){0} {1}, Урон {3}. стоимостью в {2} монет. ' .format(weaponRarity, weapon, weaponCost,weaponDamage))
    

        choice = input('Что хочешь приобрести?\n')
        if choice == '1':
            if buy (oneHpCost):
                hp += 1
                printHp()
        elif choice == '2':
            if buy(threeHpCost):
                hp += 3
                printHp()
        elif choice == '3':
            if buy(weaponCost):
                
                damage = weaponDamage
                print('Покупка совершена!')
                print('Теперь:')
                printCoins()
                printDamage()
        else:
            print('Я такое не продаю')
def meetMonster():
    global hp
    global coins
    global damage

    monsterLvl = r.randint(1,4)
    monsterHp = monsterLvl + 5
    monsterDamage = monsterLvl + 1
    monsters = ['Вепрь','Хрусталиск','Мурлок','Марсюган','Софиньон']
    # monsterStatus = ['Отравленный','Просоленный','Гневный','Разгневанный']
    monster = r.choice(monsters)
    print('')
    print('')
    print('==============')
    print ('Ты набрел на монстра - {0},{1}-уровень, у него {2} HP и {3} урона'.format(monster, monsterLvl, monsterHp, monsterDamage))
    printParameters()
    print('==============')
    

    while monsterHp > 0:
        choice = input('Что будете делать?(атака/бег):'.lower())
        
        if choice== 'атака':
            crit = r.randint(0,10)
            if crit >= 6:
                print('Критическая атака!Урон х2!')
                print('Атака составила ',damage * 2, ' урона')
                monsterHp -= damage * 2
            elif crit == 0:
                monsterHp -= 0
                print('Ты промахнулся!')
            else:
                monsterHp -= damage
                print('ты атаковал монстра и нанёс ему ', damage,' урона')
            print('Сейчас у него', monsterHp,'HP')
        elif choice == 'бег':
            chance = r.randint(0, monsterLvl)
            if chance == 0:
                print('Тебе удалось сбежать из боя')
                break
            else:
                print('Убежать не получилось, монстр настиг и нанес тебе ', monsterDamage,' урона')
        else:
            continue

        if monsterHp > 0:
            hp -= monsterDamage
            print('Монстр атакует Вас, и наносит', monsterDamage,'урона')
        if hp <= 0:
            break
    else:
        loot = r.randint(0,2) + monsterLvl
        coins += loot
        print('')
        print('')
        print('Тебе удалось одолеть монстра, за что ты получил ',loot ,' монет')
        print('Теперь у тебя', coins,'монет и',hp,'здоровья')
        print('Путешествие продолжается!')

def initGame(initHp, initCoins, initDamage):
    global hp
    global coins
    global damage

    hp = initHp
    coins = initCoins
    damage = initDamage
 
    print('Вы отправились в путешествие, навстречу приключениям. Удачи!')
    printParameters()
def GameLoop():# Функция игрового цикла. Игровых событий.
    situation = r.randint(0,8)
    if situation == 0:
        meetShop()
    elif situation == 1:
        meetMonster()
    elif situation == 2:
        meetChest()
    else:
        event()

initGame (5,25,1) #Стартовые параметры.(Здоровье, монеты, урон)

while True:
    GameLoop()


    if hp <= 0: # Условие смерти
        print('Вы погибли')
        print('x_x')
        if input('Хочешь начать сначала(да/нет):') .lower()=='да':
            initGame(5,25,1)
        else:
            break