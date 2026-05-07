# Import Libraries
import pygame
from pygame import *
from random import randint

pygame.init()

clock = time.Clock()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 750
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

WIDTH = 50
HEIGHT = 50

WHITE = (255, 255, 255)

SPAWN_RATE = 360
BULLETSPAWN_RATE = 30
FRAME_RATE = 60
BOTTOMBORDER = WINDOW_HEIGHT - 150
REG_SPEED = 5
SLOW_SPEED = 1
PLAYERHEARTS = 6
STARTING_BUCKS = 6
BUCK_RATE = 1
STARTING_BUCK_BOOSTER = 0

MAX_BAD_REVIEWS = 300
WIN_TIME = FRAME_RATE * 60 * 1

GAME_WINDOW = display.set_mode(WINDOW_RES)
display.set_caption('Attack of the Vampire Pizzas by Enzo Alexander - Level 1: Vampires Attack')

background_img = image.load('../gameassets/background.png')
background_surf = Surface.convert_alpha(background_img)
BACKGROUND =transform.scale(background_surf, WINDOW_RES)

pizza_img = image.load('../gameassets/vampire.png')
pizza_surf = Surface.convert_alpha(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf, (WIDTH, HEIGHT))

garlic_img = image.load('../gameassets/garlic.png')
garlic_surf = Surface.convert_alpha(garlic_img)
GARLIC = transform.scale(garlic_surf, (WIDTH, HEIGHT))

cutter_img = image.load('../gameassets/pizzacutter.png')
cutter_surf = Surface.convert_alpha(cutter_img)
CUTTER = transform.scale(cutter_surf, (WIDTH, HEIGHT))

pepperoni_img = image.load('../gameassets/pepperoni.png')
pepperoni_surf = Surface.convert_alpha(pepperoni_img)
PEPPERONI = transform.scale(pepperoni_surf, (WIDTH, HEIGHT))

cursiforx_img = image.load('../gameassets/Cruciforx.png')
cursiforx_surf = Surface.convert_alpha(cursiforx_img)
CURSIFORX = transform.scale(cursiforx_surf, (WIDTH, HEIGHT))

def load_beatmap(filename):
    spawn_frames = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                seconds = float(line.strip())
                spawn_frames.append(int(seconds * FRAME_RATE))
            except ValueError:
                continue
    return spawn_frames

vampire_spawn_times = load_beatmap('../gameassets/Isolation.beatmap.txt')

class VampireSprite(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = REG_SPEED
        self.lane = randint(0, 4)
        all_vampires.add(self)
        self.image = VAMPIRE_PIZZA.copy()
        x = randint(0, WINDOW_WIDTH)
        self.rect = self.image.get_rect(center=(x, 0))
        self.radius = self.rect.width // 2
        self.health = 100

    def update(self, game_window, counters):
        collided = sprite.spritecollide(self, all_anchovies, True)
        if collided is not None:
            for anchovy in collided:
                self.health -= 1
        collidedboom = sprite.spritecollide(self, all_bombs, True)
        if collidedboom is not None:
            for anchovy in collidedboom:
                for vampire in all_vampires:
                    vampire.health = 0
                for bullet in all_bullets:
                    bullet.kill()

        self.rect.y += self.speed

        if self.health <= 0 or self.rect.y > BOTTOMBORDER:
            if self.health <= 0:
                counters.score += 1
            self.kill()



        else:
            game_window.blit(self.image, (self.rect.x, self.rect.y))

class PlayerSprite(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = REG_SPEED
        self.lane = randint(0, 4)
        playersprites.add(self)
        self.image = GARLIC.copy()
        y = 325
        x = 300
        self.rect = self.image.get_rect(center=(x, y))
        self.radius = self.rect.width // 2
        self.health = PLAYERHEARTS

    def update(self, game_window, counters):

        collided = sprite.spritecollide(self, all_vampires, True)
        if collided is not None:
            for anchovy in collided:
                self.health -= 1
                counters.pizza_bucks -= 1
                counters.bad_reviews = STARTING_BUCKS
        collidedbullet = sprite.spritecollide(self, all_bullets, True)
        if collidedbullet is not None:
            for anchovy in collidedbullet:
                self.health -= 1
                counters.pizza_bucks -= 1
                counters.bad_reviews = STARTING_BUCKS

        if self.health <= 0:
            self.kill()

        if self.rect.x < 1:
            self.rect.x = 1
            game_window.blit(self.image, (self.rect.x, self.rect.y))
        if self.rect.x > WINDOW_WIDTH - WIDTH:
            self.rect.x = WINDOW_WIDTH - WIDTH
            game_window.blit(self.image, (self.rect.x, self.rect.y))
        if self.rect.y < 1:
            self.rect.y = 1
            game_window.blit(self.image, (self.rect.x, self.rect.y))
        if self.rect.y > BOTTOMBORDER:
            self.rect.y = BOTTOMBORDER
            game_window.blit(self.image, (self.rect.x, self.rect.y))


        else:
            game_window.blit(self.image, (self.rect.x, self.rect.y))


class Anchovy(sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = CUTTER.copy()
        self.speed = REG_SPEED
        all_anchovies.add(self)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect = self.image.get_rect(center=(x, y))
        self.radius = self.rect.width // 2
    def update(self, game_window):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
        else:
            game_window.blit(self.image, (self.rect.x, self.rect.y))

class BulletSprite(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = REG_SPEED
        self.lane = randint(0, 4)
        all_bullets.add(self)
        self.image = PEPPERONI.copy()
        x = randint(0, WINDOW_WIDTH)
        self.rect = self.image.get_rect(center=(x, 0))
        self.radius = self.rect.width // 2
        self.health = 100

    def update(self, game_window, counters):
        collidedboom = sprite.spritecollide(self, all_bombs, True)
        if collidedboom is not None:
            for anchovy in collidedboom:
                for vampire in all_vampires:
                    vampire.health = 0
                for bullet in all_bullets:
                    bullet.kill()
        self.rect.y += self.speed

        if self.health <= 0 or self.rect.y > BOTTOMBORDER:
            self.kill()



        else:
            game_window.blit(self.image, (self.rect.x, self.rect.y))

class Bomb(sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = CURSIFORX.copy()
        self.speed = REG_SPEED
        all_bombs.add(self)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect = self.image.get_rect(center=(x, y))
        self.radius = self.rect.width // 2
    def update(self, game_window):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
        else:
            game_window.blit(self.image, (self.rect.x, self.rect.y))

# Create a new class
class Counters(object):
    def __init__(self, pizza_bucks, buck_rate, buck_booster, timer):
        self.loop_count = 0
        self.display_font = font.Font('../gameassets/pizza_font.ttf', 25)
        self.pizza_bucks = pizza_bucks
        self.buck_rate = buck_rate
        self.buck_booster = buck_booster
        self.bucks_rect = None
        self.timer = timer
        self.timer_rect = None
        self.bad_reviews = 3
        self.bad_rev_rect = None
        self.score = 0
    def increment_bucks(self):
        if self.loop_count % self.buck_rate == 0:
            self.pizza_bucks += self.buck_booster

    def draw_bucks(self, game_window):
        if bool(self.bucks_rect):
            game_window.blit(BACKGROUND, (self.bucks_rect.x, self.bucks_rect.y), self.bucks_rect)
        bucks_surf = self.display_font.render(str(self.pizza_bucks), True, WHITE)

        self.bucks_rect = bucks_surf.get_rect()
        self.bucks_rect.x = WINDOW_WIDTH - 50
        self.bucks_rect.y = WINDOW_HEIGHT - 50
        game_window.blit(bucks_surf, self.bucks_rect)

    def draw_bad_reviews(self, game_window):
        if bool(self.bad_rev_rect):
            game_window.blit(BACKGROUND, (self.bad_rev_rect.x, self.bad_rev_rect.y), self.bad_rev_rect)
        bad_rev_surf = self.display_font.render(str(self.bad_reviews), True, WHITE)
        self.bad_rev_rect = bad_rev_surf.get_rect()
        self.bad_rev_rect.x = WINDOW_WIDTH - 150
        self.bad_rev_rect.y = WINDOW_HEIGHT - 50
        game_window.blit(bad_rev_surf, self.bad_rev_rect)

    def draw_timer(self, game_window):
        if bool(self.timer_rect):
            game_window.blit(BACKGROUND, (self.timer_rect.x, self.timer_rect.y), self.timer_rect)
        # timer_surf = self.display_font.render(str((self.timer - self.loop_count) // FRAME_RATE), True, WHITE)
        timer_surf = self.display_font.render(str(self.score), True, WHITE)
        self.timer_rect = timer_surf.get_rect()
        self.timer_rect.x = WINDOW_WIDTH - 250
        self.timer_rect.y = WINDOW_HEIGHT - 50
        game_window.blit(timer_surf, self.timer_rect)

    def update(self, game_window):
        self.loop_count += 1
        self.increment_bucks()
        self.draw_bucks(game_window)
        self.draw_bad_reviews(game_window)
        self.draw_timer(game_window)



# --------------------------------------------
# Create class instances and groups
# Create a group for all Vampire Sprite Instances
all_vampires = sprite.Group()
playersprites = sprite.Group()
all_anchovies = sprite.Group()
all_bullets = sprite.Group()
all_bombs = sprite.Group()

counters = Counters(STARTING_BUCKS,BUCK_RATE,STARTING_BUCK_BOOSTER, WIN_TIME)

#-----------------------------------------
#Initialize and Draw background Grid


#--------------------------------------Blits
#Display the background image to the screen
GAME_WINDOW.blit(BACKGROUND, (0, 0))


#------------------------------------------
# Start Main Game Loop
game_running = True
program_running = True
# Game Loop
mixer.music.load('../gameassets/Isolation.mp3')
mixer.music.play(-1)
PlayerSprite()
while game_running:
    GAME_WINDOW.blit(BACKGROUND, (0, 0))
    # Check for Events
    for event in pygame.event.get():

        # Exit the loop on Quit
        if event.type == QUIT:
            game_running = False
            program_running = False
        if event.type == KEYDOWN:
            if event.key == K_e or event.key == K_x:
                for sprote in playersprites:
                    if counters.bad_reviews >= 1:
                        Bomb(sprote.rect.x, sprote.rect.y)
                        counters.bad_reviews -= 1

    keydown = pygame.key.get_pressed()
    for sprote in playersprites:
        if keydown[K_LSHIFT] or keydown[K_RSHIFT]:
            sprote.speed = REG_SPEED /2
        else:
            sprote.speed = REG_SPEED
        if keydown[K_UP] or keydown[K_w]:
            sprote.rect.y -= sprote.speed
        if keydown[K_DOWN] or keydown[K_s]:
            sprote.rect.y += sprote.speed
        if keydown[K_LEFT] or keydown[K_a]:
            sprote.rect.x -= sprote.speed
        if keydown[K_RIGHT] or keydown[K_d]:
            sprote.rect.x += sprote.speed
        if keydown[K_q] or keydown[K_z]:
            Anchovy(sprote.rect.x,sprote.rect.y)
    if vampire_spawn_times and counters.loop_count >= vampire_spawn_times[0]:
        VampireSprite()
        vampire_spawn_times.pop(0)
    if randint(1,BULLETSPAWN_RATE) == 1:
        BulletSprite()
#------------------------------------------



    if counters.pizza_bucks <= 0:
        game_running = False
    if counters.loop_count > WIN_TIME:
        game_running = False

    for vampire in all_vampires:
        vampire.update(GAME_WINDOW, counters)
    for player in playersprites:
        player.update(GAME_WINDOW, counters)
    for anchovie in all_anchovies:
        anchovie.update(GAME_WINDOW)
    for bullet in all_bullets:
        bullet.update(GAME_WINDOW, counters)
    for bomb in all_bombs:
        bomb.update(GAME_WINDOW)
    #Update Counters
    counters.update(GAME_WINDOW)

    display.update()

    # Set the frame rate
    clock.tick(FRAME_RATE)
# End of Main Game Loop
#------------------------------------------
end_font = font.Font('../gameassets/pizza_font.ttf', 50)

#Test od either the win or lose condition is met
if program_running:
    if counters.pizza_bucks <= 0:
        end_surf = end_font.render('Game Over', True, WHITE)
    else:
        end_surf = end_font.render('You Win!', True, WHITE)
    mixer.music.stop()
    GAME_WINDOW.blit(end_surf, (350, 200))
    display.update()

#Enable exit from end game message screen
while program_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            program_running = False
        elif event.type == MOUSEBUTTONDOWN:
            import level2
            program_running = False
    clock.tick(FRAME_RATE)
# clean up
pygame.quit()

