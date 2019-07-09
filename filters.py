from PIL import Image

def load_img(image_file):
    return Image.open(image_file)

def show_img(image_file):
    image_file.show(title=None)

def save_img(image_file, newfile):
    image_file.save(newfile, "JPEG")

# def obamicon(newfile):
#     pixels=image.putdata(img)
#     for  <182:
#         newfile.new(darkBlue)
#         putpixel(darkBlue)



def main():
    img=load_img("corgi booty.jpg")
    show_img(img)
    save_img(img, "cool")
main()
# obamicon("cool")
