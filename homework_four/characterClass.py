import pygame


class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 50

    # Рисуем нашего персонажа
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.size, self.size))