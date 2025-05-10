import random
import pgzrun

WIDTH = 1200
HEIGHT = 600
TITLE = "SHOOTING GAME"

is_game_over = False
score = 0
lives = 3
speed = 5

dragon = Actor("dragon")
dragon.pos = (600,540)

enemies = []
fires = []

for i in range(8):
    enemy = Actor("enemy")
    enemy.x = random.randint(0,WIDTH - 80)
    enemy.y = random.randint(-100,0)
    enemies.append(enemy)

def display_score():
    screen.draw.text(f"Score: {score}", (50,30))
    screen.draw.text(f"Lives: {lives}", (50,60))

def on_key_down(key):
    if key == keys.SPACE:
        fire = Actor("fire")
        fire.x = dragon.x
        fire.y = dragon.y - 50
        fires.append(fire)

def update():
    global lives,score
    if keyboard.left:
        dragon.x -= speed
        if dragon.x <= 0:
            dragon.x = 0
    elif keyboard.right:
        dragon.x += speed
        if dragon.x >= WIDTH:
            dragon.x = WIDTH
    for fire in fires:
        if fire.y <= 0:
            fires.remove(fire)
        else:
            fire.y -= 10



pgzrun.go()
    