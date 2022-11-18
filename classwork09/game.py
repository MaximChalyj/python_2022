import time

import pygame
from pygame.draw import *
from random import *
import numpy as np

FPS = 60
screen = pygame.display.set_mode((1200, 900))

# Цвета шаров
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
LILAC = (182, 102, 210)
AMBER = (255, 191, 0)
VINOUS = (113, 25, 25)
RED_CORAL = (255, 127, 80)
BLUE_STEEL = (80, 127, 255)
LIME = (204, 255, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, LILAC, AMBER, VINOUS, RED_CORAL, BLUE_STEEL, LIME]


def ballz(screen: pygame.surface, n: int, x: list, y: list, velocity_x: list, velocity_y: list, r: list,
          color: list, hit: list):
    """Эта функция создает цели в форме кругов и обновляет их положение на экране. Круги движутся с постоянной
    скоростью и отскакивают от краев экрана. :экран параметров: Объект класса pygame.поверхность, на которой будут
    нарисованы кругов. :параметр n: Количество кругов. :параметр x: Список текущих горизонтальных координат центров
    кругов. :параметр y: Список текущих вертикальных координат центров кругов. :параметр velocity_x: Список текущих
    горизонтальных скоростей окружностей. :параметр velocity_y: Список текущих вертикальных скоростей окружностей.
    :параметр r: Список радиусов кругов. :цвет параметра: Список цветов кругов. :попадание параметра: список
    переменных bool для каждого круга, который имеет значение True, если пользователь нажал на него. и значение False
    в противном случае. Если это верно, функция обновляет все переменные текущего круга.
    """
    for i in range(n):
        if hit[i]:
            r[i] = (randint(10, 100))
            x[i] = (randint(r[i], 1200 - r[i]))
            y[i] = (randint(r[i], 900 - r[i]))
            velocity_x[i] = (randint(-100, 100))
            velocity_y[i] = (randint(-100, 100))
            color[i] = (COLORS[randint(0, 11)])
            hit[i] = False
        circle(screen, color[i], (round(x[i]), round(y[i])), r[i])
        x[i] += velocity_x[i] * dt_1
        y[i] += velocity_y[i] * dt_1


pygame.init()


def square(screen: pygame.surface, n: int, x: list, y: list, velocity_x: list, velocity_y: list, r: list,
           color: list, hit: list):
    """Эта функция создает цели в форме квадратов и обновляет их положение на экране. Квадараты движутся с постоянной
    скоростью и отскакивают от краев экрана. :экран параметров: Объект класса pygame.поверхность, на которой будут
    нарисованы квадраты. :параметр n: Количество квадратов. :параметр x: Список текущих горизонтальных координат
    левых нижних вершин квдаратов. :параметр y: Список текущих вертикальных координат левых нижних вершин квадратаов.
    :параметр velocity_x: Список текущих горизонтальных скоростей квдратов. :параметр velocity_y: Список текущих
    вертикальных скоростей квадратов. :параметр r: Список сторон квадратов. :цвет параметра: Список цветов квадратов.
    :попадание параметра: список переменных bool для каждого квадрата, который имеет значение True, если пользователь
    нажал на него. и значение False в противном случае. Если это верно, функция обновляет все переменные текущего
    квадрата.
    """
    for i in range(n):
        if hit[i]:
            r[i] = (randint(10, 100))
            x[i] = (randint(0, 1200 - r[i]))
            y[i] = (randint(r[i], 900))
            velocity_x[i] = (randint(-100, 100))
            velocity_y[i] = (randint(-100, 100))
            color[i] = (COLORS[randint(0, 11)])
            hit[i] = False
        polygon(screen, color[i], [[x[i], y[i]], [x[i] + r[i], y[i]], [x[i] + r[i], y[i] - r[i]], [x[i], y[i] - r[i]]])
        x[i] += velocity_x[i] * dt_2
        y[i] += velocity_y[i] * dt_2


pygame.init()

n_1 = 3  # Количество кругов на экране
r_1 = [randint(10, 100) for i in range(n_1)]  # Лист радиусов кругов
x_1 = [randint(r_1[i], 1200 - r_1[i]) for i in range(n_1)]  # Текущая горизонтальная координата круга
y_1 = [randint(r_1[i], 900 - r_1[i]) for i in range(n_1)]  # Текущая вертикальная координата круга
velocity_x_1 = [randint(0, 20) for i in range(n_1)]  # Текущая горизонтальная скорость круга
velocity_y_1 = [randint(0, 20) for i in range(n_1)]  # Текущая вертикальная скорость круга
color_1 = [COLORS[randint(0, 11)] for i in range(n_1)]  # Цвета кружочков
hit_1 = [False for i in range(
    n_1)]  # Список переменных bool для каждого круга, который имеет значение True, если пользователь нажал на круг,
# и значение False в противном случае

dt_1 = 0.1  # Интервал между промежутками движения шаров

n_2 = 3  # Количество квадратов на экране
r_2 = [randint(10, 100) for i in range(n_2)]  # Лист радиусов квадратов
x_2 = [randint(0, 1200 - r_2[i]) for i in range(n_2)]  # Текущая горизонтальная координаталевой нижней вершины квадрата
y_2 = [randint(r_2[i], 900) for i in range(n_2)]  # Текущая вертикальная координата  левой нижней вершины квадрата
velocity_x_2 = [randint(0, 20) for i in range(n_2)]  # Текущая горизонтальная скорость квадрата
velocity_y_2 = [randint(0, 20) for i in range(n_2)]  # Текущая вертикальная скорость квадрата
color_2 = [COLORS[randint(0, 11)] for i in range(n_2)]  # Цвета квадратов
hit_2 = [False for i in range(
    n_2)]  # Список переменных bool для каждого круга, который имеет значение True, если пользователь нажал на круг,
# и значение False в противном случае

dt_2 = 0.1  # Интервал между промежутками движения квадратов

score = 0  # Счёт игры
c_score = pygame.font.Font(None, 32)  # Подготовка к отображению счета во время игры
length_of_round = 20  # Продолжительность игры в секундах

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    screen.fill(WHITE)  # Заполнение экрана белым цветом
    ballz(screen, n_1, x_1, y_1, velocity_x_1, velocity_y_1, r_1, color_1,
          hit_1)  # Рисование кругов на текущих позициях
    square(screen, n_2, x_2, y_2, velocity_x_2, velocity_y_2, r_2, color_2,
           hit_2)  # Рисование квадратов на текущих позициях

    for i in range(n_1):
        for j in range(i):
            if r_1[i] + r_1[j] >= ((x_1[i] - x_1[j]) ** 2 + (y_1[i] - y_1[j]) ** 2) ** 0.5:
                alpha = (r_1[i] / r_1[j]) ** 2  # Отношение масс кругов как отношение их линейных размеров
                sin = abs(y_1[j] - y_1[i]) / (r_1[i] + r_1[j])  # Тригонометрические функции угла между прямой,
                cos = np.sign(y_1[j] - y_1[i]) * (x_1[j] - x_1[i]) / (
                            r_1[i] + r_1[j])  # соединяющей центры кругов c осью абцисс
                M = np.array([[alpha, 1, 0, 0], [0, 0, alpha, 1], [sin, 0, -cos, 0],
                              [cos, -cos, sin, -sin]])  # Правая часть системы уравнений
                V = np.array([alpha * velocity_x_1[i] + velocity_x_1[j],  # Левая часть системы уравнений
                              alpha * velocity_y_1[i] + velocity_y_1[j],
                              velocity_x_1[i] * sin - velocity_y_1[i] * cos,
                              -velocity_x_1[i] * cos - velocity_y_1[i] * sin +
                              velocity_x_1[j] * cos + velocity_y_1[j] * sin])
                A = np.linalg.solve(M, V)  # Решение системы уравнений
                velocity_x_1[i] = A[0]
                velocity_x_1[j] = A[1]
                velocity_y_1[i] = A[2]
                velocity_y_1[j] = A[3]

    for i in range(n_1):  # Отражение кругов от границ экрана
        if (x_1[i] - r_1[i] <= 0) or (x_1[i] + r_1[i] >= 1200):
            velocity_x_1[i] = -velocity_x_1[i]
        if (y_1[i] - r_1[i] <= 0) or (y_1[i] + r_1[i] >= 900):
            velocity_y_1[i] = -velocity_y_1[i]
    pygame.display.update()

    for i in range(n_2):  # Отражение квадратов от границ экрана
        if (x_2[i] <= 0) or (x_2[i] + r_2[i] >= 1200):
            velocity_x_2[i] = -velocity_x_2[i]
        if (y_2[i] - r_2[i] <= 0) or (y_2[i] >= 900):
            velocity_y_2[i] = -velocity_y_2[i]
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in range(n_1):
                if (event.pos[0] - x_1[i]) ** 2 + (event.pos[1] - y_1[i]) ** 2 <= r_1[i] ** 2:
                    hit_1[i] = True
                    score += 1
            for i in range(n_2):
                if (event.pos[0] - x_2[i] >= 0) and \
                        (x_2[i] + r_2[i] - event.pos[0] >= 0) and \
                        (y_2[i] - event.pos[1] >= 0) and \
                        (event.pos[1] + r_2[i] - y_2[i] >= 0):
                    hit_2[i] = True
                    score += 1

screen.fill(WHITE)  # Отображение результата
f_score = pygame.font.Font(None, 100)
text2 = f_score.render("Your score is: " + str(score), 1, BLACK)
screen.blit(text2, (350, 400))
pygame.display.update()
finished = False
time.sleep(1)
