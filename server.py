import socket
serv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#st Arguemnet i.e. AFinet = ipv4, stream = tcp
serv.bind(("****SERVER'S IP ADDRESS****",****PORT THROUGH WHICH SERVER AND CLIENT WILL COMMUNICATE****))
serv.listen(5)
c,addr=serv.accept()
#pri
print addr[0]
print addr[1]
c.send("reply from server")
r=c.recv(1024)
print r
c.close()
