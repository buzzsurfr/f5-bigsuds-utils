#!/usr/bin/env python
#
# bigip_active: Connects to the active member of a Device Group regardless of
#   the original hostname.

__author__ = 'buzzsurfr'
__version__ = '0.1'

#  Standard Library
import sys
import itertools

#  Related Third-Party
import getpass

#  Local Application/Library Specific
import bigsuds

def bigip_active(hostname, username='admin', password='admin', debug=False, cachedir=None, verify=False, timeout=90):
	#  Connect to specified BIG-IP
	b = bigsuds.BIGIP(hostname, username, password, debug, cachedir, verify, timeout)

	#  Determine whether device is active
	if(b.Management.DeviceGroup.get_failover_status()['status'] != 'ACTIVE'):
		local_device = b.Management.Device.get_local_device()
		new_device = False
		for device in list(set(itertools.chain.from_iterable(b.Management.DeviceGroup.get_device(b.Management.DeviceGroup.get_list())))).remove(local_device):
			if(b.Management.Device.get_failover_state(device) == 'HA_STATE_ACTIVE'):
				new_device = device
		if(new_device):
			print b.Management.Device.get_local_device()[8:]+" is not active.  Switching to "+new_device[8:]
			b = bigsuds.BIGIP(new_device[8:], username, password, debug, cachedir, verify, timeout)
	return b

if __name__ == '__main__':
	bigip_active(sys.argv[1], sys.argv[2], getpass.getpass())
