class C:

    # Game
    width = 1200
    height = 800
    background_color = (20, 20, 20)

    # GA
    max_population = 20
    mutation_rate = 20
    GA_path_color = (150, 0, 200)

    bf_color = (204, 141, 53)
    # structure
    structure_color = (255, 255, 255)
    st_width = 1

    # Cities/dots
    city_amount = 5
    city_radius = 6
    city_color = (255, 255, 255)
    border = 5

    # Route
    route_color = (255, 255, 255)
    route_width = 3

    # Text
    size = 15
    head_size = 19
    font = 'Courier New'
    text_color = (255, 255, 255)
    text_pos = (10, 10)
    stats_pos = (10, 30)

    txt_head1 = "Brute Force Method"
    txt_head2 = "Genetic Algorithm"
    txt_head1_pos = (int(0.75*width) + border, border)
    txt_head2_pos = (int(0.75*width) + border, border + int(0.5*height))
    txt_text_bf_pos = (txt_head1_pos[0], head_size + 4*border)
    txt_text_ga_pos = (txt_head2_pos[0], 4*border + int(0.5*height) + head_size)

    # button
    btn_width = 120
    btn_height = 40
    btn_pos = (int(0.75*width) + border + btn_height // 2, height - border - btn_height)
    btn_color = background_color
    btn_border_color = (204, 141, 53)
    btn_text_color = (204, 141, 53)
    btn_txt_size = 15

    rb_text = "new!"
