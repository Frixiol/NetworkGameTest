import pygame
from network import Network
from game import Bullet
pygame.font.init()


width = 700
height = 700
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Client")
game_ready = False

def redrawWindow(window):
    global players,fruit,bullets,id,n
    bullets_col = []
    touched_player_id = "oui"
    window.fill((255,255,255))

    if len(players)==1:
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255, 0, 0))
        window.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))
    else:
        for player in players:
            players[player].draw(window)
        for bullet in bullets:
            bullets[bullet].draw(window)
        fruit.draw(window)



    pygame.display.update()


def main():
    global players,fruit,bullets,angle,id,n

    run = True
    clock = pygame.time.Clock()
    n = Network()
    players = n.getP()
    print(players)
    id = len(players)-1
    print(players)

    while run:

        clock.tick(60)
        try:
            players, fruit, bullets = n.send(players[id])

        except:
            run = False
            print("Couldn't get game")
            break

        shoot = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print("shoot")
                shoot = True
        players[id].move()
        angle = players[id].rotate()

        if shoot == True:
            bullet = Bullet(players[id].x+players[id].width/2,players[id].y+players[id].height/2,angle,id)
            bullets = n.send(bullet)
            shoot = False

        score = fruit.collision(players[id].x, players[id].y, players[id].width, players[id].height)
        if score == 1:
            fruit = n.send(fruit)
            players[id].score += 1

        redrawWindow(window)


main()


