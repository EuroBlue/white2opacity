from PIL import Image
def main():
    im = Image.open('in.png')
    pixelMap = im.load()

    img = Image.new(im.mode, im.size)
    pixelsNew = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixelsNew[i, j] = (pixelMap[i, j][0], pixelMap[i, j][1], pixelMap[i, j][2], 255-int((pixelMap[i, j][0]+pixelMap[i, j][1]+pixelMap[i, j][1])/3))
    im.close()
    img.show()
    img.save("out.png")
    img.close()


if __name__ == '__main__':
    main()
