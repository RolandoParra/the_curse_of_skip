import pygame
import random
import sys
import time


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