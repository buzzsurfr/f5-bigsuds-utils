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
	print "\n\n\tUsage: %s host user pool" % sys.argv[0]
	sys.exit()

#  Get login password from CLI
userpass = getpass.getpass()

#  Connect to BIG-IP
b = bigsuds.BIGIP(sys.argv[1], sys.argv[2], userpass)

pool = sys.argv[3]
if len(pool) < 8 or pool[:8] != '/Common/':
	pool = '/Common/'+pool
print "Virtual Servers using Pool "+pool

#  Get list of pools and pool members
virtual_servers = b.LocalLB.VirtualServer.get_list()
vs_pools = b.LocalLB.VirtualServer.get_default_pool_name(virtual_servers)

#  Iterate through pool member list (has a list of members per pool referenced) looking for node
for i, vs_pool in enumerate(vs_pools):
    if pool == vs_pool:
      print "\t"+virtual_servers[i]
