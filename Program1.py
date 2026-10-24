import random as r

#Printing in a more readable format
def PImg(Img):
    for row in Img:
        print(row)

#Generating a random image
def GenImg(n):
    return [[r.randint(0, 255) for i in range(n)] for j in range(n)]

Img1=GenImg(5)
print("Randomly generated image")
PImg(Img1)

#Padding an image
def PadImg(Img):
    PaddedImg = [[0 for i in range(len(Img) + 2)] for j in range(len(Img[0]) + 2)]
    for i in range(len(Img)):
        for j in range(len(Img[0])):
            PaddedImg[i + 1][j + 1] = Img[i][j]
    return PaddedImg

#Inverting values of an image
def InvImg(Img):
    InvertedImg = [[0 for i in range(len(Img))] for j in range(len(Img[0]))]
    for i in range(len(Img)):
        for j in range(len(Img[i])):
            InvertedImg[i][j] = 255 - Img[i][j]
    return InvertedImg

#Increasing brightness of an image by a given amount
def BriImg(Img, val):
    BrightenedImg = [[0 for i in range(len(Img))] for j in range(len(Img[0]))]
    for i in range(len(Img)):
        for j in range(len(Img[i])):
            BrightenedImg[i][j] = Img[i][j] + val
            if BrightenedImg[i][j] > 255:
                BrightenedImg[i][j] = 255
    return BrightenedImg

#Setting a threshold for an image and whitening/blackening image based on it
def ThrImg(Img, val):
    ThresholdedImg = [[0 for i in range(len(Img))] for j in range(len(Img[0]))]
    for i in range(len(Img)):
        for j in range(len(Img[i])):
            if Img[i][j] >= val:
                ThresholdedImg[i][j] = 255
            else:
                ThresholdedImg[i][j] = 0
    return ThresholdedImg

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

"""print('\nPadded Image\n')
PImg(PadImg(Img1))
print("\nInverted Image\n")
PImg(InvImg(Img1))
print("\nBrighened Image\n")
PImg(BriImg(Img1,100))
print("\nThresholded image\n")
PImg(ThrImg(Img1,100))
print("\nFlipped Image\n")
PImg(FliImg(Img1))
print("\nRotated Image\n")
PImg(RotImg(Img1))
print("\nBlurred Image\n")
PImg(BluImg(Img1))"""