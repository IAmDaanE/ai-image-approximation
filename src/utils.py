import numpy
from PIL import Image
import math
import pygame

def inferno_colormap(percentage):
    p = max(0.0, min(1.0, percentage))
    p = 1 - p
    anchors = [
        (0, 0, 4),        # 0%   Very dark blue/black
        (22, 11, 57),     # 10%
        (65, 9, 103),     # 20%
        (106, 23, 110),   # 30%
        (147, 37, 103),   # 40%
        (187, 55, 84),    # 50%
        (220, 80, 57),    # 60%
        (243, 119, 25),   # 70%
        (251, 164, 10),   # 80%
        (245, 215, 69),   # 90%
        (252, 254, 164)   # 100% Bright yellow-orange
    ]
    idx_float = p * (len(anchors) - 1)
    idx_low = int(idx_float)
    idx_high = min(idx_low + 1, len(anchors) - 1)
    weight = idx_float - idx_low
    r = int(anchors[idx_low][0] * (1 - weight) + anchors[idx_high][0] * weight)
    g = int(anchors[idx_low][1] * (1 - weight) + anchors[idx_high][1] * weight)
    b = int(anchors[idx_low][2] * (1 - weight) + anchors[idx_high][2] * weight)
    return (r, g, b)

def get_image(image_path):
    img = Image.open(image_path)
    grey_img = img.convert('L')
    pixel_array_3d = numpy.array(grey_img)
    pixel_array = pixel_array_3d.flatten() / 255
    img_width, img_height = img.size
    scale = 1
    while img_width * (scale + 1) < 900 and img_height * (scale + 1) < 700:
        scale += 1
    return pixel_array, scale, img_width, img_height

def visualize_image(img_width, img_height, scale, screen, prediction_array):
    screen.fill((0,0,0))
    for i in range(img_width):
        for q in range(img_height):
            pred = prediction_array[q][i].item()
            color = inferno_colormap(pred)
            pygame.draw.rect(screen, color, (scale * i, scale * q, scale, scale))
    pygame.event.pump()
    pygame.display.flip()

def index_to_coord(number_input, image_width, image_height):
    y = math.floor(number_input / image_width)
    x = number_input - y * image_width
    return x, y