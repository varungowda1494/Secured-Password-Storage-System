#Server :
#A server has a bind() method which binds it to a specific ip and port so that it can listen to incoming requests on that ip and port.A server has a listen() method which puts the server into listen mode. This allows the server to listen to incoming connections. And last a server has an accept() and close() method. The accept method initiates a connection with the client and the close method closes the connection with the client.

# first of all import the socket library 
import socket,pickle                
store=[]  
# next create a socket object 
s = socket.socket()          
print("Socket successfully created")

# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12341                
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind((socket.gethostname(), port))         
#print("socket binded to %s",%(port) )
  
# put the socket into listening mode 
s.listen(1)      
print("socket is listening")            
  
# a forever loop until we interrupt it or  
# an error occurs 
filename='passwords.txt'
count=0
#c, addr = s.accept()
#print("Connection from: " + str(addr))
while True: 
  
   # Establish connection with client. 
   c, addr = s.accept() 
   opfile=open(filename,'a+')  
   ofile=open(filename,'r')  
   #print('Got connection from', addr) 
   data1=c.recv(256)
   #print(data1)
   data=pickle.loads(data1)
   #print(data)
   #print(data)
   print((data[0])==2)
   if(data[0]==2):
      for i in store:
         print(i)
         if(i[1]==data[1] and i[2]==data[2]):
            count=1
            c.send(i[3])
            break
      #c.send(readdata.encode())
   elif(data[0]==1):
      #print(data)
      store.append(data)
      print(store)
      opfile.write('\n')
   # send a thank you message to the client.  
   if(count==0):
      c.send(b'password not found') 
   opfile.close()
   # Close the connection with the client 
   c.close() 
   
