import sys
import pygame
from pygame import QUIT

from Geeks_M2.homework_four.characterClass import Character

# pygame инициализация
pygame.init()

# Это размер нашего экрана
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

# Это название игры
pygame.display.set_caption("White Square")


# Здесь мы создаем персонажа
player = Character(100, 100)

# Это главный игровой цикл
while True:
    # pygame.event.get() это метод который возвращает список всех событий которые произошли (нажатие на клавишы, движение мыши итд)
    for event in pygame.event.get(): # здесь мы перебираем все события в списке. Здесь мы можем обрабатывать каждое событие
        if event.type == QUIT: # Проверка - Если пользователь нажал на "X"  то мы завершаем работу библиотеки pygame
            pygame.quit()
            sys.exit() # Закрытие и завершение игры

        # Эта часть код находится в цикле для того чтобы куб двигался при зажиме нужных клавиш (wasd)
        keys = pygame.key.get_pressed() # Получение всех ключей для того чтобы двигать куб
        if keys[pygame.K_a]: # Двигаем влево
            player.x -= 10 # Меняем местоположение
        if keys[pygame.K_d]: # Двигаем вправо
            player.x += 10
        if keys[pygame.K_w]: # Двигаем вверх
            player.y -= 10
        if keys[pygame.K_s]: # Двигаем вниз
            player.y += 10

        # Здесь мы отрисовываем экран
        screen.fill((0, 0, 0)) # очищаем экран перед каждым кадром. Если мы этого не сделаем то предыд.кадры будут сохраняться и будет ощущение будто мы просто рисуем белой кистичкой
        player.draw(screen)  # Это типа наш персонаж который будет просто белым квадратом
        pygame.display.update() # Эта часть обновляет весь игровой экран или его часть для того чтобы отобразить изменения сделанные в текущем кадре