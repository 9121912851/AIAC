from PIL import Image

def compress_image(input_path, output_path, quality=30):
    with Image.open(input_path) as img:
        if img.mode == 'RGBA':
            img = img.convert('RGB')  # Remove alpha channel
        img.save(output_path, "JPEG", optimize=True, quality=quality)

# Example usage
compress_image("original.png", "compressed.jpg", quality=25)