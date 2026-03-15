level = 0
point = 0
print(f"Welcome to Alien Game!Your basic level is {level}.")
alien0 = {'color' : ['red', 'green', 'blue'], 'speed' : 'slow','point' : 1 }
print('Lets begin!')
for i in range(0,3):
    attack = str(input('Enter your attack options:'))
    if attack in alien0['color']:
        point += alien0['point']
    else:
        point -= alien0['point']
assert point >=3 ,'You lost ,game over!'
level += 1
print(f"Your level is {level}")
next_one = str(input("Do you want to play again?:"))
aliens = []
new_level =level
def next_game():
    global point
    if next_one == 'yes':
        number = new_level * 3 + 5
        for alien_number in range(0,number+1):
            new_alien = {'color' :[ 'green', 'blue', 'red'],
                         'speed' : ['slow' ,'medium' ,'fast'] ,
                         'point' : [1.5 ,3 ,5] ,
                         }
            aliens.append(new_alien)
            attack1 = str(input('Enter your attack options:'))
            if attack1 == new_alien['color'][0]:
                point += new_alien['point'][0]
                print(f'You shoot a {new_alien["speed"][0]} alien,You got {new_alien["point"][0]} point!')
            elif attack1 == new_alien['color'][1]:
                point += new_alien['point'][1]
                print(f'You shoot a {new_alien["speed"][1]} alien,You got {new_alien["point"][1]} point!')
            elif attack1 == new_alien['color'][2]:
                print(f"You miss a {new_alien['speed'][2]} alien,You are not got it.")
        aliens.clear()
    else:
        print('game over')
def level_up() :
    global level, point , next_one ,new_level
    if point > level * 4  :
        new_level = 1 + level
        print(f"Your level is {new_level}")
    elif point > level * 6 + 5:
        new_level = 2 + level
        print(f"Your level is {new_level}")
    elif point >  level * 12 :
        new_level = 3 + level
        print(f"Your level is {new_level}")
    else:
        new_level = level
    if new_level >level:
        next_one = str(input("Do you want to play again?:"))
while next_one == 'yes':
    next_game()
    level_up()
print(f'Your final level is {new_level},welcome to come again!')
