import socket as sp
import os
s = sp.socket(sp.AF_INET , sp.SOCK_DGRAM)

ip = "0.0.0.0"
#ip = "192.168.43.45"
port = 1232

s.bind((ip, port))

while True:
	data = s.recvfrom(1024)
	decoded_data = data[0].decode()
	#print(data)
	print(os.system(decoded_data))