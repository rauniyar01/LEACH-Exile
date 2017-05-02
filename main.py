#!/usr/bin/python

import argparse
from sys import exit
from node.node import Node


def parse_args():
    parser = argparse.ArgumentParser(description='node.py - used for creating sensors, cluster heads, and a sink.')
    parser.add_argument('-v', '--verbose', required=False, dest='verbose', action='store_true',
                        help='Verbose output for debugging')

    parser.add_argument('-t', '--node_type', dest='node_type', help='Choose if you want a node, clusterhead,\
    or sink', choices=['node', 'ch', 'sink'], required=True)

    parser.add_argument('-p', '--port', required=False, type=int, dest='port', default=50000,
        help='Select the port to bind to. Recommended range 50001-51000 (if sink is chosen, 50000 will be default)')

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    # Line just used for troubleshooting, should be removed before pulling into master
    # print args.verbose, args.node_type, args.port

    # Create node
    first = Node(args.node_type, args.port)
    print 'Node: {} created'.format(first)
    exit(0)


if __name__ == '__main__':
    main()
