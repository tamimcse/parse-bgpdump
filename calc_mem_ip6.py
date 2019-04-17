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
ck32_count = 0
ck48_count = 0
saill = 0.0
sailbm = 0.0

with open("ipv6-fibs/routes-293") as f:
    for line in f:
        # Do something with 'line'
	arr = line.replace("\r\n", "").split("\t")
	prefix = arr[0].split("/")

	if int(prefix[1]) >= 17 and int(prefix[1]) <= 32 :
          ip = ip6_to_integer(prefix[0]) >> 48
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True	                  
	elif  int(prefix[1]) >= 33 and int(prefix[1]) <= 48 :
          ip = (ip6_to_integer(prefix[0]) & 0XFFFF00000000) >> 32
          if ip not in ip_arr_48 :
	    ck48_count += 1
	    ip_arr_48[ip] = True	                  
    print "ck32_count=", ck32_count
    print "ck48_count=", ck48_count

    if ck48_count > 0:
    	saill = (64 + 128 + ((ck32_count * 256)/1024) + ((ck32_count * 4 * 256)/1024) + ((ck48_count * 256)/1024))/1024.0
    else:
    	saill = (64 + 128 + ((ck32_count * 256)/1024))/1024.0

    sailbm = (64 + 128 + ((ck32_count * 256)/1024) + ((ck48_count * 68)/1024) + ((ck48_count * 256)/1024))/1024.0

    print "sail-l=", saill
    print "sail-bm=", sailbm
