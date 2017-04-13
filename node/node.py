#!/usr/bin/env python
import argparse
from sys import exit


def parse_args():
    parser = argparse.ArgumentParser(description='node.py - used for creating sensors, cluster heads, and a sink.')
    parser.add_argument('-v', '--verbose', required=False, dest='verbose', action='store_true',
                        help='Verbose output for debugging')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-n', '--node', dest='node', help='Select this process to be a node',
                       action='store_true')
    group.add_argument('-ch', '--clusterhead', dest='clusterhead', help='Select this process to be a clusterhead',
                       action='store_true')
    group.add_argument('-s', '--sink', dest='sink', help='Select this process to be a sink',
                       action='store_true')

    parser.add_argument('-p', '--port', required=False, type=int, dest='port', default=50000,
        help='Select the port to bind to. Recommended range 50001-51000 (if sink is chosen, 50000 will be default)')

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    # Line just used for troubleshooting, should be removed before pulling into master
    print args.verbose, args.node, args.clusterhead, args.sink, args.port

    exit(0)


# TODO: Create function to run as a sink
# TODO: Create function to run as a node

if __name__ == "__main__":
    main()
