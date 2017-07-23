from pygame import image


class Constants:

    # Game
    width = 800
    height = 600
    game_name = "Snake"
    game_icon = image.load("pictures/snake_icon.jpg")

    # UI
    ui_height = int(height * 0.2)
    ui_snake = image.load("pictures/snake_ui.png")
    ui_background = image.load("pictures/ui.png")

    # lose screen
    lose_screen = image.load("pictures/you_suck.png")

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    dark_grey = (32, 32, 32)
    grey = (64, 64, 64)
    light_grey = (164, 164, 164)

    # movement
    speed = 20
    dir = (0, -1)

    # segments
    length = 20
    addition_rate = 1
    segment_color = dark_grey

    # food
    food_color = red

    # grid
    grid_color = light_grey
