import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt


class lab2_2():
    def __init__(self):
        pass

    def compute_histogram(self, image):
        # Calculate the histogram
        histogram = np.zeros(256, dtype=int)
        for pixel in image.ravel():
            histogram[int(pixel)] += 1
        return histogram
    
    def compute_cdf(self, histogram):
        # Calculate Cumulative Distribution Function
        cdf = np.cumsum(histogram)
        cdf_normalized = cdf / cdf.max() # Nomorlation
        return cdf, cdf_normalized
    
    def apply_hist_eq(self, image):
        histogram = self.compute_histogram(image)
        cdf, cdf_normalized = self.compute_cdf(histogram)
        L = 256 

        transform_function = (L - 1) * cdf_normalized
        # APPLY transform function
        image_eq = np.interp(image.flatten(), np.arange(0, L), cdf_normalized * (L - 1))
        image_eq = np.clip(image_eq, 0, 255).astype(np.uint8)
        return image_eq.reshape(image.shape), transform_function

    def plot_histogram(self, histogram, title='Histogram'):
        # Plot the histogram
        plt.figure(figsize=(10, 6))
        plt.bar(range(256), histogram, width=1, color='blue')
        plt.title(title)
        plt.xlabel('Pixel Intensity')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()

    def plot_transformation_function(self, transform_function):
        plt.figure(figsize=(10, 6))
        plt.plot(range(256), transform_function, color='black')
        plt.title('Histogram Equalization Transformation Function')
        plt.xlabel('Input Pixel Intensity (r)')
        plt.ylabel('Output Pixel Intensity (T(r))')
        plt.grid(True)
        plt.show()


    def save_image(self, image, output_path):
        # Save Images
        cv2.imwrite(output_path, image)
        print(f"Image saved to {output_path}")


    def process_image(self, image_path, output_path):
        # REad the image
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            print("Error: Could not read the image.")
            return

        # Plot original histogram
        histogram = self.compute_histogram(image)
        self.plot_histogram(histogram, 'Original Histogram')

        # Apply equalization
        equalized_image, transform_function = self.apply_hist_eq(image)

        # Plot transformation function
        self.plot_transformation_function(transform_function)


        # Plot equalized histogram
        equalized_histogram = self.compute_histogram(equalized_image)
        self.plot_histogram(equalized_histogram, 'Equalized Histogram')

        # Save the equalized image
        self.save_image(equalized_image, output_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("For histogram equalization: python lab2_2.py <input_image> <output_image>")
        sys.exit(1)
    
    input_image = sys.argv[1]
    output_image = sys.argv[2]
    
    demo = lab2_2()
    demo.process_image(input_image, output_image)