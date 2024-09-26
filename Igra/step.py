from data import *
from heplers import *
import sys
import time
name = input('Введите имя вашего персонажа: ')
player['name'] = name
current_enemy = randint(0,2)
a = f"""Солнце садилось за горизонт, окрашивая небо в кроваво-багровые тона, отражающие кровь, пролитую в недавнем бою. Сердце рыцаря билось учащенно, не от страха, а от боли. Свежая рана на его левом боку ныла, отдаваясь в каждом движении. Он лежал в грязном рву, скрытый от вражеских глаз. 
"""


def conti(s):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.05)


conti(a)
sleep(1)

a = f"""Еще утром {player["name"]} был одним из самых отважных воинов королевства, его доспехи блестели под солнцем, а меч был острее любого клинка. Теперь же он был изранен, обездолен, пленником вражеской армии.
"""


def conti(s):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.05)


conti(a)
sleep(1)
a = """Вспоминая о битве, рыцарь чувствовал холодный страх. Он видел, как падают его товарищи, как отступают его соратники, как сам он, ослепленный яростью, бросился в гущу вражеской пехоты. Память о том, как его свалил с ног могучий воин, и как он, истекая кровью, потерял сознание, была мучительна.
"""


def conti(s):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.05)


conti(a)
sleep(1)
a = """Проснувшись в плену, он обнаружил, что его меч, его доспехи, его гордость - все было отнято. Он был нищим, брошенным на произвол судьбы.
"""


def conti(s):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.05)


conti(a)
sleep(1)
a = """Но он был рыцарем, а рыцари не сдаются. Он был решительно настроен вернуться домой, к своей семье, к своему королевству. Взяв себя в руки, он начал планировать побег. 
"""


def conti(s):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.05)


conti(a)
sleep(1)
a = f"""Ночь была темной, как бездна. Брошенный в темницу {player["name"]}, с трудом передвигаясь, добрался до края лагеря. В его сердце бушевала надежда, но в душе царил страх. Он знал, что риск велик, но отступать было нельзя.
"""


def conti(s):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.05)


conti(a)
sleep(1)
a = """Он пробирался сквозь чащу леса, пока не добрался до знакомой тропы. Двигаясь по ней, он чувствовал, как силы покидают его. Он был слаб, голоден, измучен. Но он продолжал идти, подгоняемый волей к жизни, к возвращению домой.
"""


def conti(s):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.05)


conti(a)
sleep(1)
a = f"""Пройдя несколько дней, {player["name"]} добрался до своего родного королевства. Он был истощен, его одежда была в лохмотьях, а тело изранено. Но он был свободен. 
"""


def conti(s):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.05)


conti(a)
sleep(1)
a = """Теперь ему предстояла новая битва - битва за выживание. Ему нужно было заработать себе на пропитание, восстановить свою силу. Но он не боялся. Он был рыцарем, и он всегда находил выход из любой ситуации.
"""


def conti(s):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.05)


conti(a)
input('Enter чтобы продолжить')
print()

while True:
    action = input('''Выберите действие:
1- В бой!
2- Тренировка
3- Магазин
4- Получить валюту
5- Инвентарь
6- Информация об игроке
7- Информация о текущем противнике
''')
    
    if action == '1':
        current_enemy = fight(current_enemy)
        if current_enemy == 3:
            break
    elif action == '2':
        training_type = input('''1- тренировать атаку
2- тренировать оборону
''')
        training(training_type)

    elif action == '3':
        shop()

    elif action == '4':
        earn()
    
    elif action == '5':
        inventory()
    
    elif action == '6':
        display_player()
        print()

    elif action == '7':
        display_enemy(current_enemy)
        print()

    print()
    





