from subprocess import call

with open("Routes/routes-R6") as f:
    for line in f:
        # Do something with 'line'
	arr = line.replace("\r\n", "").split("\t")
    	print arr
	call('sudo /home/tamim/net-next/samples/bpf/sail route add {0} dev {1}'.format(arr[0], arr[1]), shell=True)

