class Constants:

    # Game
    width = 1200
    height = 800
    name = "Genetic Algorithm - Bubble Arena"
    background_color = (20, 20, 20)
    border = 10
    frm_rate = 30

    # structure
    st_color = (255, 255, 255)
    st_proportion = 0.85

    # buttons
    btn_width = 120
    btn_height = 40
    btn_mod = 2

    btn_color = background_color
    btn_border_color = (204, 141, 53)
    btn_text_color = (204, 141, 53)
    btn_txt_size = 15
    btn_font = 'Courier New'

    ps_text = 'pause'
    ps_text2 = 'resume'
    ps_pos = (border + btn_height // 2, border + int(st_proportion * height))
    rst_text = 'new!'
    rst_pos = (border + btn_height // 2, height - border - btn_height)

    # text

    # bubbles
    quantity = 30
    q_bubble = 3
    default_hp = 100

    bbl1_radius = 10
    bbl1_speed = 12
    bbl1_color = (192, 192, 192)
    bbl1_species = 1

    bbl2_radius = 20
    bbl2_speed = 8
    bbl2_color = (130, 130, 130)
    bbl2_species = 2

    bbl3_radius = 50
    bbl3_speed = 3
    bbl3_color = (96, 96, 96)
    bbl3_species = 3

    # GA
