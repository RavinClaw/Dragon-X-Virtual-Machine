# Heads up this is an incomplete verison of the file and should be treated as a beta test of the program
# It stores all the required information in a json file called 'storage.json' all files and their formatting are stored
# Information Stored: name of the file (changable), formatting of the file (changable), contents of file (chanagable), owner of file (not changable and only one owner per file... thought i am working on a share system)

# START OF FILE

import os, sys
import random, string, math
import json, csv
import tkinter as tk
from tkinter import messagebox
from tkinter import dialog
import re, struct
import hashlib, base64, uuid


class File_Handling:
    def __init__(self, filename: str):
        with open("storage.json", "r") as f:
            rawContents = json.load(f)
        self.filesJson = rawContents["Files"]

    def Add_File(self, filename: str, formatting: str, contents: str, owner: str):
        with open("storage.json", "r") as f:
            rawContents = json.load(f)
        new_file = {
            "name": "{0}".format(filename),
            "formatting": "{0}".format(formatting),
            "contents": "{0}".format(contents),
            "owner": "{0}".format(owner)
        }
        rawContents["Files"].append(new_file)
        with open("storage.json", "w") as f:
            json.dump(rawContents, f, indent=4)

    def Encoder(self, text):
        bytes_data = text.encode('utf-8')
        hex_string = ' '.join([f'\\x{byte:02x}' for byte in bytes_data])
        return hex_string

    def Decoder(self, hex_string):
        hex_list = hex_string.replace(r'\x', '').split()
        int_list = [int(byte, 16) for byte in hex_list]
        bytes_data = bytes(int_list)
        decoded_string = bytes_data.decode('utf-8')
        return decoded_string

if __name__ == "__main__":
    # Loads In the Storage.json File
    fh = File_Handling("storage.json")
    # The The Current Default Download is net.broadcast(type: str);
    text = 'net.broadcast("Running This File Can be Cool You Know");'
    # Encodes the Contents to SystemByte Format
    contents = "{0}".format(fh.Encoder(text))
    # Adding in all the Extra information that is required
    fh.Add_File(filename="storage.uni", formatting="uni/script", contents="{0}".format(contents), owner="root")

