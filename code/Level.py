#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self,window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):
        clock = pygame.time.Clock()

        while True:
            # EVENTOS (ESSENCIAL)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Limpa a tela
            self.window.fill((0, 0, 0))

            # Desenha e move
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()

            # Atualiza tela (UMA VEZ SÓ)
            pygame.display.flip()

            # Controla FPS
            clock.tick(60)

