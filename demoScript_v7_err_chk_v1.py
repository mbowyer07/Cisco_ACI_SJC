#!/usr/bin/env python

import sys
from cobra.mit.session import LoginSession
from cobra.mit.access import MoDirectory
from cobra.mit.request import ConfigRequest
from cobra.model.fv import *
import cobra.model.pol
import cobra.model.vz
import csv
import datetime
import os.path

def apic_login(hostname, username, password):
	url = "https://" + hostname
	sess = LoginSession(url, username, password)
	modir = MoDirectory(sess)
	try:
		modir.login()
		print 'Connection Successful'
	except:
		print 'Login error'
		exit(1)
	return modir
pass

def apic_filter_create(tenant_name, filter_name_file):

	filter_file_parse = csv.DictReader(open(filter_name_file))

	index = 2
	for row_name in filter_file_parse:
		filter_name=str(row_name["filter_name"])

		polUni = cobra.model.pol.Uni('')
		fvTenant = cobra.model.fv.Tenant(polUni, tenant_name)

		vzFilter = cobra.model.vz.Filter(fvTenant, ownerKey=u'', name=filter_name, descr=u'', ownerTag=u'')
		
		dToPort=str(row_name["dest_port_end"])
		dFromPort=str(row_name["dest_port_beg"])
		sToPort=str(row_name["src_port_end"])
		sFromPort=str(row_name["src_port_beg"])
		prot=str(row_name["protocol"])
		etherT=str(row_name["ethertype"])
		name=str(row_name["entry_name"])

		vzEntry = cobra.model.vz.Entry(vzFilter, dToPort=dToPort, prot=prot, \
			sFromPort=sFromPort, sToPort=sToPort, etherT=etherT, \
			dFromPort=dFromPort, name=name)
		c = cobra.mit.request.ConfigRequest()
		c.addMo(fvTenant)

	
		try:
			modir.commit(c)
		except:
			print 'Error at row ' + str(index) + '. Please check the csv file for accuracy.'
			now = datetime.datetime.now()
			time_of_err = now.strftime("%m\%d\%Y %H:%M")

			f = open('filter_create_errors.txt', 'a')
			print >> f, (time_of_err + ', ' + 'Error at row ' + str(index) + '. Please check the csv file for accuracy.')
			
		index += 1	

	f.close()

if __name__ == '__main__':
	if len(sys.argv) != 5:
		print 'Usage: demoScript_v2.py <hostname> <username> <password> <tenant_name>'
		sys.exit()
	else:
		hostname, username, password, tenant_name = sys.argv[1:]
		modir = apic_login(hostname, username, password)

		filter_name_file = raw_input('File name for filter creation?\n')
		filetest = os.path.isfile(filter_name_file)
		if filetest == True:
			apic_filter_create(tenant_name, filter_name_file)
		else:
			print 'File does not exist'
	pass
pass