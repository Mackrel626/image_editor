from PIL import Image,  ImageFilter

class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = list()

    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print("Файл не знайдено!")
        self.original.show()
    
    def black_white(self):
        bw_photo = self.original.convert("L")
        self.changed.append(bw_photo)
        bw_photo.show()

    def do_left(self):
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)
        rotated.show()

    def do_cropped(self):
        box = (250, 100, 600, 400)
        cropped = self.original.crop(box)
        self.changed.append(cropped)
        cropped.show()

myImage = ImageEditor('pig.jpg')
myImage.open()

myImage.black_white()

myImage.do_left()

myImage.do_cropped()