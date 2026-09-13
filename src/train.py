import nnlib_py as nn 
import numpy as np
from utils import get_image, visualize_image, index_to_coord
import pygame

correct_image_pixels, scale, image_width, image_height = get_image("../images/hello_world.png")

num_frequencies = 5 
frequencies = [2 ** i for i in range(num_frequencies)]
input_dim = 2 + 4 * num_frequencies
input_array = np.zeros((image_width * image_height, input_dim))
for q in range(image_height):
    for i in range(image_width):
        idx = q * image_width + i
        x = i / image_width
        y = q / image_height
        features = [x, y]
        for f in frequencies:
            features.append(np.sin(np.pi * f * x))
            features.append(np.cos(np.pi * f * x))
            features.append(np.sin(np.pi * f * y))
            features.append(np.cos(np.pi * f * y))
        input_array[idx] = features

hidden_size = 256
network = nn.Network(nn.Losses.mse)
network.add(nn.Layer(input_dim, hidden_size, nn.Activations().tanh, nn.WeightInitializers.xavier))
network.add(nn.Layer(hidden_size, hidden_size, nn.Activations().tanh, nn.WeightInitializers.xavier))
network.add(nn.Layer(hidden_size, hidden_size, nn.Activations().tanh, nn.WeightInitializers.xavier))
network.add(nn.Layer(hidden_size, hidden_size, nn.Activations().tanh, nn.WeightInitializers.xavier))
network.add(nn.Layer(hidden_size, 1, nn.Activations().sigmoid, nn.WeightInitializers.xavier))

correct_image_pixels_flat = correct_image_pixels.reshape(-1, 1)
pygame.init()
screen = pygame.display.set_mode((image_width * scale, image_height * scale))
pygame.display.set_caption("AI Image Reproducer")

prediction_array = np.empty((image_width, image_height))

batch_size = 64
num_samples = image_width * image_height

def run_training(epochs, start_lr):
    current_lr = start_lr
    running = True
    
    for epoch in range(epochs):
        if not running: 
            break
        indices = np.arange(num_samples)
        np.random.shuffle(indices)
        
        epoch_loss = 0
        counter = 0

        for start_idx in range(0, num_samples, batch_size):
            counter += 1
            if counter % 5 == 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: 
                        running = False
            batch_indices = indices[start_idx:start_idx + batch_size]
            batch_input = input_array[batch_indices]                  
            batch_target = correct_image_pixels_flat[batch_indices]   
            prediction = network.forward(batch_input)
            loss = network.loss_function(prediction, batch_target)
            epoch_loss += loss * len(batch_indices)
            network.backward(prediction, batch_target)
            network.update(current_lr)
        average_epoch_loss = epoch_loss / num_samples
        if running:
            full_prediction = network.forward(input_array) # Vorm: (num_samples, 1)
            visualize_prediction = full_prediction.reshape(image_height, image_width)
            visualize_image(image_width, image_height, scale, screen, visualize_prediction)
            print(f"Epoch {epoch} - Loss: {average_epoch_loss:.5f} - LR: {current_lr}")
        if network.screen:
            network.check_pygame_events()

    pygame.quit()


if __name__ == "__main__":
    run_training(5000000, 0.01)
