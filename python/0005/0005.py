from PIL import Image
import os


def mod_image(path,save_path):
    dir = [x for x in os.listdir(path) if os.path.splitext(x)[1] == '.jpg']
    size = 128,128
    for image in dir:
        img = Image.open(path + image)
        img.thumbnail(size)
        img.save(save_path + image,'JPEG')


if __name__ == '__main__':
    mod_image('original/','phone/')



