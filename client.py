import socket
cli=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(("192.168.1.11",1236))
cli.send("Hi this is my first socket codeeeeeeeeeee!")
a=cli.recv(1024)
print a
cli.close()