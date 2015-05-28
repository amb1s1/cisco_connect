cisco_connect
=============

Python module to ssh into cisco devices and getting output from show commands

Package Requirement:
====================

To be able to use this script you need to install pexpect on your machine.  
Here is the Doc for pexpect:  
http://pexpect.sourceforge.net/doc/ 


Example script:  
===============
```
import c_connect  
ce, child = c_connect.cjump('username','password','10.10.10.3')  
enable = c_connect.enable(child, "enable_pswd")  
hostname = c_connect.hostname(child)  
term = c_connect.term(child, hostname)  
running_config = c_connect.runconfig(child, hostname)  
close = c_connect.close(child)  
print hostname  
for i in running_config:  
	print i  
```

Explaination  
=============
First line: you will import the module  
Second Line: You will call the cjump funtion and you will get a return of the following:  
	True = You are in the router but not in enable mode  
	enable = You are in the router and in enable mode  
	If you something else, there is an error   
Third Line: If you want to go to enable mode you will call this function. You will get a true return if the device is on enable mode.  
Four Line: You will get the device hostname  
Five Line: You guess it, you will get your running config  

About Me  
=========
Name: David Gomez  
Website: gomezd.com  
Email: davidgomez.255@gmail.com  

I'm a Network Engineer First and then I'm a python programmer who also know little bit about perl. If you need to contact me about any issues you can either send me an email or report a bug. 
