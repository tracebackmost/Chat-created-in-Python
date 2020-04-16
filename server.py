import socket, time
#импортируем модули
host = socket.gethostbyname(socket.gethostname())
#принимаем ip адреса
port = 9090
#используем порт 9090, т.к. он не требует прав администратора
clients = []
#список клиентов
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#AF_INET - семейство сетевых сокетов 
#SOCK_DGRAM - тип сокетов дейтаграмного типа
s.bind((host,port))

quit = False
#для управления циклом создаем переменную 'quit' 
print("[ Server Started ]")
#выводим сообщение о старте сервера

while not quit:
    try:
        data, addr = s.recvfrom(1024)
        #1024 байта
        if addr not in clients:
            clients.append(addr)
        
        itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        #запись даты и времени
        print("["+addr[0]+"]=["+str(addr[1])+"]=["+itsatime+"]/",end="")
        #вывод даты и времени
        print(data.decode("utf-8"))
        #декодирование информации от клиента
        for client in clients:
            if addr != client:
                s.sendto(data,client)
        #перебираем клиентов, чтобы исключить отправку сообщения самому отправителю,
        #если клиент не отправитель - доставляем сообщение
    except:
        print("\n[ Server Stopped ]")
        #выводим сообщение об остановке сервера
        quit = True
        #завершаем цикл
s.close()