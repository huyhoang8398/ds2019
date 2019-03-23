import socket
from _thread import *
import threading 
import os
from stringexec import parseString, writeString
# thread fuction 
# print_lock = threading.Lock()   
def threaded(c): 
    while True: 
    # data received from client 
      data = c.recv(1024) 
      status = "done"

      if not data: 
        print('Bye') 
          
        # lock released on exit 
        # print_lock.release() 
        break
      from subprocess import check_output
      import subprocess
      command = str(data.decode("utf-8"))
      print (command)
      if "cd" in command:
        print ("contain cd")
        # subprocess.call(command)
        # os.getcwd()
        commandNew = parseString(command, 'cd ')
        print (commandNew)
        os.chdir(commandNew)
        # subprocess.Popen(cwd=commandNew)
        # os.getcwd()
        c.send(status.encode("utf-8"))
        
      else:
        # subprocess.call(data)
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

          #Launch the shell command:
        output = process.communicate()

        print (output[0].decode("utf-8"))
        # data = str(data).upper()
        # out = check_output(str(data))
        # print (str(out))
        # print ("sending" + str(data))
        c.send(output[0])
        c.send(status.encode("utf-8"))
# connection closed 
    c.close() 

def Main(): 
    host = "" 
  
    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 11345
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