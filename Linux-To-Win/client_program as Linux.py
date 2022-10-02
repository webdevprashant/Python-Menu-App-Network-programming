import socket as sp
s = sp.socket(sp.AF_INET , sp.SOCK_DGRAM)
while True:
	cmd = input("Enter command to run  in windows : ")
	s.sendto(cmd.encode() , ("192.168.43.241" , 1232))
