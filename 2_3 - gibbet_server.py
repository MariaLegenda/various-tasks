
import random
import socketserver

HOST = 'localhost'
PORT = 8888

class GibbetHandler(socketserver.BaseRequestHandler): # обработчик протокола

	def handle(self): # функция обработки сообщений
		self.data = self.request.recv(1024).decode() # перевод из байт в строку информации от клиента

		print(f'Клиент {self.client_address[0]} сообщает {self.data}')

		x = random.randint(1, 100)
		print(x)

		if self.data == 'START':
			# сервер отправляет диапезон чисел от 1 до 100
			self.request.sendall(bytes('GUESS;1;100', 'utf-8')) 
			try_count = 10

			while True:
				# получение сообщения от клиента
				self.data = self.request.recv(1024).decode() 
				data = self.data.split(';')
				
				if data[0] == 'TRY':
					print(f'Клиент {self.client_address[0]} сообщает {self.data}')
					if int(data[1]) == x:
						self.request.sendall(bytes('TRUE', 'utf-8'))
						print(f'Клиент {self.client_address[0]} выиграл')
						break
					else:
						try_count -= 1
						if try_count == 0:
							self.request.sendall(bytes('FAIL', 'utf-8'))
							break
						else:
							self.request.sendall(bytes('FALSE', 'utf-8'))

				elif data[0] == 'GOODBYE':
					print('Клиент отсоединился')
			

# запуск сервера с обработчиком handler
server = socketserver.TCPServer((HOST, PORT), GibbetHandler) 
print('Сервер игры "Виселица" запущен!')
server.serve_forever()
		