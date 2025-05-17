import random
import pgzrun

WIDTH = 1200
HEIGHT = 600
TITLE = "dragon GAME"

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

    for enemy in enemies:
        enemy.y += 5
    
        if enemy.y > HEIGHT:
            enemy.x = random.randint(0,WIDTH - 80)
            enemy.y = random.randint(-100,0)
            
        for fire in fires:
            if enemy.colliderect(fire):
                score = score + 100
                enemies.remove(enemy)
                fires.remove(fire)
        
        if enemy.colliderect(dragon):
            lives = lives - 1
            enemies.remove(enemy)
            if lives == 0:
                game_over()

    if len(enemies) < 8:
        enemy = Actor("enemy")
        enemy.x = random.randint(0,WIDTH - 80)
        enemy.y = random.randint(-100,0)
        enemies.append(enemy)

def draw():
    if lives > 0:
        screen.clear()
        screen.fill("red")
        for enemy in enemies:
            enemy.draw()
        for fire in fires:
            fire.draw()
        dragon.draw()
        display_score()
    else:
        game_over_screen()

def game_over():
    global is_game_over 
    is_game_over = True

def game_over_screen():
    screen.clear()
    screen.fill("sky blue")
    screen.draw.text("GAME OVER!!!", (WIDTH/2, HEIGHT/2), fontsize = 50, color = "black")
    screen.draw.text(f"Your final score was {score}", (WIDTH/2, HEIGHT/2 + 50), fontsize = 40, color = "black")
    screen.draw.text("Press SPACE to play again", (WIDTH/2, HEIGHT/2 + 100), fontsize = 45, color = "black")

    if keyboard.SPACE:
        restart_game()

def restart_game():
    global score, lives, fires, enemies
    score = 0
    lives = 3
    fires = []
    enemies = []



    for enemy in enemies:
        enemy = Actor("enemy")
        enemy.x = random.randint(0,WIDTH - 80)
        enemy.y = random.randint(-100,0)
        enemies.append(enemy)

pgzrun.go()
pgzrun.go()
    