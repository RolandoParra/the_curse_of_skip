import pygame
import random
import sys
import time


class Menu:
    """Clase para manejar el menú principal del juego"""
    
    def __init__(self, screen_width=800, screen_height=600):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font_title = pygame.font.SysFont(None, 72, bold=True)
        self.font_menu = pygame.font.SysFont(None, 48)
        self.font_small = pygame.font.SysFont(None, 32)
        self.selected_option = 0  # 0: Jugar, 1: Instrucciones, 2: Salir
        self.options = ["JUGAR", "INSTRUCCIONES", "SALIR"]
        self.background_color = (20, 20, 40)
        self.background_image = pygame.image.load("assets/img/menu.png")
        self.text_color = (255, 255, 255)
        self.selected_color = (255, 200, 0)
        self.in_instructions = False
        
    def handle_events(self):
        """Maneja los eventos del menú"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.in_instructions:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                        self.in_instructions = False
                else:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        return self.execute_option()
        return None
    
    def execute_option(self):
        """Ejecuta la opción seleccionada"""
        if self.selected_option == 0:  # JUGAR
            return "PLAY"
        elif self.selected_option == 1:  # INSTRUCCIONES
            self.in_instructions = True
            return None
        elif self.selected_option == 2:  # SALIR
            pygame.quit()
            sys.exit()
    
    def draw_menu(self, screen):
        """Dibuja el menú en pantalla"""
        screen.blit(self.background_image, (0, 0))
        
        if self.in_instructions:
            self.draw_instructions(screen)
        else:
            # Título
            title = self.font_title.render("THE CURSE OF SKIP", True, self.selected_color)
            title_rect = title.get_rect(center=(self.screen_width // 2, 100))
            screen.blit(title, title_rect)
            
            # Subtítulo
            subtitle = self.font_small.render("Supervivencia y terror", True, self.text_color)
            subtitle_rect = subtitle.get_rect(center=(self.screen_width // 2, 170))
            screen.blit(subtitle, subtitle_rect)
            
            # Opciones del menú
            start_y = 300
            for i, option in enumerate(self.options):
                color = self.selected_color if i == self.selected_option else self.text_color
                text = self.font_menu.render(option, True, color)
                text_rect = text.get_rect(center=(self.screen_width // 2, start_y + i * 80))
                screen.blit(text, text_rect)
            
            # Instrucciones de control
            hint = self.font_small.render("↑/↓ para navegar | ENTER para seleccionar", True, (150, 150, 150))
            hint_rect = hint.get_rect(center=(self.screen_width // 2, self.screen_height - 50))
            screen.blit(hint, hint_rect)
    
    def draw_instructions(self, screen):
        """Dibuja la pantalla de instrucciones"""
        screen.blit(self.background_image, (0, 0))
        
        title = self.font_title.render("INSTRUCCIONES", True, self.selected_color)
        title_rect = title.get_rect(center=(self.screen_width // 2, 30))
        screen.blit(title, title_rect)
        
        instructions = [
            "CONTROLES:",
            "Teclas 0-9: Cambiar entre cámaras",
            "ESPACIO: Repeler monstruos en Cámara 0",
            "",
            "OBJETIVO:",
            "Sobrevive 6 horas monitoreando las cámaras.",
            "Si un monstruo llega a la Cámara 0, ¡GAME OVER!",
            "Presiona ESPACIO cuando lleguen a tu puerta.",
            "",
            "Presiona ENTER o ESC para volver",
        ]
        
        start_y = 120
        for i, line in enumerate(instructions):
            if line == "":
                continue
            color = self.selected_color if line.isupper() and line != "" else self.text_color
            text = self.font_small.render(line, True, color)
            text_rect = text.get_rect(center=(self.screen_width // 2, start_y + i * 40))
            screen.blit(text, text_rect)


class Controller:
    def __init__(self):
        self.monstruo1_position = 0
        self.monstruo2_position = 0
        self.horas = 0
        self.minutos = 0
        # flags para comunicar al bucle principal sin importar game.py
        self.game_over_flag = False
        self.win_flag = False

    def game_over(self):
        # Señala al juego que debe ejecutar la secuencia de game over
        self.game_over_flag = True

    def check(self):
        if self.monstruo1_position > 10:
            self.game_over()
        elif self.monstruo2_position > 10:
            self.game_over()

    def update(self):
        if self.monstruo1_position == 9:
            self.monstruo1_position += 1
        elif self.monstruo2_position == 9:
            self.monstruo2_position += 1
        else:
            self.monstruo1_position = random.randint(0, 9)
            self.monstruo2_position = random.randint(0, 9)
    
    def move_enemy(self, enemy_id):
        if enemy_id == 1:
            self.monstruo1_position = random.randint(0, 10)
        elif enemy_id == 2:
            self.monstruo2_position = random.randint(0, 10)

    def reset_enemy(self, enemy_id):
        if enemy_id == 1:
            self.monstruo1_position = random.randint(0, 9)
        elif enemy_id == 2:
            self.monstruo2_position = random.randint(0, 9)
    def check_hora(self):
        if self.horas >= 6:
            # Señala al juego que ha ganado (placeholder para más lógica)
            self.win_flag = True


    def increment_hora(self):
        self.horas += 1