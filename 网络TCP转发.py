#tcp server
import socket
 
host = '192.168.0.32'          #Local Server IP
host2 = '192.168.0.31'   #Real Server IP
port = 6001 #Local Server Port
port2 = 5025 #Real Server Port
 
def ProcData(data):
    return data
    #add more code....
 
print ("Map Server start from " + host + ":" + str(port) +" to " + host2 + ":" + str(port2) +"\r\n")
 
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
#print ("127.0.0.1 Server start at "+ str(port) +"\r\n")
 
client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
client.connect((host2,port2))
print (host +" Client connect to " + host2 + ":"+str(port2)+"\n")
 
server.listen(5)
ss, addr = server.accept()
print ('got connected from',addr)
 
while 1:
    msg = ss.recv(20480)
    print ("Get:"+repr(msg)+"\r\n")
 
    client.send(msg)
    #print "Client send data %s to "%repr(msg)
    buf=client.recv(20480)
 
    #print "Client recv data %s from "%repr(buf)
    ss.send(buf)
    print ("Send:"+repr(buf)+"\r\n" )
