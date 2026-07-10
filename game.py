import pygame
import random
import sys
from assets.src.classes import Controller
import time


actual_room = 1
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juan, trae pan")

game_controller = Controller()

def random_move_delay() -> int:
    return random.randint(10_000, 20_000)

enemy1_next_move = pygame.time.get_ticks() + random_move_delay()
enemy2_next_move = pygame.time.get_ticks() + random_move_delay()
enemy1_space_deadline = None
enemy2_space_deadline = None
HOUR_MS = 30_000  #duración de las horas
next_hour_tick = pygame.time.get_ticks() + HOUR_MS

#imagenes XD
cam01 = pygame.image.load("assets/img/01.png")
cam02 = pygame.image.load("assets/img/02.png")
cam03 = pygame.image.load("assets/img/03.png")
cam04 = pygame.image.load("assets/img/04.png")
cam05 = pygame.image.load("assets/img/05.png")
cam06 = pygame.image.load("assets/img/06.png")
cam07 = pygame.image.load("assets/img/07.png")
cam08 = pygame.image.load("assets/img/08.png")
cam09 = pygame.image.load("assets/img/09.png")
cam10 = pygame.image.load("assets/img/10.png")
try:
    win = pygame.image.load("assets/img/win.png")
except Exception:
    win = pygame.Surface((800, 600))
    win.fill((0, 200, 0))
try:
    gameover = pygame.image.load("assets/img/game_over.png")
except Exception:
    gameover = pygame.Surface((800, 600))
    gameover.fill((200, 0, 0))

m1 = pygame.image.load("assets/img/monstruo1.png")
m2 = pygame.image.load("assets/img/monstruo2.png")

# cargar efectos de sonido usando pygame.mixer.Sound
class _DummySound:
    def play(self):
        return

try:
    camsd = pygame.mixer.Sound("assets/sounds/cam.mp3")
except Exception:
    camsd = _DummySound()
try:
    cambio = pygame.mixer.Sound("assets/sounds/cambio.mp3")
except Exception:
    cambio = _DummySound()
try:
    win_sound = pygame.mixer.Sound("assets/sounds/win.mp3")
except Exception:
    win_sound = _DummySound()
try:
    zap = pygame.mixer.Sound("assets/sounds/zap.mp3")
except Exception:
    zap = _DummySound()
try:
    failed = pygame.mixer.Sound("assets/sounds/failed.wav")
except Exception:
    failed = _DummySound()

font = pygame.font.SysFont(None, 36)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if enemy1_space_deadline is not None:
                    game_controller.reset_enemy(1)
                    enemy1_space_deadline = None
                    enemy1_next_move = pygame.time.get_ticks() + random_move_delay()
                if enemy2_space_deadline is not None:
                    game_controller.reset_enemy(2)
                    enemy2_space_deadline = None
                    enemy2_next_move = pygame.time.get_ticks() + random_move_delay()
    

    texto_horas = font.render(f"Horas: {game_controller.horas}", True, (255, 255, 255))
    texto_horas_rect = texto_horas.get_rect(topright=(780, 10))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        actual_room = 1
        camsd.play()
    elif keys[pygame.K_2]:
        actual_room = 2
        camsd.play()
    elif keys[pygame.K_3]:
        actual_room = 3
        camsd.play()
    elif keys[pygame.K_4]:
        actual_room = 4
        camsd.play()
    elif keys[pygame.K_5]:
        actual_room = 5
        camsd.play()
    elif keys[pygame.K_6]:
        actual_room = 6
        camsd.play()
    elif keys[pygame.K_7]:
        actual_room = 7
        camsd.play()
    elif keys[pygame.K_8]:
        actual_room = 8
        camsd.play()
    elif keys[pygame.K_9]:
        actual_room = 9
        camsd.play()
    elif keys[pygame.K_0]:
        actual_room = 10
        camsd.play()

    if actual_room == 1:
        screen.blit(cam01, (0, 0))
    elif actual_room == 2:
        screen.blit(cam02, (0, 0))
    elif actual_room == 3:  
        screen.blit(cam03, (0, 0))
    elif actual_room == 4:
        screen.blit(cam04, (0, 0))
    elif actual_room == 5:
        screen.blit(cam05, (0, 0))
    elif actual_room == 6:
        screen.blit(cam06, (0, 0))
    elif actual_room == 7:
        screen.blit(cam07, (0, 0))
    elif actual_room == 8:
        screen.blit(cam08, (0, 0))
    elif actual_room == 9:
        screen.blit(cam09, (0, 0))
    elif actual_room == 10:
        screen.blit(cam10, (0, 0))

    if game_controller.monstruo1_position == actual_room:
        screen.blit(m1, (random.randint(0, 600), random.randint(0, 400)))
    if game_controller.monstruo2_position == actual_room:
        screen.blit(m2, (random.randint(0, 600), random.randint(0, 400)))
    now = pygame.time.get_ticks()

    if enemy1_space_deadline is not None and now >= enemy1_space_deadline:
        game_controller.game_over()
    if enemy2_space_deadline is not None and now >= enemy2_space_deadline:
        game_controller.game_over()

    if enemy1_space_deadline is None and now >= enemy1_next_move:
        game_controller.move_enemy(1)
        cambio.play()
        if game_controller.monstruo1_position == 10:
            enemy1_space_deadline = now + 20_000
            enemy1_next_move = None
        else:
            enemy1_next_move = now + random_move_delay()

    if enemy2_space_deadline is None and now >= enemy2_next_move:
        game_controller.move_enemy(2)
        cambio.play()
        if game_controller.monstruo2_position == 10:
            enemy2_space_deadline = now + 20_000
            enemy2_next_move = None
        else:
            enemy2_next_move = now + random_move_delay()

    if now >= next_hour_tick:
        next_hour_tick = now + HOUR_MS
        game_controller.increment_hora()
        game_controller.check_hora()
    
    screen.blit(texto_horas, texto_horas_rect)

    game_controller.check()

    # manejar estados finales mediante flags (no exceptions)
    if getattr(game_controller, 'game_over_flag', False):
        try:
            failed.play()
        except Exception:
            pass
        try:
            screen.blit(gameover, (0, 0))
            pygame.display.flip()
        except Exception:
            screen.fill((0, 0, 0))
            pygame.display.flip()
        time.sleep(7)
        sys.exit()

    if getattr(game_controller, 'win_flag', False):
        try:
            win_sound.play()
        except Exception:
            pass
        try:
            screen.blit(win, (0, 0))
            pygame.display.flip()
        except Exception:
            screen.fill((0, 200, 0))
            pygame.display.flip()
        time.sleep(10)
        sys.exit()

    clock.tick(60)
    pygame.display.flip()