import os
import sys
import socket
import socketserver
import random
from tqdm import tqdm
from getpass import getpass

def Settings():
    code = ""
    coding = []
    kcode = ""
    print("Setting Up The Website")
    print("[WARNING] This program will be rewritten if you have already written a program here")
    print("# code-exit to return from the coding area")
    while code != "# code-exit":
        code = input(f"[{len(coding)+1}]: ")
        coding.append(code)
    print("Website Code")
    for x in range(len(coding)):
        print(f"[{x+1}] {coding[x]}")
        kcode += str(coding[x]) + "\n"
    with open("app.py", "w") as file:
        file.write(kcode)

def RunWeb():
    try:
        os.system("py app.py")
    except:
        print("Error File Not Found\n You haven't created a website yet\n Use 'sudo run' or 'webserver.run'")