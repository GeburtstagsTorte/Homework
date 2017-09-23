from Button import Button as Btn


class Constants:
    width = 800
    height = 600
    name = "Fang den Ball!"

    ball_color = (0, 0, 255)
    ball_radius = 20
    time = 120
    time_factor = 0.90
    lives = 10
    ui_color = (0, 0, 0)
    ui_py = 100
    ui_height = height - ui_py

    font = "impact"
    font_size = 20
    font_lost_size = 40
    score_pos = (10, height - ui_py + 10)
    lives_pos = (10, height - ui_py + int(font_size*2))
    lost_pos = (width//2, height//2 - font_lost_size)
    text_color = ui_color
    
    btn_width = 120
    btn_height = 40
    btn_pos = (width//2 - btn_width//2, height//2 - btn_height//2 + 20)
    btn_color = ball_color
    btn_text = "Restart!"
    btn_txt_color = (255, 255, 255)
    btn_font = font
    btn_font_size = 20
    
    @staticmethod
    def initialize_restart_button(surface):
        return Btn(surface, Constants.btn_pos, Constants.btn_width,
                   Constants.btn_height, Constants.btn_color,
                   Constants.btn_text, text_size=Constants.btn_font_size,
                   text_color=Constants.btn_txt_color,
                   font=Constants.btn_font, mod=2, extend=True)
