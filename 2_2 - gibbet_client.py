
import socket

HOST = 'localhost'
PORT = 8888

print('клиент игры "Виселица" приветствует вас')
print(f'Подкючение к серверу {HOST}: {PORT}')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

sock.sendall(bytes('START', 'utf-8')) # отправление сообщения не сервер

# полученные байтовые данные пользователем преобразованные в строку 
data = sock.recv(1024).decode() 
data = data.split(';') #разделение строковых данных - data[0] = Guess, data[1] = 1 ...

if data[0] == 'GUESS':
	print(f'Угадайте число от {data[1]} до {data[2]}. У вас 10 попыток')
	try_count = 10
	while True:
		x = input('Ваш ответ: ')
		if x == 'q':
			break

		sock.sendall(bytes(f'TRY; {x}', 'utf-8'))
		data = sock.recv(1024).decode() #отправка команды и параметров на сервер
		data = data.split(';')

		# реакция на ответ от сервера
		if data[0] == 'TRUE':
			print('Вы угадали!')
			break 
		elif data[0] == 'FALSE':
			try_count -= 1
			print(f'Вы не правы. Осталось попыток: {try_count}')
		elif data[0] == 'FAIL':
			print('Вы не угадали')
			break

sock.sendall(bytes('GOODBAY', 'utf-8'))
sock.close()
