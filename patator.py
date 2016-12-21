import socket, sys
import time
import RPi.GPIO as GPIO
import urllib
import threading
import os as os

# os.system("fuser -k 50000/tcp")

#-----------------------Conf GPIO-------------------
#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

def Patator():
#----------------------Conf adresse-------------------

	HOST = '192.168.1.30' # IP
	PORT = 60000 # PORT

#----------------------creation du socket------------
	mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#--------------liaison du socket a une adresse precise------------
	try:
	  mySocket.bind((HOST, PORT))
	except socket.error:
	  print("La liaison du socket a l'adresse choisie a echoue.")
	  sys.exit

	while 1:

#----------Attente de la requete de connexion d'un client------------
		print("Serveur pret, en attente de requetes ...")
		mySocket.listen(1)

#---------------Etablissement de la connexion-------------------------
		connexion, adresse = mySocket.accept()
		print("Client connecte, adresse IP %s, port %s" % (adresse[0], adresse[1]))

#--------------------------Traitement------------------------
		while 1:
			msg = connexion.recv(1024)
			if msg == "feu":
				print("GPIO_Feu")
				GPIO.output(16, GPIO.HIGH)
				time.sleep(1)
				GPIO.output(16, GPIO.LOW)
			if msg == "charge":
				print("GPIO_Charge")
				GPIO.output(12, GPIO.HIGH)
			if msg == "uncharge":
				print("GPIO_UnCharge")
				GPIO.output(12, GPIO.LOW)
			if(msg==""):
				break

#------------------------Fermeture de la connexion------------
	#print("Connexion interrompue.")
	#connexion.close()
try:
    Patator()
except KeyboardInterrupt:
    GPIO.cleanup()
