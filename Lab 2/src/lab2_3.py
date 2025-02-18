import cv2
import numpy as np
import sys
import imageio.v3 as cv2


class lab2_3:
    def __init__(self):
        pass

    def read_image(self, image_path):
        image = cv2.imread(image_path, mode='L')
        if image is None:
            print(f"Error: Could not read the image {image_path}")
            sys.exit(1)
        return np.float32(image)

    def save_image(self, image, output_path):
        image = self.scale_image(image)
        cv2.imwrite(output_path, np.uint8(image))
        print(f"Processed image saved to {output_path}")

    def scale_image(self, image):
        # Scaling
        min_val = np.min(image)
        max_val = np.max(image)

        if max_val == min_val:
            return np.zeros_like(image)

        scaled_image = (image - min_val) / (max_val - min_val) * 255
        return scaled_image

    def add_images(self, image1_path, image2_path, output_path):
        """ Addition """
        img1 = self.read_image(image1_path)
        img2 = self.read_image(image2_path)
        if img1.shape != img2.shape:
            raise ValueError("Error: The two images must have the same dimensions!")

        added_image = img1 + img2
        self.save_image(added_image, output_path)

    def subtract_images(self, image1_path, image2_path, output_path):
        """ Subtraction """
        img1 = self.read_image(image1_path)
        img2 = self.read_image(image2_path)
        if img1.shape != img2.shape:
            raise ValueError("Error: The two images must have the same dimensions!")

        subtracted_image = img1 - img2
        self.save_image(subtracted_image, output_path)

    def multiply_images(self, image1_path, image2_path, output_path):
        """ Multiplication between images"""
        img1 = self.read_image(image1_path)
        img2 = self.read_image(image2_path)
        if img1.shape != img2.shape:
            raise ValueError("Error: The two images must have the same dimensions!")
        
        multiplied_image = img1 * img2
        self.save_image(multiplied_image, output_path)

    def multiply_image_by_constant(self, image_path, output_path, constant):
        """ Multiplication with constant """
        img = self.read_image(image_path)

        multiplied_image = img * constant
        self.save_image(multiplied_image, output_path)

    def divide_images(self, image1_path, image2_path, output_path):
        """ Division """
        img1 = self.read_image(image1_path)
        img2 = self.read_image(image2_path)
        if img1.shape != img2.shape:
            raise ValueError("Error: The two images must have the same dimensions!")

        img2 = np.where(img2 == 0, 1e-5, img2) # Zero problem
        divided_image = img1 / img2
        self.save_image(divided_image, output_path)


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage:")
        print("For addition: python lab2_3.py add <image1> <image2> <output_image>")
        print("For subtraction: python lab2_3.py sub <image1> <image2> <output_image>")
        print("For multiplication: python lab2_3.py mul <image1> <image2> <output_image>")
        print("For multiplication by a constant: python lab2_3.py mulc <image> <output_image> <constant>")
        print("For division: python lab2_3.py div <image1> <image2> <output_image>")
        sys.exit(1)

    mode = sys.argv[1].lower()
    demo = lab2_3()

    if mode == "add":
        demo.add_images(sys.argv[2], sys.argv[3], sys.argv[4])
    elif mode == "sub":
        demo.subtract_images(sys.argv[2], sys.argv[3], sys.argv[4])
    elif mode == "mul":
        demo.multiply_images(sys.argv[2], sys.argv[3], sys.argv[4])
    elif mode == "mulc":
        if len(sys.argv) < 6:
            print("Error: Missing constant for multiplication.")
            sys.exit(1)
        constant = float(sys.argv[5])
        demo.multiply_image_by_constant(sys.argv[2], sys.argv[3], constant)
    elif mode == "div":
        demo.divide_images(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Invalid mode. Use 'add', 'sub', 'mul', 'mulc', or 'div'.")
