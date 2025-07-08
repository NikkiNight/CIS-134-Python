"""
Author: Nicola Ward
File: PhoneBookClient.py
Last Date Modified: 4/19/2024

Client file for the phone book project. Command-line interface that provides
methods for users to interact with the phone book. 
"""

import socket
from codecs import decode

from PhoneBookHandler import PhoneBookHandler

HOST = 'localhost'
PORT = 9000
BUFSIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f'Connected to {HOST}:{PORT}')

    phoneBook = PhoneBookHandler(s)

    try:

        print("Hello!")
        print("Please enter one of the following options: \
                         \nLookup \nAdd \nQuit") # Choice Options
    
        while True:

            response = input("What would you like to do: ").upper() # User Input

            if response == "QUIT": # Quit Program
                s.close() # Close Connection
                break

            elif response == "LOOKUP": # Lookup Name In phoneBook
                
                name = input("Enter Name: ").upper()
                
                number = phoneBook.lookup(name)
                
                phoneBook.lookup(name) # Lookup Name
                
                print("Number: ", number) # Display Number

            elif response == "ADD": # Add Name To phoneBook

                name = input("Enter Name: ")
                number = input ("Enter Phone Number: ")

                phoneBook.add(name, number) # Add To Phone Book
    
    except ConnectionRefusedError:
        print("Error connecting to server.")
