import threading,time
#from scapy.all import *
import socket
ip = ""
nthreads = 128
tout = 0.0
socket.setdefaulttimeout(tout)

def chkport(port,ind):
	
	for p in range(port, port+(65536//nthreads)):

			socket.socket(2,1).connect_ex((ip,p))
			time.sleep(0.03)


if __name__ == "__main__":

	st=time.time()
	for i in range(nthreads):
		_=threading.Thread(target=chkport, args=(65536//nthreads*i,i))
		_.start()

	_.join()
		
	
		
	print(time.time()-st)
