import json
import os
from sys import exit, path, argv
path.append("../node")
from node import Node
from scapy.all import *


def main():
    if len(argv) != 2:
        exit('Wrong args. Supply the snort logfile')

    alerts = []

    snortNode = Node('snort', 1337)
    print snortNode

    try:
        while True:
            # This will need to point to /var/log/snort/snort.log.*
            pcap = rdpcap('/Users/bojak/Projects/SCADA/LEACH-Exile/utilities/{}'.format(argv[1]))
            try:
                last_pkt = pcap[-1]
                print last_pkt.show()
            except IndexError:
                continue

            if last_pkt not in alerts:
                alerts.append(last_pkt)
                # Send message to the sink with the bad node ID
                # send_message(s, 'Snort', 'localhost:50000', '{}'.format(json.loads(str(pkt[TCP].payload))['id_str']))
            else:
                continue

    except KeyboardInterrupt:
        exit('Exiting Snory.py...')


if __name__ == '__main__':
    main()
