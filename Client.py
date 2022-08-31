from tkinter import *
from socket import *
from threading import *
tino=0
HEIGHT = 300
WIDTH = 500
flag=0
def so():
    global tino
    tino=1
    return
def senddd(connection,add):
    while True:
        re=''
        global tino
        while(tino!=1):
            re=texttosendclient.get()
        tino=0
        texttosendclient.delete(0,END)
        global flag
        if flag==0:
            connection.send(re.encode('UTF-8'))
            if re=='!':
                break
        else:
            flag=0
            break
def receiveee(connection,add):
    while True:
        re=connection.recv(1024).decode('UTF-8')
        if re:
            recievetextclient.configure(text="Server->"+re)
            if re=='!!':
                break
            if re=='!':
                global flag
                flag=1
                re+='!'
                connection.send(re.encode('UTF-8'))
                break
def mainn(client,address):
    thread1=Thread(target=senddd,args=(client,address))
    thread2=Thread(target=receiveee,args=(client,address))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    client.close()
def lo1():
    port=entry2.get()
    if len(port)<5:
        return
    address,portt=port.split(':')
    print(address,portt)
    client=socket(AF_INET, SOCK_STREAM)
    client.connect((address,int(portt)))
    connect.configure(state=DISABLED)
    portno_ip.configure(state=DISABLED)
    texttosendclient.configure(state=NORMAL)
    entry2.configure(state=DISABLED)
    sendbutton.configure(state=NORMAL)
    label2.configure(text='CONNECTED',bg='green')
    mainthread=Thread(target=mainn,args=(client,5))
    recievetextclient.configure(text='Connected')
    mainthread.start()
#window2
ws2 = Tk()
ws2.title("Instant LAN Messanger Client")
ws2.geometry("%dx%d" % (650,380))
portno_ip=Label(ws2,font=('Arial',13),text='Enter IP and Port: ',padx=8)
portno_ip.place(y=20,anchor  = NW)
entry2=Entry(ws2,font=('Arial',13),width=40)
entry2.place(y=51,x=13,anchor=NW)
label2=Label(ws2,borderwidth=3,font=('Arial',13),text='NOT CONNECTED',padx=3,pady=3,bg='red',width=39,height=1)
label2.place(relx=0.02,rely=0.21)
connect=Button(ws2,command=lo1,text='CONNECT',font=('Arial',17,'bold'),relief=RAISED,bd=10,bg='black',fg='white',activebackground='black',activeforeground='grey',state=ACTIVE)
connect.place(relx = 0.927,rely=0.12, x =-2, y = 2, anchor = NE)
recievetextclient=Label(ws2,borderwidth=3,font=('Arial',13),text='Not Connected',padx=30,pady=30,bg='grey',width=58,height=3)
recievetextclient.place(relx=0.0199999,rely=0.35)
texttosendclient=Entry(ws2,font=('Arial',13),width=65,state=DISABLED)
texttosendclient.place(relx=0.0199999,rely=0.7)
sendbutton=Button(ws2,command=so,text='SEND',font=('Arial',20,'bold'),relief=RAISED,bd=10,bg='black',fg='white',activebackground='black',activeforeground='grey',state=DISABLED)
sendbutton.place(relx=0.745,rely=0.8)
ws2.mainloop()