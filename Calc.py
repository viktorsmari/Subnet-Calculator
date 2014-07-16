import sys
import os

''' 
The broadcast address for an IPv4 host can be obtained by performing
a bitwise OR operation between the bit complement of the subnet 
mask and the host's IP address.
'''

myip = '134.77.168.143'
mysub = '255.255.255.224'

total = len(sys.argv)
if total > 2 :
	myip = sys.argv[1]
	mysub = sys.argv[2]


# Change string arguments to a list
iplist = myip.split('.') 
sublist = mysub.split('.')

# Ip AND subnet mask = Network Address
nwlist = ['a','b','c','d'] 
nwlist[0] = str(int(iplist[0]) & int(sublist[0]))
nwlist[1] = str(int(iplist[1]) & int(sublist[1]))
nwlist[2] = str(int(iplist[2]) & int(sublist[2]))
nwlist[3] = str(int(iplist[3]) & int(sublist[3]))

# Bit complement of Subnet Mask OR Host IP
bclist = ['a','b','c','d'] 
bclist[0] = str( int(iplist[0]) | ~int(sublist[0]) + 256)
bclist[1] = str( int(iplist[1]) | ~int(sublist[1]) + 256)
bclist[2] = str( int(iplist[2]) | ~int(sublist[2]) + 256)
bclist[3] = str( int(iplist[3]) | ~int(sublist[3]) + 256)

# Change all lists to strings 
str_nw_addr = '.'.join(nwlist)
str_bc_addr = '.'.join(bclist)

# Figure out Class and Max hosts
if (int(sublist[0])) < 255:
	netclass = 'A'
	maxhosts = (256-int(sublist[0])) * 256**3

elif (int(sublist[1])) < 255:
	netclass = 'A'
	maxhosts = (256-int(sublist[1])) * 256**2

elif (int(sublist[2])) < 255:
	netclass = 'B'
	maxhosts = (256-int(sublist[2])) * 256

else:
	netclass = 'C'
	maxhosts = 256-int(sublist[3])

#Remember to withdraw 2 addresses, (1 bcast + 1 net base) !

print "\t****| Network calculator |****\n"
print "\tThis host is a part of netw \t : " + str_nw_addr
print "\tMaximum of hosts on the net \t :" ,maxhosts - 2
print "\tThe broadcast address is    \t : " + str_bc_addr
print "\tAnd the network is a class  \t : " + netclass
