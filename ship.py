import pygame


class Ship:
    """Класс для управления кораблем"""

    def __init__(self, si_game):
        """Инициализирует корбаль и задает его начальную точку"""
        self.screen = si_game.screen
        self.settings = si_game.settings
        self.screen_rect = self.screen.get_rect()

        # Загружает картинку и получает прямоугольник
        self.image = pygame.image.load('img/ship.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты корабля
        self.x = float(self.rect.x)

        # Флаги перемещение
        self.move_right = False
        self.move_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.move_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в определенной позиции"""
        self.screen.blit(self.image, self.rect)
