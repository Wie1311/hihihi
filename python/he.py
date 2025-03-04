import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Tạo màn hình hiển thị
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Giới thiệu trò chơi")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED_BROWN = (139, 0, 0)
# Phông chữ
font1 = pygame.font.Font("P2.otf", 50)
font2 = pygame.font.Font("P1.ttf", 30)

# Nội dung giới thiệu
title_text = font1.render("Welcome to my world!", True, BLACK)

# Tải âm thanh
pygame.mixer.music.load("background_music.mp3")
# Chạy âm thanh nền
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.3)  # Giảm âm lượng nền

# Hiệu ứng động
title_alpha = 0
fade_in = True
clock = pygame.time.Clock()

# Tải hình ảnh nút "Start" với hai trạng thái
start_button_default = pygame.image.load("start1.png")
start_button_pressed = pygame.image.load("start2.jpg")
background_image = pygame.image.load("ani1.jpg")
background_image = pygame.transform.scale(background_image, (800, 600))

# Điều chỉnh kích thước nút
new_width, new_height = 200, 100
start_button_default = pygame.transform.scale(start_button_default, (new_width, new_height))
start_button_pressed = pygame.transform.scale(start_button_pressed, (new_width, new_height))

# Lấy vị trí của nút
start_button_rect = start_button_default.get_rect(center=(400, 300))
is_button_pressed = False


def intro_screen():
    """Màn hình giới thiệu với hiệu ứng mờ dần."""
    global title_alpha, fade_in, is_button_pressed
    running = True
    while running:
        screen.fill(WHITE)

        # Kiểm tra sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    is_button_pressed = True
            if event.type == pygame.MOUSEBUTTONUP:
                if start_button_rect.collidepoint(event.pos):
                    is_button_pressed = False
                    running = False

        # Hiệu ứng mờ dần cho tiêu đề
        if fade_in:
            title_alpha += 5
            if title_alpha >= 255:
                title_alpha = 255
                fade_in = False

        # Vẽ tiêu đề
        title_surface = title_text.copy()
        title_surface.set_alpha(title_alpha)
        screen.blit(title_surface, (400 - title_surface.get_width() // 2, 200))

        # Hiển thị nút "Start"
        if is_button_pressed:
            screen.blit(start_button_pressed, start_button_rect.topleft)
        else:
            screen.blit(start_button_default, start_button_rect.topleft)

        pygame.display.flip()
        clock.tick(60)


def type_text_lines_with_background(lines, font, color, x, y, background, line_spacing=10, delay=50):
    """Hiển thị từng dòng văn bản với hiệu ứng tự đánh chữ và giữ lại các dòng trước."""
    displayed_lines = []
    for line in lines:
        displayed_text = ""
        while len(displayed_text) < len(line):
            displayed_text += line[len(displayed_text)]
            screen.blit(background, (0, 0))  # Hiển thị ảnh nền
            draw_text_lines(screen, displayed_lines, font, color, x, y, line_spacing)
            draw_text_lines(screen, [displayed_text], font, color, x, y + len(displayed_lines) * (font.get_height() + line_spacing), line_spacing)
            pygame.display.flip()
            pygame.time.delay(delay)
        displayed_lines.append(line)


def draw_text_lines(surface, lines, font, color, x, y, line_spacing):
    """Hiển thị các dòng văn bản cách nhau khoảng cách cố định."""
    for i, line in enumerate(lines):
        line_surface = font.render(line, True, color)
        surface.blit(line_surface, (x, y + i * (font.get_height() + line_spacing)))


# Chạy màn hình giới thiệu
intro_screen()

# Hiển thị màn hình chính
screen.blit(background_image, (0, 0))  # Hiển thị hình nền
text_lines = [
    "   Once upon a time, there was a wicked dragon",
    "that kidnapped a princess. From that moment, a",
    "heroic young man emerged overcoming many",
    "obstaclesto rescue the princess.",
]
type_text_lines_with_background(text_lines, font2, RED_BROWN, 120, 150, background_image, line_spacing=10, delay=50)

# Logic trò chơi chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
