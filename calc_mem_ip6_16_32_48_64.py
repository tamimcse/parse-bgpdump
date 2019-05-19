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

ip_arr_32 = {}
ip_arr_48 = {}
ip_arr_64 = {}
ck32_count = 0
ck48_count = 0
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
#	print ip6_to_integer(prefix[0]) >> 64
	if int(prefix[1]) > 16 and int(prefix[1]) <= 32 :
          ip = ip6_to_integer(prefix[0]) >> (48 + 64)
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True
	elif int(prefix[1]) > 32 and int(prefix[1]) <= 48 :
          ip = ip6_to_integer(prefix[0]) >> (32 + 64)
          if ip not in ip_arr_48 :
	    ck48_count += 1
	    ip_arr_48[ip] = True
          ip = ip6_to_integer(prefix[0]) >> (48 + 64)
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True
	elif  int(prefix[1]) > 48 and int(prefix[1]) <= 64 :
          ip = ip6_to_integer(prefix[0]) >> (16 + 64)
          if ip not in ip_arr_64 :
	    ck64_count += 1
	    ip_arr_64[ip] = True
          ip = ip6_to_integer(prefix[0]) >> (32 + 64)
          if ip not in ip_arr_48 :
	    ck48_count += 1
	    ip_arr_48[ip] = True
          ip = ip6_to_integer(prefix[0]) >> (48 + 64)
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True
	elif  int(prefix[1]) > 64 :
	    ck120_count += 1

    print "ck32_count=", ck32_count
    print "ck48_count=", ck48_count
    print "ck64_count=", ck64_count
    print "ck120_count=", ck120_count
