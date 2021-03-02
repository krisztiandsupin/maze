import pygame
import Settings
from Color import Color

def text_display(screen, x, y, string, size, color = Color.black, background = Color.white, allign = 'center'):  # centered text display
    myfont = pygame.font.SysFont('cabria', size)
    text = myfont.render(string, True, color, background)

    if allign == 'center': #text display in center allignment
        textrect = text.get_rect()  #center of textbox
        textrect.centerx = x
        textrect.centery = y
        screen.blit(text, textrect)

    elif allign == 'left':
        text = myfont.render(string, True, color, background) #(x,y): upper left corner of textbox
        screen.blit(text, (x, y))

def text_box(x, y, string, size):
    myfont = pygame.font.SysFont('cabria', size)
    text = myfont.render(string, True, (0,0,0), (0,0,0))

    textrect = text.get_rect()  # center of textbox
    textrect.centerx = x
    textrect.centery = y

    return textrect

def update_delay(milisecond):
    pygame.display.flip()
    pygame.time.delay(milisecond)


def buttonpress_detect():
    RUNNING, PAUSE = 0, 1
    state = RUNNING
    while True:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    raise SystemExit

                elif e.key == pygame.K_SPACE:
                    Settings.keyboard_space_press = True

                elif e.key == pygame.K_LEFT:
                    Settings.keyboard_left_press = True

                elif e.key == pygame.K_RIGHT:
                    Settings.keyboard_right_press = True

                elif e.key == pygame.K_UP:
                    Settings.keyboard_up_press = True

                elif e.key == pygame.K_DOWN:
                    Settings.keyboard_down_press = True

                elif e.key == pygame.K_r:
                    Settings.keyboard_r_press = True

                elif e.key == pygame.K_BACKSPACE:
                    Settings.keyboard_back_press = True

                elif e.key == pygame.K_w:
                    Settings.keyboard_w_press = True

                elif e.key == pygame.K_s:
                    Settings.keyboard_s_press = True

                elif e.key == pygame.K_a:
                    Settings.keyboard_a_press = True

                elif e.key == pygame.K_d:
                    Settings.keyboard_d_press = True


            elif e.type == pygame.MOUSEBUTTONUP:
                Settings.mouse_click_position = pygame.mouse.get_pos()

        while state == PAUSE:
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit()
                        raise SystemExit
                    elif e.key == pygame.K_SPACE:
                        state = RUNNING
        break

def buttonpress_reset():
    Settings.keyboard_space_press = None
    Settings.keyboard_left_press = None
    Settings.keyboard_right_press = None
    Settings.keyboard_up_press = None
    Settings.keyboard_down_press = None
    Settings.keyboard_r_press = None
    Settings.keyboard_back_press = None
    Settings.keyboard_w_press = None
    Settings.keyboard_s_press = None
    Settings.keyboard_a_press = None
    Settings.keyboard_d_press = None

def mouse_reset():
    Settings.mouse_click_position = None