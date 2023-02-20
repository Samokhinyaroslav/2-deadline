import pygame


class Radish(pygame.sprite.Sprite):
    is_alive = True
    on_ground = False
    power_jump = 150
    gravity = 3
    is_in_house = False

    def __init__(self, image, pos, size, speed, *group):
        super().__init__(*group)
        self.image = image
        self.speed = speed
        self.rect = self.image.get_rect().move(
            size[0] * pos[0] + 15, size[1] * pos[1] + 5)

    def walk(self, event):
        if event.type == pygame.KEYDOWN and event.type != pygame.KEYUP:
            if event.key == pygame.K_a:
                self.rect.x -= self.speed
            if event.key == pygame.K_d:
                self.rect.x += self.speed
            if event.key == pygame.K_SPACE:
                self.jump()

    def jump(self):
        if self.on_ground:
            self.rect.y -= self.power_jump

    def go_in_house(self, control_point_group):
        if pygame.sprite.spritecollideany(self, control_point_group):
            return True

    def fall(self):
        self.rect.y += self.gravity
        self.on_ground = False

    def check_collide(self, platform_group, enemy_group):
        platforms = pygame.sprite.spritecollide(self, platform_group, False)
        if not platforms:
            self.fall()
        else:
            for platform in platforms:
                if self.rect.right + self.speed <= platform.rect.left:
                    self.rect.right = platform.rect.left

                if self.rect.left - self.speed >= platform.rect.right:
                    self.rect.left = platform.rect.right

                if self.rect.bottom - self.gravity <= platform.rect.top:
                    self.rect.bottom = platform.rect.top + self.gravity
                    self.on_ground = True

                if self.rect.top + platform.rect.width // 2 >= platform.rect.bottom:
                    self.rect.top = platform.rect.bottom

        if pygame.sprite.spritecollideany(self, enemy_group):
            self.kill()

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

    def run(self):
        self.rect.x += self.speed

    def update(self, *args):
        self.run()