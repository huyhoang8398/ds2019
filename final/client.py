import socket
import time
ETH_P_ALL = 3
interface = 'lo'
dst = b'\x08\x00\x27\xdd\xd7\x43'  # destination MAC address
src = b'\x08\x00\x27\x8e\x75\x44'  # source MAC address
proto = b'\x88\xb5'                # ethernet frame type
# print (payload)
# while True:
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))
s.bind((interface, 0))
payload = input()
while payload != 'q':
	command = ('command'+payload).encode()
	print (command)
	s.sendall(dst + src + proto + command)
	data = s.recv(1514)
	data = s.recv(1514)
	# data = s.recv(1514)
	# data = s.recv(1514)
	# data = s.recv(1514)
	# data = s.recv(1514)

	dataParse = str(data[14:])
	# print (dataParse)
	# print (dataParse)
	if dataParse.find('output'):
		# dataParseN = dataParse.decode()
		# output = dataParse.replace('output', '')
		print (dataParse)
	# print (data)
	payload = input()
# s.sendall(payload)
s.close()
# time.sleep(0.9)
# print ('gui ')
