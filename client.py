import socket, threading, time
#импортируем модули
key = 8194
#создаем ключ шифрования данных
shutdown = False
join = False

def receving (name, sock):
#создаем функцию, принимающую данные от другого клиента
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                addr
                #криптографическая связь, начало
                decrypt = ""; k = False
                for i in data.decode("utf-8"):
                    if i == ":":
                        k = True
                        decrypt += i
                    elif k == False or i == " ":
                        decrypt += i
                    else:
                        decrypt += chr(ord(i)^key)
                print(decrypt)
                #криптографическая связь, конец

                time.sleep(0.2)
        except:
            pass

host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("192.168.1.7",9090)
#записываем данные сервера
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#AF_INET - семейство сетевых сокетов 
#SOCK_DGRAM - тип сокетов дейтаграмного типа
s.bind((host,port))
s.setblocking(0)
#собираем ошибки

alias = input("Name: ")
#записываем в переменную имя клиента
rT = threading.Thread(target=receving, args=("RecvThread", s))
rT.start()
#создание и запуск многопоточности
while shutdown == False:
    if join == False:
        s.sendto(("["+alias + "] => join chat ").encode("utf-8"),server)
        join = True
    else:
        try:
            message = input()

            #криптографическая связь, начало
            crypt = ""
            for i in message:
                crypt += chr(ord(i)^key)
            message = crypt
            #криптографическая связь, конец

            if message != "":
                s.sendto(("["+alias + "] :: "+message).encode("utf-8"),server)

            time.sleep(0.2)
            #пауза между отправкой и получением сообщения
        except:
            s.sendto(("["+alias + "] <= left chat ").encode("utf-8"),server)
            shutdown = True

rT.join()
s.close()