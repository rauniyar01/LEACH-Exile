from sys import exit, path, argv
path.append("../node")
from node import Node
from scapy.all import *
from leach_utils import *
from parser import *


def main():
    if len(argv) != 2:
        exit('Wrong args. Supply the snort logfile')

    alerts = []

    snortNode = Node('snort', 13337)

    try:
        while True:
            # This will need to point to /var/log/snort/snort.log.*
            pcap = rdpcap('/Users/bojak/Projects/SCADA/LEACH-Exile/utilities/{}'.format(argv[1]))
            try:
                last_pkt = pcap[-1]
            except IndexError:
                continue

            if last_pkt not in alerts:
                alerts.append(last_pkt)
                sendSock = snortNode._bind('localhost', 13338)
                send_message(sendSock, socketStr_to_tuple("localhost:50000"),
                             vals_to_json(snortNode.id_str, 'exile', str_to_json(last_pkt[TCP].payload)['orig_sender']))
            else:
                continue

    except KeyboardInterrupt:
        exit('Exiting Snory.py...')


if __name__ == '__main__':
    main()
