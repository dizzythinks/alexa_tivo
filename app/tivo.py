import socket
import sys
import time
import os.path


class Tivo:
    def __init__(self, tivo_address):
        self.tivo_address = tivo_address

    def connect(self):
        try:
            sock = socket.socket()
            sock.settimeout(5)
            sock.connect((self.tivo_address, 31339))
            sock.settimeout(None)
            self.sock = sock

        except Exception, msg:
            print msg
            sys.exit()

    def send_code(self, code):
        try:
            self.sock.sendall("IRCODE %s\r" % code)
            time.sleep(0.1)
        except Exception, msg:
            print msg

    def close(self):
        self.sock.close()


