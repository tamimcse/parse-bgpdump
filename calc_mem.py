import socket
import struct

def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]

ip_arr_24 = {}
ip_arr_32 = {}
ck24_count = 0
ck32_count = 0

with open("Routes/fib1") as f:
    for line in f:
        # Do something with 'line'
	arr = line.replace("\r\n", "").split("\t")
	prefix = arr[0].split("/")
	if int(prefix[1]) >= 17 and int(prefix[1]) <= 24 :
          ip = ip2int(prefix[0]) >> 16
          if ip not in ip_arr_24 :
	    ck24_count += 1
	    ip_arr_24[ip] = True	                  
            print "ck24_count=", ck24_count
	elif  int(prefix[1]) > 24 :
          ip = ip2int(prefix[0]) >> 8
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True	                  
            print "ck32_count=", ck32_count
