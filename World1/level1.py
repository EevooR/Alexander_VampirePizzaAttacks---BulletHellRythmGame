# Import Libraries
import pygame
from pygame import *
from random import randint

CONTINUEGAME = True


while CONTINUEGAME:
    pygame.init()

    clock = time.Clock()

    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 750
    WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

    WIDTH = 50
    HEIGHT = 50
    HALF_WIDTH = WIDTH / 2
    HALF_HEIGHT = HEIGHT / 2

    ENEMYHEALTH = 60
    ENEMYHEALTHDEDUCTION = 2

    SONGFILES = {
        1: ("ByeByeBye.beatmap.txt", "ByeByeBye.mp3", "Bye Bye Bye", 4),
        2: ("Cara_Mia_Addio.beatmap.txt", "Cara_Mia_Addio.mp3", "Cara Mia Addio", 3),
        3: ("Evanescence-Sick.beatmap.txt", "Evanescence-Sick.mp3", "Sick", 4),
        4: ("Isolation.beatmap.txt", "Isolation.mp3", "Isolation", 3),
        5: ("MiseryBusiness.beatmap.txt", "MiseryBusiness.mp3", "Misery Business", 4),
        6: ("Pearlescent.beatmap.txt", "Pearlescent.mp3", "Pearlescent", 3),
        7: ("Positivity.beatmap.txt", "Positivity.mp3", "Positivity", 3),
        8: ("Still_Alive_Radio_Mix.beatmap.txt", "Still_Alive_Radio_Mix.mp3", "Still Alive Radio", 1),
        9: ("StillAlive.beatmap.txt", "StillAlive.mp3", "Still Alive", 3),
        10: ("ThatsWhatYouGet.beatmap.txt", "ThatsWhatYouGet.mp3", "That's What You Get", 4),
        11: ("ThePlagues.beatmap.txt", "ThePlagues.mp3", "The Plagues", 3),
        12: ("Thoughts.beatmap.txt", "Thoughts.mp3", "Thoughts", 2),
        13: ("TouchOfGold-Extended.beatmap.txt", "TouchOfGold-Extended.mp3", "Touch of Gold", 5),
        14: ("Turret_Wife_Serenade.beatmap.txt", "Turret_Wife_Serenade.mp3", "Turret Wife Serenade", 2),
        15: ("Want_You_Gone.beatmap.txt", "Want_You_Gone.mp3", "Want You Gone", 3),
        16: ("YouCantEscapeYouKnow.beatmap.txt", "YouCantEscapeYouKnow.mp3", "You Can't Escape You Know", 7),
        17: ("GoldenLand.beatmap.txt", "GoldenLand.mp3", "Golden Lands of Prester John", 5)
    }

    SONGCHOICE = randint(1, 17)
    SONGBMP = '../gameassets/Music/' + str(SONGFILES[SONGCHOICE][0])
    SONG = '../gameassets/Music/' + str(SONGFILES[SONGCHOICE][1])

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

    ICCOOLDOWN = 480
    VAMPIRISM = 5

    OCOOLDOWN = 200
    SLOWSPEED = 1

    PCOOLDOWN = 240
    LCOOLDOWN = 120
    KILLRATE = 5
    KCOOLDOWN = 960
    IMMUNITYCOOLDOWN = 240
    JCOOLDOWN = 240

    MAX_BAD_REVIEWS = 300
    WIN_TIME = FRAME_RATE * 60 * SONGFILES[SONGCHOICE][3]

    GAME_WINDOW = display.set_mode(WINDOW_RES)
    display.set_caption('Attack of the Vampire Pizzas by Enzo Alexander - BulletHell')

    background_img = image.load('../gameassets/background.png')
    background_surf = Surface.convert_alpha(background_img)
    BACKGROUND = transform.scale(background_surf, WINDOW_RES)

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

    basil_img = image.load('../gameassets/basil1.png')
    basil_surf = Surface.convert_alpha(basil_img)
    BASIL = transform.scale(basil_surf, (WIDTH, HEIGHT))

    anchovy_img = image.load('../gameassets/anchovy.png')
    anchovy_surf = Surface.convert_alpha(anchovy_img)
    ANCHOVY = transform.scale(anchovy_surf, (WIDTH, HEIGHT))

    pepper_img = image.load('../gameassets/pepper.png')
    pepper_surf = Surface.convert_alpha(pepper_img)
    PEPPER = transform.scale(pepper_surf, (WIDTH, HEIGHT))

    cheese_img = image.load('../gameassets/cheese.png')
    cheese_surf = Surface.convert_alpha(cheese_img)
    CHEESE = transform.scale(cheese_surf, (WIDTH, HEIGHT))

    Sushi_img = image.load('../gameassets/sushi1.png')
    sushi_surf = Surface.convert_alpha(Sushi_img)
    SUSHI = transform.scale(sushi_surf, (WIDTH, HEIGHT))

    supersushi_img = image.load('../gameassets/sushi2.png')
    supersushi_surf = Surface.convert_alpha(supersushi_img)
    SUPERSUSHI = transform.scale(supersushi_surf, (WIDTH, HEIGHT))

    pineapple_img = image.load('../gameassets/pineapple.png')
    pineapple_surf = Surface.convert_alpha(pineapple_img)
    PINEAPPLE = transform.scale(pineapple_surf, (WIDTH, HEIGHT))

    BASILMINI = transform.scale(basil_surf, (HALF_WIDTH, HALF_HEIGHT))
    ANCHOVYMINI = transform.scale(anchovy_surf, (HALF_WIDTH, HALF_HEIGHT))
    PEPPERMINI = transform.scale(pepper_surf, (HALF_WIDTH, HALF_HEIGHT))
    CHEESEMINI = transform.scale(cheese_surf, (HALF_WIDTH, HALF_HEIGHT))
    SUSHIMINI = transform.scale(sushi_surf, (HALF_WIDTH, HALF_HEIGHT))
    SUPERSUSHIMINI = transform.scale(supersushi_surf, (HALF_WIDTH, HALF_HEIGHT))
    PINEAPPLEMINI = transform.scale(pineapple_surf, (HALF_WIDTH, HALF_HEIGHT))

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


    # vampire_spawn_times = load_beatmap('../gameassets/Music/TouchOfGold-Extended.beatmap.txt')
    vampire_spawn_times = load_beatmap(SONGBMP)


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
            self.health = ENEMYHEALTH

        def update(self, game_window, counters):
            collided = sprite.spritecollide(self, all_anchovies, True)
            if collided is not None:
                for anchovy in collided:
                    self.health -= ENEMYHEALTHDEDUCTION
            collidedboom = sprite.spritecollide(self, all_bombs, True)
            if collidedboom is not None:
                for anchovy in collidedboom:
                    for vampire in all_vampires:
                        vampire.health = 0
                    for bullet in all_bullets:
                        bullet.kill()
            collidedspell = sprite.spritecollide(self, all_spellcards, True)
            if collidedspell is not None:
                for spell in collidedspell:
                    if spell.spellcard == "heal":
                        healup = 0
                        for vampire in all_vampires:
                            healup += 1
                        for bullet in all_bullets:
                            healup += 1
                        healup = healup // VAMPIRISM
                        counters.pizza_bucks += healup
                        for vampire in all_vampires:
                            vampire.health = 0
                        for bullet in all_bullets:
                            bullet.kill()
                    elif spell.spellcard == "slow":
                        for vampire in all_vampires:
                            vampire.speed = SLOWSPEED
                        for bullet in all_bullets:
                            bullet.speed = SLOWSPEED
                    elif spell.spellcard == "block":
                        counters.bmpactivated = False
                    elif spell.spellcard == "draw":
                        for vampire in all_vampires:
                            vampire.rect.x = self.rect.x
                        for bullet in all_bullets:
                            bullet.rect.x = self.rect.x
                    elif spell.spellcard == "immune":
                        counters.playerimmune = True
                    elif spell.spellcard == "randomkill":
                        for vampire in all_vampires:
                            if randint(1, KILLRATE) == 1:
                                vampire.health = 0
                        for bullet in all_bullets:
                            if randint(1, KILLRATE) == 1:
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
            self.immuneimage = SUPERSUSHI.copy()
            y = 325
            x = 300
            self.rect = self.image.get_rect(center=(x, y))
            self.radius = self.rect.width // 2
            self.health = PLAYERHEARTS

        def update(self, game_window, counters):

            collided = sprite.spritecollide(self, all_vampires, True)
            if collided is not None and not counters.playerimmune:
                for anchovy in collided:
                    self.health -= 1
                    counters.pizza_bucks -= 1
                    counters.bad_reviews = STARTING_BUCKS
                    for vampire in all_vampires:
                        vampire.kill()
                    for bullet in all_bullets:
                        bullet.kill()
            collidedbullet = sprite.spritecollide(self, all_bullets, True)
            if collidedbullet is not None and not counters.playerimmune:
                for anchovy in collidedbullet:
                    self.health -= 1
                    counters.pizza_bucks -= 1
                    counters.bad_reviews = STARTING_BUCKS
                    for vampire in all_vampires:
                        vampire.kill()
                    for bullet in all_bullets:
                        bullet.kill()
            if self.health != counters.pizza_bucks:
                self.health = counters.pizza_bucks
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
                if counters.playerimmune:
                    game_window.blit(self.immuneimage, (self.rect.x, self.rect.y))
                else:
                    game_window.blit(self.image, (self.rect.x, self.rect.y))


    class Anchovy(sprite.Sprite):
        def __init__(self, x, y):
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
            collidedspell = sprite.spritecollide(self, all_spellcards, True)
            if collidedspell is not None:
                for spell in collidedspell:
                    if spell.spellcard == "heal":
                        healup = 0
                        for vampire in all_vampires:
                            healup += 1
                        for bullet in all_bullets:
                            healup += 1
                        healup = healup // VAMPIRISM
                        counters.pizza_bucks += healup
                        for vampire in all_vampires:
                            vampire.health = 0
                        for bullet in all_bullets:
                            bullet.kill()
                    elif spell.spellcard == "slow":
                        for vampire in all_vampires:
                            vampire.speed = SLOWSPEED
                        for bullet in all_bullets:
                            bullet.speed = SLOWSPEED
                    elif spell.spellcard == "block":
                        counters.randombulletsactivated = False
                    elif spell.spellcard == "draw":
                        for vampire in all_vampires:
                            vampire.rect.x = self.rect.x
                        for bullet in all_bullets:
                            bullet.rect.x = self.rect.x
                    elif spell.spellcard == "immune":
                        counters.playerimmune = True
                    elif spell.spellcard == "randomkill":
                        for vampire in all_vampires:
                            if randint(1, KILLRATE) == 1:
                                vampire.health = 0
                        for bullet in all_bullets:
                            if randint(1, KILLRATE) == 1:
                                bullet.kill()

            self.rect.y += self.speed

            if self.health <= 0 or self.rect.y > BOTTOMBORDER:
                self.kill()



            else:
                game_window.blit(self.image, (self.rect.x, self.rect.y))


    class Bomb(sprite.Sprite):
        def __init__(self, x, y):
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

    class SpellCardHeal(sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = BASIL.copy()
            self.speed = 0
            all_spellcards.add(self)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.rect = self.image.get_rect(center=(x, y))
            self.radius = self.rect.width // 2
            self.spellcard = "heal"

        def update(self, game_window):
            self.rect.y -= self.speed
            if self.rect.y <= 0:
                self.kill()
            else:
                game_window.blit(self.image, (self.rect.x, self.rect.y))

    class SpellCardSlow(SpellCardHeal):
        def __init__(self, x, y):
            super(SpellCardSlow, self).__init__(x, y)
            self.image = ANCHOVY.copy()
            self.spellcard = "slow"

    class SpellCardBlock(SpellCardHeal):
        def __init__(self, x, y):
            super(SpellCardBlock, self).__init__(x, y)
            self.image = PEPPER.copy()
            self.spellcard = "block"

    class SpellCardDraw(SpellCardHeal):
        def __init__(self, x, y):
            super(SpellCardDraw, self).__init__(x, y)
            self.image = CHEESE.copy()
            self.spellcard = "draw"

    class SpellCardImmune(SpellCardHeal):
        def __init__(self, x, y):
            super(SpellCardImmune, self).__init__(x, y)
            self.image = SUSHI.copy()
            self.spellcard = "immune"

    class SpellCardRandomKill(SpellCardHeal):
        def __init__(self, x, y):
            super(SpellCardRandomKill, self).__init__(x, y)
            self.image = PINEAPPLE.copy()
            self.spellcard = "randomkill"

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
            self.song_rect = None
            self.bad_reviews = 3
            self.bad_rev_rect = None
            self.score = 0
            self.healactive = True
            self.slowactive = True
            self.blockactive = True
            self.bmpactivated = True
            self.randombulletsactivated = True
            self.drawactive = True
            self.immuneactive = True
            self.playerimmune = False
            self.randomdeathactive = True

            self.basilicon_rect = None
            self.anchovyicon_rect = None
            self.peppericon_rect = None
            self.cheeseicon_rect = None
            self.sushiicon_rect = None
            self.supersushiicon_rect = None
            self.pineappleicon_rect = None

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

        def draw_name(self, game_window):
            if bool(self.song_rect):
                game_window.blit(BACKGROUND, (self.song_rect.x, self.song_rect.y), self.song_rect)
            song_surf = self.display_font.render(str(SONGFILES[SONGCHOICE][2]), True, WHITE)
            self.song_rect = song_surf.get_rect()
            self.song_rect.x = WINDOW_WIDTH - 500
            self.song_rect.y = WINDOW_HEIGHT - 75
            game_window.blit(song_surf, self.song_rect)

        def draw_basilicon(self, game_window):
            if bool(self.basilicon_rect):
                game_window.blit(BACKGROUND, (self.basilicon_rect.x, self.basilicon_rect.y), self.basilicon_rect)
            self.basilicon_rect = BASILMINI.get_rect()
            self.basilicon_rect.x = WINDOW_WIDTH - 600
            self.basilicon_rect.y = WINDOW_HEIGHT - 90
            if self.healactive:
                game_window.blit(BASILMINI, self.basilicon_rect)

        def draw_anchovyicon(self, game_window):
            if bool(self.anchovyicon_rect):
                game_window.blit(BACKGROUND, (self.anchovyicon_rect.x, self.anchovyicon_rect.y), self.anchovyicon_rect)
            self.anchovyicon_rect = ANCHOVYMINI.get_rect()
            self.anchovyicon_rect.x = WINDOW_WIDTH - 575
            self.anchovyicon_rect.y = WINDOW_HEIGHT - 90
            if self.slowactive:
                game_window.blit(ANCHOVYMINI, self.anchovyicon_rect)

        def draw_peppericon(self, game_window):
            if bool(self.peppericon_rect):
                game_window.blit(BACKGROUND, (self.peppericon_rect.x, self.peppericon_rect.y), self.peppericon_rect)
            self.peppericon_rect = PEPPERMINI.get_rect()
            self.peppericon_rect.x = WINDOW_WIDTH - 550
            self.peppericon_rect.y = WINDOW_HEIGHT - 90
            if self.blockactive:
                game_window.blit(PEPPERMINI, self.peppericon_rect)

        def draw_cheeseicon(self, game_window):
            if bool(self.cheeseicon_rect):
                game_window.blit(BACKGROUND, (self.cheeseicon_rect.x, self.cheeseicon_rect.y), self.cheeseicon_rect)
            self.cheeseicon_rect = CHEESEMINI.get_rect()
            self.cheeseicon_rect.x = WINDOW_WIDTH - 600
            self.cheeseicon_rect.y = WINDOW_HEIGHT - 65
            if self.drawactive:
                game_window.blit(CHEESEMINI, self.cheeseicon_rect)

        def draw_sushiicon(self, game_window):
            if bool(self.sushiicon_rect):
                game_window.blit(BACKGROUND, (self.sushiicon_rect.x, self.sushiicon_rect.y), self.sushiicon_rect)
            self.sushiicon_rect = SUSHIMINI.get_rect()
            self.sushiicon_rect.x = WINDOW_WIDTH - 575
            self.sushiicon_rect.y = WINDOW_HEIGHT - 65
            if self.immuneactive:
                game_window.blit(SUSHIMINI, self.sushiicon_rect)

        def draw_supersushiicon(self, game_window):
            if bool(self.supersushiicon_rect):
                game_window.blit(BACKGROUND, (self.supersushiicon_rect.x, self.supersushiicon_rect.y), self.supersushiicon_rect)
            self.supersushiicon_rect = SUPERSUSHIMINI.get_rect()
            self.supersushiicon_rect.x = WINDOW_WIDTH - 575
            self.supersushiicon_rect.y = WINDOW_HEIGHT - 40
            if self.playerimmune:
                game_window.blit(SUPERSUSHIMINI, self.supersushiicon_rect)

        def draw_pineappleicon(self, game_window):
            if bool(self.pineappleicon_rect):
                game_window.blit(BACKGROUND, (self.pineappleicon_rect.x, self.pineappleicon_rect.y), self.pineappleicon_rect)
            self.pineappleicon_rect = PINEAPPLEMINI.get_rect()
            self.pineappleicon_rect.x = WINDOW_WIDTH - 550
            self.pineappleicon_rect.y = WINDOW_HEIGHT - 65
            if self.randomdeathactive:
                game_window.blit(PINEAPPLEMINI, self.pineappleicon_rect)

        def update(self, game_window):
            self.loop_count += 1
            self.increment_bucks()
            self.draw_bucks(game_window)
            self.draw_bad_reviews(game_window)
            self.draw_timer(game_window)
            self.draw_name(game_window)
            self.draw_basilicon(game_window)
            self.draw_anchovyicon(game_window)
            self.draw_peppericon(game_window)
            self.draw_cheeseicon(game_window)
            self.draw_sushiicon(game_window)
            self.draw_supersushiicon(game_window)
            self.draw_pineappleicon(game_window)


    # --------------------------------------------
    # Create class instances and groups
    # Create a group for all Vampire Sprite Instances
    all_vampires = sprite.Group()
    playersprites = sprite.Group()
    all_anchovies = sprite.Group()
    all_bullets = sprite.Group()
    all_bombs = sprite.Group()
    all_spellcards = sprite.Group()

    counters = Counters(STARTING_BUCKS, BUCK_RATE, STARTING_BUCK_BOOSTER, WIN_TIME)

    # -----------------------------------------
    # Initialize and Draw background Grid

    # --------------------------------------Blits
    # Display the background image to the screen
    GAME_WINDOW.blit(BACKGROUND, (0, 0))

    # ------------------------------------------
    # Start Main Game Loop
    game_running = True
    program_running = True
    # Game Loop
    mixer.music.load(SONG)
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
                CONTINUEGAME = False
            if event.type == KEYDOWN:
                if event.key == K_e or event.key == K_x:
                    for sprote in playersprites:
                        if counters.bad_reviews >= 1:
                            Bomb(sprote.rect.x, sprote.rect.y)
                            counters.bad_reviews -= 1
                if event.key == K_ESCAPE:
                    game_running = False
                    program_running = False
                    CONTINUEGAME = False
                if event.key == K_i:
                    if counters.healactive:
                        counters.healactive = False
                        for playerchar in playersprites:
                            SpellCardHeal(playerchar.rect.x, playerchar.rect.y)
                if event.key == K_o:
                    if counters.slowactive:
                        counters.slowactive = False
                        for playerchar in playersprites:
                            SpellCardSlow(playerchar.rect.x, playerchar.rect.y)
                if event.key == K_p:
                    if counters.blockactive:
                        counters.blockactive = False
                        for playerchar in playersprites:
                            SpellCardBlock(playerchar.rect.x, playerchar.rect.y)
                if event.key == K_j:
                    if counters.drawactive:
                        counters.drawactive = False
                        for playerchar in playersprites:
                            SpellCardDraw(playerchar.rect.x, playerchar.rect.y)
                if event.key == K_k:
                    if counters.immuneactive:
                        counters.immuneactive = False
                        for playerchar in playersprites:
                            SpellCardImmune(playerchar.rect.x, playerchar.rect.y)
                if event.key == K_l:
                    if counters.randomdeathactive:
                        counters.randomdeathactive = False
                        for playerchar in playersprites:
                            SpellCardRandomKill(playerchar.rect.x, playerchar.rect.y)

        keydown = pygame.key.get_pressed()
        for sprote in playersprites:
            if keydown[K_LSHIFT] or keydown[K_RSHIFT]:
                sprote.speed = REG_SPEED / 2
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
                Anchovy(sprote.rect.x, sprote.rect.y)
        if vampire_spawn_times and counters.loop_count >= vampire_spawn_times[0]:
            if counters.bmpactivated:
                VampireSprite()
            vampire_spawn_times.pop(0)
        if randint(1, BULLETSPAWN_RATE) == 1 and counters.randombulletsactivated:
            BulletSprite()
        if randint(1, ICCOOLDOWN) == 1:
            counters.healactive = True
        if randint(1, OCOOLDOWN) == 1:
            counters.slowactive = True
        if randint(1, ICCOOLDOWN) == 1:
            counters.healactive = True
        if randint(1, PCOOLDOWN) == 1:
            counters.blockactive = True
            counters.randombulletsactivated = True
            counters.bmpactivated = True
        if randint(1, JCOOLDOWN) == 1:
            counters.drawactive = True
        if randint(1, KCOOLDOWN) == 1:
            counters.immuneactive = True
        if randint(1, IMMUNITYCOOLDOWN) == 1:
            counters.playerimmune = False
        if randint(1, LCOOLDOWN) == 1:
            counters.randomdeathactive = True
        # ------------------------------------------

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
        for cards in all_spellcards:
            cards.update(GAME_WINDOW)
        # Update Counters
        counters.update(GAME_WINDOW)

        display.update()

        # Set the frame rate
        clock.tick(FRAME_RATE)
    # End of Main Game Loop
    # ------------------------------------------
    end_font = font.Font('../gameassets/pizza_font.ttf', 50)

    # Test od either the win or lose condition is met
    if program_running:
        if counters.pizza_bucks <= 0:
            end_surf = end_font.render('Game Over', True, WHITE)
        else:
            end_surf = end_font.render('You Win!', True, WHITE)
        mixer.music.stop()
        GAME_WINDOW.blit(end_surf, (350, 200))
        display.update()

    # Enable exit from end game message screen
    while program_running:
        for event in pygame.event.get():
            if event.type == QUIT:
                program_running = False
                CONTINUEGAME = False
            elif event.type == MOUSEBUTTONDOWN:
                program_running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    program_running = False
                    CONTINUEGAME = False
                if event.key == K_RETURN:
                    program_running = False
        clock.tick(FRAME_RATE)
    # clean up
    pygame.quit()

