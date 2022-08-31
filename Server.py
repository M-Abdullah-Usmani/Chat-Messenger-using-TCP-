from socket import *
from threading import *
tino=0
HEIGHT = 300
WIDTH = 500
from tkinter import *
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
            re=texttosend.get()
        tino=0
        texttosend.delete(0,END)
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
            recievetext.configure(text="Client->"+re)
            if re=='!!':
                break
            if re=='!':
                global flag
                flag=1
                re+='!'
                connection.send(re.encode('UTF-8'))
                break
def mainn(server,d):
    print("Server is listening :")
    while True:
        connection,add=server.accept()
        texttosend.configure(state=NORMAL)
        sendbutton.configure(state=ACTIVE)
        recievetext.configure(text="Connected")
        thread1=Thread(target=senddd,args=(connection,add))
        thread2=Thread(target=receiveee,args=(connection,add))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        connection.close()
        texttosend.configure(state=DISABLED)
        sendbutton.configure(state=DISABLED)
        recievetext.configure(text="Not Connected")
def lo():
    port=int(entry.get())
    if port>=0 and port<=65535:
        print('')
    else:
        return
    address=gethostbyname(gethostname())
    server=socket( AF_INET, SOCK_STREAM)
    server.bind((address,port))
    server.listen(1)
    label.configure(state=DISABLED)
    entry.configure(state=DISABLED)
    mainthread=Thread(target=mainn,args=(server,5))
    mainthread.start()
    
window=Tk()
portno=Label(window,font=('Arial',13),text='Port Number :',padx=8)
recievetext=Label(window,borderwidth=3,font=('Arial',13),text='Not Connected',padx=30,pady=30,bg='grey',width=54,height=3)
entry=Entry(window,font=('Arial',13))
portno.place(y=20,anchor  = NW)
entry.place(y=21,x=130,anchor=NW)
label=Button(window,command=lo,text='Start Listening',font=('Arial',11,'bold'),relief=RAISED,bd=5,bg='black',fg='white',activebackground='black',activeforeground='grey',state=ACTIVE)
label.place(relx = 0.92,rely=0.025, x =-2, y = 2, anchor = NE)
recievetext.place(relx=0.07,rely=0.22)
texttosend=Entry(window,font=('Arial',13),width=61,state=DISABLED)
texttosend.place(relx=0.07,rely=0.6)
sendbutton=Button(window,command=so,text='SEND',font=('Arial',20,'bold'),relief=RAISED,bd=10,bg='black',fg='white',activebackground='black',activeforeground='grey',state=DISABLED)
sendbutton.place(relx=0.745,rely=0.8)
window.geometry("%dx%d" % (650,380))
window.title("Instant LAN Messanger Server")
window.mainloop()
