#!/usr/bin/env python3
import random
import string
import itertools
import subprocess #Process commands
import socket #Process socket data
import pyfiglet
import sys
import os
from subprocess import call





def menu():
    ascii_banner = pyfiglet.figlet_format("ANONIK TOOLKIT")
    print(ascii_banner)
    print("()()()(((((((((((((((((((((())))))))))))))))))))))")
    print("----------------->ANONI TOOLKIT V 1.0.0b<-------------------")
    print("")
    print("                      ENJOY :))))                            ")
    print("()()()(((((((((((((((((((((())))))))))))))))))))))")
    
def sceltamenu():
    print("Scegli le tue opzioni: ")
    print("<>1 Hacktool")
    print("<>2 Forenics Tool")
    print("<>3 Office Activation")
    print("<>4 Miscellouns Toolkit")
    print("<>5 Shhh ;)")
        
#=====================================================================================================================
#funcion

import pyfiglet

def HackTool():
    ascii_banner2 = pyfiglet.figlet_format("HACKTOOL V.1.0")
    print(ascii_banner2)
    print("By AnOnIk <> - Enjoy ;)")
    print("_")
    


    def CrackPsw():
        try:
            qs1 = int(input("Lunghezza password: "))
        except ValueError:
            print("Inserisci un numero valido!")
            return

        qs2_name = input("Nome: ")
        qs3_surname = input("Cognome: ")

        base = qs2_name + qs3_surname

        # rimuove duplicati (opzionale ma consigliato)
        base = "".join(set(base))

        totale = len(base) ** qs1

        print(f"\nTotale combinazioni: {totale}")

        # limite di sicurezza
        if totale > 1_000_000:
            print("Troppe combinazioni! Riduci la lunghezza.")
            return

        nome_file = "wordlist.txt"

        print(f"\nSto generando il file '{nome_file}'...\n")

        with open(nome_file, "w") as file:
            combinazioni = itertools.product(base, repeat=qs1)

            for c in combinazioni:
                password = "".join(c)
                file.write(password + "\n")

        print("File creato con successo!")

    CrackPsw()


            






def userselect():
    scelta_user = int(input("Digita Il Numero per accedere al menu che ti interessa <>...: "))
    try:
        if scelta_user == int(1):
            print("Primo menu")
            HackTool()
        if scelta_user == int(2):
            print("Secondo menu")
        if scelta_user == int(3):
            print("Terzo Menu")
        if scelta_user == int(4):
            print("Quarto Menu")
        if scelta_user == int(5):
            print("Riservatoo")
        
        elif scelta_user >= int(6):
            print("Nessun numero corrisponde")
            return userselect()
    except ValueError:
        print("Inserisci un numero e non un carattere")
        return userselect()
        
            

            
print (menu())
print (sceltamenu())
print (userselect())

        