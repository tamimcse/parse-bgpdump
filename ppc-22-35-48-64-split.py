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


filenames = ["routes-293", "routes-852", "routes-19016", "routes-19151", "routes-23367", "routes-53828" ]

for filename in filenames :

	ip_arr_35 = {}
	ip_arr_48 = {}
	ip_arr_64 = {}
	ck35_count = 0
	ck48_count = 0
	ck64_count = 0
	n35_cnt = 0
	n48_cnt = 0
	n64_cnt = 0
	ppc = 0
  
	with open("ipv6-fibs/" + filename) as f:
	    for line in f:
		# Do something with 'line'
		arr = line.replace("\r\n", "").split("\t")
		prefix = arr[0].split("/")
	#       Extract 64-bit from the 128-bit prefix
		prefix64 = ip6_to_integer(prefix[0]) >> 64
		if int(prefix[1]) > 22 and int(prefix[1]) <= 35 :
		  ip = prefix64 >> 42
		  if ip not in ip_arr_35 :
		    ck35_count += 1
		    ip_arr_35[ip] = True
		  n35_cnt += 1 << (35 - int(prefix[1]))

		elif int(prefix[1]) > 35 and int(prefix[1]) <= 48 :
		  ip = prefix64 >> 29
		  if ip not in ip_arr_48 :
		    ck48_count += 1
		    ip_arr_48[ip] = True
		  n48_cnt += 1 << (48 - int(prefix[1]))

		  ip = prefix64 >> 42
		  if ip not in ip_arr_35 :
		    ck35_count += 1
		    ip_arr_35[ip] = True

		elif  int(prefix[1]) > 48 and int(prefix[1]) <= 64 :
		  ip = prefix64 >> 16
		  if ip not in ip_arr_64 :
		    ck64_count += 1
		    ip_arr_64[ip] = True
		  n64_cnt += 1 << (64 - int(prefix[1]))

		  ip = prefix64 >> 29
		  if ip not in ip_arr_48 :
		    ck48_count += 1
		    ip_arr_48[ip] = True

		  ip = prefix64 >> 42
		  if ip not in ip_arr_35 :
		    ck35_count += 1
		    ip_arr_35[ip] = True

	    print "ck35_count=", ck35_count
	    print "ck48_count=", ck48_count
	    print "ck64_count=", ck64_count
	    print "n35_cnt=", n35_cnt
	    print "n48_cnt=", n48_cnt
	    print "n64_cnt=", n64_cnt
	    print "total_n=", (n35_cnt + n48_cnt + n64_cnt)/(1024*1024.0), " MB"

	    ppc = (1310720 + n35_cnt + n48_cnt + n64_cnt + (ck35_count + ck48_count) * 20 * 128 + + ck64_count * 10 * 1024)/(1024*1024)
	    print filename + "  PPC=", ppc , "MB"
