access_temp = [
		'switchport mode access',
		'switchport access vlan {}',
		'switchport nonegotiate',
		'spanning-tree portfast',
		'spanning-tree bpduguard enable'
	      ]
print ('\n'.join(access_temp).format(5))