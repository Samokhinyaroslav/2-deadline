import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    # else:
    #     image = image.convert_alpha()
    return image


class Level:
    tile_images = {
        'wall': load_image('block.png'),
        'empty': load_image('fon.png'),
        'house': load_image('house.png')
    }
    player_image = load_image('radish.png')
    grater_image = load_image('grater.png')

    tile_width = tile_height = 50

    def __init__(self, filename):
        self.filename = filename
        self.data_level = self.load_level()

    def load_level(self):
        # читаем уровень, убирая символы перевода строки
        with open(self.filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]

        # и подсчитываем максимальную длину
        max_width = max(map(len, level_map))

        # дополняем каждую строку пустыми клетками ('.')
        return list(map(lambda x: x.ljust(max_width, '.'), level_map))

    def generate_level(self, tile_module, character_module, player_group, tile_group, wall_group, empty_group, all_sprites):
        new_player, x, y = None, None, None
        for y in range(len(self.data_level)):
            for x in range(len(self.data_level[y])):
                if self.data_level[y][x] == '#':
                    tile_module.Tile(self.tile_images['wall'], (x, y), (50, 50), wall_group, tile_group, all_sprites)

                elif self.data_level[y][x] == '+':
                    tile_module.Tile(self.tile_images['empty'], (x, y), (50, 50), empty_group, tile_group, all_sprites)
                    grater = character_module.Grater(self.grater_image, (x, y), (50, 50), 10, player_group, all_sprites)
                elif self.data_level[y][x] == '@':
                    tile_module.Tile(self.tile_images['empty'], (x, y), (50, 50), empty_group, tile_group, all_sprites)
                    new_player = character_module.Radish(self.player_image, (x, y), (50, 50), 20, player_group, all_sprites)
                elif self.data_level[y][x] == '/':
                    tile_module.Tile(self.tile_images['house'], (x, y), (50, 50), wall_group, tile_group, all_sprites)

        # вернем игрока, а также размер поля в клетках
        return new_player, x, y

class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target, width, height):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)



