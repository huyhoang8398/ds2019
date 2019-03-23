import socket

def Main():
  host = '127.0.0.1'
  port = 61345
  s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  # s = socket.socket()
  s.connect((host, port))
  message = input("-> ")
  while message != 'q':
    s.send(message.encode('ascii'))     
    data = s.recv(1024)
    print (data.decode("utf-8"))
    message = input("-> ")
  s.close

if __name__ == '__main__':
  Main()