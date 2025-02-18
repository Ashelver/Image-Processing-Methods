import cv2
import numpy as np
import sys

class lab2_1():
    def __init__(self):
        pass

    def log_transform(self, image_path, output_path, c=1.0):
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            print("Error: Could not read the image.")
            return
        
        image = np.float32(image)
        log_image = c * np.log(1 + image)  # Apply log transformation
        log_image = np.uint8(np.clip(log_image, 0, 255))  # Restrict the pixel in [0,255]
        
        cv2.imwrite(output_path, log_image)
        print(f"Log transformed image saved to {output_path}")

    def power_law_transform(self, image_path, output_path, c=1.0, gamma=1.0):
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            print("Error: Could not read the image.")
            return
        
        image = np.float32(image)
        power_image = c * np.power(image, gamma)  # Apply power-law transformation
        power_image = np.uint8(np.clip(power_image, 0, 255))  # Restrict the pixel in [0,255]
        
        cv2.imwrite(output_path, power_image)
        print(f"Power-law transformed image saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage:")
        print("For log transform: python lab2_1.py log <input_image> <output_image> <c>")
        print("For power-law transform: python lab2_1.py power <input_image> <output_image> <c> <gamma>")
        sys.exit(1)
    
    mode = sys.argv[1].lower()
    input_image = sys.argv[2]
    output_image = sys.argv[3]
    
    demo = lab2_1()
    
    if mode == "log":
        c = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
        demo.log_transform(input_image, output_image, c)
    elif mode == "power":
        c = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
        gamma = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0
        demo.power_law_transform(input_image, output_image, c, gamma)
    else:
        print("Invalid mode. Use 'log' or 'power'.")
