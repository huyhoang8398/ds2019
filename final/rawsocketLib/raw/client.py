from rawsocketpy import RawSocket;
import time
sock = RawSocket('lo', 0xEEFA)
while True:
  sock.send('Boo')
  print('Boo has been sent')
  time.sleep(0.5)