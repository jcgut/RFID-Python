#coding=utf-8
#Script Python to read and save the code on clipboard.
#By Juan Carlos Gutierrez Arguedas - 22.01.2019

import urllib
import time
import os, sys
import serial
import socket
from keyboard_alike import reader
import pyperclip
import keyboard

def read_rfid():
    try:
        os.system('clear')
        print "Escuchando entradas..."
        data = None
        ser = None

        try:
            ser = reader.Reader(0xffff, 0x0035, 84, 16, should_reset=False)
            ser.initialize()
            data = ser.read().strip()
            ser.disconnect()
            dec = int(data)
            dec=str(dec)

            return dec
            ser.flushInput()
            data.flushInput()

        except:
            print "****ERROR****"

    except:
         pass

#Main
while True:
    os.system('clear')
    dec=read_rfid()
    dec=str(dec)

    if dec != "None":

        try:
    #        print dec
            time.sleep(1)
            pyperclip.copy(dec)
            keyboard.send('ctrl+v')

        except:
            pass

    else:
        os.system('clear')
	break
        pass

