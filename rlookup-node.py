#!/usr/bin/env python

__author__ = 'buzzsurfr'
__version__ = '0.1'

#  Standard Library
import sys
import re

#  Related Third-Party
import getpass

#  Local Application/Library Specific
import bigsuds

if len(sys.argv) < 4:
	print "\n\n\tUsage: %s host user node" % sys.argv[0]
	sys.exit()

#  Get login password from CLI
userpass = getpass.getpass()

#  Connect to BIG-IP
b = bigsuds.BIGIP(sys.argv[1], sys.argv[2], userpass)

#  Get list of pools and pool members
pools = b.LocalLB.Pool.get_list()
pool_members = b.LocalLB.Pool.get_member_v2(pools)

#  Node to search for
node = sys.argv[3]
if len(node) < 8 or node[:8] != '/Common/':
	node = '/Common/'+node
print "Pools using Node "+node

#  Iterate through pool member list (has a list of members per pool referenced) looking for node
for i, pool in enumerate(pool_members):
    for member in pool:
        if node == member['address']:
          print "\t"+pools[i]
