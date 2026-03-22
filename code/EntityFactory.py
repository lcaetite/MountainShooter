#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(2):
                    list_bg.append(Background(f'Level1Bg{i}',(0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10,200))
            case 'Player2':
                return Player('Player2', (80,200))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, 200))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, 200))

