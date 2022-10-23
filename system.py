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
import Ipackages
import create_website

# The Testing is in progress

if os.name == "nt":
  cls = "cls"

if os.name != "nt":
  cls = "clear"

active_ports = []
needs_sudo_pass = True
sudo_password = "1234567890"
dirs = []
end = ">"
user = "Ravin"
path = f"C:\\Users\\{user}"
__version__ = "Beta-Test-v0.1"

commands = ["--version", "--login", "cd", "mkdir", "clear", "ls", "sudo run", "exit", "--logout", "--ipconfig", "--ports random", "--close port", "--ports", "--ipackages", "--help", "curl", "create web", "webserver.run", "nano"]
def Main():
    global path, dirs, needs_sudo_pass
    print(f"System: Dragonx X -- Version: {__version__}")
    for main in range(100000000000000000):
        for system in range(10000000000000000000000000000):
            for y in range(10000000000000000000000000000000000):
                for x in range(100):
                    user_input = input(f"{path}{end}")
                    if user_input == commands[0]:
                        print(f"Dragon X Version: {__version__}")
                    if user_input == commands[2]:
                        print(f"{path}")
                        newpath = input("Enter New Path: ")
                        for dir in range(len(dirs)):
                            if newpath == dirs[dir]:
                                path = dirs[dir]
                    if user_input == commands[3]:
                        print("Create a new Dir")
                        newdir = input(f"New Dir Under: {path}\\")
                        fff = path + "\\" + newdir
                        dirs.append(fff)
                        print("New Directory Created")
                    if user_input == commands[4]:
                        os.system(cls)
                    if user_input == commands[5]:
                        with open("saved_ports.txt", "r") as file:
                            dirs = file.read().split("\n")
                        for dir in range(len(dirs)):
                            print(f"{dir+1}: {dirs[dir]}")
                        print("End of Directories")
                    if user_input == commands[6] and needs_sudo_pass == False:
                        print(":: Filename :+: Extension ::")
                        runfile = input("Enter Filename: ")
                        print("Running...")
                        os.system(f"python {runfile}")
                    if user_input == commands[6] and needs_sudo_pass == True:
                        print("Sudo Permission Required to use this command use --login")
                    if user_input == commands[7]:
                        print("Data will not be saved -- this function does not exist yet")
                        exit()
                    if user_input == commands[1] and needs_sudo_pass == True:
                        print("Login to sudo")
                        user_password = ""
                        while user_password != sudo_password:
                            user_password = getpass("Enter Sudo Password: ")
                        print("** Sudo Password Aquired **")
                        needs_sudo_pass = False
                        continue
                    if user_input == commands[1] and needs_sudo_pass == False:
                        print("Sudo Password has already been entered or is not required")
                    if user_input == commands[8]:
                        print("Logging Out....")
                        needs_sudo_pass = True
                    if user_input == commands[9] and needs_sudo_pass == False:
                        with open("connectivity.disk", "r") as hoststuff:
                            hosty = hoststuff.read().split("\n")
                        host = "host" + user
                        IPV8 = hosty[0]
                        IPV12 = hosty[1]
                        print(f"Username: {user}")
                        print(f"Hostname: {host}")
                        print(f"IPV8 Address: {IPV8}")
                        print(f"IPV12 Address: {IPV12}")
                        if len(active_ports) == 0:
                            print("No Active Ports")
                        if len(active_ports) != 0:
                            for x in range(len(active_ports)):
                                print(f"Port Number: {active_ports[x]} :: Active")
                    if user_input == commands[9] and needs_sudo_pass == True:
                        print("Sudo Permission Required to use this command use --login")
                    if user_input == commands[10]:
                        print("How many ports do you want to activate")
                        user_input_a = int(input("Number of Ports: "))
                        for x in range(user_input_a):
                            port = randint(0, 9999)
                            active_ports.append(port)
                        print(f"Activating Random ports\nNumber of ports: {user_input_a}")
                    if user_input == commands[11]:
                        print("|| ---  Close a port  --- ||")
                        print("All Ports: ")
                        for x in range(len(active_ports)):
                            print(f"||{x}||\t\t\t{active_ports[x]}")
                        close_port = int(input("What port to close: "))
                        active_ports.pop(close_port)
                    if user_input == commands[12]:
                        print(f"|| ---  All Ports -| |- {len(active_ports)}  --- ||")
                        for x in range(len(active_ports)):
                            print(f"||{x}|| Port: {active_ports[x]}")
                    if user_input == commands[13]:
                        Ipackages.Main()
                    if user_input == commands[14]:
                        print("[@] All Commands")
                        for x in range(len(commands)):
                            print(f"{commands[x]}")
                    if user_input == commands[15]:
                        print("Use https:// or http://")
                        url_request = input("curl -vvv ")
                        os.system(f"curl -vvv {url_request}")
                    if user_input == commands[16]:
                        create_website.Settings()
                    if user_input == commands[17]:
                        create_website.RunWeb()
                    if user_input == commands[18]:
                        code = ""
                        kcode = []
                        coding = ""
                        rawfiledata = []
                        print("Filename: ||filename |+| extension|| example: example.txt")
                        nano_name = input("Name: ")
                        try:
                            with open(f"{nano_name}", "r") as rawfile:
                                rawfiledata = rawfile.read.split("@")
                            
                            print("File Found")
                            for x in range(len(rawfiledata)):
                                print(f"[{x+1}] {rawfiledata[x]}")
                            while edit != "# code-exit":
                                print(f"What line do you want to edit? use 1 - {len(rawfiledata)+1}, if you want to exit use # code-exit")
                                edit = input("Line: ")
                                line = edit - 1
                                print("Change the line, depending on what you want to do you have to rewrite the whole line")
                                print(f"{rawfiledata[line]}")
                                code = input(f"[{line+1}] ")
                                rawfiledata.pop(line)
                                rawfiledata.insert(line, code)

                        except:
                            print(f"|| ---  Nano ~{nano_name}")
                            while code != "# code-exit":
                                code = input(f"[{len(kcode)+1}] ")
                                kcode.append(code)
                            for x in range(len(kcode)):
                                coding += kcode[x] + "@"
                            print("Creating File")
                            with open(f"{nano_name}", "w") as rawfile:
                                rawfile.write(coding)

Main()