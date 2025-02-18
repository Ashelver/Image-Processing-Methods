import cv2
import numpy as np
import sys
import json

class lab3_1:
    def __init__(self, w1, w2, w3, w4, w5, w6, w7, w8, w9, scaling=False):
        """ 3x3 filter """
        self.kernel = np.array([[w1, w2, w3],
                                [w4, w5, w6],
                                [w7, w8, w9]], dtype=np.float32)
        self.scaling = scaling

    def apply_filter(self, image_path, output_path):
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            print("Error: Could not read the image.")
            return
        
        # Zero padding
        padded_image = np.pad(image, pad_width=1, mode='constant', constant_values=0)
        
        # Convolution
        filtered_image = np.zeros_like(image, dtype=np.float32)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                region = padded_image[i:i+3, j:j+3]
                filtered_image[i, j] = np.sum(region * self.kernel)
        
        # Scaling if required
        if self.scaling:
            filtered_image = filtered_image - filtered_image.min()  # Normalize to [0, max]
            filtered_image = (filtered_image / filtered_image.max()) * 255  # Scale to [0, 255]
            filtered_image = filtered_image.astype(np.uint8)

        # Clip values to ensure they are within [0, 255]
        filtered_image = np.uint8(np.clip(filtered_image, 0, 255))

        cv2.imwrite(output_path, filtered_image)
        print(f"Filtered image saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python lab3_1.py <config.json> <input_image> <output_image> [scaling=True|False]")
        sys.exit(1)

    config_file = sys.argv[1]
    input_image = sys.argv[2]
    output_image = sys.argv[3]
    scaling = bool(sys.argv[4]) if len(sys.argv) > 4 else False  # Default scaling to False

    # Json conf
    with open(config_file, 'r') as file:
        config = json.load(file)

    # Load the filter
    filter_values = config["filter"]
    flattened_values = [value for row in filter_values for value in row]

    demo = lab3_1(*flattened_values, scaling=scaling)
    demo.apply_filter(input_image, output_image)
