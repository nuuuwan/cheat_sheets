# Python - Pillow

## 1. **Install Pillow**

```bash
pip install Pillow
```

## 2. **Import the Library**

```python
from PIL import Image, ImageFilter, ImageDraw, ImageFont
```

## 3. **Open an Image**

```python
img = Image.open("image.jpg")
```

## 4. **Save an Image**

```python
img.save("new_image.jpg")
```

## 5. **Display an Image**

```python
img.show()
```

## 6. **Resize an Image**

```python
resized_img = img.resize((200, 300))  # Width, Height in pixels
```

## 7. **Rotate an Image**

```python
rotated_img = img.rotate(90)  # Rotate 90 degrees
```

## 8. **Crop an Image**

```python
cropped_img = img.crop((left, top, right, bottom))  # Define box coordinates
```

## 9. **Convert Image Mode (e.g., Grayscale)**

```python
gray_img = img.convert("L")  # "L" mode for grayscale
```

## 10. **Apply a Filter (e.g., Blur)**

```python
blurred_img = img.filter(ImageFilter.BLUR)
```

## 11. **Draw on an Image**

```python
draw = ImageDraw.Draw(img)
draw.rectangle([(50, 50), (150, 150)], outline="red", width=5)  # Draw rectangle
```

## 12. **Add Text to an Image**

```python
font = ImageFont.truetype("arial.ttf", 36)  # Load font
draw.text((100, 100), "Hello, World!", font=font, fill="white")
```

## 13. **Merge/Composite Two Images**

```python
img1 = Image.open("img1.jpg")
img2 = Image.open("img2.jpg")
blended_img = Image.blend(img1, img2, alpha=0.5)
```

## 14. **Change Image Transparency (Alpha)**

```python
img = img.convert("RGBA")
transparent_img = img.putalpha(128)  # Set alpha to 128 (range 0-255)
```

## 15. **Thumbnail an Image (Maintain Aspect Ratio)**

```python
img.thumbnail((200, 200))  # Max size (width, height), aspect ratio is kept
```

## 16. **Image Format Conversion**

```python
img = Image.open("image.png")
img.save("image_converted.jpg", "JPEG")  # Convert to JPEG
```

## 17. **Get Image Size**

```python
width, height = img.size
```

## 18. **Get Pixel Data (RGB)**

```python
pixel = img.getpixel((50, 50))  # Get pixel color at x=50, y=50
```

## 19. **Paste an Image onto Another**

```python
img.paste(img2, (100, 100))  # Paste img2 at position (100, 100) on img
```

## 20. **Adjust Brightness**

```python
from PIL import ImageEnhance
enhancer = ImageEnhance.Brightness(img)
bright_img = enhancer.enhance(1.5)  # 1.5x brighter
```

## 21. **Flip Image Horizontally**

```python
flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
```

## 22. **Flip Image Vertically**

```python
flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
```

## 23. **Transpose Image (Rotate & Flip Together)**

```python
transposed_img = img.transpose(Image.ROTATE_90)  # Rotate 90 degrees counterclockwise
```

## 24. **Convert Image to Binary (Black & White)**

```python
binary_img = img.convert("1")  # Converts to 1-bit pixels
```

## 25. **Add a Border to an Image**

```python
from PIL import ImageOps
bordered_img = ImageOps.expand(img, border=10, fill="black")  # Add 10px black border
```

## 26. **Create an Image from Scratch (Blank Image)**

```python
new_img = Image.new("RGB", (400, 400), color="white")  # Create blank white image
```

## 27. **Change Image DPI**

```python
img.save("high_dpi_image.jpg", dpi=(300, 300))  # Save with 300 DPI
```

## 28. **Adjust Contrast**

```python
enhancer = ImageEnhance.Contrast(img)
contrast_img = enhancer.enhance(2.0)  # Increase contrast
```

## 29. **Adjust Sharpness**

```python
enhancer = ImageEnhance.Sharpness(img)
sharp_img = enhancer.enhance(2.0)  # Sharpen the image
```

## 30. **Adjust Image Color**

```python
enhancer = ImageEnhance.Color(img)
colorful_img = enhancer.enhance(2.0)  # Enhance color intensity
```

## 31. **Apply Gaussian Blur**

```python
blurred_img = img.filter(ImageFilter.GaussianBlur(radius=5))  # 5-pixel radius blur
```

## 32. **Edge Detection**

```python
edge_img = img.filter(ImageFilter.FIND_EDGES)  # Detect edges in the image
```

## 33. **Emboss Effect**

```python
embossed_img = img.filter(ImageFilter.EMBOSS)
```

## 34. **Apply Contour Effect**

```python
contour_img = img.filter(ImageFilter.CONTOUR)
```

## 35. **Image Inversion (Negative)**

```python
from PIL import ImageOps
inverted_img = ImageOps.invert(img.convert("RGB"))  # Invert colors
```

## 36. **Add Drop Shadow**

```python
shadow = ImageOps.expand(img, border=10, fill="black")  # Add black shadow-like border
```

## 37. **Round Image Corners**

```python
mask = Image.new("L", img.size, 0)
draw = ImageDraw.Draw(mask)
draw.rounded_rectangle([0, 0, *img.size], radius=30, fill=255)
rounded_img = Image.composite(img, Image.new("RGBA", img.size), mask)
```

## 38. **Get Image Histogram (Pixel Intensity Distribution)**

```python
histogram = img.histogram()  # Get the histogram of the image
```

## 39. **Overlay Text with Transparency**

```python
text_img = Image.new("RGBA", img.size, (255, 255, 255, 0))  # Transparent image
draw = ImageDraw.Draw(text_img)
draw.text((50, 50), "Transparent Text", fill=(255, 0, 0, 128))  # Semi-transparent red
overlay_img = Image.alpha_composite(img.convert("RGBA"), text_img)
```

## 40. **Apply Sepia Tone Effect**

```python
sepia_img = ImageOps.colorize(img.convert("L"), black="#704214", white="#C0C0C0")  # Apply sepia
```

## 41. **Convert Image to ASCII Art (Simple Example)**

```python
import numpy as np
char_map = "@%#*+=-:. "
img = img.convert("L").resize((100, 50))  # Resize and convert to grayscale
pixels = np.array(img)
ascii_art = "\n".join("".join(char_map[pixel // 32] for pixel in row) for row in pixels)
print(ascii_art)
```

## 42. **Create a Gradient Background**

```python
width, height = 400, 400
gradient_img = Image.new("RGB", (width, height))
for i in range(height):
    r = int(255 * (i / height))
    for j in range(width):
        gradient_img.putpixel((j, i), (r, 0, 0))  # Gradient from black to red
```

## 43. **Watermark an Image**

```python
watermark = Image.open("watermark.png").resize((100, 50))  # Resize watermark
img.paste(watermark, (50, 50), watermark)  # Paste with transparency
```

## 44. **Masking an Image (Circular Mask Example)**

```python
mask = Image.new("L", img.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((50, 50, 300, 300), fill=255)  # Circle mask
masked_img = Image.composite(img, Image.new("RGBA", img.size), mask)
```

## 45. **Tile an Image**

```python
tile_img = Image.new("RGB", (800, 800))
for i in range(0, 800, img.width):
    for j in range(0, 800, img.height):
        tile_img.paste(img, (i, j))  # Paste image in a tile pattern
```

## 46. **Convert Image to NumPy Array**

```python
import numpy as np
img_array = np.array(img)
```

## 47. **Convert NumPy Array to Image**

```python
new_img = Image.fromarray(img_array)
```

## 48. **Find Image Difference**

```python
img1 = Image.open("image1.jpg")
img2 = Image.open("image2.jpg")
diff_img = ImageChops.difference(img1, img2)
```

## 49. **Add Noise to an Image**

```python
noisy_img = img.copy()
import numpy as np
noise = np.random.randint(0, 50, img.size, dtype=np.uint8)  # Generate random noise
noisy_img = Image.fromarray(np.array(noisy_img) + noise.reshape(noisy_img.size[1], noisy_img.size[0], 3))
```

## 50. **Draw a Polygon**

```python
draw = ImageDraw.Draw(img)
draw.polygon([(100, 100), (150, 200), (200, 100)], outline="blue", fill="yellow")
```
