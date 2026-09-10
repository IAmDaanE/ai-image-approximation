def rgb_gradient(base_rgb, top_rgb, percentage):
    base_red = base_rgb[0]
    base_green = base_rgb[1]
    base_blue = base_rgb[2]

    top_red = base_rgb[0]
    top_green = base_rgb[1]
    top_blue = base_rgb[2]

    red_jump = (top_red - base_red) / 100
    green_jump = (top_red - base_red) / 100
    blue_jump = (top_red - base_red) / 100

    return (red)