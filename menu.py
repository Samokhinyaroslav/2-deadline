import pygame
import pygame_menu

def create_theme_menu():
    myimage = pygame_menu.baseimage.BaseImage(
        image_path="data/Prew2.jpg",
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,
        drawing_offset=(0, 0)
    )
    mytheme = pygame_menu.Theme(background_color=myimage,
                                      title_background_color=(193, 0, 113),
                                      title_font_shadow=True,
                                      widget_padding=30)
    return mytheme


def start_menu(screen, size_screen, theme_menu=None):
    menu = pygame_menu.Menu(
        height=size_screen[1],
        theme=theme_menu,
        title='Добро пожаловать',
        width=size_screen[0]
    )
    menu.add.button("Начать игру", lambda: start_game(screen))
    menu.add.button("Выход", pygame_menu.events.EXIT)
    menu.mainloop(screen)


def start_game(screen):
    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type ** pygame.QUIT:
                running = False

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 900, 550
    screen = pygame.display.set_mode(size)
    start_menu(screen, size, create_theme_menu())