from scapy.all import *
def print_summary(pkt):
    if IP in pkt:
        ip_src=pkt[IP].src
        ip_dst=pkt[IP].dst
        # data=pkt[IP].load
    if TCP in pkt:
        tcp_sport=pkt[TCP].sport
        tcp_dport=pkt[TCP].dport
        data=pkt[TCP].load
        print (' IP src ' + str(ip_src) + ' TCP sport ' + str(tcp_sport) + str(data)) 
        print (' IP dst ' + str(ip_dst) + ' TCP dport ' + str(tcp_dport) + str(data))
    if UDP in pkt:
        udp_sport=pkt[UDP].sport
        udp_dport=pkt[UDP].dport
        print (' IP src ' + str(ip_src) + ' UDP sport ' + str(udp_sport))
        print (' IP dst ' + str(ip_dst) + ' UDP dport ' + str(udp_dport))
	# if ((pkt[IP].src == '192.168.0.1') or (pkt[IP].dst == '192.168.0.1')):
        # print (' receive ')
# sniff(filter='ip',prn=print_summary)
# or it possible to filter with filter parameter...!
sniff(filter='dst port 5555',prn=print_summary)
