import socket

def Main():
  host = '127.0.0.1'
  port = 11000

  s = socket.socket()
  s.bind((host, port))
  s.listen(1)
  c, addr = s.accept()
  print ("Connection from:" + str(addr))
  while True:
    data = c.recv(1024)
    if not data:
      break
    print ("from connected user:" +str(data))
    from subprocess import check_output
    import subprocess
    # subprocess.call(data)
    process = subprocess.Popen(str(data), stdout=subprocess.PIPE, stderr=None, shell=True)

    #Launch the shell command:
    output = process.communicate()

    print output[0]
    # data = str(data).upper()
    # out = check_output(str(data))
    # print (str(out))
    # print ("sending" + str(data))
    c.send(output[0])
  c.close()

if __name__ == '__main__':
  Main()