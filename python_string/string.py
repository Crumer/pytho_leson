tunnel= """
	interface Tunnel0
	ip add 10.10.10.1 255.255.255.0
	ip mtu 1416
	ip ospf hello interval 5
	tunnel souce fasteth1/0
	tunnel protect ipsec profile DMVPN
	"""
print(tunnel)