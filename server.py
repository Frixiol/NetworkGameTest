import socket
from _thread import *
from player import Player
import pickle
from game import Fruit

server = "192.168.1.28"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("waiting for connection, Server Started")

fruit = Fruit()
connected = set()
games_ready = False
players = {}
b_number = 0
bullets = {}
idCount = -1

def threaded_client(conn, id_player):
    global idCount,fruit,bullets,players,b_number
    conn.sendall(pickle.dumps((players)))
    print(players)
    bullets_col = {}
    reply = ""
    while True:
        try:

            print("data")
            data = pickle.loads(conn.recv(2048*4))
            print(data)
            if not data:
                break
            else:
                if data.id == "bullet":
                    data.define_numb(b_number)
                    bullets[b_number] = data
                    b_number += 1
                    conn.sendall(pickle.dumps((bullets)))
                elif data.id == id_player:
                    players[id_player] = data




                    for bullet in bullets:
                        if bullets[bullet].shooter == id_player:
                            wcollision = bullets[bullet].move()
                            if wcollision == True:
                                bullets_col[bullet] = bullets[bullet]
                        else:
                            pcollision = bullets[bullet].player_col(players[id_player].x, players[id_player].y,players[id_player].width, players[id_player].height)
                            if pcollision == True:
                                players[id_player].health -= 10
                                bullets_col[bullet] = bullets[bullet]
                                if players[id_player].health <= 0:
                                    players[id_player].health = 100
                                    players[id_player].position()
                    for bullet in bullets_col:
                        bullets.pop(bullet)
                    bullets_col = {}

                    conn.sendall(pickle.dumps((players, fruit, bullets)))
                elif data.id == "fruit":
                    fruit = data
                    conn.sendall(pickle.dumps((fruit)))

        except:
            break



    print(id_player, "Lost connection")
    idCount -= 1
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to", addr, conn)
    if idCount > -1:
        games_ready = True
    idCount += 1

    players[idCount] = Player(idCount)

    start_new_thread(threaded_client, (conn, idCount))
