import socket
import struct

def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]

ip_arr_24 = {}
ip_arr_32 = {}
ck24_count = 0
ck32_count = 0
saill = 0.0
sailbm = 0.0

with open("Routes/fib6") as f:
    for line in f:
        # Do something with 'line'
	arr = line.replace("\r\n", "").split("\t")
	prefix = arr[0].split("/")
	if int(prefix[1]) >= 17 and int(prefix[1]) <= 24 :
          ip = ip2int(prefix[0]) >> 16
          if ip not in ip_arr_24 :
	    ck24_count += 1
	    ip_arr_24[ip] = True	                  
	elif  int(prefix[1]) > 24 :
          ip = ip2int(prefix[0]) >> 8
          if ip not in ip_arr_32 :
	    ck32_count += 1
	    ip_arr_32[ip] = True	                  
    print "ck24_count=", ck24_count
    print "ck32_count=", ck32_count

    if ck32_count > 0:
    	saill = (64 + 128 + ((ck24_count * 256)/1024) + ((ck24_count * 4 * 256)/1024) + ((ck32_count * 256)/1024))/1024.0
    else:
    	saill = (64 + 128 + ((ck24_count * 256)/1024))/1024.0

    sailbm = (64 + 128 + ((ck24_count * 256)/1024) + ((ck32_count * 68)/1024) + ((ck32_count * 256)/1024))/1024.0

    print "sail-l=", saill
    print "sail-bm=", sailbm
