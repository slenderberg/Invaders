import pygame
from sys import exit
import random
import math


class Levels:
    LEVEL1 = 0
    LEVEL2 = 50
    LEVEL3 = 125
    LEVEL4 = 250
    LEVEL5 = 400
    LEVEL6 = 600
    LEVEL7 = 850


class Colors:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    GREY = (128, 128, 128)


class ButtonOrText:

    def __init__(self, font, text, antialias, color, bgcolor, x, y):
        self.font = font
        self.text = text
        self.antialias = antialias
        self.color = color
        self.bgcolor = bgcolor
        self.x = x
        self.y = y
        self.img = font.render(self.text, self.antialias, self.color, self.bgcolor)
        self.rect = self.img.get_rect(center=(self.x, self.y))


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        spaceship1 = pygame.image.load('spaceships\\spaceship1.png').convert_alpha()
        spaceship2 = pygame.image.load('spaceships\\spaceship2.png').convert_alpha()
        spaceship3 = pygame.image.load('spaceships\\spaceship3.png').convert_alpha()
        spaceship4 = pygame.image.load('spaceships\\spaceship4.png').convert_alpha()
        spaceship5 = pygame.image.load('spaceships\\spaceship5.png').convert_alpha()
        spaceship6 = pygame.image.load('spaceships\\spaceship6.png').convert_alpha()
        self.list = [spaceship1, spaceship2, spaceship3, spaceship4, spaceship5, spaceship6]
        self.surf = self.list[0]
        self.x = 500
        self.y = 500
        self.rect = self.surf.get_rect(center=(self.x, self.y))

    def move(self):
        mouse_x_pos, mouse_y_pos = pygame.mouse.get_pos()
        self.rect.center = (mouse_x_pos, mouse_y_pos)

    def create_bullet(self, num):
        if num == 1:
            bullet1 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 0)
            return bullet1
        elif num == 2:
            bullet1 = Bullet(pygame.mouse.get_pos()[0] - 24, pygame.mouse.get_pos()[1], 0)
            bullet2 = Bullet(pygame.mouse.get_pos()[0] + 24, pygame.mouse.get_pos()[1], 0)
            return bullet1, bullet2
        elif num == 3:
            bullet1 = Bullet(pygame.mouse.get_pos()[0] - 24, pygame.mouse.get_pos()[1], 0)
            bullet2 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 0)
            bullet3 = Bullet(pygame.mouse.get_pos()[0] + 24, pygame.mouse.get_pos()[1], 0)
            return bullet1, bullet2, bullet3
        elif num == 4:
            bullet1 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1)
            bullet2 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], -1)
            bullet3 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], -2)
            bullet4 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 2)
            return bullet1, bullet2, bullet3, bullet4
        elif num == 5:
            bullet1 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], -2)
            bullet2 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], -1)
            bullet3 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 0)
            bullet4 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1)
            bullet5 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 2)
            return bullet1, bullet2, bullet3, bullet4, bullet5
        elif num == 6:
            bullet1 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], -3)
            bullet2 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], -2)
            bullet3 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], -1)
            bullet4 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1)
            bullet5 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 2)
            bullet6 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 3)
            return bullet1, bullet2, bullet3, bullet4, bullet5, bullet6
        elif num == 7:
            bullet1 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], -3)
            bullet2 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], -2)
            bullet3 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], -1)
            bullet4 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 0)
            bullet5 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1)
            bullet6 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 2)
            bullet7 = Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 3)
            return bullet1, bullet2, bullet3, bullet4, bullet5, bullet6, bullet7

    def change_player(self, score):

        if score >= Levels.LEVEL1:
            self.surf = self.list[0]
        if score >= Levels.LEVEL2:
            self.surf = self.list[1]
        if score >= Levels.LEVEL3:
            self.surf = self.list[2]
        if score >= Levels.LEVEL4:
            self.surf = self.list[3]
        if score >= Levels.LEVEL5:
            self.surf = self.list[4]
        if score >= Levels.LEVEL6:
            self.surf = self.list[5]


class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y, x_speed):
        super().__init__()
        self.image = pygame.transform.rotate(pygame.image.load('bullets\\flame.png').convert_alpha(), 180)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.speed_x = x_speed
        self.speed_y = 10

    def update(self):
        self.rect.y -= self.speed_y
        self.rect.x -= self.speed_x
        if self.rect.y <= -20:
            self.kill()


class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__()
        enemy1 = pygame.image.load('enemies\\enemy1.png').convert_alpha()
        enemy2 = pygame.image.load('enemies\\enemy2.png').convert_alpha()
        enemy3 = pygame.image.load('enemies\\enemy3.png').convert_alpha()
        enemy4 = pygame.image.load('enemies\\enemy4.png').convert_alpha()
        enemy5 = pygame.image.load('enemies\\enemy5.png').convert_alpha()
        enemy6 = pygame.image.load('enemies\\enemy6.png').convert_alpha()
        self.list = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6]
        self.image = self.list[0]
        self.speed = 1.5
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def update(self):
        self.rect.y += self.speed


pygame.init()
clock = pygame.time.Clock()

screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Invaders")
pygame.display.set_icon(pygame.image.load('spaceships\\spaceship1.png'))

background = pygame.image.load('background.png').convert_alpha()

font1 = pygame.font.Font('fonts\\PaladinsCondensed-rB77.otf', 50)
font2 = pygame.font.Font('fonts\\PaladinsStraight-2a7v.otf', 80)
font3 = pygame.font.Font('fonts\\PaladinsGradient-R6VW.otf', 50)
font4 = pygame.font.Font('fonts\\PaladinsCondensed-rB77.otf', 100)

# -----------------------------------------------------------------------
# music

menu_music = pygame.mixer.Sound('music\\spacemusic.mp3')
menu_music.set_volume(0.1)
play_music = pygame.mixer.Sound('music\\spacemusic1.mp3')
play_music.set_volume(0.5)

# -----------------------------------------------------------------------
# playing game

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

game_score = 0
enemy_escape_life = 5
someNum = 0
# --------------------------------------------------------------------------
# menu screen

play_button = ButtonOrText(font4, "PLAY", True, Colors.YELLOW, None, 500, 270)
quit_button = ButtonOrText(font4, "QUIT", True, Colors.YELLOW, None, 500, 370)

game_name_logo = pygame.image.load('misc\\game name.png').convert_alpha()
game_name_rect = game_name_logo.get_rect(topleft=(175, 50))

# --------------------------------------------------------------------------
# game over

game_over_logo = pygame.image.load('misc\\game over.png').convert_alpha()
game_over_rect = game_over_logo.get_rect(topleft=(150, 30))

play_again_logo = pygame.image.load('misc\\play again.png').convert_alpha()
play_again_rect = play_again_logo.get_rect(topleft=(320, 300))

main_menu_logo = pygame.image.load('misc\\main menu.png').convert_alpha()
main_menu_rect = main_menu_logo.get_rect(topleft=(300, 400))

quit_logo = pygame.image.load('misc\\quit.png').convert_alpha()
quit_rect = quit_logo.get_rect(topleft=(420, 500))

# --------------------------------------------------------------------------

INCREASE_LIFE = pygame.USEREVENT + 1
pygame.time.set_timer(INCREASE_LIFE, 20000)


def spawn_enemy():
    global someNum, enemy_per_wave, level
    if game_score >= Levels.LEVEL1:
        enemy_per_wave = 10
        level = 1
    if game_score >= Levels.LEVEL2:
        enemy_per_wave = 15
        level = 2
    if game_score >= Levels.LEVEL3:
        enemy_per_wave = 20
        level = 3
    if game_score >= Levels.LEVEL4:
        enemy_per_wave = 25
        level = 4
    if game_score >= Levels.LEVEL5:
        enemy_per_wave = 30
        level = 5
    if game_score >= Levels.LEVEL6:
        enemy_per_wave = 35
        level = 6
    if game_score >= Levels.LEVEL7:
        enemy_per_wave = 40
        level = 7

    if someNum <= enemy_per_wave:
        enemy_x = random.randint(32, 968)
        enemy_y = random.randint(-500, -100)
        enemy_group.add(Enemy(enemy_x, enemy_y))

    if len(enemy_group) == 0:
        someNum = 0


def detect_collisions(bullets, enemies):
    global game_score
    for bullet in bullets:
        for enemy in enemies:
            distance = math.sqrt((math.pow(enemy.rect.x - bullet.rect.x, 2)) +
                                 (math.pow(bullet.rect.y - enemy.rect.y, 2)))
            if distance <= 50:
                enemy.kill()
                bullet.kill()
                game_score += 1


def check_enemy_escapes(enemies):
    for enemy in enemies:
        if enemy.rect.y >= 600:
            enemies.remove(enemy)
            global enemy_escape_life
            enemy_escape_life -= 1


def change_enemy(score, enemies):

    for enemy in enemies:

        if score == 0:
            enemy.image = enemy.list[0]
        if score >= Levels.LEVEL2:
            enemy.image = enemy.list[1]
            enemy.speed = 2
        if score >= Levels.LEVEL3:
            enemy.image = enemy.list[2]
            enemy.speed = 2
        if score >= Levels.LEVEL4:
            enemy.image = enemy.list[3]
            enemy.speed = 3
        if score >= Levels.LEVEL5:
            enemy.image = enemy.list[4]
            enemy.speed = 3
        if score >= Levels.LEVEL6:
            enemy.image = enemy.list[5]
            enemy.speed = 4
        if score >= Levels.LEVEL7:
            enemy.speed = 5


level = 1

main_menu = True
game_active = False
game_over = False
game_pause = False

while True:
    pygame.mouse.set_cursor(*pygame.cursors.arrow)
    screen.fill(Colors.BLACK)
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if main_menu:
            play_music.stop()
            menu_music.play(-1)
            point = pygame.mouse.get_pos()

            play_button = ButtonOrText(font4, "PLAY", True, Colors.YELLOW, None, 500, 270)
            quit_button = ButtonOrText(font4, "QUIT", True, Colors.YELLOW, None, 500, 370)

            if play_button.rect.collidepoint(point):
                play_button = ButtonOrText(font4, "PLAY", True, Colors.YELLOW, Colors.BLACK, 500, 270)
                if pygame.mouse.get_pressed(3)[0]:
                    menu_music.stop()
                    pygame.mouse.set_pos(player.x, player.y)
                    game_active = True
                    main_menu = False
                    game_over = False

            if quit_button.rect.collidepoint(point):
                quit_button = ButtonOrText(font4, "QUIT", True, Colors.YELLOW, Colors.BLACK, 500, 370)
                if pygame.mouse.get_pressed(3)[0]:
                    pygame.quit()
                    exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        if game_over:
            play_music.stop()
            menu_music.play(-1)
            bullet_group.empty()
            enemy_escape_life = 5
            point = pygame.mouse.get_pos()

            if pygame.mouse.get_pressed(3)[0]:
                if play_again_rect.collidepoint(point):
                    level = 1
                    game_score = 0
                    player.x = 500
                    player.y = 500
                    pygame.mouse.set_pos(500, 500)
                    main_menu = False
                    game_over = False
                    game_active = True

                if main_menu_rect.collidepoint(point):
                    game_score = 0
                    game_active = False
                    game_over = False
                    main_menu = True

                if quit_rect.collidepoint(point):
                    pygame.quit()
                    exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        if game_active:
            play_music.play(-1)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_pause = True
            if event.type == pygame.MOUSEMOTION:
                player.move()

            if event.type == INCREASE_LIFE:
                enemy_escape_life += 2

            if not pygame.mouse.get_focused():
                game_active = False
                game_pause = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(3)[0]:
                    bullet_group.add(player.create_bullet(level))

        if game_pause:
            game_active = False
            game_over = False
            main_menu = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_pause = False
                    game_active = True

    if main_menu:
        screen.blit(game_name_logo, game_name_rect)
        screen.blit(play_button.img, play_button.rect)
        screen.blit(quit_button.img, quit_button.rect)

    if game_active:
        if pygame.mouse.get_pos()[0] >= screen_width - 32:
            player.rect.x = screen_width - 64
        if pygame.mouse.get_pos()[0] <= 32:
            player.rect.x = 0
        if pygame.mouse.get_pos()[1] <= 32:
            player.rect.y = 0
        if pygame.mouse.get_pos()[1] >= screen_height - 32:
            player.rect.y = screen_height - 64

        detect_collisions(bullet_group, enemy_group)
        bullet_group.draw(screen)
        bullet_group.update()
        screen.blit(player.surf, player.rect)
        spawn_enemy()
        enemy_group.draw(screen)
        check_enemy_escapes(enemy_group)

        game_score_text = ButtonOrText(font1, f"KILLS: ", True, Colors.RED, None, 150, 575)
        enemy_escape_life_text = ButtonOrText(font1, f"LIFE:{enemy_escape_life}", True, Colors.GREEN, None, 850, 575)
        game_score_text_num = font1.render(f"{game_score}", True, Colors.RED, None)
        game_score_text_num_rect = game_score_text_num.get_rect(bottomleft=(230, 600))

        screen.blit(game_score_text_num, game_score_text_num_rect)
        screen.blit(enemy_escape_life_text.img, enemy_escape_life_text.rect)
        screen.blit(game_score_text.img, game_score_text.rect)

        change_enemy(game_score, enemy_group)
        player.change_player(game_score)
        enemy_group.update()
        someNum += 1

        if pygame.sprite.groupcollide(player_group, enemy_group, False, False) or enemy_escape_life <= 0:
            enemy_group.empty()
            main_menu = False
            game_active = False
            game_over = True

    if game_pause:
        game_active = False
        game_over = False
        main_menu = False

        game_paused_text = ButtonOrText(font2, "GAME PAUSED", True, Colors.BLACK, None, 500, 100)

        resume_button = ButtonOrText(font3, "RESUME", True, Colors.BLACK, None, 500, 200)
        restart_button = ButtonOrText(font3, "RESTART", True, Colors.BLACK, None, 500, 300)
        endgame_button = ButtonOrText(font3, 'ENDGAME', True, Colors.BLACK, None, 500, 400)
        quit_button_pause = ButtonOrText(font3, 'QUIT', True, Colors.BLACK, None, 500, 500)

        point = pygame.mouse.get_pos()
        if pygame.MOUSEMOTION:

            if resume_button.rect.collidepoint(point):
                resume_button = ButtonOrText(font3, "RESUME", True, Colors.BLACK, Colors.WHITE, 500, 200)
            elif restart_button.rect.collidepoint(point):
                restart_button = ButtonOrText(font3, "RESTART", True, Colors.BLACK, Colors.WHITE, 500, 300)
            elif endgame_button.rect.collidepoint(point):
                endgame_button = ButtonOrText(font3, 'ENDGAME', True, Colors.BLACK, Colors.WHITE, 500, 400)
            elif quit_button_pause.rect.collidepoint(point):
                quit_button_pause = ButtonOrText(font3, 'QUIT', True, Colors.BLACK, Colors.WHITE, 500, 500)

        if pygame.mouse.get_pressed(3)[0]:

            if resume_button.rect.collidepoint(point):
                game_active = True
                game_pause = False
                pygame.mouse.set_pos(500, 450)

            elif restart_button.rect.collidepoint(point):
                game_active = True
                game_pause = False
                level = 1
                game_score = 0
                game_over_life = 5
                enemy_group.empty()
                pygame.mouse.set_pos(500, 450)

            elif endgame_button.rect.collidepoint(point):
                game_over = True
                game_pause = False
                game_active = False

            elif quit_button_pause.rect.collidepoint(point):
                pygame.quit()
                exit()

        screen.blit(game_paused_text.img, game_paused_text.rect)
        screen.blit(resume_button.img, resume_button.rect)
        screen.blit(restart_button.img, restart_button.rect)
        screen.blit(endgame_button.img, endgame_button.rect)
        screen.blit(quit_button_pause.img, quit_button_pause.rect)

    if game_over:
        game_over_score_text = ButtonOrText(font1, f"Final Score: {game_score}", True, Colors.GREY, None, 500, 220)

        screen.blit(game_over_logo, game_over_rect)
        screen.blit(game_over_score_text.img, game_over_score_text.rect)
        screen.blit(play_again_logo, play_again_rect)
        screen.blit(main_menu_logo, main_menu_rect)
        screen.blit(quit_logo, quit_rect)

    pygame.display.update()
    clock.tick(60)
