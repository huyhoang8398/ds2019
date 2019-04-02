from rawsocketpy import RawSocket
from stringexec import parseString
sock = RawSocket('lo', 0xEEFA)
while True:
  package = sock.recv().data
  print package