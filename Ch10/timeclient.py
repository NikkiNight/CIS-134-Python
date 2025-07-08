"""
Modified By: Nicola Ward
File: timeclient.py
Project 10.2
Last Date Modified: 4/19/2024

Client for obtaining the day and time. Recovers from connection errors.
"""

from socket import *
from codecs import decode

HOST = "localhost" 
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

try:
    server = socket(AF_INET, SOCK_STREAM)               # Socket
    server.connect(ADDRESS)                             # Connect To Host
    dayAndTime = decode(server.recv(BUFSIZE), "ascii")  # Read String
    print(dayAndTime)
    server.close()                                      # Close Connection
except ConnectionRefusedError:
    print("Error connecting to server.")
