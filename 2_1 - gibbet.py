import random
import turtle
import sys

def gotoxy(x,y):
	turtle.penup() #поднять курсор
	turtle.goto(x,y) #переместить курсор
	turtle.pendown() #опустить курсор

def draw_line(from_x, from_y, to_x, to_y):
	gotoxy(from_x, from_y)
	turtle.goto(to_x, to_y)

def draw_head(x, y, r):
	gotoxy(x, y)
	turtle.circle(r)

def erase(from_x, from_y, to_x, to_y):
	turtle.color('white')
	turtle.width(80)
	gotoxy(from_x, from_y)
	turtle.goto(to_x, to_y)

funcs = [draw_line, draw_line, draw_line, draw_line, 
	draw_head, draw_line, draw_line, draw_line, draw_line, draw_line]

def draw_gibbet(step, coord): #пошаговая отрисовка виселицы
	turtle.color('blue')
	funcs[step](*coord_list[step])


x = random.randint(1,100) #загаданное число
print(x)

turtle.speed(0) # скорость рисования
coord_list = []

coord = open('gibbet_coords.txt')

for line in coord:
	line = line.strip().split(',') # strip убирает перенос строки, split делить запятой
	nums = [] # для преобразования строки в число
	for n in line:
		nums.append(int(n))
	coord_list.append(nums) 

print(coord_list)

answer = turtle.textinput('Играть?', 'y/n')

if answer == 'n':
	sys.exit()

hints = False # подсказки выключены
answer = turtle.textinput('Давать подсказки?', 'y/n')
if answer == 'y':
	hints = True

try_count = 0

while True:
	number = turtle.numinput('Угадайте', 'число', 0, 0, 100)

	if number == x:
		erase(-150, 100, 300, 100) # в случае победы закрашивает надпись неверно
		turtle.color('green')
		gotoxy(-150, 200)
		turtle.write('Ура! Вы победили!', font=('Arial', 28, 'normal'))
		break #выход из цикла, когда число угадано
	
	else:
		turtle.color('red')
		gotoxy(-150, 100)
		turtle.write('Неверно', font=('Arial', 28, 'normal'))

		if hints:
			gotoxy(100, 100 - try_count * 15) # постоянное смещение
			if number > x:
				turtle.write(str(number) + ' Загаданное число меньше')
			else:
				turtle.write(str(number) + ' Загаданное число больше')


		draw_gibbet(try_count, coord_list)
		
		try_count += 1


		if try_count == 10:
			gotoxy(-100, 100)
			turtle.write('Вы проиграли!', font=('Arial', 44, 'normal'))
			break




