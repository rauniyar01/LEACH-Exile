import socket
import json
from sys import exit, argv
from scapy.all import *
from message import send_message


def _bind(ip, port):
    try:
        print "[*] Attempting to bind on port: {} with ip: {}".format(port, ip)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, port))
        s.listen(5)
        return s

    except socket.error:
        print "[!] Error: port already in use, incrementing port from {} to {}".format(port, port+1)
        s = _bind(ip, port+1)
        return s


def main():
    if len(argv) != 2:
        exit('Wrong args. Supply the snort logfile')

    alerts = []
    s = _bind('localhost', 1337)
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
                # Send message to the sink with the bad node ID
                # send_message(s, 'Snort', 'localhost:50000', '{}'.format(json.loads(str(pkt[TCP].payload))['id_str']))
            else:
                continue

    except KeyboardInterrupt:
        exit('Exiting...')


if __name__ == '__main__':
    main()
