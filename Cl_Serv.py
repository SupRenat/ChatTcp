import socket
from tkinter import *
import json
import random
import generator
import math
import time

count = random.randint(3,5)
tempMin = 23
tempMax = 27
pressMin = 742
pressMax = 750
wetMin = 70
wetMax=80
radMin = 0
radMax = 0.5
windStrMin = 0
windStrMax = 3
#values = {'tempMin':23,'tempMax':27,'pressMin':742, 'pressMax':750,'wetMin':70,'wetMax':80,'radMin':0,'radMax':0.5,'windStrMin':0, 'windStrMax':3}

#генерить и отправлять в функции sendproc с интервалом в 10 секунд
#в начале функции, чтобы потом записать в файл
weird_json = generator.Generate(count,tempMin,tempMax,pressMin,pressMax,wetMin,wetMax,radMin,radMax,windStrMin,windStrMax)
print(weird_json)
send = json.dumps(weird_json)

tk=Tk()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
host = s.getsockname()[0]
#host =socket.gethostbyname(socket.gethostname())
s.close()
print(host)
#host = "0.0.0.0"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 11719
s.bind((host, port))
s.listen(5)


#интерфейс
text=StringVar()
name=StringVar()
name.set('HabrUser')
text.set('')
tk.title('MegaChat')
tk.geometry('400x300')

log = Text(tk)
nick = Entry(tk, textvariable=name)
msg = Entry(tk, textvariable=text)
msg.pack(side='bottom', fill='x', expand='true')
nick.pack(side='bottom', fill='x', expand='true')
log.pack(side='top', fill='both',expand='true')

#while True:
    #Wait for a connection
    #print (sys.stderr, 'waiting for a connection')
    #connection, client_address = s.accept()

tick = 0
propability =round(random.uniform(0.1,0.5),1)
denied =0

def loopproc():
    delay = 10000
    global s
    global tick
    if failure(delay)==True:
        s= reset_connect(s)
        print(s)
    log.see(END)
    s.setblocking(False)
    c = None
    try:
        c, addr = s.accept()
        message = c.recv(128)
        log.insert(END, message.decode("utf-8") + '\n')
    except:
        tick+=1
        tk.after(1, loopproc)
        return
    tick += 1
    tk.after(1, loopproc)
    return

def sendproc(event):
    WtF=0
    i=0
    addr=[("192.168.43.179", 11719),("192.168.56.1",11719),("127.0.0.1",11719)]
    addrL = len(addr)
    for i in  range (addrL):
       try:
            s = socket.socket()
            s.settimeout(2)
            s.connect(addr[i])
            s.settimeout(None)
            sData = name.get() + ':' + text.get() #должно стоять в пробеле ниже, добавил сюда чтоб можно было проверить и записать этот коммит для исправления в дальнейшем
            s.send(send.encode())  # тут меняем ip-шники  sData.encode("utf-8")
            log.insert(END, send + '\n')
            text.set('')
            s.close()
            break
       except:
            WtF += 1
            s.close()
            print("error %s - is not available" % i)
    if (WtF == addrL):
        print("in file")
        f = open('data.txt', 'w')
        f.write(send + '\n')
        f.close()   

def reset_connect(self):
    self.close()
    print(self)
    time.sleep(5)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return s



def failure(delay):
    global tick
    global propability
    global denied
    if tick>=delay:
        tick=0
        denied += math.exp(propability)
        if denied >=2.6:
            propability = round(random.uniform(0.1,0.5),1)
            denied =0
            return True
        else:
            propability+=0.05
            return False
    return False

msg.bind('<Return>',sendproc)

msg.focus_set()

tk.after(1,loopproc)
tk.mainloop()
