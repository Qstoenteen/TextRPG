import random as r
import time
x = 0
y = 0 
damage = 5
monsterHp = 100
monsterName = ('Вепрь')
while monsterHp > 0:
    print('Ты набрел на монстра "', monsterName, '"')
    choice = input('Что будете делать? (атака/бег)'.lower())
    print(choice)
    if choice == 'атака':
        monsterHp -= 5
        print('Ты нанес монстру', damage, 'урона')
        print('Теперь у него', monsterHp, 'ХП')
    