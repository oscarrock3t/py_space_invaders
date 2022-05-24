import sys, pygame
from settings import Settings
from ship import Ship


class SpaceInvaders():
    """Класс для управления игровыми ресурсами"""

    def __init__(self):
        """Инициализация игры и ресурсов"""
        self.settings = Settings()
        pygame.init()
        pygame.display.set_caption(self.settings.caption)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height), vsync=False)
        self.ship = Ship(self)

    def _check_events(self):
        """Отслеживание нажатий клавиш"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        if event.key == pygame.K_LEFT:
            self.ship.move_left = True
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

    def run_game(self):
        """Запуск основого цикла игры"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()




if __name__ == '__main__':
    si = SpaceInvaders()
    si.run_game()
