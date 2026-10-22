import random as r

#Printing in a more readable format
def PImg(Img):
    for row in Img:
        print(row)

#Generating a random image
def GenImg(n):
    return [[r.randint(0, 255) for i in range(n)] for j in range(n)]

#Padding an image
def PadImg(Img):
    PaddedImg = [[0 for i in range(len(Img) + 2)] for j in range(len(Img[0]) + 2)]
    for i in range(len(Img)):
        for j in range(len(Img[0])):
            PaddedImg[i + 1][j + 1] = Img[i][j]
    return PaddedImg

#Inverting values of an image
def InvImg(Img):
    for i in range(len(Img)):
        for j in range(len(Img[i])):
            Img[i][j] = 255 - Img[i][j]
    return Img

#Increasing brightness of an image by a given amount
def BriImg(Img, val):
    for i in range(len(Img)):
        for j in range(len(Img[i])):
            Img[i][j] += val
            if Img[i][j] > 255:
                Img[i][j] = 255
    return Img

#Setting a threshold for an image and whitening/blackening image based on it
def ThrImg(Img, val):
    for i in range(len(Img)):
        for j in range(len(Img[i])):
            if Img[i][j] >= val:
                Img[i][j] = 255
            else:
                Img[i][j] = 0
    return Img

#Flipping an image horizontally
def FliImg(Img):
    return [row[::-1] for row in Img]

#Rotating an image clockwise by 90 degrees
def RotImg(Img):
    RotatedImg = [[None for i in range(len(Img))] for j in range(len(Img[0]))]
    for i in range(len(Img)):
        for j in range(len(Img[0])):
            RotatedImg[j][len(Img) - 1 - i] = Img[i][j]
    return RotatedImg

#Blurring an image using mean average of surrounding 3x3 pixels
def BluImg(Img):
    Img = PadImg(Img)
    BlurredImg = [[0 for i in range(len(Img[0]))] for j in range(len(Img))]
    for i in range(1, len(Img) - 1):
        for j in range(1, len(Img[0]) - 1):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    BlurredImg[i][j] += Img[i + k][j + l]
            BlurredImg[i][j] = round(BlurredImg[i][j] / 9)
    return BlurredImg
