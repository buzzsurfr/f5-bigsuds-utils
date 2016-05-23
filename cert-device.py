#!/usr/bin/env python

__author__ = 'buzzsurfr'
__version__ = '0.1'

def get_device_certificate(api):
	'''
	Gets device certificate information from multiple F5 BIG-IP devices.

	Prototype
		dict get_device_certificate(
			BIGIP.bigip api,
		);

	Parameters
		api of type BIGIP.bigip contains the established connection.

	Return Type
		dict containing the certificate properties.
	'''

	return api.Management.KeyCertificate.get_certificate_list_v2('MANAGEMENT_MODE_WEBSERVER')[0]['certificate']

#  Standard Library
import sys
import re

#  Related Third-Party
import getpass

#  Local Application/Library Specific
import bigsuds

if len(sys.argv) < 3:
	print "\n\n\tUsage: %s user host ..." % sys.argv[0]
	sys.exit()

#  Get login password from CLI
userpass = getpass.getpass()

#  Store results in variables for all hosts as dict
result = {}

#  Iterate over hosts
for host in sys.argv[2:]:

	#  Connect to BIG-IP
	api = bigsuds.BIGIP(host, sys.argv[1], userpass)
	api = api.with_session_id()

	result[host] = get_device_certificate(api)

#  Get console output column widths
space = 2
columns = {}
columns['host'] = max([len(host) for host in result])
columns['subject'] = max([len(cert['subject']['common_name']) for cert in result.values()])
columns['issuer'] = max([len(cert['issuer']['common_name']) for cert in result.values()])
columns['bit_length'] = 4
columns['expiration_string'] = max([len(cert['expiration_string']) for cert in result.values()])
print_string = "%-"+str(columns['host'])+"s"+(' '*space)+\
               "%-"+str(columns['subject'])+"s"+(' '*space)+\
			   "%-"+str(columns['issuer'])+"s"+(' '*space)+\
			   "%"+str(columns['bit_length'])+"s"+(' '*space)+\
			   "%-"+str(columns['expiration_string'])+"s"

#  Output to console
print print_string % ("Host", "Subject", "Issuer", "Bits", "Expiration Date")
print print_string % ('='*columns['host'], '='*columns['subject'], '='*columns['issuer'], '====', '='*columns['expiration_string'])
for host, certificate in result.iteritems():
	print print_string % (host, certificate['subject']['common_name'], certificate['issuer']['common_name'], str(certificate['bit_length']), certificate['expiration_string'])
