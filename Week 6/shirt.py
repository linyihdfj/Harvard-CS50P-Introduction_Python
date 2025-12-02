import sys
import os
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    input_name, input_ext = os.path.splitext(input_path)
    output_name, output_ext = os.path.splitext(output_path)
    
    valid_extensions = [".jpg", ".jpeg", ".png"]
    
    if input_ext.lower() not in valid_extensions:
        sys.exit("Invalid input")
    if output_ext.lower() not in valid_extensions:
        sys.exit("Invalid output")
    
    if input_ext.lower() != output_ext.lower():
        sys.exit("Input and output have different extensions")
    
    try:
        input_image = Image.open(input_path)
    except FileNotFoundError:
        sys.exit("Input does not exist")
    
    shirt = Image.open("shirt.png")
    
    size = shirt.size
    
    input_image = ImageOps.fit(input_image, size)
    
    input_image.paste(shirt, shirt)
    
    input_image.save(output_path)


if __name__ == "__main__":
    main()
