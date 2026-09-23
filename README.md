# AI Image Approximation

Train a neural network to learn and reproduce any image you give it. Not really a problem that had to be solved but perfect to learn how neural networks learn and to visualize the entire process.

---

<p align="center">
  <img src="https://github.com/user-attachments/assets/adcbf638-5120-4cca-a10c-0f7b1cb4213e" alt="Schermafbeelding 2026-09-13 114848" width="32%" />
  <img src="https://github.com/user-attachments/assets/b6e6aa48-d144-4c5a-b6e2-3bbc132c400f" alt="Schermafbeelding 2026-09-13 114942" width="32%" />
  <img src="https://github.com/user-attachments/assets/b954e19e-2342-49cf-984d-9eeea6eb3764" alt="Schermafbeelding 2026-09-13 120015" width="32%" />
</p>

## About the Project

This was written in python using [my very own machine learning library](https://github.com/IAmDaanE/bare-bones-ml). The input to the neural network is the coordinate of the pixel on the image, the output is its approximation of the greyscale value of that pixel.

## Getting Started

**Requires:** Python 3.10 - 3.14
1. Install the required libraries, preferably in a venv.

    ```
    pip install -r requirements.txt
    ```
2. Run the program, replace the string with the path to the image you want to train on.

    ```
    python src/train.py "../images/hello_world.png"
    ```

## License

This project is open-source and available under the MIT License.
