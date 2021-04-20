import socket
import pickle
from player import Player #i dunno why but this need to be here in the exe but not in the ide wtf ? 

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.28"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            print("yes")
            self.client.connect(self.addr)
            print("yesi")
            return pickle.loads(self.client.recv(2048*16))
        except socket.error as e:
            print("problem",e)
            return {}

    def send(self, data):
        try:
            self.client.sendall(pickle.dumps((data)))
            return pickle.loads(self.client.recv(2048*16))
        except socket.error as e:
            print(e)

