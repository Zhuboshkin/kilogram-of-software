import pygame
import random

# Константы для размеров поля и сетки
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвета
BOARD_BACKGROUND_COLOR = (0, 0, 0)
APPLE_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)
BORDER_COLOR = (93, 216, 228)


class GameObject:
    """Базовый класс для всех игровых объектов на поле."""

    def __init__(self):
        """Инициализирует позицию по центру экрана и пустой цвет."""
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.body_color = None

    def draw(self, surface):
        """Абстрактный метод отрисовки. Переопределяется в дочерних классах."""
        pass


class Apple(GameObject):
    """Класс, описывающий яблоко на игровом поле."""

    def __init__(self, snake_positions=None):
        """Устанавливает цвет яблока и генерирует его стартовую позицию."""
        super().__init__()
        self.body_color = APPLE_COLOR
        if snake_positions is None:
            snake_positions = [self.position]
        self.randomize_position(snake_positions)

    def randomize_position(self, snake_positions):
        """
        Генерирует новую случайную позицию для яблока.
        Гарантирует, что яблоко не появится на теле змейки.
        """
        while True:
            new_position = (
                random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE
            )
            if new_position not in snake_positions:
                self.position = new_position
                break

    def draw(self, surface):
        """Отрисовывает яблоко на переданной поверхности."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.body_color, rect)
        pygame.draw.rect(surface, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Класс, описывающий змейку и её поведение."""

    def __init__(self):
        """Инициализирует змейку, задает цвет и устанавливает в начальное положение."""
        super().__init__()
        self.body_color = SNAKE_COLOR
        self.reset()

    def reset(self):
        """Сбрасывает состояние змейки до начального (длина 1, центр экрана)."""
        self.length = 1
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.next_direction = None
        self.last = None

    def update_direction(self):
        """
        Обновляет направление движения на основе нажатой пользователем клавиши.
        Запрещает змейке мгновенно разворачиваться на 180 градусов.
        """
        if self.next_direction:
            # Проверяем, не является ли новое направление противоположным текущему
            if (self.direction[0] * -1, self.direction[1] * -1) != self.next_direction:
                self.direction = self.next_direction
            self.next_direction = None

    def get_head_position(self):
        """Возвращает координаты головы змейки."""
        return self.positions[0]

    def move(self):
        """
        Двигает змейку на одну клетку.
        Реализует прохождение сквозь стены и обработку столкновения с собой.
        """
        head_x, head_y = self.get_head_position()
        dir_x, dir_y = self.direction

        # Вычисляем новую голову с использованием остатка от деления (проход сквозь границы)
        new_head = (
            (head_x + (dir_x * GRID_SIZE)) % SCREEN_WIDTH,
            (head_y + (dir_y * GRID_SIZE)) % SCREEN_HEIGHT
        )

        # Столкновение с собственным телом (самоукус)
        if new_head in self.positions[2:]:
            self.reset()
            return

        # Добавляем новую голову
        self.positions.insert(0, new_head)

        # Если длина змейки не увеличилась (яблоко не съедено), удаляем хвост
        if len(self.positions) > self.length:
            self.last = self.positions.pop()
        else:
            self.last = None

    def draw(self, surface):
        """Отрисовывает все сегменты змейки и затирает её след."""
        for position in self.positions:
            rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.body_color, rect)
            pygame.draw.rect(surface, BORDER_COLOR, rect, 1)

        # Затирание следа (последнего удаленного сегмента)
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, BOARD_BACKGROUND_COLOR, last_rect)


def handle_keys(snake):
    """
    Обрабатывает события Pygame и нажатия клавиш.
    Устанавливает планируемое направление (next_direction) для змейки.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.next_direction = UP
            elif event.key == pygame.K_DOWN:
                snake.next_direction = DOWN
            elif event.key == pygame.K_LEFT:
                snake.next_direction = LEFT
            elif event.key == pygame.K_RIGHT:
                snake.next_direction = RIGHT
            # Закрытие игры на ESC (из списка рекомендаций)
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit


def main():
    """Основной игровой цикл."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Изгиб Питона")
    clock = pygame.time.Clock()

    snake = Snake()
    apple = Apple(snake.positions)

    # Изначально заливаем экран чёрным фоном
    screen.fill(BOARD_BACKGROUND_COLOR)

    while True:
        # Обработка пользовательского ввода
        handle_keys(snake)
        
        # Обновление состояния объектов
        snake.update_direction()
        snake.move()

        # Если змейка врезалась в себя, метод move() вызвал reset().
        # В таком случае очищаем весь экран, чтобы старое тело не "повисло" графически.
        if len(snake.positions) == 1 and snake.last is None:
            screen.fill(BOARD_BACKGROUND_COLOR)

        # Проверка, съела ли змейка яблоко
        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position(snake.positions)

        # Отрисовка
        snake.draw(screen)
        apple.draw(screen)

        # Обновление экрана
        pygame.display.update()
        # Ограничение частоты кадров
        clock.tick(10)
if __name__ == '__main__':
    main()