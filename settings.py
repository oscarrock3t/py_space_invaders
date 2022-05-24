class Settings():
    """Класс для хранения всех настроек игры Space Invaders"""

    def __init__(self):
        #Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (25, 25, 26)

        #Заголовок окна
        self.caption = 'Space Invaders'

        # Настройки корабля
        self.ship_speed = 1.5
