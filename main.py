import pygame
import random

pygame.init()
clock = pygame.time.Clock()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slot machine")

running = True
spinning = False
spin_duration = 800

symbols = ["CH", "LE", "OR", "BAR", "7", "$", "*", "DI", "BE"]

font = pygame.font.Font(None, 100)

symbol = font.render("7", True, (0, 0, 0))
symbol2 = font.render("7", True, (0, 0, 0))
symbol3 = font.render("7", True, (0, 0, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos) and not spinning:
                spinning = True
                spin_start = pygame.time.get_ticks()

                result1 = random.choice(symbols)
                result2 = random.choice(symbols)
                result3 = random.choice(symbols)

    # symbol list

    if spinning:
        symbol = font.render(random.choice(symbols), True, (0, 0, 0))
        symbol2 = font.render(random.choice(symbols), True, (0, 0, 0))
        symbol3 = font.render(random.choice(symbols), True, (0, 0, 0))

    if spinning and pygame.time.get_ticks() - spin_start >= spin_duration:
        spinning = False
        symbol = font.render(result1, True, (0, 0, 0))
        symbol2 = font.render(result2, True, (0, 0, 0))
        symbol3 = font.render(result3, True, (0, 0, 0))

    # simbol windows
    screen.fill((30, 30, 30))
    button_rect = pygame.Rect(300, 450, 200, 70)

    pygame.draw.rect(screen, (255, 255, 255), (120, 180, 160, 200), border_radius=15)
    pygame.draw.rect(screen, (255, 255, 255), (320, 180, 160, 200), border_radius=15)
    pygame.draw.rect(screen, (255, 255, 255), (520, 180, 160, 200), border_radius=15)

    # button window
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (220, 110, 40), button_rect, border_radius=8)
    else:
        pygame.draw.rect(screen, (180, 80, 30), button_rect, border_radius=8)

    button_text = font.render("SPIN", True, (255, 255, 255))

    button_x = 300 + (200 - button_text.get_width()) // 2
    button_y = 450 + (70 - button_text.get_height()) // 2
    screen.blit(button_text, (button_x, button_y))

    # symbol print
    x = 120 + (160 - symbol.get_width()) // 2
    y = 180 + (200 - symbol.get_height()) // 2
    screen.blit(symbol, (x, y))

    x2 = 320 + (160 - symbol2.get_width()) // 2
    y2 = 180 + (200 - symbol2.get_height()) // 2
    screen.blit(symbol2, (x2, y2))

    x3 = 520 + (160 - symbol3.get_width()) // 2
    y3 = 180 + (200 - symbol3.get_height()) // 2
    screen.blit(symbol3, (x3, y3))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
