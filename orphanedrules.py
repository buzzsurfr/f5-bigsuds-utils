#!/usr/bin/env python

__author__ = 'buzzsurfr'
__version__ = '0.1'

def get_orphaned_rules(obj, recursive = True):
	'''
	Gets a list of orphaned rules.
	
	Prototype
		String [] get_orphaned_rules(
			BIGIP.bigip obj,
			bool recursive = True
		);
	
	Parameters
		obj of type BIGIP.bigip contains the established connection.
		recursive of type boolean indicates whether to perform a recursive search throughout the entire configuration.  Defaults to True.
	
	Return Type
		String [] containing the list of all orphaned rules.
	'''
	
	#  Get current values to override for search
	active_folder = obj.System.Session.get_active_folder()
	recursive_query_state = obj.System.Session.get_recursive_query_state()

	#  Enable fully-recursive search
	if recursive:
		obj.System.Session.set_active_folder('/')
		obj.System.Session.set_recursive_query_state("STATE_ENABLED")
	
	#  Get list of iRules
	rules = obj.LocalLB.Rule.get_list()
	
	#  Create starting list of orphaned iRules.  These will be removed from
	#  list as they are found to be in use.
	orphaned_rules = rules
	
	#  Get list of all iRules associated on virtual servers
	vs_rules = obj.LocalLB.VirtualServer.get_rule(obj.LocalLB.VirtualServer.get_list())
	
	#  Check each virtual server for iRules and remove from orphaned if exists
	for virtual_server in vs_rules:
		for rule in virtual_server:
			if rule['rule_name'] in rules:
				#  If found, remove from orphaned_rules
				orphaned_rules.remove(rule['rule_name'])
	
	#  Reset values overridden for search
	if recursive:
		obj.System.Session.set_active_folder(active_folder)
		obj.System.Session.set_recursive_query_state(recursive_query_state)
	
	return orphaned_rules

#  Instance Mode (Run as script)
if __name__ == "__main__":

	#  Standard Library
	import sys

	#  Related Third-Party
	import getpass

	#  Local Application/Library Specific
	import bigsuds

	if len(sys.argv) < 3:
		print "\n\n\tUsage: %s ip_address username" % sys.argv[0]
		sys.exit()
	
	#  Get password from CLI
	userpass = getpass.getpass()
	
	#  Connect to BIG-IP
	try:
		bigconn = bigsuds.BIGIP(
			hostname = sys.argv[1],
			username = sys.argv[2],
			password = userpass
		)
	except Exception as e:
		print e

	orphans = get_orphaned_rules(bigconn)

	print "Orphaned iRules"
	for orphan in orphans:
		print "\t" + orphan
