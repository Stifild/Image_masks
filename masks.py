from PIL import Image


class Masks:
    def pixel_apperation(self, pixel):
        pass

    def pixel_apply(self, img):
        for x in range(img.width):
            for y in range(img.hight):
                new_pixel = self.pixel_apperation(img.getpixel((x, y)))
                img = img.putpixel((x, y), new_pixel)
        return img


class Invert(Masks):
    def pixel_apperation(self, pixel):
        r, g, b = pixel
        r = 255 - r
        g = 255 - g
        b = 255 - b
        pixel = (r, g, b)
        return pixel
