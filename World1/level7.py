# Import Libraries
import pygame
from pygame import *
from random import randint, choice


pygame.init()

clock = time.Clock()

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

WIDTH = 100
HEIGHT = 100

WHITE = (255, 255, 255)

SPAWN_RATE = 150
FRAME_RATE = 60
WEAKEN_RATE = 800



REG_SPEED = 2
SLOW_SPEED = 1
FAST_SPEED = 3

cannon_coordinates = []
FIRE_RATE = 60
STARTING_BUCKS = 15
BUCK_RATE = 120
STARTING_BUCK_BOOSTER = 1
CANT_AFFORD = pygame.mixer.Sound('../gameassets/Bzzt.mp3')
TRAPBREAK = pygame.mixer.Sound('../gameassets/TrapBreak.mp3')
MINEEXPLODE = pygame.mixer.Sound('../gameassets/SPUDOW.mp3')
CURRENT_ROW = 1
STARTING_HEALTH = 100


MAX_BAD_REVIEWS = 10
WIN_TIME = FRAME_RATE * 60 * 3

GAME_WINDOW = display.set_mode(WINDOW_RES)
display.set_caption('Attack of the Vampire Pizzas by Enzo Alexander - Level 7: Anchovy Cannons and Table Mines')

background_img = image.load('../gameassets/restaurant.jpg')
background_surf = Surface.convert_alpha(background_img)
BACKGROUND =transform.scale(background_surf, WINDOW_RES)

pizza_img = image.load('../gameassets/vampire.png')
pizza_surf = Surface.convert_alpha(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf, (WIDTH, HEIGHT))

med_health_img = image.load('../gameassets/pizza60health.png')
med_health_surf = Surface.convert_alpha(med_health_img)
MED_HEALTH = transform.scale(med_health_surf, (WIDTH, HEIGHT))

low_health_img = image.load('../gameassets/pizza30health.png')
low_health_surf = Surface.convert_alpha(low_health_img)
LOW_HEALTH = transform.scale(low_health_surf, (WIDTH, HEIGHT))

garlic_img = image.load('../gameassets/garlic.png')
garlic_surf = Surface.convert_alpha(garlic_img)
GARLIC = transform.scale(garlic_surf, (WIDTH, HEIGHT))

cutter_img = image.load('../gameassets/pizzacutter.png')
cutter_surf = Surface.convert_alpha(cutter_img)
CUTTER = transform.scale(cutter_surf, (WIDTH, HEIGHT))

pepperoni_img = image.load('../gameassets/pepperoni.png')
pepperoni_surf = Surface.convert_alpha(pepperoni_img)
PEPPERONI = transform.scale(pepperoni_surf, (WIDTH, HEIGHT))

good_pizza_img = image.load('../gameassets/pizza_slice.png')
good_pizza_surf = Surface.convert_alpha(good_pizza_img)
GOODPIZZA = transform.scale(good_pizza_surf, (WIDTH, HEIGHT))

were_img = image.load('../gameassets/were_pizza.png')
were_surf = Surface.convert_alpha(were_img)
WERE_PIZZA = transform.scale(were_surf, (WIDTH, HEIGHT))

zombie_img = image.load('../gameassets/zombie_pizza.png')
zombie_surf = Surface.convert_alpha(zombie_img)
ZOMBIE_PIZZA = transform.scale(zombie_surf, (WIDTH, HEIGHT))

cthulhu_img = image.load('../gameassets/cthulu-pizza.png')
cthulhu_surf = Surface.convert_alpha(cthulhu_img)
CTHULHU_PIZZA = transform.scale(cthulhu_surf, (WIDTH, HEIGHT))

table_img = image.load('../gameassets/pizza-table.png')
table_surf = Surface.convert_alpha(table_img)
TABLE = transform.scale(table_surf, (WIDTH, HEIGHT))

cannon_img = image.load('../gameassets/anchovy-cannon.png')
cannon_surf = Surface.convert_alpha(cannon_img)
CANNON = transform.scale(cannon_surf, (WIDTH, HEIGHT))

anchovy_img = image.load('../gameassets/anchovy.png')
anchovy_surf = Surface.convert_alpha(anchovy_img)
ANCHOVY = transform.scale(anchovy_surf, (WIDTH, HEIGHT))

class VampireSprite(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = REG_SPEED
        self.lane = randint(0, 4)
        all_vampires.add(self)
        self.image = VAMPIRE_PIZZA.copy()
        y = 50 + self.lane * 100
        self.rect = self.image.get_rect(center = (1100,y))
        self.health = STARTING_HEALTH

    def update(self, game_window, counters):
        game_window.blit(BACKGROUND, (self.rect.x, self.rect.y), self.rect)

        collided = sprite.spritecollide(self, all_anchovies, True)
        if collided is not None:
            for anchovy in collided:
                self.health -= 30

        self.rect.x -= self.speed

        if self.health <= 0 or self.rect.x <= 100:
            self.kill()
            if self.rect.x <= 100:
                counters.bad_reviews += 1


        else:
            if 30 < self.health * 100 // STARTING_HEALTH < 60:
                self.image = MED_HEALTH.copy()
            elif self.health * 100 // STARTING_HEALTH <= 30:
                self.image = LOW_HEALTH.copy()
            game_window.blit(self.image, (self.rect.x, self.rect.y))

    def attack(self, tile):
        if tile.trap == SLOW:
            self.speed = SLOW_SPEED
        if tile.trap == DAMAGE:
            self.health -= 1
        if tile.trap == MINE:
            self.health = 0
            tile.trap = None
            mixer.Sound.play(MINEEXPLODE)
        if bool(tile.trap):
            if randint(1, WEAKEN_RATE) == 1:
                tile.trap = None
                self.speed = SLOW_SPEED
                mixer.Sound.play(TRAPBREAK)

class GoodPizzaSprite(VampireSprite):
    def __init__(self):
        super().__init__()
        self.image = GOODPIZZA.copy()

    def update(self, game_window, counters):
        game_window.blit(BACKGROUND, (self.rect.x, self.rect.y), self.rect)

        self.rect.x -= self.speed
        if self.health <= 0 or self.rect.x <= 100:
            self.kill()
            if self.rect.x <= 100:
                counters.bad_reviews -= 1
                counters.pizza_bucks = 0

        else:
            game_window.blit(self.image, (self.rect.x, self.rect.y))

    def attack(self, tile):
        if tile.trap == SLOW:
            self.speed = SLOW_SPEED
        if tile.trap == EARN:
            self.health -= 1
        if tile.trap == MINE:
            self.health = 0
            tile.trap = None
            mixer.Sound.play(MINEEXPLODE)

class WerePizza(VampireSprite):
    def __init__(self):
        super(WerePizza, self).__init__()
        self.speed = FAST_SPEED
        self.image = WERE_PIZZA.copy()
    def attack(self, tile):
        if tile.trap == SLOW:
            self.speed = SLOW_SPEED
        if tile.trap == DAMAGE:
            self.health -= 1
        if tile.trap == MINE:
            self.health = 0
            tile.trap = None
            mixer.Sound.play(MINEEXPLODE)
        if bool(tile.trap):
            if randint(1, WEAKEN_RATE) == 1:
                tile.trap = None
                self.speed = SLOW_SPEED
                mixer.Sound.play(TRAPBREAK)

class ZombiePizza(VampireSprite):
    def __init__(self):
        super(ZombiePizza, self).__init__()
        self.health = STARTING_HEALTH * 2
        self.image = ZOMBIE_PIZZA.copy()

    def update(self, game_window, counters):
        game_window.blit(BACKGROUND, (self.rect.x, self.rect.y), self.rect)
        self.rect.x -= self.speed

        collided = sprite.spritecollide(self, all_anchovies, True)
        if collided is not None:
            for anchovy in collided:
                self.health -= 30

        if self.health <= 0 or self.rect.x <= 100:
            if self.health <= 0 or self.rect.x <= 100:
                if self.rect.x <= 100:
                    counters.bad_reviews += 1
                self.kill()

        else:
            percent_health = self.health * 100 // STARTING_HEALTH * 2
            if percent_health > 80:
                self.image = ZOMBIE_PIZZA.copy()
            elif percent_health > 65:
                self.image = MED_HEALTH.copy()
            elif percent_health > 50:
                self.image = LOW_HEALTH.copy()
            elif percent_health > 35:
                self.image = ZOMBIE_PIZZA.copy()
            elif percent_health > 20:
                self.image = MED_HEALTH.copy()
            else:
                self.image = LOW_HEALTH.copy()
            GAME_WINDOW.blit(self.image, (self.rect.x, self.rect.y))

class CthulhuPizza(VampireSprite):
    def __init__(self):
        super(CthulhuPizza, self).__init__()
        self.image = CTHULHU_PIZZA.copy()
        self.speed = FAST_SPEED

    def update(self, game_window, counters):
        game_window.blit(BACKGROUND, (self.rect.x, self.rect.y), self.rect)
        self.rect.x -= self.speed

        collided = sprite.spritecollide(self, all_anchovies, True)
        if collided is not None:
            for anchovy in collided:
                self.health -= 10

        if self.health <= 0 or self.rect.x <= 100:
            if self.health <= 0 or self.rect.x <= 100:
                if self.rect.x <= 100:
                    counters.bad_reviews += 1
                self.kill()
        else:
            GAME_WINDOW.blit(self.image, (self.rect.x, self.rect.y))


    def attack(self, tile):
        if tile.trap == SLOW:
            self.health -= 2
        if tile.trap == DAMAGE:
            self.health += 1
        if tile.trap == EARN:
            self.speed = SLOW_SPEED
        if tile.trap == MINE:
            self.health = 0
            tile.trap = None
            mixer.Sound.play(MINEEXPLODE)
        if bool(tile.trap):
            if randint(1, WEAKEN_RATE) == 1:
                tile.trap = None
                self.speed = SLOW_SPEED
                mixer.Sound.play(TRAPBREAK)


# Create a new class
class Counters(object):
    #Set up the innit method with four arguments
    def __init__(self, pizza_bucks, buck_rate, buck_booster, timer, fire_rate):
        self.fire_rate = fire_rate
        #Start the gameloop counter at 0
        self.loop_count = 0
        # Set up the look of the counter on the screen
        self.display_font = font.Font('../gameassets/pizza_font.ttf', 25)
        #Define the pizza_bucks attribute using the pizza_bucks argument
        self.pizza_bucks = pizza_bucks
        #define the buck_rate attribute using the buck rate argument
        self.buck_rate = buck_rate
        self.buck_booster = buck_booster
        self.bucks_rect = None
        self.timer = timer
        self.timer_rect = None
        self.bad_reviews = 0
        self.bad_rev_rect = None
        #Increase the Player's Pzza bucks based on time passing
    def increment_bucks(self):
        # Add a set number of pizza bucks to the player's total once every 120 times the game loop runs (Aprox. every 2 secs)
        if self.loop_count % self.buck_rate == 0:
            self.pizza_bucks += self.buck_booster
    def update_cannon(self):
        for location in cannon_coordinates :
            if self.loop_count % self.fire_rate ==0:
                Anchovy(location)

    #Define a new method with 2 arguments
    def draw_bucks(self, game_window):
        #Erase what has been written (last number from game window)
        if bool(self.bucks_rect):
            game_window.blit(BACKGROUND, (self.bucks_rect.x, self.bucks_rect.y), self.bucks_rect)
        bucks_surf = self.display_font.render(str(self.pizza_bucks), True, WHITE)

        #Create a rect for the bucks surf so that we can place it on our window
        self.bucks_rect = bucks_surf.get_rect()
        #Place the counter in the middle of the tile on the bottom right corner
        self.bucks_rect.x = WINDOW_WIDTH - 50
        self.bucks_rect.y = WINDOW_HEIGHT - 50
        #Display the new pizza bucks total to the game window
        game_window.blit(bucks_surf, self.bucks_rect)

    # Draw The player's Bad reviews total to the screen
    def draw_bad_reviews(self, game_window):
        #test if there is a new number if bad reviews and erase the old number if there is.
        if bool(self.bad_rev_rect):
            game_window.blit(BACKGROUND, (self.bad_rev_rect.x, self.bad_rev_rect.y), self.bad_rev_rect)
        #tell the program the font and color to use in the display
        bad_rev_surf = self.display_font.render(str(self.bad_reviews), True, WHITE)
        #Set up rect so that we can interact with the number
        self.bad_rev_rect = bad_rev_surf.get_rect()
        #Put the display in the second to last column and bottom row of the Grid
        self.bad_rev_rect.x = WINDOW_WIDTH - 150
        self.bad_rev_rect.y = WINDOW_HEIGHT - 50
        #Display the number on the screen
        game_window.blit(bad_rev_surf, self.bad_rev_rect)

    # Draw our Timer to the game window
    def draw_timer(self, game_window):
        if bool(self.timer_rect):
            game_window.blit(BACKGROUND, (self.timer_rect.x, self.timer_rect.y), self.timer_rect)
        timer_surf = self.display_font.render(str((self.timer - self.loop_count) // FRAME_RATE), True, WHITE)
        self.timer_rect = timer_surf.get_rect()
        self.timer_rect.x = WINDOW_WIDTH - 250
        self.timer_rect.y = WINDOW_HEIGHT - 50
        game_window.blit(timer_surf, self.timer_rect)

        #Define Update function (Method)
    def update(self, game_window):
        self.loop_count += 1
        self.increment_bucks()
        self.draw_bucks(game_window)
        self.draw_bad_reviews(game_window)
        self.draw_timer(game_window)
        self.update_cannon()


#Set up the different kinds of traps
class Trap(object):
    def __init__(self, trap_kind, cost, trap_img):
        self.trap_kind = trap_kind
        self.cost = cost
        self.trap_img = trap_img

#Create a class for the trap applicator
class TrapApplicator(object):
    def __init__(self):
        self.selected = None

    def select_trap(self, trap):
        if trap.cost <= counters.pizza_bucks:
            self.selected = trap
    def select_tile(self, tile, counters):
        self.selected = tile.set_trap(self.selected,counters)
# Create a background tile object
class BackgroundTile(sprite.Sprite):
    # Set up instances of background tiles
    def __init__(self, rect):
        super().__init__()
        self.trap = None
        self.rect = rect


#Subclass of BackgroundTile where the player can set traps
class PlayTile(BackgroundTile):
    #Set trap on selected playtile
    def set_trap(self, trap, counters):
        if bool(trap) and not bool(self.trap):
            counters.pizza_bucks -= trap.cost
            self.trap = trap
            if trap == EARN :
                counters.buck_booster += 2
            if trap == PROJECTILE :
                cannon_coordinates.append((self.rect.x, self.rect.y))
        return None

    #Draw the trap image to the selected playtile
    def draw_trap(self, game_window, trap_applicator):
        if bool(self.trap):
            game_window.blit(self.trap.trap_img, (self.rect.x, self.rect.y))

class ButtonTile(BackgroundTile):
    def set_trap(self, trap, counters):
        if counters.pizza_bucks >= self.trap.cost:
            return self.trap
        else:
            CANT_AFFORD.play()
            return None

    def draw_trap(self, game_window, trap_applicator):
        if bool(trap_applicator.selected):
            if trap_applicator.selected == self.trap:
                draw.rect(game_window, (234,190,47), (self.rect.x, self.rect.y, WIDTH, HEIGHT), 5)

class InactiveTile(BackgroundTile):
    #Do Nothing if clicked
    def set_trap(self, trap, counters):
        return None

    #Do Not Display anything
    def draw_trap(self, game_window, trap_applicator):
        pass

class Anchovy(sprite.Sprite):
    def __init__(self, coordinates):
        super().__init__()
        self.image = ANCHOVY.copy()
        self.speed = REG_SPEED
        all_anchovies.add(self)
        self.rect = self.image.get_rect()
        self.rect.x = coordinates[0] +40
        self.rect.y = coordinates[1]
    def update(self, game_window):
        game_window.blit(BACKGROUND, (self.rect.x, self.rect.y), self.rect)
        self.rect.x += self.speed
        if self.rect.x > 1200:
            self.kill()
        else:
            game_window.blit(self.image, (self.rect.x, self.rect.y))
# --------------------------------------------
# Create class instances and groups
# Create a group for all Vampire Sprite Instances
all_vampires = sprite.Group()
all_anchovies = sprite.Group()


enemy_types = []
enemy_types.append(VampireSprite)
enemy_types.append(WerePizza)
enemy_types.append(GoodPizzaSprite)
enemy_types.append(ZombiePizza)
enemy_types.append(CthulhuPizza)
counters = Counters(STARTING_BUCKS,BUCK_RATE,STARTING_BUCK_BOOSTER, WIN_TIME, FIRE_RATE)

SLOW = Trap('SLOW', 5, GARLIC)
DAMAGE = Trap('DAMAGE', 3, CUTTER)
EARN = Trap('EARN', 7, PEPPERONI)
MINE = Trap('MINE', 10, TABLE)
PROJECTILE = Trap('PROJECTILE', 8, CANNON)

trap_applicator = TrapApplicator()
#-----------------------------------------
#Initialize and Draw background Grid
tile_grid = []
tile_color = WHITE
for row in range(6) :
    #Create ab empty list each time the loop runs
    row_of_tiles = []
    #Add each of the six list calles rows_of_tiles to the tile grid list
    tile_grid.append(row_of_tiles)
    for column in range(11) :
        # Create an invisible rect for each background tile sprite
        tile_rect = Rect(WIDTH * column, HEIGHT * row, WIDTH, HEIGHT)
        #for each column in each row,create a new background Tile Sprite
        if column <= 1 :
            new_tile = InactiveTile(tile_rect)
        else:
            if row == 5 :
                if 2<= column <= 6:
                    new_tile = ButtonTile(tile_rect)
                    new_tile.trap = [SLOW, DAMAGE, EARN, MINE, PROJECTILE][column-2]
                else:
                    new_tile = InactiveTile(tile_rect)
            else:
                new_tile = PlayTile(tile_rect)
        #add each new background tile sprite to the correct row_of_tiles list
        row_of_tiles.append(new_tile)
        if row ==5 and 2 <= column <= 6 :
            BACKGROUND.blit(new_tile.trap.trap_img,(new_tile.rect.x, new_tile.rect.y))
        if column != 0 and row != 5:
            if column != 1 :
                draw.rect(BACKGROUND, tile_color, (WIDTH * column, HEIGHT * row, WIDTH, HEIGHT), 1)


def trapchange(traprowin):
    for row in range(6):
        row_of_tiles = []
        # Add each of the six list calles rows_of_tiles to the tile grid list
        tile_grid.pop()
        tile_grid.append(row_of_tiles)
        for column in range(11):
            tile_rect = Rect(WIDTH * column, HEIGHT * row, WIDTH, HEIGHT)

            if row == 5:
                if 2 <= column <= 6:
                    new_tile = ButtonTile(tile_rect)
                    if traprowin == 1 :
                        new_tile.trap = [SLOW, DAMAGE, EARN, MINE, PROJECTILE][column - 2]
                else:
                    new_tile = InactiveTile(tile_rect)
                row_of_tiles.append(new_tile)
                if row == 5 and 2 <= column <= 6:
                    cropped_background = background_surf.subsurface(400, 500, 100, 100)
                    cropped_background_surf = transform.scale(cropped_background, (WIDTH, HEIGHT))

                    BACKGROUND.blit(cropped_background_surf, (tile_rect.x, tile_rect.y))
                    BACKGROUND.blit(new_tile.trap.trap_img, (new_tile.rect.x, new_tile.rect.y))
                if column != 0 and row != 5:
                    if column != 1:
                        draw.rect(BACKGROUND, tile_color, (WIDTH * column, HEIGHT * row, WIDTH, HEIGHT), 1)




#--------------------------------------Blits
#Display the background image to the screen
GAME_WINDOW.blit(BACKGROUND, (0, 0))


#------------------------------------------
# Start Main Game Loop
game_running = True
program_running = True

mixer.music.load('../gameassets/pizzaday.mp3')
mixer.music.play(-1)

# Game Loop
while game_running:

    # Check for Events
    for event in pygame.event.get():

        # Exit the loop on Quit
        if event.type == QUIT:
            game_running = False
            program_running = False
        # Listen for the mouse button to be clicked and un when clicked
        elif event.type == MOUSEBUTTONDOWN:
            #Get the (x,y) coordinate where the mouse was clicked on the screen
            coordinates = pygame.mouse.get_pos()
            x = coordinates[0]
            y = coordinates[1]

            # Find the background tile at the loctation where the mouse was clicked and change the value of effect to true

            tile_y = y // 100
            tile_x = x // 100


            try :
                trap_applicator.select_tile(tile_grid[tile_y][tile_x], counters)
            except :
                trapchange(CURRENT_ROW)
                trap_applicator.select_tile(tile_grid[tile_y][tile_x], counters)
        elif event.type == KEYDOWN :
            if event.key == K_1 :
                try:
                    trap_applicator.select_tile(tile_grid[5][2], counters)
                except:
                    trapchange(CURRENT_ROW)
                    trap_applicator.select_tile(tile_grid[5][2], counters)
            elif event.key == K_2 :
                try:
                    trap_applicator.select_tile(tile_grid[5][3], counters)
                except:
                    trapchange(CURRENT_ROW)
                    trap_applicator.select_tile(tile_grid[5][3], counters)
            elif event.key == K_3 :
                try:
                    trap_applicator.select_tile(tile_grid[5][4], counters)
                except:
                    trapchange(CURRENT_ROW)
                    trap_applicator.select_tile(tile_grid[5][4], counters)
            elif event.key == K_4 :
                try:
                    trap_applicator.select_tile(tile_grid[5][5], counters)
                except:
                    trapchange(CURRENT_ROW)
                    trap_applicator.select_tile(tile_grid[5][5], counters)
            elif event.key == K_5 :
                try:
                    trap_applicator.select_tile(tile_grid[5][6], counters)
                except:
                    trapchange(CURRENT_ROW)
                    trap_applicator.select_tile(tile_grid[5][6], counters)


    #Spawn Vampire Pizza Sprites
    if randint(1,SPAWN_RATE) == 1:
        choice(enemy_types)()

        for tile_row in tile_grid:
            for tile in tile_row:
                if bool(tile.trap):
                    GAME_WINDOW.blit(BACKGROUND, (tile.rect.x, tile.rect.y), tile.rect)
#------------------------------------------
    #Set up Collision detection

    #list all_vampires
    for vampire in all_vampires:
        #store the row where the vampire sprtie is located
        tile_row = tile_grid[vampire.rect.y // 100]
        # Store the current location of the left edge of the vampire sprite
        vamp_left_side = vampire.rect.x // 100
        # Store the current location of the right edge of the vampire sprite
        vamp_right_side = (vampire.rect.x + vampire.rect.width) // 100
        #if the vampire sprite is on the grid, find which column it is in
        if 0 <= vamp_left_side <= 10 :
            left_tile = tile_row[vamp_left_side]
        #Return no column if the vampire is not on the grid
        else:
            left_tile = None

        #checking if right side of vampire is on grid
        if 0 <= vamp_right_side <= 10 :
            right_tile = tile_row[vamp_right_side]
        else:
            right_tile = None

        # Test if the left side of the vampire pizza is touching a tile and if that tile has been clicked
        #if true, change the vampitre speed to 1
        if bool(left_tile) :
            vampire.attack(left_tile)

        if bool(right_tile) :
            if right_tile != left_tile :
                vampire.attack(right_tile)


    #Set win/lose conditions
    if counters.bad_reviews >= MAX_BAD_REVIEWS:
        game_running = False
    if counters.loop_count > WIN_TIME:
        game_running = False

    # Update the Displays
    for vampire in all_vampires:
        #Add a new argument to the update method for our vampire sprites
        vampire.update(GAME_WINDOW, counters)

    for tile_row in tile_grid:
        for tile in tile_row:
            tile.draw_trap(GAME_WINDOW, trap_applicator)
    for anchovy in all_anchovies:
        anchovy.update(GAME_WINDOW)
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
    if counters.bad_reviews >= MAX_BAD_REVIEWS:
        end_surf = end_font.render('Game Over', True, WHITE)
    else:
        end_surf = end_font.render('You Win!', True, WHITE)
    GAME_WINDOW.blit(end_surf, (350, 200))
    display.update()

#Enable exit from end game message screen
while program_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            program_running = False
        elif event.type == MOUSEBUTTONDOWN:
            print('orb')
    clock.tick(FRAME_RATE)
# clean up
pygame.quit()

