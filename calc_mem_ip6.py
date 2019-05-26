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

ip_arr_24 = {}
ip_arr_32 = {}
ip_arr_40 = {}
ip_arr_48 = {}
ip_arr_56 = {}
ip_arr_64 = {}
ck24_count = 0
ck32_count = 0
ck40_count = 0
ck48_count = 0
ck56_count = 0
ck64_count = 0
ppc = 0
sail = 0

filename = "ipv6-fibs/routes-19653" 

with open(filename) as f:
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

	elif int(prefix[1]) > 32 and int(prefix[1]) <= 40 :
          ip = ip6_to_integer(prefix[0]) >> (32 + 64)
          if ip not in ip_arr_40 :
	    ck40_count += 1
	    ip_arr_40[ip] = True

          ip = ip6_to_integer(prefix[0]) >> (48 + 64)
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True

	elif int(prefix[1]) > 40 and int(prefix[1]) <= 48 :
          ip = ip6_to_integer(prefix[0]) >> (24 + 64)
          if ip not in ip_arr_48 :
	    ck48_count += 1
	    ip_arr_48[ip] = True

          ip = ip6_to_integer(prefix[0]) >> (32 + 64)
          if ip not in ip_arr_40 :
	    ck40_count += 1
	    ip_arr_40[ip] = True

          ip = ip6_to_integer(prefix[0]) >> (48 + 64)
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True

	elif  int(prefix[1]) > 48 and int(prefix[1]) <= 64 :
          ip = ip6_to_integer(prefix[0]) >> (16 + 64)
          if ip not in ip_arr_64 :
	    ck64_count += 1
	    ip_arr_64[ip] = True

          ip = ip6_to_integer(prefix[0]) >> (24 + 64)
          if ip not in ip_arr_48 :
	    ck48_count += 1
	    ip_arr_48[ip] = True

          ip = ip6_to_integer(prefix[0]) >> (32 + 64)
          if ip not in ip_arr_40 :
	    ck40_count += 1
	    ip_arr_40[ip] = True

          ip = ip6_to_integer(prefix[0]) >> (48 + 64)
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True

    print "ck32_count=", ck32_count
    print "ck40_count=", ck40_count
    print "ck48_count=", ck48_count
    print "ck64_count=", ck64_count

    ppc = (65536 * 3 + (ck32_count + ck64_count) * 65536 + (ck40_count + ck48_count) * 256 + ck32_count * 10 * 1024 + (ck40_count + ck48_count) * 10 * 4)/(1024*1024)
    sail = (65536 * 3 + (ck32_count + ck64_count) * 65536 + (ck40_count + ck48_count) * 256 + ck32_count * 65536 * 4 + (ck40_count + ck48_count) * 256 * 4)/(1024*1024)
    print "PPC=", ppc , "MB"
    print "SAIL-16-32-40-48-64 =", sail, "MB"

################ Splitting by 8 bit ###############################

ip_arr_24 = {}
ip_arr_32 = {}
ip_arr_40 = {}
ip_arr_48 = {}
ip_arr_56 = {}
ip_arr_64 = {}
ck24_count = 0
ck32_count = 0
ck40_count = 0
ck48_count = 0
ck56_count = 0
ck64_count = 0
ppc = 0
sail = 0

with open(filename) as f:
    for line in f:
	arr = line.replace("\r\n", "").split("\t")
	prefix = arr[0].split("/")
	if int(prefix[1]) > 16 and int(prefix[1]) <= 24 :
          ip = ip6_to_integer(prefix[0]) >> (48 + 64)
          if ip not in ip_arr_24 :
	    ck24_count += 1
	    ip_arr_24[ip] = True
	elif int(prefix[1]) > 24 and int(prefix[1]) <= 32 :
          ip = ip6_to_integer(prefix[0]) >> (40 + 64)
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True
          ip = ip6_to_integer(prefix[0]) >> (48 + 64)
          if ip not in ip_arr_24 :
	    ck24_count += 1
	    ip_arr_24[ip] = True
	elif int(prefix[1]) > 32 and int(prefix[1]) <= 40 :
          ip = ip6_to_integer(prefix[0]) >> (32 + 64)
          if ip not in ip_arr_40 :
	    ck40_count += 1
	    ip_arr_40[ip] = True
          ip = ip6_to_integer(prefix[0]) >> (40 + 64)
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True
          ip = ip6_to_integer(prefix[0]) >> (48 + 64)
          if ip not in ip_arr_24 :
	    ck24_count += 1
	    ip_arr_24[ip] = True
	elif int(prefix[1]) > 40 and int(prefix[1]) <= 48 :
          ip = ip6_to_integer(prefix[0]) >> (24 + 64)
          if ip not in ip_arr_48 :
	    ck48_count += 1
	    ip_arr_48[ip] = True
          ip = ip6_to_integer(prefix[0]) >> (32 + 64)
          if ip not in ip_arr_40 :
	    ck40_count += 1
	    ip_arr_40[ip] = True
          ip = ip6_to_integer(prefix[0]) >> (40 + 64)
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True
          ip = ip6_to_integer(prefix[0]) >> (48 + 64)
          if ip not in ip_arr_24 :
	    ck24_count += 1
	    ip_arr_24[ip] = True
	elif  int(prefix[1]) > 48 and int(prefix[1]) <= 56 :
          ip = ip6_to_integer(prefix[0]) >> (16 + 64)
          if ip not in ip_arr_56 :
	    ck56_count += 1
	    ip_arr_56[ip] = True
          ip = ip6_to_integer(prefix[0]) >> (24 + 64)
          if ip not in ip_arr_48 :
	    ck48_count += 1
	    ip_arr_48[ip] = True
          ip = ip6_to_integer(prefix[0]) >> (32 + 64)
          if ip not in ip_arr_40 :
	    ck40_count += 1
	    ip_arr_40[ip] = True
          ip = ip6_to_integer(prefix[0]) >> (40 + 64)
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True
          ip = ip6_to_integer(prefix[0]) >> (48 + 64)
          if ip not in ip_arr_24 :
	    ck24_count += 1
	    ip_arr_24[ip] = True
	elif  int(prefix[1]) > 56 and int(prefix[1]) <= 64 :
          ip = ip6_to_integer(prefix[0]) >> (8 + 64)
          if ip not in ip_arr_64 :
	    ck64_count += 1
	    ip_arr_64[ip] = True
          ip = ip6_to_integer(prefix[0]) >> (16 + 64)
          if ip not in ip_arr_56 :
	    ck56_count += 1
	    ip_arr_56[ip] = True
          ip = ip6_to_integer(prefix[0]) >> (24 + 64)
          if ip not in ip_arr_48 :
	    ck48_count += 1
	    ip_arr_48[ip] = True
          ip = ip6_to_integer(prefix[0]) >> (32 + 64)
          if ip not in ip_arr_40 :
	    ck40_count += 1
	    ip_arr_40[ip] = True
          ip = ip6_to_integer(prefix[0]) >> (40 + 64)
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True
          ip = ip6_to_integer(prefix[0]) >> (48 + 64)
          if ip not in ip_arr_24 :
	    ck24_count += 1
	    ip_arr_24[ip] = True


    print "ck24_count=", ck24_count
    print "ck32_count=", ck32_count
    print "ck40_count=", ck40_count
    print "ck48_count=", ck48_count
    print "ck56_count=", ck56_count
    print "ck64_count=", ck64_count


    sail = (65536 * 3 + (ck24_count + ck32_count + ck40_count + ck48_count + ck56_count + ck64_count) * 256 + (ck24_count + ck32_count + ck40_count + ck48_count + ck56_count) * 256 * 2)/(1024*1024)
    print "SAIL-16-24-32-40-48-56-64 =", sail, "MB"
