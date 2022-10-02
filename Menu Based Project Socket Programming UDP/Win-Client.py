import socket as sp
import os
s = sp.socket(sp.AF_INET , sp.SOCK_DGRAM)
print("""
Press 1 : To Run date
Press 2 : To Run cal
Press 3 : To Make dir
Press 4 : To Run list
Press 5 : To Get Ip address
Press 6 : To Setup Web Server
Press 7 : To Setup C++
Press 8 : To Configure yum  
Press 9 : To Install Any Software
Press 10: Check Software installed or not in OS
Press 11: To Create file  
Press 12: To Create User  
Press 13: To Delete User  
Press 14: To Create Group
Press 15: To Add user in Group
Press 16: To Check Internet Connectivity
Press 17: To Stop SELinux
Press 18: To Start SELinux
Press 19: To Check status of SELinux Security
Press 20: To Set Privileges Escalation(Sudo Power) in user 
Press 21: To Setup SSH key Setup between 2 systems
Press 22: To exit
""")

while True:
		userinp = input("Enter command to run in Linux : ")
		#s.sendto(userinp.encode() , ("192.168.43.45" , 1232))
		s.sendto(userinp.encode() , ("192.168.43.152" , 1232))
		print()
		#userinp = int(input())