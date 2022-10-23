import os
import sys
import socket
import socketserver
import random
from time import sleep
from random import randint
from getpass import getpass
import numpy as np
import csv
import base64
import turtle

def OnStart():
    with open("connectivity.disk", "r") as file:
        hoststuff = file.read().split("\n")
    if len(hoststuff) < 2:
        rd1 = randint(0, 255)
        rd2 = randint(0, 255)
        rd3 = randint(0, 255)
        rd4 = randint(0, 255)
        rd5 = randint(0, 255)
        rd6 = randint(0, 255)
        rd7 = randint(0, 255)
        rd8 = randint(0, 255)
        ipv8 = str(rd1) + "." + str(rd1) + "." + str(rd2) + "." + str(rd3) + "." + str(rd4) + "." + str(rd5) + "." + str(rd6) + "." + str(rd7) + "." + str(rd8)
        rd1 = randint(0, 255)
        rd2 = randint(0, 255)
        rd3 = randint(0, 255)
        rd4 = randint(0, 255)
        rd5 = randint(0, 255)
        rd6 = randint(0, 255)
        rd7 = randint(0, 255)
        rd8 = randint(0, 255)
        rd9 = randint(0, 255)
        rd10 = randint(0, 255)
        rd11 = randint(0, 255)
        rd12 = randint(0, 255)
        ipv12 = str(rd1) + "." + str(rd1) + "." + str(rd2) + "." + str(rd3) + "." + str(rd4) + "." + str(rd5) + "." + str(rd6) + "." + str(rd7) + "." + str(rd8) + "." + str(rd9) + "." + str(rd10) + "." + str(rd11) + "." + str(rd12)
        hoststuff = ipv8 + "\n" + ipv12
        with open("connectivity.disk", "w") as file:
            file.write(hoststuff)
    if len(hoststuff) > 1:
        ipv8 = hoststuff[0]
        ipv12 = hoststuff[1]
        print("|| ---  IP Configuration  --- ||")
        print(f"|| ---  Ipv8: {ipv8}")
        print(f"|| ---  Ipv12: {ipv12}")
        print("This Information Cannot be changed")
        print("All port numbers are available from 0 - 9999")

OnStart()