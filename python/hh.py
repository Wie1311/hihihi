import pygame
import sys
import random

# Khởi tạo Pygame
pygame.init()
pygame.mixer.init()

# Kích thước màn hình
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Hàm vẽ khung chứa chữ
def draw_text_box(text, font, color, x, y, width, height):
    pygame.draw.rect(screen, WHITE, (x, y, width, height))
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 2)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

# Tạo màn hình
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Math Heroes: Quest for Knowledge")

# Phông chữ
font = pygame.font.Font(None, 36)

# Tải hình nền và điều chỉnh kích thước
background = pygame.image.load("background2.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Tải nhân vật
character = pygame.image.load("character.png")
character = pygame.transform.scale(character, (50, 50))
character_width, character_height = character.get_size()

# Vị trí nhân vật
character_x = SCREEN_WIDTH // 6 - character_width // 2
character_y = 400 - character_height // 2
character_speed = 5

# Tọa độ nền
bg_x = 0

# Đồng hồ để điều khiển tốc độ khung hình
clock = pygame.time.Clock()
FPS = 60

# Vòng lặp trò chơi
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Nhận phím bấm
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if character_x > SCREEN_WIDTH // 4:
            character_x -= character_speed
        elif bg_x < 0:
            bg_x += character_speed
    if keys[pygame.K_RIGHT]:
        if character_x < 3 * SCREEN_WIDTH // 4 - character_width:
            character_x += character_speed
        elif bg_x > -SCREEN_WIDTH:
            bg_x -= character_speed

    # Vẽ nền (Đảm bảo nền luôn phủ hết màn hình)
    screen.blit(background, (bg_x % SCREEN_WIDTH, 0))
    if bg_x % SCREEN_WIDTH != 0:
        screen.blit(background, (bg_x % SCREEN_WIDTH - SCREEN_WIDTH, 0))
    
    # Vẽ nhân vật
    screen.blit(character, (character_x, character_y))

    # Cập nhật màn hình
    pygame.display.flip()
    clock.tick(FPS)

# Thoát Pygame
pygame.quit()
sys.exit()
