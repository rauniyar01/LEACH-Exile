from sys import exit, path, argv
#path.append("/home/bojak/LEACH-Exile/utilities")
from node.node import Node
from scapy.all import *
from utilities.leach_utils import *
from utilities.parser import *


def main():
    if len(argv) != 2:
        exit('Wrong args. Supply the snort logfile')

    alerts = []

    snortNode = Node('snort', 13337)

    try:
        while True:
            try:
                pcap = rdpcap('/var/log/snort/{}'.format(argv[1]))
            except scapy.error.Scapy_Exception:
                continue

            try:
                last_pkt = pcap[-1]
		#last_pkt.display()
            except IndexError:
                continue

            if last_pkt not in alerts:
                alerts.append(last_pkt)
                sendSock = snortNode._bind('127.0.0.1', 13338)
		j = str_to_json(str(last_pkt[TCP].payload))
		
                print send_message(sendSock, socketStr_to_tuple("127.0.0.1:50000"),
                             vals_to_json(snortNode.id_str, 'exile', j['data']['orig_source']))
            else:
                continue

    except KeyboardInterrupt:
        exit('Exiting Snory.py...')


if __name__ == '__main__':
    main()
