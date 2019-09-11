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

	ip_arr_22 = {}
	ip_arr_28 = {}
	ip_arr_34 = {}
	ip_arr_40 = {}
	ip_arr_46 = {}
	ip_arr_52 = {}
	ip_arr_58 = {}
	ip_arr_64 = {}
	ck22_count = 0
	ck28_count = 0
	ck34_count = 0
	ck40_count = 0
	ck46_count = 0
	ck52_count = 0
	ck58_count = 0
	ck64_count = 0
	n22_cnt = 0
	n28_cnt = 0
	n34_cnt = 0
	n40_cnt = 0
	n46_cnt = 0
	n52_cnt = 0
	n58_cnt = 0
	n64_cnt = 0

	poptrie = 0
  
	with open("ipv6-fibs/" + filename) as f:
	    for line in f:
		# Do something with 'line'
		arr = line.replace("\r\n", "").split("\t")
		prefix = arr[0].split("/")
	#       Extract 64-bit from the 128-bit prefix
		prefix64 = ip6_to_integer(prefix[0]) >> 64

		if int(prefix[1]) > 16 and int(prefix[1]) <= 22 :
		  ip = prefix64 >> 48
		  if ip not in ip_arr_22 :
		    ck22_count += 1
		    ip_arr_22[ip] = True
		  n22_cnt += 1 << (22 - int(prefix[1]))

		if int(prefix[1]) > 22 and int(prefix[1]) <= 28 :
		  ip = prefix64 >> 42
		  if ip not in ip_arr_28 :
		    ck28_count += 1
		    ip_arr_28[ip] = True
		  n28_cnt += 1 << (28 - int(prefix[1]))

		  ip = prefix64 >> 48
		  if ip not in ip_arr_22 :
		    ck22_count += 1
		    ip_arr_22[ip] = True

		elif int(prefix[1]) > 28 and int(prefix[1]) <= 34 :
		  ip = prefix64 >> 36
		  if ip not in ip_arr_34 :
		    ck34_count += 1
		    ip_arr_34[ip] = True
		  n34_cnt += 1 << (34 - int(prefix[1]))

		  ip = prefix64 >> 42
		  if ip not in ip_arr_28 :
		    ck28_count += 1
		    ip_arr_28[ip] = True

		  ip = prefix64 >> 48
		  if ip not in ip_arr_22 :
		    ck22_count += 1
		    ip_arr_22[ip] = True

		elif int(prefix[1]) > 34 and int(prefix[1]) <= 40 :
		  ip = prefix64 >> 30
		  if ip not in ip_arr_40 :
		    ck40_count += 1
		    ip_arr_40[ip] = True
		  n40_cnt += 1 << (40 - int(prefix[1]))

		  ip = prefix64 >> 36
		  if ip not in ip_arr_34 :
		    ck34_count += 1
		    ip_arr_34[ip] = True

		  ip = prefix64 >> 42
		  if ip not in ip_arr_28 :
		    ck28_count += 1
		    ip_arr_28[ip] = True

		  ip = prefix64 >> 48
		  if ip not in ip_arr_22 :
		    ck22_count += 1
		    ip_arr_22[ip] = True

		elif int(prefix[1]) > 40 and int(prefix[1]) <= 46 :
		  ip = prefix64 >> 24
		  if ip not in ip_arr_46 :
		    ck46_count += 1
		    ip_arr_46[ip] = True
		  n46_cnt += 1 << (46 - int(prefix[1]))

		  ip = prefix64 >> 30
		  if ip not in ip_arr_40 :
		    ck40_count += 1
		    ip_arr_40[ip] = True

		  ip = prefix64 >> 36
		  if ip not in ip_arr_34 :
		    ck34_count += 1
		    ip_arr_34[ip] = True

		  ip = prefix64 >> 42
		  if ip not in ip_arr_28 :
		    ck28_count += 1
		    ip_arr_28[ip] = True

		  ip = prefix64 >> 48
		  if ip not in ip_arr_22 :
		    ck22_count += 1
		    ip_arr_22[ip] = True

		elif int(prefix[1]) > 46 and int(prefix[1]) <= 52 :
		  ip = prefix64 >> 18
		  if ip not in ip_arr_52 :
		    ck52_count += 1
		    ip_arr_52[ip] = True
		  n52_cnt += 1 << (52 - int(prefix[1]))

		  ip = prefix64 >> 24
		  if ip not in ip_arr_46 :
		    ck46_count += 1
		    ip_arr_46[ip] = True

		  ip = prefix64 >> 30
		  if ip not in ip_arr_40 :
		    ck40_count += 1
		    ip_arr_40[ip] = True

		  ip = prefix64 >> 36
		  if ip not in ip_arr_34 :
		    ck34_count += 1
		    ip_arr_34[ip] = True

		  ip = prefix64 >> 42
		  if ip not in ip_arr_28 :
		    ck28_count += 1
		    ip_arr_28[ip] = True

		  ip = prefix64 >> 48
		  if ip not in ip_arr_22 :
		    ck22_count += 1
		    ip_arr_22[ip] = True

		elif int(prefix[1]) > 52 and int(prefix[1]) <= 58 :
		  ip = prefix64 >> 12
		  if ip not in ip_arr_58 :
		    ck58_count += 1
		    ip_arr_58[ip] = True
		  n58_cnt += 1 << (58 - int(prefix[1]))

		  ip = prefix64 >> 18
		  if ip not in ip_arr_52 :
		    ck52_count += 1
		    ip_arr_52[ip] = True

		  ip = prefix64 >> 24
		  if ip not in ip_arr_46 :
		    ck46_count += 1
		    ip_arr_46[ip] = True

		  ip = prefix64 >> 30
		  if ip not in ip_arr_40 :
		    ck40_count += 1
		    ip_arr_40[ip] = True

		  ip = prefix64 >> 36
		  if ip not in ip_arr_34 :
		    ck34_count += 1
		    ip_arr_34[ip] = True

		  ip = prefix64 >> 42
		  if ip not in ip_arr_28 :
		    ck28_count += 1
		    ip_arr_28[ip] = True

		  ip = prefix64 >> 48
		  if ip not in ip_arr_22 :
		    ck22_count += 1
		    ip_arr_22[ip] = True

		elif int(prefix[1]) > 58 and int(prefix[1]) <= 64 :
		  ip = prefix64 >> 6
		  if ip not in ip_arr_64 :
		    ck64_count += 1
		    ip_arr_64[ip] = True
		  n64_cnt += 1 << (64 - int(prefix[1]))

		  ip = prefix64 >> 12
		  if ip not in ip_arr_58 :
		    ck58_count += 1
		    ip_arr_58[ip] = True

		  ip = prefix64 >> 18
		  if ip not in ip_arr_52 :
		    ck52_count += 1
		    ip_arr_52[ip] = True

		  ip = prefix64 >> 24
		  if ip not in ip_arr_46 :
		    ck46_count += 1
		    ip_arr_46[ip] = True

		  ip = prefix64 >> 30
		  if ip not in ip_arr_40 :
		    ck40_count += 1
		    ip_arr_40[ip] = True

		  ip = prefix64 >> 36
		  if ip not in ip_arr_34 :
		    ck34_count += 1
		    ip_arr_34[ip] = True

		  ip = prefix64 >> 42
		  if ip not in ip_arr_28 :
		    ck28_count += 1
		    ip_arr_28[ip] = True

		  ip = prefix64 >> 48
		  if ip not in ip_arr_22 :
		    ck22_count += 1
		    ip_arr_22[ip] = True

	    print "ck32_count=", ck32_count
	    print "ck40_count=", ck40_count
	    print "ck48_count=", ck48_count
	    print "ck64_count=", ck64_count
	    print "n32_cnt=", n32_cnt
	    print "n40_cnt=", n40_cnt
	    print "n48_cnt=", n48_cnt
	    print "n64_cnt=", n64_cnt
	    print "total_n=", (n32_cnt + n40_cnt + n48_cnt + n64_cnt)/(1024*1024.0), " MB"
	    
	    #10240 byte is needed for B16 and C16, 0 byte is needed for N16
	    poptrie = (65536 * 3 + n32_cnt + n40_cnt + n48_cnt + n64_cnt + ck32_count * 20 * 1024 + + ck64_count * 10 * 1024 + (ck40_count + ck48_count) * 20 * 4)/(1024*1024.0)
	    print filename + "  PPC=", poptrie , "MB"
