from scapy.all import *
try:
    send(IP(dst="192.168.0.1")/TCP(dport=5555)/Raw(load="Hello"))
    print ("[+] Request Sent!")
except Exception as e:
    raise e
