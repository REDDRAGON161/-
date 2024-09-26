from random import randint
from time import sleep
from data import *

def fight(current_enemy):
    round = randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]['hp']
    print(f'Противник - {enemy["name"]}: {enemy["script"]}')
    input('Enter чтобы продолжить')
    print()
    while player['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}.')
            crit = randint(1, 100)
            if crit < player['luck']:
                enemy_hp -= player['attack'] * 3
            else:
                enemy_hp -= player['attack']
            sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}.')
            player['hp'] -= enemy['attack'] * player['armor']
            sleep(1)
        print(f'''{player['name']}: {player['hp']}
{enemy['name']}: {enemy_hp}''')
        print()
        sleep(1)
        round += 1

    if player['hp'] > 0:
        print(f'После того как вы нанесли сокрушительный удар {enemy["name"]} упал и произнёс:\n- {enemy["win"]}')
        current_enemy += 1
    else:
        print(f'Вы достойно сражались, но не смогли победить. Когда вы упали, ваш противник {enemy["name"]} произнёс:\n- {enemy["loss"]}')
    player['hp'] = 100
    return current_enemy

def training(training_type):
    for i in range(0,100,20):
        print(f'Тренировка завершена на {i} %')
        sleep(1.5)
    if training_type =='1':
        if player['money'] >= 5:
            player['money'] -= 5
            player['attack'] += 2
            print(f'Тренировка окончена! Теперь ваша величина атаки равна {player["attack"]}.\nКоличество денег - {player["money"]}')
        else:
            print(f'Тебе не хватает средств для тренировки. Количество денег - {player["money"]}. Твоя величина атаки равна {player["attack"]}')
            
    if training_type == '2':
        if player['money'] >= 5:
            player['money'] -= 5
            player['armor']-= 0.09
        print(f'тренировка окончена! Теперь броня поглощает {100 - player["armor"] * 100} % урона.\nКоличество денег - {player["money"]}')
 
def display_player():
    print(f'Игрок - {player["name"]}')
    print(f'Величина атаки-  {player["attack"]}. Шанс критического урона ({player["attack"]}) ед. равен {player["luck"]}')
    print(f'Броня {(1 - player["armor"]) * 100} % урона')
    print(f'Количество денег - {player["money"]}')

def display_enemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f'{enemy["name"]}')
    print(f'{enemy["attack"]}')
    print(f'{enemy["hp"]}')

def inventory():
    print('У вас есть:')
    for value in player['inventory']:
        print(value)

    print(f'{player["money"]} монет')
    print()
    kl = input('Что желаешь использовать?(напиши название): ')
    if kl == 'Амулет Войны':
        if 'Амулет Войны' in player['inventory']:
            potion = input('''Надеть амулет?
1 - да
2 - нет
        ''')
            if potion == '1':
                player['luck'] += 7
                print(f'Вы надели Амулет Войны. Да благославят вас Боги войны!\nШанс нанести критический урон равен {player["luck"]}%')
                player['inventory'].remove('Амулет Войны')
    elif kl == 'Пропуск тренировки':
        if 'Пропуск тренировки' in player['inventory']:
            potion = input('''Что будете делать?
1 - тренировать атаку                        
2 - закалить броню
3 - ничего
''')
            if potion == '1':
                player['attack'] += 2
                print(f'Вы усердно тренировались.\nТеперь ваша величина атаки - {player["attack"]}.')
                player['inventory'].remove('Пропуск тренировки')
            elif potion == '2':
                player['armor'] -= .09
                print(f'Вы закалили броню.\nБроня поглощает {100 - player["armor"] * 100}% урона.')
    elif kl == 'Длинный острый меч':
        if 'Длинный острый меч' in player['inventory']:
            potion = input('''Сменить меч?
1- да
2- нет
''')
            if potion == '1':
                player['attack'] +=15
                print(f'Вы сменили свой старый меч на новый.\nВаша величина атаки - {player["attack"]}.')
                player['inventory'].remove('Длинный острый меч')
    elif kl == 'Тяжёлые доспехи':
        if 'Тяжёлые доспехи' in player['inventory']:
            potion = input('''Сменить броню?
1- да
2- нет                           
''')
            if potion == '1':
                player["armor"] -= 0.3
                print(f'Вы сменили свою старую и потрёпаную броню.\nБроня поглощает {100 - player["armor"] * 100}% урона.')

def shop():
    print('Приветствую тебя в моём магазине! Что желаешь купить?')
    print(f'У тебя есть {player["money"]} монет')
    for key, value in items.items():
        print(f'{key} - {value["name"]}: {value["price"]}')

    item = input('Что хотите купить? (1/4)')

    if item in player['inventory']:
        print(f'У тебя уже есть {player[item]["name"]}')

    elif player["money"] >= items[item]["price"]:
        print(f'Поздравляю с приобретение {items[item]["name"]}')
        player['inventory'].append(items[item]["name"])
        player["money"] -= items[item]["price"]
    else:
        print('У тебя не хватает денег. Когда появятся приходи ещё.')


def earn():
    print('Здравствуй! У меня есть для тебя работа. Если выполнишь всё без косяков, то я тебе хорошо заплачу. Но если будут серьёзные косяки, то денег не жди.')
    input('Enter чтобы продолжить')
    print()
    result = randint(1, 100)
    sleep(1.5)
    print('Вы подготавливаетесь к заданию...')
    sleep(1.5)
    print('Вы отправились в путь...')
    sleep(1.5)
    print('Вы перешли к выполнению задания...')
    sleep(1.5)
    print('Вы возвращаетесь с задания...')
    sleep(1.5)
    if result <67:
        print('Вы выполнили задание и получили 500 монет.')
        player["money"] += 500
    else:
        print('Вы провалили задание и ничего не получили.')

    print()
    print(f'У вас {player["money"]} монет')
    print()


def training(training_type):
    skip = '2'
    if items ['2']["name"] in player['inventory']:
        skip = input('''Желаете пропустить тренировку?
1 - да                     
2 - нет                     
''')
    if skip == '2':
        for i in range(0, 101, 20):
            print(f'Тренировка завершена на {i}%')
            sleep(1.5)
    if training_type == '1':
        player['attack'] += 2
        print(f'Тренировка завершена. Теперь ваша величина атаки равна {player["attack"]}')
    elif training_type == '2':
        player['armor'] -= .09
        print(f'Броня улучшена. Теперь броня поглощает {100 - player["armor" * 100]}% урона.')
        print