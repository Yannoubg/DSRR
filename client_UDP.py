# -*- coding: utf-8 -*-

import socket # import la library "socket"
IP_Serv="192.168.0.202" # adresse IP du server
PORT=5005 #port associé au server

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.settimeout(1.0) #attendre

sock.connect((IP_Serv,PORT))# c'est l'adresse a laquelle le client va se connecter
sock.send("cinema")#le message a envoyer


trameReponse, addr = sock.recvfrom(1024) # taille du buffer 1024 octets

print "Réception de la trame de réponse", trameReponse.encode("hex") # afficher un text puis le message transmit par le server coder en hexa

#decaler tout les bite pour les faire prendre leur place originel
code0=((ord(trameReponse[0]))<<0)&0xFF
code1=((ord(trameReponse[1]))<<8)&0xFF00
code2=((ord(trameReponse[2]))<<16)&0xFF0000
code3=((ord(trameReponse[3]))<<24)&0xFF000000

#faire un ou logique pour avoir le code de cette de carte
code =code0|code1|code2|code3

#afficher le code de la carte
print code