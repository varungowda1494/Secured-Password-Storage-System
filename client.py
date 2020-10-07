    # Import socket module 
import socket 
import cryptography
import pickle
from cryptography.fernet import Fernet
key1=Fernet.generate_key()
key2=Fernet.generate_key()                
store2=[]  
# Create a socket object 
s = socket.socket() 
filename='passwords.txt'         
opfile=open(filename,'a')
rfile=open(filename,'r')
# Define the port on which you want to connect 
port = 12341   
             
# connect to the server on local computer 
s.connect((socket.gethostname(), port))
option=int(input())
if(option==1):
    message1=input()
    message2=input()
    message3=input()
    #print(key1)
    #print(type(key1))
    t2=(message1,message2,key1)
    #txt=str(t2)
    opfile.write(str(t2))
    opfile.close()
    
    #key=pickle.dumps(f1)
    #opfile.write(key)    
    #print(f1_key)
    f1=Fernet(key1)
    encrypted1=f1.encrypt(message3.encode())
    t=(option,message1,message2,encrypted1)
    data=pickle.dumps(t)
    print(store2)
    s.send(data) 

if(option==2):
    message1=input()
    message2=input()
    t=(option,message1,message2)
    data=pickle.dumps(t)
    s.send(data)
    daat=s.recv(256)
    #print(lst)
    f1=Fernet(key1)
    line=rfile.readline()
    lines=list()
    random=list()
    while line:
        #print(line)
        lines.append(line)
        line=rfile.readline()
        #print(line)
    for i in range(0,len(lines)):
        x=lines[i]
        x=x[1:len(x)]
        temp=x.split(',')
        random.append(temp)
    #print(random)
        #print(temp)
    
    #print(store2)
    for i in store2:
        print(i)
        if (i[0]==message1 and i[1]==message2):
            temp=i[3]
            decrypted=temp.decrypt(daat.decode())
            print(decrypted)

    for i in random:
        k1=i[0]
        k1=k1[1:-1]
        #print(k)
        k2=i[1]
        
        k2=k2[2:-1]
        #print(k1,k2)

        k3=i[2]
        k3=k3[0:48]
        k4=k3[3:-1]
        k4=k4.encode()
        #print(k4)
        #print(k3)
        #print(daat)
        if(k1==message1 and k2==message2):
            
            f1=Fernet(k4)
            decrypted=f1.decrypt(daat)
            print(decrypted.decode())
            


    #decrypted=f1.decrypt(daat)
    #data=pickle.loads(daat)
    #print(daat)



#data.decode('utf-8') 
 
# receive data from the server 
#print(s.recv(1024)) 
# close the connection 
s.close()
