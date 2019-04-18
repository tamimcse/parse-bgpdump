from socket import inet_pton, AF_INET6
from struct import unpack
import socket
import struct

def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]

def ip6_to_integer(ip6):
    ip6 = inet_pton(AF_INET6, ip6)
    a, b = unpack(">QQ", ip6)
    return (a << 64) | b

ip_arr_26 = {}
ip_arr_36 = {}
ip_arr_46 = {}
ip_arr_56 = {}
ip_arr_66 = {}
ck26_count = 0
ck36_count = 0
ck46_count = 0
ck56_count = 0
ck66_count = 0
ck120_count = 0
saill = 0.0
sailbm = 0.0

CHUNK = 65536

with open("ipv6-fibs/routes-53828") as f:
    for line in f:
        # Do something with 'line'
	arr = line.replace("\r\n", "").split("\t")
	prefix = arr[0].split("/")
#	print prefix
	if int(prefix[1]) > 16 and int(prefix[1]) <= 26 :
          ip = ip6_to_integer(prefix[0]) >> (48 + 64)
          if ip not in ip_arr_26 :
	    ck26_count += 1
	    ip_arr_26[ip] = True
	elif int(prefix[1]) > 26 and int(prefix[1]) <= 36 :
          ip = ip6_to_integer(prefix[0]) >> (38 + 64)
          if ip not in ip_arr_36 :
	    ck36_count += 1
	    ip_arr_36[ip] = True
	elif int(prefix[1]) > 36 and int(prefix[1]) <= 46 :
          ip = ip6_to_integer(prefix[0]) >> (28 + 64)
          if ip not in ip_arr_46 :
	    ck46_count += 1
	    ip_arr_46[ip] = True
	elif  int(prefix[1]) > 46 and int(prefix[1]) <= 56 :
          ip = ip6_to_integer(prefix[0]) >> (18 + 64)
          if ip not in ip_arr_56 :
	    ck56_count += 1
	    ip_arr_56[ip] = True
	elif  int(prefix[1]) > 56 and int(prefix[1]) <= 66 :
          ip = ip6_to_integer(prefix[0]) >> (8 + 64)
          if ip not in ip_arr_66 :
	    ck66_count += 1
	    ip_arr_66[ip] = True
	elif  int(prefix[1]) > 64 :
	    ck120_count += 1
    print "ck26_count=", ck26_count
    print "ck36_count=", ck36_count
    print "ck46_count=", ck46_count
    print "ck56_count=", ck56_count
    print "ck66_count=", ck66_count
    print "ck120_count=", ck120_count
