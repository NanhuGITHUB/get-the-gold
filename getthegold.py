import pgzrun
from secrets import randbits

WIDTH = 520
HEIGHT = 520
score = 0
game_over = False
gover = "Hi!"

fox = Actor("fox")
fox.x = randbits(9)
fox.y = randbits(9)

coin = Actor("coin")

def place_actors():
    coin.x = randbits(9)
    coin.y = randbits(9)

def time_up(): 
    global game_over
    game_over = True

def update():
    global score
    
    if keyboard.left:
        fox.x -= 6
    elif keyboard.right:
        fox.x += 6
    elif keyboard.up:
        fox.y -= 6
    elif keyboard.down:
        fox.y += 6
    
    coin_collected = fox.colliderect(coin)
    
    if coin_collected:
        score += 10
        place_actors()

clock.schedule(time_up, 120.0)
place_actors()

def draw():
    screen.fill("yellow")
    fox.draw()
    coin.draw()
    screen.draw.text(f"Score : {score}", color="black", topleft=(10, 10))
    if game_over:
        screen.fill("navy")
        screen.draw.text(f"Final Score: {score}", topleft=(10,10), fontsize=80)

pgzrun.go()