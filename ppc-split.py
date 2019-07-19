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
n32_cnt = 0
n40_cnt = 0
n48_cnt = 0
n64_cnt = 0
ppc = 0
sail = 0

filename = "routes-53828" 

with open("ipv6-fibs/" + filename) as f:
    for line in f:
        # Do something with 'line'
	arr = line.replace("\r\n", "").split("\t")
	prefix = arr[0].split("/")
#       Extract 64-bit from the 128-bit prefix
	prefix64 = ip6_to_integer(prefix[0]) >> 64
	if int(prefix[1]) > 16 and int(prefix[1]) <= 32 :
          ip = prefix64 >> 48
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True
            n32_cnt += 1 << (32 - int(prefix[1]))

	elif int(prefix[1]) > 32 and int(prefix[1]) <= 40 :
          ip = prefix64 >> 32
          if ip not in ip_arr_40 :
	    ck40_count += 1
	    ip_arr_40[ip] = True
            n40_cnt += 1 << (40 - int(prefix[1]))

          ip = prefix64 >> 48
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True

	elif int(prefix[1]) > 40 and int(prefix[1]) <= 48 :
          ip = prefix64 >> 24
          if ip not in ip_arr_48 :
	    ck48_count += 1
	    ip_arr_48[ip] = True
            n48_cnt += 1 << (48 - int(prefix[1]))

          ip = prefix64 >> 32
          if ip not in ip_arr_40 :
	    ck40_count += 1
	    ip_arr_40[ip] = True

          ip = prefix64 >> 48
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True

	elif  int(prefix[1]) > 48 and int(prefix[1]) <= 64 :
          ip = prefix64 >> 16
          if ip not in ip_arr_64 :
	    ck64_count += 1
	    ip_arr_64[ip] = True
            n64_cnt += 1 << (64 - int(prefix[1]))

          ip = prefix64 >> 24
          if ip not in ip_arr_48 :
	    ck48_count += 1
	    ip_arr_48[ip] = True

          ip = prefix64 >> 32
          if ip not in ip_arr_40 :
	    ck40_count += 1
	    ip_arr_40[ip] = True

          ip = prefix64 >> 48
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True

    print "ck32_count=", ck32_count
    print "ck40_count=", ck40_count
    print "ck48_count=", ck48_count
    print "ck64_count=", ck64_count
    print "n32_cnt=", n32_cnt
    print "n40_cnt=", n40_cnt
    print "n48_cnt=", n48_cnt
    print "n64_cnt=", n64_cnt

    ppc = (65536.0 * 3 + n32_cnt + n40_cnt + n48_cnt + n64_cnt + ck32_count * 20 * 1024 + + ck64_count * 10 * 1024 + (ck40_count + ck48_count) * 10 * 4)/(1024*1024)
    print "PPC=", ppc , "MB"

