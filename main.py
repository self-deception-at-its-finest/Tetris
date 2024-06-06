import sys
import pygame
import pygame_menu
from game import Game
from colours import Colours


pygame.init()

titlefont = pygame.font.Font(None,40)
score_surface = titlefont.render('Score:', True, Colours.dark_grey)
next_fig_surface = titlefont.render('Next:', True, Colours.dark_grey)
gameover_sign = titlefont.render('GAME OVER',True, Colours.col5)
pause_sign = titlefont.render('Paused',True, Colours.dark_grey)
screen = pygame.display.set_mode((520, 630))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()
game = Game()

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
gamefps = pygame.USEREVENT
pygame.time.set_timer(gamefps, 200)
controls_bg = pygame.image.load('controls_bg.png').convert_alpha()
background = pygame.image.load('bg.jpg').convert_alpha()
Wooden_Sign = pygame.image.load('Wooden_Sign_Hanging.png').convert_alpha()
next_fig_sign = pygame.image.load('next_fig.png').convert_alpha()


def back_to_menu():
    while True:
        screen.blit(background, (0, 0))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
        if menu.is_enabled():
            menu.update(events)
            menu.draw(screen)
        pygame.display.update()


def controls():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    back_to_menu()
        screen.blit(background, (0, 0))
        screen.blit(controls_bg,(15,60))
        pygame.display.update()
        clock.tick(120)
        screen.blit(controls_bg,(10,10))


def new_game():
    game.reset()
    start_the_game()


def start_the_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and game.gameover == True:
                    game.gameover = False
                    game.reset()
                if event.key == pygame.K_LEFT and game.gameover == False:
                    game.move_left()
                if event.key == pygame.K_RIGHT and game.gameover == False:
                    game.move_right()
                if event.key == pygame.K_DOWN and game.gameover == False:
                    game.move_down()
                if event.key == pygame.K_UP and game.gameover == False:
                    game.rotate()
                if event.key == pygame.K_BACKSPACE and game.gameover == False:
                    game.pause()
                if event.key == pygame.K_ESCAPE:
                    back_to_menu()
            if event.type == gamefps and game.gameover == False:
                game.move_down()
        score_value_surface = titlefont.render(str(game.score), True, Colours.dark_grey)
        screen.blit(background, (0, 0))
        screen.blit(Wooden_Sign, (10, 1))
        screen.blit(next_fig_sign, (-40, 120))
        screen.blit(score_surface, (40, 50, 60, 40))
        screen.blit(next_fig_surface, (70, 170, 60, 40))
        screen.blit(score_value_surface, (130, 50, 60, 40))
        if game.gameover == True:
            screen.blit(Wooden_Sign, (10, 1))
            screen.blit(gameover_sign, (20, 50, 130, 150))
        game.draw(screen)
        pygame.display.update()
        clock.tick(120)


main_theme = pygame_menu.themes.THEME_GREEN.copy()
main_theme.set_background_color_opacity(0.0)
menu = pygame_menu.Menu('Tetris', 300, 300, theme=main_theme)


menu.add.button('Play', start_the_game)
menu.add.button('New Game', new_game)
menu.add.button('Controls', controls)
menu.add.button('Quit', pygame_menu.events.EXIT)


back_to_menu()