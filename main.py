import threading,time
#from scapy.all import *
import socket
ip = "ip"
nthreads = 128
tout = 0.0
tout = 0.0
socket.setdefaulttimeout(tout)
#socket.
#eeto=[None for __ in range(jj)]
#conf.verb=False
#iph=IP(dst=ip)
def chkport(port,ind):
	
	for p in range(port, port+(65536//nthreads)):
		#try:
			#print(p,ind)
			#socket.socket(2,socket.SOCK_RAW, socket.IPPROTO_TCP)
			#eeto[ind] = 
			#for __ in range(10):
				#socket.socket(2,1).connect_ex((ip,p))
				#time.sleep(0.05)
				#tete.close()
			socket.socket(2,1).connect_ex((ip,p))
			time.sleep(0.03)
			#send(iph/TCP(dport=p, flags="S"))
			#send(iph/TCP(dport=p,flags="R"))
			#eeto[ind].connect_ex((ip,p))
			
			#eeto[ind].send(bytes(4))
			#print(p)
			
		#except Exception as e:
			#print(e)
		#finally:
			#eeto[ind].
			#time.sleep(tout)
			#...
	#print(f"Thread {ind}:", time.time()-st)
		#n個のスレッドで、指定された範囲のポートスキャンを回す

if __name__ == "__main__":
	#multiprocessing.freeze_support()
	st=time.time()
	for i in range(jj):
		_=threading.Thread(target=chkport, args=(65536//jj*i,i))
		_.start()
		#_=multiprocessing.Process(target=chkport, args=(65536//jj*i,i))
		#_.start()
			#print(i,j )
		#print(jj*i+j)
	
		#time.sleep(tout)
		#time.sleep(0.5)
	_.join()
		
	
		
	print(time.time()-st)
