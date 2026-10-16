import pygame
import os
import random
import tile_map
#game variables
TILE_SIZE = 32
ROW_COUNT = 16
COLUMN_COUNT = ROW_COUNT
GAME_WIDTH = TILE_SIZE * COLUMN_COUNT
GAME_HEIGHT = TILE_SIZE * ROW_COUNT
GAME_MAP = tile_map.OPTIMIZED_GAME_MAP1

PLAYER_X = GAME_WIDTH / 2
PLAYER_Y = GAME_HEIGHT / 2
HEALTH_WIDTH = 16
HEALTH_HEIGHT = 4
METALL_WIDTH = 36
METALL_HEIGHT = 30

PLAYER_BULLET_WIDTH = 16
PLAYER_BULLET_HEIGHT = 12
PLAYER_BULLET_VELOCITY_X = 8
METALL_BULLET_WIDTH = 12
METALL_BULLET_HEIGHT = METALL_BULLET_WIDTH
METALL_BULLET_VELOCITY_X = 2
METALL_BULLET_VELOCITY_Y = METALL_BULLET_VELOCITY_X
LIFE_ENERGY_WIDTH = 20
LIFE_ENERGY_HEIGHT = 24
BIG_LIFE_ENERGY_WIDTH = 28
BIG_LIFE_ENERGY_HEIGHT = 32
ITEM_VELOCITY_Y = -11
PLAYER_WIDTH = 42
PLAYER_HEIGHT = 48
PLAYER_SHOOT_WIDTH = 62
PLAYER_JUMP_SHOOT_WIDTH = 58
PLAYER_JUMP_WIDTH = 52
PLAYER_JUMP_HEIGHT = 60
PLAYER_DISTANCE = 5
GRAVITY = 0.5
FRICTION = 0.4
PLAYER_VELOCITY_Y= -11
PLAYER_VELOCITY_X = 5
BLADER_WIDTH = 32
BLADER_HEIGHT = 40
BLADER_VELOCITY_X = 4
BLADER_VELOCITY_Y = 2
PLAYER_WALK_WIDTH = 48
PLAYER_WALK_HEIGHT = 48
PLAYER_WALK_SHOOT_WIDTH  = 62

#images

def load_image(image_name, scale = None):
    image = pygame.image.load(os.path.join("images", image_name))
    if scale is not None:
        image = pygame.transform.scale(image, scale)
    return image

background_image = load_image("background.png")
player_image_right = load_image("megaman-right.png", (PLAYER_WIDTH, PLAYER_HEIGHT))
player_image_left = load_image("megaman-left.png", (PLAYER_WIDTH, PLAYER_HEIGHT))
player_image_shoot_right = load_image("megaman-right-shoot.png", (PLAYER_SHOOT_WIDTH, PLAYER_HEIGHT))
player_image_shoot_left = load_image("megaman-left-shoot.png", (PLAYER_SHOOT_WIDTH, PLAYER_HEIGHT))
player_image_jump_right = load_image("megaman-right-jump.png", (PLAYER_JUMP_WIDTH, PLAYER_JUMP_HEIGHT))
player_image_jump_shoot_right = load_image("megaman-right-jump-shoot.png", (PLAYER_JUMP_SHOOT_WIDTH, PLAYER_JUMP_HEIGHT))
player_image_jump_shoot_left = load_image("megaman-left-jump-shoot.png", (PLAYER_JUMP_SHOOT_WIDTH, PLAYER_JUMP_HEIGHT))
player_image_jump_left = load_image("megaman-left-jump.png", (PLAYER_JUMP_WIDTH, PLAYER_JUMP_HEIGHT))
floor_tile_image = load_image("floor-tile.png", (TILE_SIZE, TILE_SIZE))
player_image_bullet = load_image("bullet.png", (PLAYER_BULLET_WIDTH, PLAYER_BULLET_HEIGHT))
metall_image_guard_right = load_image("metall-right-guard.png", (METALL_WIDTH, METALL_HEIGHT))
metall_image_guard_left = load_image("metall-left-guard.png", (METALL_WIDTH, METALL_HEIGHT))
metall_image_left = load_image("metall-left.png", (METALL_WIDTH, METALL_HEIGHT))
metall_image_right = load_image("metall-right.png", (METALL_WIDTH, METALL_HEIGHT))
metall_image_bullet = load_image("metall-bullet.png", (METALL_BULLET_WIDTH, METALL_BULLET_HEIGHT))
health_image = load_image("health.png", (HEALTH_WIDTH, HEALTH_HEIGHT))
life_energy_image = load_image("life-energy.png", (LIFE_ENERGY_WIDTH, LIFE_ENERGY_HEIGHT))
big_life_energy_image = load_image("big-life-energy.png", (BIG_LIFE_ENERGY_WIDTH, BIG_LIFE_ENERGY_HEIGHT))
blader_image_left = load_image("blader-left.png", (BLADER_WIDTH, BLADER_HEIGHT))
blader_image_right = load_image("blader-right.png", (BLADER_WIDTH, BLADER_HEIGHT))
spike_image = load_image("spike.png", (TILE_SIZE, TILE_SIZE))
wall_tile_image = load_image("wall-tile.png", (TILE_SIZE, TILE_SIZE))
beam_tile_image = load_image("beam-tile.png", (TILE_SIZE, TILE_SIZE))
rock_tile1_image = load_image("rock-tile1.png", (TILE_SIZE, TILE_SIZE))
rock_tile2_image = load_image("rock-tile2.png", (TILE_SIZE, TILE_SIZE))
rock_tile3_image = load_image("rock-tile3.png", (TILE_SIZE, TILE_SIZE))
rock_tile4_image = load_image("rock-tile4.png", (TILE_SIZE, TILE_SIZE))
door_tile_image = load_image("door-tile.png", (TILE_SIZE, TILE_SIZE))
room_tile_image = load_image("room-tile.png", (TILE_SIZE, TILE_SIZE))
score_ball_image = load_image("score-ball.png", (TILE_SIZE/2, TILE_SIZE/2))

player_image_walk_right = [load_image(f"megaman-right-walk{i}.png", (PLAYER_WALK_WIDTH, PLAYER_WALK_HEIGHT)) for i in range(4)]
player_image_walk_left = [load_image(f"megaman-left-walk{i}.png", (PLAYER_WALK_WIDTH, PLAYER_WALK_HEIGHT)) for i in range(4)]
player_image_walk_shoot_right = [load_image(f"megaman-right-walk-shoot{i}.png", (PLAYER_WALK_SHOOT_WIDTH, PLAYER_WALK_HEIGHT)) for i in range(4)]
player_image_walk_shoot_left = [load_image(f"megaman-left-walk-shoot{i}.png", (PLAYER_WALK_SHOOT_WIDTH, PLAYER_WALK_HEIGHT)) for i in range(4)]

pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Pygame Window Example")
pygame.display.set_icon(player_image_right)
clock = pygame.time.Clock()
pygame.font.init()
game_font = pygame.font.Font("./megaman-game-font.otf", 24)
menu_font = pygame.font.Font("./megaman-game-font.otf", 20)
game_over = False

INVENCIBLE_END = pygame.USEREVENT + 0
SHOOTING_END = pygame.USEREVENT + 1


class Player(pygame.Rect):
    class Bullet(pygame.Rect):
        def __init__(self):
            if player.direction == "left":
                pygame.Rect.__init__(self, player.x , player.y + TILE_SIZE/2 , PLAYER_BULLET_WIDTH, PLAYER_BULLET_HEIGHT)
                self.velocity_x = -PLAYER_BULLET_VELOCITY_X * 2
            elif player.direction == "right":
                pygame.Rect.__init__(self, player.x + player.width, player.y + TILE_SIZE/2 , PLAYER_BULLET_WIDTH, PLAYER_BULLET_HEIGHT)
                self.velocity_x = PLAYER_BULLET_VELOCITY_X * 2
            self.image = player_image_bullet
            self.used = False
    def __init__(self):
        pygame.Rect.__init__(self, PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.image = player_image_right
        self.velocity_y = 0
        self.velocity_x = 0
        self.direction = "right"
        self.jumping = False
        self.invencible = False
        self.max_health = 28
        self.health = self.max_health
        self.shooting = False
        self.bullets = []
        self.score = 0
        self.walking = False
        self.cuurent_walk_index = 0
        self.last_update_walk_index = pygame.time.get_ticks() 
        
    def update_image(self):
        if self.walking and not self.jumping:
            if self.shooting:
                if self.direction == "right":
                    self.image = player_image_walk_shoot_right[self.cuurent_walk_index]
                elif self.direction == "left":
                    self.image = player_image_walk_shoot_left[self.cuurent_walk_index]
            else:
                if self.direction == "right":
                    self.image = player_image_walk_right[self.cuurent_walk_index]
                elif self.direction == "left":
                    self.image = player_image_walk_left[self.cuurent_walk_index]
            self.update_walk_animation()

        else:
            self.current_walk_index = 0
            
            if self.jumping and self.shooting:
                             
                        if self.direction == "right":
                            self.image = player_image_jump_shoot_right
                        elif self.direction == "left":
                            self.image = player_image_jump_shoot_left
                    
            elif self.shooting:
                        if self.direction == "right":
                            self.image = player_image_shoot_right
                        elif self.direction == "left":
                            self.image = player_image_shoot_left
            elif self.jumping:
                     
                        if self.direction == "right":
                            self.image = player_image_jump_right
                        elif self.direction == "left":
                            self.image = player_image_jump_left
            else:
                     
                
                        if self.direction == "right":
                          self.image = player_image_right
                        elif self.direction == "left":
                          self.image = player_image_left
        
              
    def update_walk_animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update_walk_index >= 250:
            self.last_update_walk_index = now
            self.cuurent_walk_index = (self.cuurent_walk_index + 1) % len(player_image_walk_right)
              
    def set_invencible(self, milliseconds=1000):
        self.invencible = True
        pygame.time.set_timer(INVENCIBLE_END, milliseconds, 1)
        
    def set_shooting(self):
        if not self.shooting:
         self.shooting = True
         self.bullets.append(Player.Bullet())
         pygame.time.set_timer(SHOOTING_END, 250, 1)
class Tile(pygame.Rect):
    def __init__(self, x, y, image):
        pygame.Rect.__init__(self, x, y, TILE_SIZE, TILE_SIZE)
        self.image = image
        
class Item(pygame.Rect):
    def __init__(self, x, y, image):
        pygame.Rect.__init__(self, x, y, image.get_width(), image.get_height())
        self.image = image  
        self.jumping = False     
        self.velocity_y = ITEM_VELOCITY_Y
        self.used = False
    

        
class Metall(pygame.Rect):
    class Bullet(pygame.Rect):
        def __init__(self, metall, velocity_y):
            if metall.direction == "left":
                pygame.Rect.__init__(self, metall.x , metall.y + TILE_SIZE/2 , METALL_BULLET_WIDTH, METALL_BULLET_HEIGHT)
                self.velocity_x = -METALL_BULLET_VELOCITY_X
            elif metall.direction == "right":
                pygame.Rect.__init__(self, metall.x + metall.width , metall.y + TILE_SIZE/2 , METALL_BULLET_WIDTH, METALL_BULLET_HEIGHT)
                self.velocity_x = METALL_BULLET_VELOCITY_X
            self.velocity_y = velocity_y
            self.image = metall_image_bullet
            self.used = False

    def __init__(self, x, y):
        pygame.Rect.__init__(self, x, y, METALL_WIDTH, METALL_HEIGHT)
        self.image = metall_image_left
        self.velocity_y = 0
        self.direction = "left"
        self.jumping = False 
        self.health = 1
        self.bullets = []
        self.last_fired = pygame.time.get_ticks()
        self.guarding = False
    def update_image(self):
        if self.direction == "left":
            if self.guarding:
                self.image = metall_image_guard_left
            else:
             self.image = metall_image_left
        elif self.direction == "right":
            if self.guarding:
                self.image = metall_image_guard_right
            else:
                self.image = metall_image_right
    def set_shooting(self):
        if abs(self.x - player.x) <= TILE_SIZE * 4:
         self.guarding = False
         now = pygame.time.get_ticks()
         if now - self.last_fired >= 1000 :
          self.last_fired = now
          self.bullets.append(Metall.Bullet(self, -METALL_BULLET_VELOCITY_Y))
          self.bullets.append(Metall.Bullet(self, 0))
          self.bullets.append(Metall.Bullet(self, METALL_BULLET_VELOCITY_Y))
        else:
            self.guarding = True
            
class Blader(pygame.Rect):
    def __init__(self, x, y):
        pygame.Rect.__init__(self, x, y, BLADER_WIDTH, BLADER_HEIGHT)
        self.image = blader_image_right
        self.direction = "right"
        self.health = 3
        self.velocity_x = BLADER_VELOCITY_X
        self.velocity_y = BLADER_VELOCITY_Y
        self.start_x = x
        self.start_y = y
        self.max_range_x = TILE_SIZE * 4
        self.max_range_y = TILE_SIZE
        
    def update_image(self):
        if self.direction == "left":
            self.image = blader_image_left
        elif self.direction == "right":
            self.image = blader_image_right 
def append_tiles(map_code, tile):
    if map_code < 0:
        background_tiles.append(tile)
    else:
        tiles.append(tile)
def create_map():
    for column in range(len(GAME_MAP[0])):
        for row in range(len(GAME_MAP)):
            map_code = GAME_MAP[row][column]
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            if map_code == 0:
                continue
            elif abs(map_code) == 1:
                append_tiles(map_code, Tile(x, y, rock_tile1_image))
            elif abs(map_code) == 2:
                append_tiles(map_code, Tile(x, y, rock_tile2_image))
            elif abs(map_code) == 3:
                append_tiles(map_code, Tile(x, y, rock_tile3_image))
            elif abs(map_code) == 4:
                append_tiles(map_code, Tile(x, y, rock_tile4_image))
            elif abs(map_code) == 5:
                append_tiles(map_code, Tile(x, y, floor_tile_image))
            elif abs(map_code) == 6:
                append_tiles(map_code, Tile(x, y, wall_tile_image))
            elif map_code == 7:
                background_tiles.append(Tile(x, y, beam_tile_image))
            elif map_code == 8:
                spikes.append(Tile(x, y, spike_image))
            elif map_code == 9:
                background_tiles.append(Tile(x, y, door_tile_image))
            elif map_code == 10:
                background_tiles.append(Tile(x, y, room_tile_image))
            elif map_code == 11:
                metalls.append(Metall(x, y))
            elif map_code == 12:
                bladers.append(Blader(x, y))

def reset_game():
    global metalls, tiles, items, metall_bullets, spikes, bladers, background_tiles, player, game_over
    player  = Player()
    metalls = []
    tiles = []
    items = []
    metall_bullets = []
    spikes = []
    bladers = []
    background_tiles = []
    game_over = False
    create_map()
    
             

    

        
def check_tile_collision(character):
    for tile in tiles:
        if character.colliderect(tile):
            return tile
        elif tile.x - character.x > GAME_WIDTH:
            return None
    return None

def check_tile_collision_x(character):
    tile = check_tile_collision(character)
    if tile is not None:
        if character.velocity_x < 0:
            character.x = tile.width + tile.x
        elif character.velocity_x > 0:
            character.x = tile.x - character.width
        character.velocity_x = 0
        
        
def check_tile_collision_y(character):
    tile = check_tile_collision(character)
    if tile is not None:
        if character.velocity_y < 0:
            character.y = tile.y + tile.height
        elif character.velocity_y > 0:
            character.y = tile.y  - character.height
            character.jumping = False
        character.velocity_y = 0
        
def drop_item(character):
    random_number = random.randint(1, 100)
    if 0 < random_number <=20:
        items.append(Item(character.x, character.y, big_life_energy_image))
    elif 20 < random_number <= 50:
        items.append(Item(character.x, character.y, life_energy_image))
    elif 50 < random_number <= 75:
        items.append(Item(character.x, character.y, score_ball_image))


def move_player_x(velocity_x):
    move_map_x(velocity_x)
    tile = check_tile_collision(player)
    if tile is not None:
        move_map_x(-velocity_x)
    
def move_map_x(velocity_x):
    for tile in tiles:
        tile.x += velocity_x
    for tile in background_tiles:
        tile.x += velocity_x
    for spike in spikes:
        spike.x += velocity_x
    for item in items:
        item.x += velocity_x
    for blader in bladers:
        blader.start_x += velocity_x
        blader.x += velocity_x
    for metall in metalls:
        metall.x += velocity_x
        for bullet in metall.bullets:
            bullet.x += velocity_x
    for bullet in metall_bullets:
        bullet.x += velocity_x

def move():
    global metalls
    global items
    global bladers
    global metall_bullets
    global game_over
    #if player.direction == "left" and player.velocity_x < 0:
       # player.velocity_x += FRICTION
   # elif player.direction == "right" and player.velocity_x > 0:
   #     player.velocity_x -= FRICTION   
   # else:
   #     player.velocity_x = 0
    
   # player.x +=player.velocity_x
   # if player.x < 0:
   #     player.x = 0
   # elif player.x + player.width > GAME_WIDTH:
    #    player.x = GAME_WIDTH - player.width    
        
   # check_tile_collision_x(player)
    
    player.velocity_y += GRAVITY
    player.y += player.velocity_y
    
    check_tile_collision_y(player)
    
    for spike in spikes:
        if player.colliderect(spike) and not player.invencible:
            player.health = 0
    
    for bullet in player.bullets:
        bullet.x += bullet.velocity_x
        for metall in metalls:
            if metall.health > 0 and not bullet.used and bullet.colliderect(metall):
                bullet.used = True
                if not metall.guarding:
                    metall.health -= 1
                    if metall.health <= 0:
                        drop_item(metall)
                        metall_bullets.extend(metall.bullets)
                        player.score += 500
                        
        for blader in bladers:
         if blader.health > 0 and not bullet.used and bullet.colliderect(blader):
            bullet.used = True
            blader.health -= 1
            if blader.health <= 0:
                drop_item(blader)
                player.score += 500
    player.bullets = [bullet for bullet in player.bullets if not bullet.used and bullet.x + bullet.width > 0 and bullet.x < GAME_WIDTH]  
    metalls = [metall for metall in metalls if metall.health > 0]          
    bladers = [blader for blader in bladers if blader.health > 0]
    
    for metall in metalls:
        if player.x < metall.x:
            metall.direction = "left"
        else:
            metall.direction = "right"
        metall.velocity_y += GRAVITY
        metall.y += metall.velocity_y 
        check_tile_collision_y(metall)
    
        if not player.invencible and player.colliderect(metall):
          print("Player collided with Metall!")
          player.health -= 1
          player.set_invencible()
          
        metall.set_shooting()
        for bullet in metall.bullets:
            bullet.x += bullet.velocity_x
            bullet.y += bullet.velocity_y
            if not player.invencible and bullet.colliderect(player):
                player.health -= 1
                bullet.used = True
                player.set_invencible()
        metall.bullets = [bullet for bullet in metall.bullets if not bullet.used and bullet.x + bullet.width > 0 and bullet.x < GAME_WIDTH ]
    for bullet in metall_bullets:
            bullet.x += bullet.velocity_x
            bullet.y += bullet.velocity_y
            if not player.invencible and bullet.colliderect(player):
                player.health -= 1
                bullet.used = True
                player.set_invencible()
    metall_bullets = [bullet for bullet in metall_bullets if not bullet.used and bullet.x + bullet.width > 0 and bullet.x < GAME_WIDTH ]    
    for item in items:
        item.velocity_y += GRAVITY
        item.y  += item.velocity_y 
        check_tile_collision_y(item)
        if player.colliderect(item) and not item.used:
            item.used = True
            if item.image == life_energy_image:
                player.health = min(player.health + 2, player.max_health)
            elif item.image == big_life_energy_image:
                player.health = min(player.health + 8, player.max_health)
            elif item.image == score_ball_image:
                player.score += 1000
    items = [item for item in items if not item.used ]
    
    for blader in bladers:
       if abs(blader.x + blader.velocity_x - blader.start_x) >= blader.max_range_x:
           blader.velocity_x *= -1
           if blader.velocity_x < 0:
                blader.direction = "left"
           elif blader.velocity_x > 0:
                blader.direction = "right"
       else:
              blader.x += blader.velocity_x
       if abs(blader.y + blader.velocity_y - blader.start_y) >= blader.max_range_y:
           blader.velocity_y *= -1
       else:
              blader.y += blader.velocity_y
       if not player.invencible and player.colliderect(blader):

          player.health -= 1
          player.set_invencible()
    
    if player.health <= 0 or player.y > GAME_HEIGHT:
       game_over = True
   
        
            
    
    
    
def draw():
    #window.fill("blue")
    window.fill((20, 18, 167))
    window.blit(background_image, (0,80))
    player.update_image()
    window.blit(player.image, player)
    for tile in background_tiles:
        if tile.x > GAME_WIDTH:
            break
        window.blit(tile.image, tile)
    for bullet in player.bullets:
        window.blit(bullet.image, bullet)
    for metall in metalls:
        if metall.x <= GAME_WIDTH:
         metall.update_image()
         window.blit(metall.image, metall)
        for bullet in metall.bullets:
            window.blit(bullet.image, bullet)
    for bullet in metall_bullets:
        window.blit(bullet.image, bullet)
    for tile in tiles:
        if tile.x > GAME_WIDTH:
            break
        window.blit(tile.image, tile)
    for spike in spikes:
        if spike.x > GAME_WIDTH:
            break
        window.blit(spike.image, spike)
    for item in items:
        if item.x > GAME_WIDTH:
            break
        window.blit(item.image, item)
    for blader in bladers:
        if blader.x > GAME_WIDTH:
            break
        blader.update_image()
        window.blit(blader.image, blader)
  #  pygame.draw.rect(window, "red", (TILE_SIZE, TILE_SIZE, 10 * player.max_health, 10))
   # pygame.draw.rect(window, "green", (TILE_SIZE, TILE_SIZE, 10 * player.health, 10))
    pygame.draw.rect(window, "black", (TILE_SIZE, TILE_SIZE, HEALTH_WIDTH, HEALTH_HEIGHT * player.max_health))
    for i in range(player.max_health - player.health, player.max_health):
       window.blit(health_image, (TILE_SIZE, TILE_SIZE + i * HEALTH_HEIGHT, HEALTH_WIDTH, HEALTH_HEIGHT))
       
    text_score = str(player.score)
    while(text_score.__len__() < 7):
        text_score = "0" + text_score
    text_surface = game_font.render(text_score, False, "white")
    window.blit(text_surface, (GAME_WIDTH/2, TILE_SIZE/2))
    
    if game_over:
        text_surface = game_font.render("GAME OVER", False, "red")
        window.blit(text_surface, (GAME_WIDTH/8, GAME_HEIGHT/2))
        text_surface = game_font.render("[ENTER] para reiniciar", False, "white")
        window.blit(text_surface, (GAME_WIDTH/8, GAME_HEIGHT/2 + TILE_SIZE))


def start_screen():
    menu_image = load_image("OIP (5).webp")
    menu_image = pygame.transform.scale(menu_image, (GAME_WIDTH, GAME_HEIGHT))
    options = ("COMECAR", "SAIR")
    selected_option = 0
    option_rects = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w, pygame.K_DOWN, pygame.K_s):
                    selected_option = 1 - selected_option
                elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE):
                    return selected_option == 0
                elif event.key == pygame.K_ESCAPE:
                    return False
            if event.type == pygame.MOUSEMOTION:
                for index, option_rect in enumerate(option_rects):
                    if option_rect.collidepoint(event.pos):
                        selected_option = index
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for index, option_rect in enumerate(option_rects):
                    if option_rect.collidepoint(event.pos):
                        return index == 0

        window.blit(menu_image, (0, 0))

        overlay = pygame.Surface((GAME_WIDTH, GAME_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 100))
        window.blit(overlay, (0, 0))



        option_rects = []
        for index, option in enumerate(options):
            option_surface = menu_font.render(
                option,
                False,
                "yellow" if index == selected_option else "white",
            )
            option_rect = option_surface.get_rect(
                center=(GAME_WIDTH // 2, GAME_HEIGHT // 2 + index * TILE_SIZE * 2)
            )
            option_rects.append(option_rect)
            window.blit(option_surface, option_rect)

        pygame.display.update()
        clock.tick(60)


player  = Player()
#metall = Metall(player.x + TILE_SIZE*3, TILE_SIZE*6)
metalls = []
tiles = []
items = []
metall_bullets = []
spikes = []
bladers = []
background_tiles = []
create_map()

if not start_screen():
    pygame.quit()
    exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == INVENCIBLE_END:
            player.invencible = False
        elif event.type == SHOOTING_END:
            player.shooting = False
  
    """
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP , pygame.K_w) :
                player.y -=5
            if event.key in (pygame.K_DOWN , pygame.K_s) :
                player.y +=5
            if event.key in (pygame.K_LEFT , pygame.K_a) :
                player.x -=5
            if event.key in (pygame.K_RIGHT , pygame.K_d) :
                player.x +=5
"""

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]) and game_over:
        reset_game()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and not player.jumping:
        ##player.y -=PLAYER_DISTANCE
        ##if player.y < 0:
        ## player.y = 0
        ## player.y = max(player.y - PLAYER_DISTANCE,0)
        player.velocity_y = PLAYER_VELOCITY_Y
        player.jumping = True
        
    if keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.walking = True
    else:
        player.walking = False

    ##if keys[pygame.K_DOWN] or keys[pygame.K_s]:
       ## player.y = min(player.y + PLAYER_DISTANCE, GAME_HEIGHT - player.height)
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        ##player.x = max(player.x - PLAYER_DISTANCE, 0)
       # player.velocity_x  = -PLAYER_VELOCITY_X
        move_player_x(PLAYER_VELOCITY_X)
        player.direction = "left"
        
        
        
        
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        ##player.x = min(player.x + PLAYER_DISTANCE, GAME_WIDTH - player.width)
      #  player.velocity_x  = PLAYER_VELOCITY_X
        move_player_x(-PLAYER_VELOCITY_X)
        player.direction = "right"
        
    if keys[pygame.K_x] or keys[pygame.K_SPACE]:
        player.set_shooting()
    
    if not game_over:  
     move()
     draw()
     pygame.display.update()
     clock.tick(60)