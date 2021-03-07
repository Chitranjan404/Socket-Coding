import socket
cli=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(("****SERVER'S IP ADDRESS****",****PORT THROUGH WHICH SERVER AND CLIENT WILL COMMUNICATE****))
cli.send("Hi this is my first socket codeeeeeeeeeee!")
a=cli.recv(1024)
print a
cli.close()
