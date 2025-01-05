from PIL import Image,  ImageFilter

with Image.open("pig.jpg") as photo:
    print(photo.size)
    print(photo.format)
    print(photo.mode)


    photo = photo.convert('L')
    photo = photo.filter(ImageFilter.BLUR)
    photo = photo.transpose(Image.ROTATE_90)

    #photo.save("new_photo.jpg")
    photo.show()