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
	print(type(decoded_data))
	userinp = int(decoded_data)
	if userinp == 1:
		os.system("date")
	elif userinp == 2:
		os.system("cal")
	elif userinp == 3:
		foldername = input("Enter folder name : ")
		os.system("mkdir {0}".format(foldername))
	elif userinp == 4:
		os.system("ls")
	elif userinp == 5:
		os.system("ifconfig enp0s3")
	elif userinp == 6:
		os.system("yum install httpd -y ; cd /var/www/html; echo new > index.html ; systemctl enable httpd --now")  		
	elif userinp == 7:
		os.system("yum install gcc-c++ -y")		
	elif userinp == 8:
		os.system("cp dvd.repo /etc/yum.repos.d/ ; yum repolist")		
	elif userinp == 9:
		softwarename = input("Enter Software name : ")
		os.system("yum install {0} -y".format(softwarename))
	elif userinp == 10:
		softwarename = input("Enter Software name to check : ")
		os.system("rpm -q (0)".format(softwarename))
	elif userinp == 11:
		fname=input("Enter File Name")
		os.system("touch {0}".format(fname))
	elif userinp == 12:
		uname = input("Enter Username to create")  
		os.system("useradd {0}".format(uname))      
	elif userinp == 13:
		duname = input("Enter Username to delete")  
		os.system("userdel {0}".format(dunname))        
	elif userinp == 14:
		gname = input("Enter Groupname to create")  
		os.system("groupadd {0}".format(gname))      
	elif userinp == 15:
		uname = input("Enter Username to create")  
		os.system("useradd {0}".format(uname))      
		gname = input("Enter Groupname to create")  
		os.system("groupadd {0}".format(gname))      
		print("Add {0} user in group".format(uname))
		os.system("useradd -G (1) {0}".format(uname, gname))        
	elif userinp == 16:
		os.system("ping 8.8.8.8")
	elif userinp == 17:
		os.systeM("setenforce 0")
	elif userinp == 18:
		os.system("setenforce 1")
	elif userinp == 19:
		os.system("getenforce")
	elif userinp == 20:
		uname = input("Enter Username to create : ")  
		os.system("useradd {0}".format(uname))
		os.system("echo (0) 	ALL=ALL    NOPASSWD: ALL >> /etc/sudoers".format(uname)) 
	elif userinp == 21:
		print("SSH key Generating ......")
		os.system("ssh-keygen")
		ipadd = input("Enter Ip of 2nd system : ")
		os.system("ssh-copy-id root@{0}".format(ipadd))
		print("Setup successfull Check via login")
	elif userinp == 22:
		break
	#print(os.system(decoded_data))
