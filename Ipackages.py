import os
from zipfile import ZipFile
import time

def install():
    print("Example: test --> links to deamon.ml/download/test")
    package_name = input("Enter package name: ")
    print("Installing Package...")
    os.system(f"start http://deamon/download/{package_name}")
    print("Download Complete")

def extract():
    print("Extract Zipfile")
    print("[Note] zip file must be in same folder")
    package_name = input("Zipfile name :+: exstension: ")
    file_name = f"{package_name}"
    with ZipFile(file_name, 'r') as zip:
        zip.printdir()
    print('Extracting all the files now...')
    zip.extractall()
    print('Done!')


def Main():
    print("|| ---  IPackages  --- ||")
    print("|| ---  install, extract")
    user_input = input(":: ")
    if user_input == "install":
        install()
    if user_input == "extract":
        extract()