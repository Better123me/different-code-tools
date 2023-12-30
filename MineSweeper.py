import pygame
import random
import sys

# 初始化 Pygame
pygame.init()

width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('MyMineSweeper')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
RED = (255, 0, 0)

grid_size = 20
cols, rows = 20, 20
mine_count = 40

def create_board():
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    mines_placed = 0

    while mines_placed < mine_count:
        x, y = random.randint(0, cols - 1), random.randint(0, rows - 1)
        if board[y][x] == 0:
            board[y][x] = -1
            mines_placed += 1

            # 更新周围的数字
            for i in range(-1, 2):
                for j in range(-1, 2):
                    nx, ny = x + i, y + j
                    if 0 <= nx < cols and 0 <= ny < rows and board[ny][nx] != -1:
                        board[ny][nx] += 1
    return board

# 绘制游戏板
def draw_board(board, revealed):
    for y in range(rows):
        for x in range(cols):
            rect = pygame.Rect(x*grid_size, y*grid_size, grid_size, grid_size)
            if revealed[y][x]:
                if board[y][x] == -1:
                    pygame.draw.rect(screen, RED, rect)
                    font = pygame.font.Font(None, 24)
                    text = font.render("Bomb", True, BLACK)
                    text_rect = text.get_rect(center=rect.center)
                    screen.blit(text, text_rect)
                else:
                    pygame.draw.rect(screen, WHITE, rect)
                    if board[y][x] > 0:
                        font = pygame.font.Font(None, 24)
                        text = font.render(str(board[y][x]), True, BLACK)
                        text_rect = text.get_rect(center=rect.center)
                        screen.blit(text, text_rect)
            else:
                pygame.draw.rect(screen, GRAY, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

# 弹出触雷窗口
def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render("Boom!!!You failed", True, BLACK)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    sys.exit()

# 主函数
def main():
    board = create_board()
    revealed = [[False for _ in range(cols)] for _ in range(rows)]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x //= grid_size
                y //= grid_size
                revealed[y][x] = True
                if board[y][x] == -1:
                    game_over()

        screen.fill(BLACK)
        draw_board(board, revealed)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
