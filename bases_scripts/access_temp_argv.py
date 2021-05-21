from sys import argv

interface = argv[1]
vlan = argv[2]

access_temp = [
		    'switchport mode access',
		    'switchport access vlan {}',
		    'switchport nonegotiate',
		    'spanning-tree portfast',
		    'spanning-tree bpduguard enable'
		]

print('interface {}'.format(interface))
print('\n'.join(access_temp).format(vlan))