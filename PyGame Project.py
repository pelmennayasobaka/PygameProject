import pygame as pg
from random import randint
from functools import lru_cache
import sys
import os

# Инициализация Pygame
pg.init()

# Константы
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = "#de2148"
BROWN = "#8a594d"
FPS = 60
FLYING_END = pg.USEREVENT + 1
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('СУПРЕ МЕГА ДУДЛЕ ДЖАПМ version 52.42')


# функция для завершения игры
def terminate():
    pg.quit()
    sys.exit()


# функция для загрузки файлов
def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    return image


# функция для отображения стартового экрана
def start_screen(skin='hero.png'):
    play_button = pg.Rect(200, 120, 400, 100)
    rules_button = pg.Rect(200, 250, 400, 100)
    facts_button = pg.Rect(200, 380, 400, 100)
    skins_button = pg.Rect(200, 490, 400, 100)
    clock = pg.time.Clock()
    fon = pg.transform.scale(load_image('main_fon.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    play = pg.transform.scale(load_image('play_note.png'), (400, 100))
    screen.blit(play, (200, 120))
    rules = pg.transform.scale(load_image('rules_note.png'), (400, 100))
    screen.blit(rules, (200, 250))
    facts = pg.transform.scale(load_image('facts_note.png'), (400, 100))
    screen.blit(facts, (200, 380))
    skins = pg.transform.scale(load_image('skins_note.png'), (400, 100))
    screen.blit(skins, (200, 490))
    font = pg.font.Font(None, 30)
    string_rendered = font.render("СУПРЕ МЕГА ДУДЛЕ ДЖАПМ", 1, pg.Color('black'))
    file = open("data/scores.txt", "rt")
    best_score = file.readlines()[0]
    score_string = font.render(f"лучший результат: {best_score}", 1, pg.Color('black'))
    file.close()
    score_rect = score_string.get_rect()
    score_rect.top = 60
    score_rect.x = 290
    screen.blit(score_string, score_rect)
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 20
    intro_rect.x = 250
    screen.blit(string_rendered, intro_rect)
    # выбор действия в главном меню
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if rules_button.collidepoint(mouse_pos):
                    rules_screen()
                    return
                elif facts_button.collidepoint(mouse_pos):
                    facts_screen()
                    return
                elif skins_button.collidepoint(mouse_pos):
                    skins_screen()
                    return
                elif play_button.collidepoint(mouse_pos):
                    game(skin)
                    return
        pg.display.flip()
        clock.tick(FPS)


# отображение правил игры
def rules_screen():
    pon_button = pg.Rect(300, 400, 200, 100)
    clock = pg.time.Clock()
    intro_text = ["ВАЖНЫЕ ПРАВИЛА ИГРЫ!!!!!!!!!!!!!", "", "",
                  "1. Не играть в игру",
                  "2. Всё"]
    fon = pg.transform.scale(load_image('rules_fon.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    play = pg.transform.scale(load_image('pon_note.png'), (200, 100))
    screen.blit(play, (300, 400))
    font = pg.font.Font(None, 50)
    text_coord = 20
    for line in intro_text:
        string_rendered = font.render(line, 1, pg.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 120
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if pon_button.collidepoint(mouse_pos):
                    start_screen()
                    return
        pg.display.flip()
        clock.tick(FPS)


# отображение фактов об игре
def facts_screen():
    pon_button = pg.Rect(300, 400, 200, 100)
    clock = pg.time.Clock()
    intro_text = ["                   ИНТЕРЕСНЫЕ (нет) ФАКТЫ ПРО ИГРУ", "",
                  "1. Это игра была сделана за пару дней, так как",
                  "у создателей игры были важные дела, такие как ничего",
                  "2. Среднестатистически каждый первый человек, который",
                  "зашёл поиграть в нашу крутую игру, потерял пару IQ",
                  "4. Я разучился считать",
                  "52. Тут больше ничего нет"]
    fon = pg.transform.scale(load_image('facts_fon.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    play = pg.transform.scale(load_image('pon_note.png'), (200, 100))
    screen.blit(play, (300, 400))
    font = pg.font.Font(None, 38)
    text_coord = 20
    for line in intro_text:
        string_rendered = font.render(line, 1, pg.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if pon_button.collidepoint(mouse_pos):
                    start_screen()
                    return
        pg.display.flip()
        clock.tick(FPS)


# отображение выбора скина
def skins_screen():
    clock = pg.time.Clock()
    skin_button = pg.Rect(25, 150, 150, 150)
    skin1_button = pg.Rect(225, 150, 150, 150)
    skin2_button = pg.Rect(425, 150, 150, 150)
    skin3_button = pg.Rect(625, 150, 150, 150)
    fon = pg.transform.scale(load_image('skins_fon.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    skin = pg.transform.scale(load_image('hero.png'), (150, 150))
    screen.blit(skin, (25, 150))
    skin1 = pg.transform.scale(load_image('hero1.png'), (150, 150))
    screen.blit(skin1, (225, 150))
    skin2 = pg.transform.scale(load_image('hero2.png'), (150, 150))
    screen.blit(skin2, (425, 150))
    skin3 = pg.transform.scale(load_image('hero3.png'), (150, 150))
    screen.blit(skin3, (625, 150))
    font = pg.font.Font(None, 50)
    string_rendered = font.render("Выберите скин", 1, pg.Color('white'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 20
    intro_rect.x = 280
    screen.blit(string_rendered, intro_rect)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if skin_button.collidepoint(mouse_pos):
                    start_screen('hero.png')
                    return
                elif skin1_button.collidepoint(mouse_pos):
                    start_screen('hero1.png')
                    return
                elif skin2_button.collidepoint(mouse_pos):
                    start_screen('hero2.png')
                    return
                elif skin3_button.collidepoint(mouse_pos):
                    start_screen('hero3.png')
                    return
        pg.display.flip()
        clock.tick(FPS)


# отображение правил игры
def game_over_screen(skin):
    pon_button = pg.Rect(300, 400, 200, 100)
    clock = pg.time.Clock()
    pon = pg.transform.scale(load_image('pon_note.png'), (200, 100))
    screen.blit(pon, (300, 400))
    font = pg.font.Font(None, 50)
    string_rendered = font.render("К сожалению, вы проиграли :(", 1, pg.Color('red'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 20
    intro_rect.x = 150
    screen.blit(string_rendered, intro_rect)
    font = pg.font.Font(None, 30)
    string_rendered = font.render("Попробуйте снова!", 1, pg.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 70
    intro_rect.x = 300
    screen.blit(string_rendered, intro_rect)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if pon_button.collidepoint(mouse_pos):
                    start_screen(skin)
                    return
        pg.display.flip()
        clock.tick(FPS)


# Класс платформы по которым будет прыгать герой
class Platform:
    def __init__(self, x, y, width, row):
        n = randint(1, 100)
        if n <= 5:
            self.type = "jumping"
        elif n <= 20:
            self.type = "broken"
        else:
            self.type = "normal"
        self.rect = pg.Rect(x, y, width, 10)
        self.row = row
        if self.type == "jumping":
            self.velocity_change = -35
        else:
            self.velocity_change = -15

    def draw(self):
        if self.type == "normal":
            pg.draw.rect(screen, BLACK, self.rect)
        elif self.type == "jumping":
            pg.draw.rect(screen, RED, self.rect)
        else:
            pg.draw.rect(screen, BROWN, self.rect)


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.y += self.dy

    def update(self, target):
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


# Класс игрока
class Player:
    def __init__(self, skin):
        self.image = pg.transform.scale(load_image(skin), (50, 50))
        self.rect = pg.Rect(WIDTH // 2 - 15, HEIGHT - 150, 30, 30)
        self.velocity_y = 0

    def update(self, flying):
        if not flying:
            self.velocity_y += 0.5  # Гравитация
        self.rect.y += self.velocity_y
        # Проверка на выход за границы
        if self.rect.y > HEIGHT:
            self.rect.y = HEIGHT - 30
            self.velocity_y = 0

    def jump(self):
        self.velocity_y = -15

    def draw(self):
        screen.blit(self.image, self.rect)


class Rocket:
    def __init__(self, x, y):
        self.image = pg.transform.scale(load_image('empty_rocket.png'), (100, 100))
        self.rect = pg.Rect(x, y, 100, 100)

    def draw(self):
        screen.blit(self.image, self.rect)


def generate_platform(platform_y, point, k):
    platforms = []
    rockets = []
    for i in range(point % 10, point % 10 + k):
        if randint(1, 100) > 96:
            rockets.append(Rocket(randint(60, WIDTH - 60), platform_y - 100 * i + 50))
        n = randint(1, 3)
        if n == 1:
            platforms.append(Platform(randint(60, WIDTH - 60), platform_y - 100 * i, randint(60, 120), point + i))
        elif n == 2:
            platforms.append(Platform(randint(60, 300), platform_y - 100 * i, randint(60, 120), point + i))
            platforms.append(Platform(randint(300, WIDTH - 60), platform_y - 100 * i, randint(60, 120), point + i))
        else:
            platforms.append(Platform(randint(60, 200), platform_y - 100 * i, randint(60, 120), point + i))
            platforms.append(Platform(randint(200, 400), platform_y - 100 * i, randint(60, 120), point + i))
            platforms.append(Platform(randint(400, WIDTH - 60), platform_y - 100 * i, randint(60, 120), point + i))
    return platforms, rockets


@lru_cache
def game(skin):
    clock = pg.time.Clock()
    camera = Camera()
    player = Player(skin)
    platform_y = 500
    font = pg.font.Font(None, 36)
    score = 0
    rockets = []
    flying = False  # проверка, летит ли герой на ракете
    is_flipped = False # отвечает за поворот героя
    # создание платформ по которым прыгает герой
    platforms = list()
    platforms.append(Platform(WIDTH // 2 - 60, HEIGHT - 50, 120, 0))
    plat = generate_platform(platform_y, platforms[-1].row, 50)
    platforms += plat[0]
    rockets += plat[1]
    running = True
    while running:
        string_rendered = font.render(f"Счет {score}", 1, pg.Color('black'))
        score_rect = string_rendered.get_rect()
        score_rect.top = 50
        score_rect.x = 700
        camera.update(player)
        # обновляем положение всех спрайтов
        for sprite in platforms:
            camera.apply(sprite)
        for rocket in rockets:
            camera.apply(rocket)
        camera.apply(player)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                terminate()
            if event.type == FLYING_END:
                flying = False
                pg.time.set_timer(FLYING_END, 0)
                is_flipped = False
                clock.tick()
                player.image = pg.transform.scale(load_image(skin), (50, 50))
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and player.rect.left > 0:
            player.rect.x -= 5
            if not is_flipped and not flying:
                player.image = pg.transform.flip(player.image, True, False)
                is_flipped = True
        if keys[pg.K_RIGHT] and player.rect.right < WIDTH:
            player.rect.x += 5
            if is_flipped and not flying:
                player.image = pg.transform.flip(player.image, True, False)
                is_flipped = False
        player.update(flying)
        # быстрое падение, если персонаж ниже платформ
        if player.rect.bottom > platforms[0].rect.bottom + 100:
            player.velocity_y += 3
        # удаление платформ снизу игрока
        for plat in platforms[:10]:
            if plat.rect.bottom >= player.rect.bottom + 500:
                platforms.remove(plat)
        for rocket in rockets[:10]:
            if rocket.rect.bottom >= player.rect.bottom + 500:
                rockets.remove(rocket)
        if len(platforms) < 21:
            plat = generate_platform(platform_y, platforms[-1].row, 30)
            platforms += plat[0]
            rockets += plat[1]
        # Проверка коллизий с платформами
        for platform in platforms:
            if player.rect.colliderect(platform.rect) and player.velocity_y >= 0:
                if platform.type == "broken":
                    platforms.remove(platform)
                score = platform.row
                player.rect.bottom = platform.rect.top
                player.velocity_y = platform.velocity_change
        for rocket in rockets:
            if player.rect.colliderect(rocket.rect) and player.velocity_y >= 0:
                player.velocity_y = -20
                flying = True
                if skin == 'hero.png':
                    player.image = pg.transform.scale(load_image('rocket.png'), (100, 100))
                elif skin == 'hero1.png':
                    player.image = pg.transform.scale(load_image('rocket1.png'), (100, 100))
                elif skin == 'hero2.png':
                    player.image = pg.transform.scale(load_image('rocket2.png'), (100, 100))
                elif skin == 'hero3.png':
                    player.image = pg.transform.scale(load_image('rocket3.png'), (100, 100))
                pg.time.set_timer(FLYING_END, 2000)
        screen.blit(pg.transform.scale(load_image('play_fon.png'), (WIDTH, HEIGHT)), (0, 0))
        screen.blit(string_rendered, score_rect)
        if HEIGHT - 20 <= player.rect[1] <= HEIGHT:
            file = open("data/scores.txt", "r+")
            if int(file.readlines()[0]) < score:
                file.seek(0)
                file.write(str(score))
                file.close()
            return game_over_screen(skin)
        # выход за экран
        if player.rect[0] >= WIDTH - 30:
            player.rect[0] = 1
        elif player.rect[0] <= 0:
            player.rect[0] = WIDTH - 30
        player.draw()
        for platform in platforms:
            platform.draw()
        for rocket in rockets:
            rocket.draw()
        pg.display.flip()
        clock.tick(FPS)
    pg.quit()


if __name__ == '__main__':
    start_screen()