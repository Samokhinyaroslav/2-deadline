import pygame


class Radish(pygame.sprite.Sprite):
    def __init__(self, image, pos, size, speed, *group):
        super().__init__(*group)
        self.image = image
        self.speed = speed
        self.rect = self.image.get_rect().move(
            size[0] * pos[0] + 15, size[1] * pos[1] + 5)

    def walk(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            self.rect.x -= self.speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            self.rect.x += self.speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            self.rect.y -= self.speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            self.rect.y += self.speed


    def update(self, *args):
        if args:
            self.walk(args[0])


class Grater(pygame.sprite.Sprite):
    def __init__(self, image, pos, size, speed, *group):
        super().__init__(*group)
        self.image = image
        self.speed = speed
        self.rect = self.image.get_rect().move(
            size[0] * pos[0] + 15, size[1] * pos[1] + 5)

    def run(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            self.rect.x += self.speed

