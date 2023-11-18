from PIL import Image
import random


class Masks:
    def pixel_operation(self, pixel):
        raise NotImplementedError()

    def pixel_apply(self, img: Image.Image) -> Image.Image:
        for x in range(img.width):
            for y in range(img.height):
                new_pixel = self.pixel_operation(img.getpixel((x, y)))
                img.putpixel((x, y), new_pixel)
        return img


class Inversion(Masks):
    def pixel_operation(self, pixel):
        r, g, b = pixel
        r = 255 - r
        g = 255 - g
        b = 255 - b
        pixel = (r, g, b)
        return pixel


class Uorhal(Masks):
    def pixel_operation(self, pixel):
        r, g, b = pixel
        r = 255 - r
        g = 255 - r
        b = 255 - r
        pixel = (r, g, b)
        return pixel


class Contrast(Masks):
    def pixel_operation(self, pixel):
        r, g, b = pixel
        r = r - 30 if r < 127.5 else r + 30
        g = g - 30 if g < 127.5 else g + 30
        b = b - 30 if b < 127.5 else b + 30
        pixel = (r, g, b)
        return pixel


class Noise(Masks):
    def pixel_operation(self, pixel):
        r, g, b = pixel
        r = r - 90 + random.randint(0, 180)
        g = g - 90 + random.randint(0, 180)
        b = b - 90 + random.randint(0, 190)
        pixel = (r, g, b)
        return pixel
