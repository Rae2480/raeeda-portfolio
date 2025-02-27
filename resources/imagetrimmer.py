from PIL import Image

def trim_transparency(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    bbox = img.getbbox()  # Get bounding box of non-transparent pixels
    if bbox:
        cropped_img = img.crop(bbox)
        cropped_img.save(output_path, format="PNG")

# Example usage
trim_transparency("input.png", "output.png")
