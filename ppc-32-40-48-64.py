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

filename = "ipv6-fibs/routes-53828" 

with open(filename) as f:
    for line in f:
        # Do something with 'line'
	arr = line.replace("\r\n", "").split("\t")
	prefix = arr[0].split("/")
#	print prefix
#	print ip6_to_integer(prefix[0]) >> 64
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

    ppc = (n32_cnt + n40_cnt + n48_cnt + n64_cnt + ck32_count * 20 * 67108864 + + ck64_count * 10 * 1024 + (ck40_count + ck48_count) * 10 * 4)/(1024*1024)
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
#       Extract 64-bit from the 128-bit prefix
	prefix64 = ip6_to_integer(prefix[0]) >> 64
	if int(prefix[1]) > 16 and int(prefix[1]) <= 24 :
          ip = prefix64 >> 48
          if ip not in ip_arr_24 :
	    ck24_count += 1
	    ip_arr_24[ip] = True
	elif int(prefix[1]) > 24 and int(prefix[1]) <= 32 :
          ip = prefix64 >> 40
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True
          ip = prefix64 >> 48
          if ip not in ip_arr_24 :
	    ck24_count += 1
	    ip_arr_24[ip] = True
	elif int(prefix[1]) > 32 and int(prefix[1]) <= 40 :
          ip = prefix64 >> 32
          if ip not in ip_arr_40 :
	    ck40_count += 1
	    ip_arr_40[ip] = True
          ip = prefix64 >> 40
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True
          ip = prefix64 >> 48
          if ip not in ip_arr_24 :
	    ck24_count += 1
	    ip_arr_24[ip] = True
	elif int(prefix[1]) > 40 and int(prefix[1]) <= 48 :
          ip = prefix64 >> 24
          if ip not in ip_arr_48 :
	    ck48_count += 1
	    ip_arr_48[ip] = True
          ip = prefix64 >> 32
          if ip not in ip_arr_40 :
	    ck40_count += 1
	    ip_arr_40[ip] = True
          ip = prefix64 >> 40
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True
          ip = prefix64 >> 48
          if ip not in ip_arr_24 :
	    ck24_count += 1
	    ip_arr_24[ip] = True
	elif  int(prefix[1]) > 48 and int(prefix[1]) <= 56 :
          ip = prefix64 >> 16
          if ip not in ip_arr_56 :
	    ck56_count += 1
	    ip_arr_56[ip] = True
          ip = prefix64 >> 24
          if ip not in ip_arr_48 :
	    ck48_count += 1
	    ip_arr_48[ip] = True
          ip = prefix64 >> 32
          if ip not in ip_arr_40 :
	    ck40_count += 1
	    ip_arr_40[ip] = True
          ip = prefix64 >> 40
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True
          ip = prefix64 >> 48
          if ip not in ip_arr_24 :
	    ck24_count += 1
	    ip_arr_24[ip] = True
	elif  int(prefix[1]) > 56 and int(prefix[1]) <= 64 :
          ip = prefix64 >> 8
          if ip not in ip_arr_64 :
	    ck64_count += 1
	    ip_arr_64[ip] = True
          ip = prefix64 >> 16
          if ip not in ip_arr_56 :
	    ck56_count += 1
	    ip_arr_56[ip] = True
          ip = prefix64 >> 24
          if ip not in ip_arr_48 :
	    ck48_count += 1
	    ip_arr_48[ip] = True
          ip = prefix64 >> 32
          if ip not in ip_arr_40 :
	    ck40_count += 1
	    ip_arr_40[ip] = True
          ip = prefix64 >> 40
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True
          ip = prefix64 >> 48
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

################ Splitting by 6 bit ###############################

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
poptrie = 0

num_prefixes = 0

with open(filename) as f:
    for line in f:
	arr = line.replace("\r\n", "").split("\t")
	prefix = arr[0].split("/")
	prefix64 = ip6_to_integer(prefix[0]) >> 64
	if int(prefix[1]) > 18 and int(prefix[1]) <= 64 :
	  num_prefixes += 1
	if int(prefix[1]) > 18 and int(prefix[1]) <= 24 :
          ip = prefix64 >> 46
          if ip not in ip_arr_24 :
	    ck24_count += 1
	    ip_arr_24[ip] = True
	elif int(prefix[1]) > 24 and int(prefix[1]) <= 30 :
          ip = prefix64 >> 40
          if ip not in ip_arr_30 :
	    ck30_count += 1
	    ip_arr_30[ip] = True
          ip = prefix64 >> 46
          if ip not in ip_arr_24 :
	    ck24_count += 1
	    ip_arr_24[ip] = True
	elif int(prefix[1]) > 30 and int(prefix[1]) <= 36 :
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
	elif int(prefix[1]) > 36 and int(prefix[1]) <= 42 :
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
	elif  int(prefix[1]) > 42 and int(prefix[1]) <= 48 :
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
	elif  int(prefix[1]) > 48 and int(prefix[1]) <= 54 :
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
	elif  int(prefix[1]) > 54 and int(prefix[1]) <= 60 :
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
	elif  int(prefix[1]) > 60 and int(prefix[1]) <= 64 :
          ip = prefix64 >> 4
          if ip not in ip_arr_64 :
	    ck64_count += 1
	    ip_arr_64[ip] = True


#Assuming number of N entries is 1.5 * num_prefixes
    poptrie = (262144 * 5 + (ck24_count + ck30_count + ck36_count + ck42_count + ck48_count + ck54_count + ck60_count) * 8 * 2 + num_prefixes*1.5*8 + (ck24_count + ck30_count + ck36_count + ck42_count + ck48_count + ck54_count + ck60_count) * 16)/(1024*1024)
    print "Poptrie =", poptrie, "MB"
