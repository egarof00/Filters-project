darkBlue=(0, 51, 76)
red=(217, 26, 33)
lightBlue=(112, 150, 158)
yellow=(252, 227, 166)

from PIL import Image
im =Image.open("cool")

pixels= list(im.getdata())
list_length=len(pixels)

for i in range(list_length):
    redpixels = pixels [i][0]
    bluepixels= pixels [i][1]
    greenpixels = pixels[i][2]
    sum = redpixels + bluepixels + greenpixels

    if sum< 182:
        pixels[i] = darkBlue
    elif sum >= 182 and sum<364:
        pixels[i]=red
    elif sum >= 364 and sum < 546:
        pixels[i]=lightBlue
    else:
        pixels[i]=yellow
im.putdata(pixels)
im.show()
