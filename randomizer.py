import random as r

item = ['Мечь','Топор','Кинжал','Лопата','Кирка', 'Вилка']
material = ['Дерева', 'Камня','Железа', 'Золота', 'Изумруда', 'Картона', 'Пластика']
effect = ['Огня','Воды', 'Лавы', 'Природы', 'Разложения']
while True:
    input('Нажмите enter для генерации')
    y = r.randint(0,(len(item)-1))
    x = r.randint(0,( len(material)-1))
    z = r.randint(0,(len(effect)-1))
    print('Сгенерированный предмет:')
    print(item[y], 'из', material[x],'наделенный стихией', effect[z])
