"""
Author: Nicola Ward
File: PhoneBookHandler.py
Last Date Modified: 4/19/2024

Client handler for phone book project.
"""
import socket
import os
from threading import Thread
from codecs import decode

BUFSIZE = 1024

class PhoneBookHandler(Thread):
    
    """Handles a client request."""
    def __init__(self, client):
        Thread.__init__(self)
        self.client = client
        
        self.phoneBook = {} # Phone Book Declaration

    def lookup(self, name): # Lookup Number By Name
        name = name.upper() # Convert Name To Uppercase
        self.load() # Load File
        if name in self.phoneBook: # If Name In phoneBook, Display
            return self.phoneBook[name]
        else: # If Not Found, Error
            print("Error. Name not found.")
            return
        
    def add(self, name, number): # Add New Name And Number
        name = name.upper() # Convert Name To Uppercase
        self.phoneBook[name] = number
        self.save() # Save To File
        print("Saved.")
        return


# Save To File
    def save(self): # If file doesn't exist, it will create on first time adding data
        try:
            file_name = "phoneBook.txt"
            file_path = os.path.join(os.getcwd(), file_name)  # Save To Current Directory
            with open(file_path, "a") as file:
                for name, number in self.phoneBook.items():
                    file.write(f"{name}: {number}\n")
        except IOError as e:
            print(f"Error occurred while saving phone book data: {e}")

# Load From File
    def load(self):
        try:
            file_name = "phoneBook.txt"
            file_path = os.path.join(os.getcwd(), file_name)
            with open(file_path, "r") as file:
                for line in file:
                    # Process Each Line, Extract Name And Number
                    parts = line.strip().split(": ")
                    if len(parts) == 2:
                        name = parts[0].strip()
                        number = parts[1].strip()
                        # Add Name And Number To phoneBook
                        self.phoneBook[name] = number
        except IOError as e:
            print(f"Error occurred while reading phone book data: {e}")

