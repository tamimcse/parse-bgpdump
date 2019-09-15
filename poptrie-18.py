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

	ip_arr_24 = {}
	ip_arr_30 = {}
	ip_arr_36 = {}
	ip_arr_42 = {}
	ip_arr_48 = {}
	ip_arr_54 = {}
	ip_arr_60 = {}
	ip_arr_64 = {}
	ck24_count = 0
	ck30_count = 0
	ck36_count = 0
	ck42_count = 0
	ck48_count = 0
	ck54_count = 0
	ck60_count = 0
	ck64_count = 0
	n24_cnt = 0
	n30_cnt = 0
	n36_cnt = 0
	n42_cnt = 0
	n48_cnt = 0
	n54_cnt = 0
	n60_cnt = 0
	n64_cnt = 0
        total_n = 0

        prefix_count = 0

	poptrie = 0
  
	with open("ipv6-fibs/" + filename) as f:
	    for line in f:
		# Do something with 'line'
		arr = line.replace("\r\n", "").split("\t")
		prefix = arr[0].split("/")
	#       Extract 64-bit from the 128-bit prefix
		prefix64 = ip6_to_integer(prefix[0]) >> 64

                prefix_count += 1

		if int(prefix[1]) > 18 and int(prefix[1]) <= 24 :
		  ip = prefix64 >> 46
		  if ip not in ip_arr_24 :
		    ck24_count += 1
		    ip_arr_24[ip] = True
		  n24_cnt += 1 << (24 - int(prefix[1]))

		if int(prefix[1]) > 24 and int(prefix[1]) <= 30 :
		  ip = prefix64 >> 40
		  if ip not in ip_arr_30 :
		    ck30_count += 1
		    ip_arr_30[ip] = True
		  n30_cnt += 1 << (30 - int(prefix[1]))

		  ip = prefix64 >> 46
		  if ip not in ip_arr_24 :
		    ck24_count += 1
		    ip_arr_24[ip] = True

		elif int(prefix[1]) > 30 and int(prefix[1]) <= 36 :
		  ip = prefix64 >> 34
		  if ip not in ip_arr_36 :
		    ck36_count += 1
		    ip_arr_36[ip] = True
		  n36_cnt += 1 << (36 - int(prefix[1]))

		  ip = prefix64 >> 40
		  if ip not in ip_arr_30 :
		    ck30_count += 1
		    ip_arr_30[ip] = True

		  ip = prefix64 >> 46
		  if ip not in ip_arr_24 :
		    ck24_count += 1
		    ip_arr_24[ip] = True

		elif int(prefix[1]) > 36 and int(prefix[1]) <= 42 :
		  ip = prefix64 >> 28
		  if ip not in ip_arr_42 :
		    ck42_count += 1
		    ip_arr_42[ip] = True
		  n42_cnt += 1 << (42 - int(prefix[1]))

		  ip = prefix64 >> 34
		  if ip not in ip_arr_36 :
		    ck36_count += 1
		    ip_arr_36[ip] = True

		  ip = prefix64 >> 40
		  if ip not in ip_arr_30 :
		    ck30_count += 1
		    ip_arr_30[ip] = True

		  ip = prefix64 >> 46
		  if ip not in ip_arr_24 :
		    ck24_count += 1
		    ip_arr_24[ip] = True

		elif int(prefix[1]) > 42 and int(prefix[1]) <= 48 :
		  ip = prefix64 >> 22
		  if ip not in ip_arr_48 :
		    ck48_count += 1
		    ip_arr_48[ip] = True
		  n48_cnt += 1 << (48 - int(prefix[1]))

		  ip = prefix64 >> 28
		  if ip not in ip_arr_42 :
		    ck42_count += 1
		    ip_arr_42[ip] = True

		  ip = prefix64 >> 34
		  if ip not in ip_arr_36 :
		    ck36_count += 1
		    ip_arr_36[ip] = True

		  ip = prefix64 >> 40
		  if ip not in ip_arr_30 :
		    ck30_count += 1
		    ip_arr_30[ip] = True

		  ip = prefix64 >> 46
		  if ip not in ip_arr_24 :
		    ck24_count += 1
		    ip_arr_24[ip] = True

		elif int(prefix[1]) > 48 and int(prefix[1]) <= 54 :
		  ip = prefix64 >> 16
		  if ip not in ip_arr_54 :
		    ck54_count += 1
		    ip_arr_54[ip] = True
		  n54_cnt += 1 << (54 - int(prefix[1]))

		  ip = prefix64 >> 22
		  if ip not in ip_arr_48 :
		    ck48_count += 1
		    ip_arr_48[ip] = True

		  ip = prefix64 >> 28
		  if ip not in ip_arr_42 :
		    ck42_count += 1
		    ip_arr_42[ip] = True

		  ip = prefix64 >> 34
		  if ip not in ip_arr_36 :
		    ck36_count += 1
		    ip_arr_36[ip] = True

		  ip = prefix64 >> 40
		  if ip not in ip_arr_30 :
		    ck30_count += 1
		    ip_arr_30[ip] = True

		  ip = prefix64 >> 46
		  if ip not in ip_arr_24 :
		    ck24_count += 1
		    ip_arr_24[ip] = True

		elif int(prefix[1]) > 54 and int(prefix[1]) <= 60 :
		  ip = prefix64 >> 10
		  if ip not in ip_arr_60 :
		    ck60_count += 1
		    ip_arr_60[ip] = True
		  n60_cnt += 1 << (60 - int(prefix[1]))

		  ip = prefix64 >> 16
		  if ip not in ip_arr_54 :
		    ck54_count += 1
		    ip_arr_54[ip] = True

		  ip = prefix64 >> 22
		  if ip not in ip_arr_48 :
		    ck48_count += 1
		    ip_arr_48[ip] = True

		  ip = prefix64 >> 28
		  if ip not in ip_arr_42 :
		    ck42_count += 1
		    ip_arr_42[ip] = True

		  ip = prefix64 >> 34
		  if ip not in ip_arr_36 :
		    ck36_count += 1
		    ip_arr_36[ip] = True

		  ip = prefix64 >> 40
		  if ip not in ip_arr_30 :
		    ck30_count += 1
		    ip_arr_30[ip] = True

		  ip = prefix64 >> 46
		  if ip not in ip_arr_24 :
		    ck24_count += 1
		    ip_arr_24[ip] = True

		elif int(prefix[1]) > 60 and int(prefix[1]) <= 64 :
		  ip = prefix64 >> 4
		  if ip not in ip_arr_64 :
		    ck64_count += 1
		    ip_arr_64[ip] = True
		  n64_cnt += 1 << (64 - int(prefix[1]))

		  ip = prefix64 >> 10
		  if ip not in ip_arr_60 :
		    ck60_count += 1
		    ip_arr_60[ip] = True

		  ip = prefix64 >> 16
		  if ip not in ip_arr_54 :
		    ck54_count += 1
		    ip_arr_54[ip] = True

		  ip = prefix64 >> 22
		  if ip not in ip_arr_48 :
		    ck48_count += 1
		    ip_arr_48[ip] = True

		  ip = prefix64 >> 28
		  if ip not in ip_arr_42 :
		    ck42_count += 1
		    ip_arr_42[ip] = True

		  ip = prefix64 >> 34
		  if ip not in ip_arr_36 :
		    ck36_count += 1
		    ip_arr_36[ip] = True

		  ip = prefix64 >> 40
		  if ip not in ip_arr_30 :
		    ck30_count += 1
		    ip_arr_30[ip] = True

		  ip = prefix64 >> 46
		  if ip not in ip_arr_24 :
		    ck24_count += 1
		    ip_arr_24[ip] = True

	    print "ck24_count=", ck24_count
	    print "ck30_count=", ck30_count
	    print "ck36_count=", ck36_count
	    print "ck42_count=", ck42_count
	    print "ck48_count=", ck48_count
	    print "ck54_count=", ck54_count
	    print "ck60_count=", ck60_count
	    print "ck64_count=", ck64_count
#            total_n = (n22_cnt + n28_cnt + n34_cnt + n40_cnt + n46_cnt + n52_cnt + n58_cnt + n64_cnt);
            total_n = prefix_count * 2
	    print "total_n=", total_n/(1024*1024.0), " MB"
	    
	    #10240 byte is needed for B16 and C16, 0 byte is needed for N16
	    poptrie = (262144 * 3 + total_n + (ck24_count + ck30_count + ck36_count + ck42_count + ck48_count + ck54_count + ck60_count+ ck64_count) * 24)/(1024*1024.0)
	    print filename + "  Poptrie-18=", poptrie , "MB"
