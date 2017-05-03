# LEACH-Exile
An emulation of the LEACH protocol for wireless sensor networks that implements an Intrusion Detection System and will exile malicious nodes from the network

## Disclaimer
In order to emulate LEACH, without implementing it to paper/RFC specifications, certain techniques were implemented differently. We are aware there are additional security implementations that are forgone for this process, they aren’t without acknowledgement. This was done for a few reasons:
* Time saver
* Implement LEACH without physical hardware
* Implement LEACH and be able to change the protocol 
  * (This would have been difficult with NS3 and other tools like it)
* Run multiple nodes on one machine to avoid resource constraints, such as running many virtual machines.

## Node Configuration
Nodes will hold an election process to determine who will become a clusterhead this round. 
* Sink
  * Will have a static unique identifier of 0
* Clusterhead (CH)
  * Will bind to a local socket, be ready to send data to sink
  * Begin forwarding incoming traffic to the sink
  * ID assigned from when it was a node will not change
* Node
  * Will bind to a local socket, be ready to send data to CH
  * Will look at local listening ports from 50000 - 51000 (Structured to simulate radio range)
  * Send either good or bad traffic to socket depending on predetermined node type
  * Will generate a random unique identifier upon startup

## Communication Flow
Once the election process is complete. The CH will forward all traffic to the sink. The sink will then forward to traffic to SNORT where an IDS rule will be triggered if a node is deemed malicious. The alert will be sent back to the sink who will broadcast out the bad node’s MAC address to all other nodes.  (In our case this won’t be the MAC address, it will be the node's unique identifier). The broadcast will be signed with the private key of the sink to ensure authenticity of the broadcast. 

Nodes that receive this transmission will check the signature, and if valid, will add the exiled node to their internal exiled list. All communication that would normally go to that node will instead be dropped. (In the case of actual implementation, the node would create a static arp entry to sinkhole traffic). 

Once a node has been remediated by an administrator, they can then request the sink to send a revert broadcast removing the previously exiled node from the list. This will also trigger the node to remove the sinkhole mechanism that was in place to exile said node.
