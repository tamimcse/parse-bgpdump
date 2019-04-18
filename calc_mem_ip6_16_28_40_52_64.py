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

ip_arr_28 = {}
ip_arr_40 = {}
ip_arr_52 = {}
ip_arr_64 = {}
ck28_count = 0
ck40_count = 0
ck52_count = 0
ck64_count = 0
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
	if int(prefix[1]) > 16 and int(prefix[1]) <= 28 :
          ip = ip6_to_integer(prefix[0]) >> (48 + 64)
          if ip not in ip_arr_28 :
	    ck28_count += 1
	    ip_arr_28[ip] = True
	elif int(prefix[1]) > 28 and int(prefix[1]) <= 40 :
          ip = ip6_to_integer(prefix[0]) >> (36 + 64)
          if ip not in ip_arr_40 :
	    ck40_count += 1
	    ip_arr_40[ip] = True
	elif  int(prefix[1]) > 40 and int(prefix[1]) <= 52 :
          ip = ip6_to_integer(prefix[0]) >> (24 + 64)
          if ip not in ip_arr_52 :
	    ck52_count += 1
	    ip_arr_52[ip] = True
	elif  int(prefix[1]) > 52 and int(prefix[1]) <= 64 :
          ip = ip6_to_integer(prefix[0]) >> (12 + 64)
          if ip not in ip_arr_64 :
	    ck64_count += 1
	    ip_arr_64[ip] = True
	elif  int(prefix[1]) > 64 :
	    ck120_count += 1
    print "ck28_count=", ck28_count
    print "ck40_count=", ck40_count
    print "ck52_count=", ck52_count
    print "ck64_count=", ck64_count
    print "ck120_count=", ck120_count
