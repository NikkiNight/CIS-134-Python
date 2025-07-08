"""
Author: Nicola Ward
File: PhoneBookServer.py
Last Date Modified: 4/19/2024

Server file for online phonebook project.
"""

import socket

from PhoneBookHandler import PhoneBookHandler

HOST = 'localhost'
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    print(f'Server listening on {HOST}:{PORT}')
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected to', addr)

            # Create New Thread To Handle Client Requests
            handler = PhoneBookHandler(conn) # New Instance
            handler.start()

