import socket
# 						Udp Protocol

myprotocol = socket.SOCK_DGRAM

# 			Address / Network Family name
afn = socket.AF_INET

s = socket.socket(afn, myprotocol)
ip="192.168.43.45"
port=1234
s.bind( (ip , port)  )
x = s.recvfrom(1024)
print(x)
