#!/usr/bin/python
#This scripts inputs BGPdump output and a peer ID and extracts routing table for the peer

import sys

class Peer:

  def __init__(self, peer_id):
    self.prefix_set = set()
    self.nh_dict = {}
    self.nh_total = 0
    self.out = open("routes-{0}".format(peer_id), "w")

  def myfunc(self):
    print("Hello my name is " + self.name)

#prefix_set = set()
#nh_dict = {}
#i = 0

peer_dict = {}

if len(sys.argv) != 2 :
	print "sudo python bgpdump-parser.py inputfile"
	print "where"
	print "inputfile  ---	Output of BGPdump -m option "
	sys.exit()

bgpdump_output_file = sys.argv[1] 
#target_peer_id = sys.argv[2]
#outputfile = sys.argv[3]

#out = open(outputfile, "w")

with open(bgpdump_output_file) as f:
    for line in f:
	arr = line.replace("\r\n", "").split("|")
        as_id = arr[4]#Extract the AS
	prefix = arr[5]#Extract the prefix
	next_hop = arr[8]

	if as_id not in peer_dict :
		peer_dict[as_id] = Peer(as_id)

	if prefix not in peer_dict[as_id].prefix_set :
	    peer_dict[as_id].prefix_set.add(prefix)
            if next_hop not in peer_dict[as_id].nh_dict :
	        peer_dict[as_id].nh_dict[next_hop] = peer_dict[as_id].nh_total
                peer_dict[as_id].nh_total = peer_dict[as_id].nh_total + 1
		print "number of next-hops in {0} is {1}".format(as_id, peer_dict[as_id].nh_total)
	    peer_dict[as_id].out.write("{0}\tveth{1}\n".format(prefix, peer_dict[as_id].nh_dict[next_hop]%32))
#	    out.write("{0}\t{1}\n".format(arr[5], next_hop))
