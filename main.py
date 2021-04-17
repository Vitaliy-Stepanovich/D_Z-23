import random
import sys
import pygame

# pyanimation
def main():
    pygame.init()  # Инициализация всех модулей

    WIDTH = 640
    HEIGHT = 400

    # BG_COLOR = (0, 0, 0)

    # Создаём экран
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Тир по бабочкам')
    bg = pygame.image.load('fon.jpeg')
    
    # Задаём FPS
    clock = pygame.time.Clock()

    # Задаём цвет прицела
    red = random.randint(70, 255)
    green = random.randint(70, 255)
    blue = random.randint(70, 255)
    linecolor = (red, green, blue)
    x_mouse_pos = 0
    y_mouse_pos = 0
    pygame.mouse.set_visible(False)
    size_scope = 20

    # Бабочки
    target_image = pygame.image.load('butterfly.png')
    
    target_rect = target_image.get_rect()  # Вписываем картинку в прямоугольник
    target_rect.x = random.randint(0, WIDTH - target_rect.w)
    target_rect.y = random.randint(0, HEIGHT - target_rect.h)
    
    target_rect1 = target_image.get_rect()  # Вписываем картинку в прямоугольник
    target_rect1.x = random.randint(0, WIDTH - target_rect.w)
    target_rect1.y = random.randint(0, HEIGHT - target_rect.h)
    
    target_rect2 = target_image.get_rect()  # Вписываем картинку в прямоугольник
    target_rect2.x = random.randint(0, WIDTH - target_rect.w)
    target_rect2.y = random.randint(0, HEIGHT - target_rect.h)
    
    # Звук выстрела
    shot_sound = pygame.mixer.Sound('weapons/ak47.wav')
    shot_sound.set_volume(0.5)

    # Музыка
    pygame.mixer.music.load('music/Highway_to_Hell.ogg')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # Надпись очков
    score = 0
    font_obj = pygame.font.Font('font/scootchover-sans.ttf', 24)
    font_color = (255, 255, 255)
    
    while True:
        # Обработчик событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                x_mouse_pos, y_mouse_pos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    shot = pygame.Rect(x_mouse_pos, y_mouse_pos, 1, 1)
                    if shot.colliderect(target_rect):
                        target_rect.x = random.randint(0, WIDTH - 78)
                        target_rect.y = random.randint(0, HEIGHT - 72)
                        score += 10
                        shot_sound.play()
                    elif shot.colliderect(target_rect1):
                        target_rect1.x = random.randint(0, WIDTH - 78)
                        target_rect1.y = random.randint(0, HEIGHT - 72)
                        score += 10
                        shot_sound.play()  
                    elif shot.colliderect(target_rect2):
                        target_rect2.x = random.randint(0, WIDTH - 78)
                        target_rect2.y = random.randint(0, HEIGHT - 72)
                        score += 10
                        shot_sound.play()     
                    else:
                      print('МИМО!')
                      score -= 10
   
        # Заливка фона
        surface.blit(bg, (0, 0))
        
        # Отображаем бабочки
        surface.blit(target_image, target_rect)
        surface.blit(target_image, target_rect1)
        surface.blit(target_image, target_rect2)
        
        
        # Горизонтальная линия
        pygame.draw.line(surface, linecolor, (x_mouse_pos - size_scope, y_mouse_pos), (x_mouse_pos + size_scope, y_mouse_pos), 3)
        # Вертикальная линия
        pygame.draw.line(surface, linecolor, (x_mouse_pos, y_mouse_pos - size_scope), (x_mouse_pos, y_mouse_pos + size_scope), 3)

        # Отображение надписи
        score_text = font_obj.render(f'Score: {score}', True, font_color)
        surface.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(30)  # Аналогия FPS (Frame Per Second)


if __name__ == '__main__':
    main()