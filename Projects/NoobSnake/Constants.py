from pygame import image


class Constants:

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    dark_grey = (32, 32, 32)
    grey = (64, 64, 64)
    light_grey = (164, 164, 164)

    # Game

    width = 800
    height = 600
    game_name = "NoobSnake"
    background_color = white
    game_icon = image.load("pictures/snake_icon.jpg")

    player_name = "player 1"

    # UI
    ui_height = int(height * 0.2)
    ui_snake = image.load("pictures/snake_ui.png")
    ui_background = image.load("pictures/ui.png")

    # lose screen
    lose_screen = image.load("pictures/you_suck.png")

    # movement
    magnitude = 20
    speed = magnitude
    dir = (0, -1)

    # segments
    length = 20
    addition_rate = 1
    segment_color = dark_grey

    # food
    food_color = red

    # grid
    grid_color = light_grey

    # score
    score_text = 'Score: '
    score_font = 'impact'
    score_size = 35
    score_color = black
    score_pos = (50, height - ui_height + score_size)

    # menu
    menu_font = 'impact'
    menu_size = 50
    menu_text = game_name + " - Menu"
    menu_color = black
    menu_height = int(height * 0.2)

    # buttons
    btn_menu_width = 200
    btn_menu_height = 50

    btn_width = 120
    btn_height = 40

    btn_color = (34, 177, 76)
    btn_font_color = white
    btn_font = 'impact'
    btn_size = 20

    btn_restart_txt = "Try again!"
    btn_pause_txt = "Pause"
    btn_pause_txt2 = "Resume"
    btn_settings_txt = "Settings"
    btn_exit_txt = "Exit"
    btn_scores_txt = "Highscores"
    btn_start_txt = "Start!"

    btn_restart_pos = (width - btn_width - btn_height, height - ui_height + 15)
    btn_pause_pos = (width - btn_width - btn_height, height - btn_height - 15)

    x_pos = (width - btn_menu_width) // 2

    btn_start_pos = (x_pos, menu_height + menu_size)
    btn_scores_pos = (x_pos, menu_height + menu_size + btn_menu_height + 20)
    btn_settings_pos = (x_pos, menu_height + menu_size + 2*btn_menu_height + 2*20)
    btn_exit_pos = (x_pos, menu_height + menu_size + 3*btn_menu_height + 3*20)


