# AI Image Approximation

Train a neural network to learn and reproduce any image you give it. Not really a problem that had to be solved but perfect to learn how neural networks learn and to visualize the entire process.

---

<p align="center">
  <img src="https://github.com/user-attachments/assets/adcbf638-5120-4cca-a10c-0f7b1cb4213e" alt="Schermafbeelding 2026-09-13 114848" width="32%" />
  <img src="https://github.com/user-attachments/assets/b6e6aa48-d144-4c5a-b6e2-3bbc132c400f" alt="Schermafbeelding 2026-09-13 114942" width="32%" />
  <img src="https://github.com/user-attachments/assets/b954e19e-2342-49cf-984d-9eeea6eb3764" alt="Schermafbeelding 2026-09-13 120015" width="32%" />
</p>

## About the Project

This was written in python using [my very own neural network library](https://github.com/IAmDaanE/neural-network-library). The input to the neural network is the coordinate of the pixel on the image, the output is its approximation of the greyscale value of that pixel.

## Getting Started

### Getting the Source

This project is [hosted on GitHub](https://github.com/IAmDaanE/ai-image-approximation). You can download the zip or clone this project directly using this command:

```
git clone git@github.com:IAmDaanE/ai-image-approximation.git
```

### Running the Program

Requirements: You must have Python 3.9 - 3.13.
1. Clone the repository or download the zip and unpack it to your directory of choice.
2. Navigate to that directory in a terminal.
3. In a venv or the global python version install the needed libraries.
    ```
    pip install -r requirements.txt
    ```
4. Run the program.

    ```
    python src/train.py "images/hello_world.png" 
    ```

## License

This project is open-source and available under the MIT License.
