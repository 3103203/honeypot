import webbrowser
import logging
import socket
from datetime import datetime,time
attempt=0
for i in range(0,3):
    u=input("Enter the Username : ")
    p=input("Enter the Password : ")
    uf=r'E:\honeypot project\username.txt'
    pf='E:\honeypot project\password.txt'
    with open(uf,'r') as file:
        f1=file.read()
    fl1=f1.split()
    with open(pf,'r') as file:
        f2=file.read()
    fl2=f2.split()

    cur_time=datetime.now().time()
    tar_time1=time(18,0,0)
    tar_time2=time(8,0,0)

    if p in fl2 and u in fl1 and cur_time < tar_time1 and cur_time > tar_time2 :
        fie='E:\honeypot project\orginaldatabase.html'
        webbrowser.open(fie)  
        break
    if p in fl2 and u in fl1 and cur_time > tar_time1 or cur_time < tar_time2:
        fie='E:\honeypot project\orginaldatabase.html'
        webbrowser.open(fie)  
        user_ip=socket.gethostbyname(socket.gethostname())
        logging.basicConfig(filename='logdatafortime.log',level=logging.INFO, format=' %(message)s')
        timestamp=datetime.now().strftime('%y-%m-%d %H:%M:%S')
        log_mess=f'Timestamp:{timestamp}, Username:{u}, Password:{p}, ip:{user_ip}'
        logging.info(log_mess)
        break    
    else:
        attempt+=1 
        
        if attempt >= 3  : 
            user_ip=socket.gethostbyname(socket.gethostname())

            logging.basicConfig(filename='logdataforfailesattempts.log',level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
            timestamp=datetime.now().strftime('%y-%m-%d %H:%M:%S')
            log_mess=f'Timestamp:{timestamp}, Username:{u}, Password:{p}, ip:{user_ip} ,location:{"india"}'
            logging.info(log_mess)
            fie='E:\honeypot project\duplicatedatabase.html'
            webbrowser.open(fie) 
        else:
            print("INVALID USERNAME OR PASSWORD")       