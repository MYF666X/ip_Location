#!/usr/bin/env python2.7
#
#
#

import os
import sys
d3=os.system("curl http://ipinfo.io/ip")
os.system("clear && clear && clear")
logo = '''\033[0m 
__  __          __  __            __
 |  \/  |        |  \/  |          / _|
 | \  / |  _ __  | \  / |  _   _  | |_
 | |\/| | | '__| | |\/| | | | | | |  _|
 | |  | | | |    | |  | | | |_| | | |
 |_|  |_| |_|    |_|  |_|  \__, | |_|
                            __/ |
                           |___/\033[0m  \033[91m    \033[1m 
       }--{+} +62 By MR-Myf666X {+}--{
     }----{+}  I-HACK {+}----{
       }--{+} NKRI HARGA MATI  {+}--{                               
     '''
menu = '''\033[0m
    {1}--Pencarian Whois 
    {2}--Traceroute
    {3}--Pencarian DNS
    {4}--Membalikkan Pencarian DNS
    {5}--Pencarian Geo Ip
    {6}--Memindai Scan
    {7}--Pencarian geo ip
    {0}--INSTALL & UPDATE
    {99}-Keluar                                                                                                                   
 '''
print logo
print menu
def quit():
            con = raw_input('Continue [Y/n] -> ')
            if con[0].upper() == 'N':
                exit()
            else:
                os.system("clear")
                print logo
                print menu
                select()
           
def  select():
  try:
    choice = input("MR-Myf666X~# ")
    if choice == 1:
      d3 = raw_input('Enter IP Or Domain : ')
      os.system("clear")
      print("""
__  __          __  __
 |  \/  |        |  \/  |          / _|
 | \  / |  _ __  | \  / |  _   _  | |_
 | |\/| | | '__| | |\/| | | | | | |  _|
 | |  | | | |    | |  | | | |_| | | |
 |_|  |_| |_|    |_|  |_|  \__, | |_|
                            __/ |
                           |___/
      """)
      os.system("curl http://api.hackertarget.com/whois/?q=" + d3)
      print("")
      quit()
    elif choice == 0:
	  os.system("clear")
	  print("This tool is only available for Linux and similar systems  ")
	  os.system("git clone https://github.com/Manisso/Crips.git")
	  os.system("cd Crips && sudo bash ./update.sh")
	  os.system("crips")
    elif choice == 2:
      d3 = raw_input('Enter IP Or Domain : ')
      os.system("clear")
      print("""
__  __          __  __            __
 |  \/  |        |  \/  |          / _|
 | \  / |  _ __  | \  / |  _   _  | |_
 | |\/| | | '__| | |\/| | | | | | |  _|
 | |  | | | |    | |  | | | |_| | | |
 |_|  |_| |_|    |_|  |_|  \__, | |_|
                            __/ |
                           |___/
""")
      os.system("curl https://api.hackertarget.com/mtr/?q=" + d3 )
      print("")
      quit()
    elif choice == 3:
      d3 = raw_input('Enter Domain : ')
      os.system("clear")
      print("""
__  __ ____    ____  _______   __
|  \/  |  _ \  |  _ \| ____\ \ / /
| |\/| | |_) | | |_) |  _|  \ V /
| |  | |  _ <  |  _ <| |___  | |
|_|  |_|_| \_\ |_| \_\_____| |_|
""")
      os.system("curl http://api.hackertarget.com/dnslookup/?q=" + d3 )
      print("")
      quit()    
    elif choice == 0:
      print "Bye Bye"
      os.system("clear")
      exit()
    elif choice == 4:
	  d3 = raw_input('Enter IP Address - IP Range Or Domain  : ')
	  os.system("clear")
	  print("""
__  __          __  __            __ 
 |  \/  |        |  \/  |          / _|
 | \  / |  _ __  | \  / |  _   _  | |_ 
 | |\/| | | '__| | |\/| | | | | | |  _|
 | |  | | | |    | |  | | | |_| | | |  
 |_|  |_| |_|    |_|  |_|  \__, | |_|  
                            __/ |      
                           |___/
                                                    
	  """)
	  os.system("curl https://api.hackertarget.com/reversedns/?q=" + d3 )
	  print("")
	  quit()
    elif choice == 5:
	  d3 = raw_input('Enter IP Or Domain : ')
	  os.system("clear")
	  print("""
_   _ _  ______  ___
| \ | | |/ /  _ \|_ _|
|  \| | ' /| |_) || |
| |\  | . \|  _ < | |
|_| \_|_|\_\_| \_\___|
                                	
	""")
	  os.system("curl http://api.hackertarget.com/geoip/?q=" + d3 )
	  print("")
	  print("")
	  quit()
    elif choice == 6:
      d3 = raw_input('Enter IP Or Domain : ')
      os.system("clear")
      print("""
__  __          __  __            __ 
 |  \/  |        |  \/  |          / _|
 | \  / |  _ __  | \  / |  _   _  | |_ 
 | |\/| | | '__| | |\/| | | | | | |  _|
 | |  | | | |    | |  | | | |_| | | |  
 |_|  |_| |_|    |_|  |_|  \__, | |_|  
                            __/ |      
                           |___/
      """)
      os.system("curl http://api.hackertarget.com/nmap/?q=" + d3 )
      print("")
      quit()
    elif choice == 7:
	  d3 = raw_input('Enter IP Or Domain : ')
	  os.system("clear")
	  print("""
__  __          __  __            __ 
 |  \/  |        |  \/  |          / _|
 | \  / |  _ __  | \  / |  _   _  | |_ 
 | |\/| | | '__| | |\/| | | | | | |  _|
 | |  | | | |    | |  | | | |_| | | |  
 |_|  |_| |_|    |_|  |_|  \__, | |_|  
                            __/ |      
                           |___/
	  """)
	  os.system("wget http://api.hackertarget.com/reverseiplookup/?q=" + d3 )
	  os.system("clear")
	  os.system("curl http://api.hackertarget.com/reverseiplookup/?q=" + d3 )
	  print("")
	  print("\033[91m\033[1mFile Saved On : ")
	  os.system("pwd")
	  print("File : index.html?q=" +d3)
	  print("\033[0m")
	  quit()
  except(KeyboardInterrupt):
    print ""
select()
