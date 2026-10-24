import random as r

#Printing in a more readable format
def PImg(Img):
    for row in Img:
        print(row)

#Generating a random greyscale image
def GreImg(m,n):
    return [[[r.randint(0, 255)] for i in range(n)] for j in range(m)]

#Generating a random RGB image
def RGBImg(m,n):
    return [[[r.randint(0, 255) for i in range(0,3)] for j in range(n)] for k in range(m)]

#Padding an image
def PadImg(Img):
    PaddedImg = [[[0 for i in range(len(Img[0][0]))] for j in range(len(Img[0]) + 2)] for k in range(len(Img) + 2)]
    for i in range(len(Img)):
        for j in range(len(Img[0])):
            for k in range(len(Img[0][0])):
                PaddedImg[i + 1][j + 1][k] = Img[i][j][k]
    return PaddedImg

#Inverting values of an image
def InvImg(Img):
    InvertedImg = [[[0 for i in range(len(Img[0][0]))] for j in range(len(Img[0]))] for k in range(len(Img))]
    for i in range(len(Img)):
        for j in range(len(Img[i])):
            for k in range(len(Img[i][j])):
                InvertedImg[i][j][k] = 255 - Img[i][j][k]
    return InvertedImg

#Increasing brightness of an image by a given amount
def BriImg(Img, val):
    BrightenedImg = [[[0 for i in range(len(Img[0][0]))] for j in range(len(Img[0]))] for k in range(len(Img))]
    for i in range(len(Img)):
        for j in range(len(Img[i])):
            for k in range(len(Img[i][j])):
                BrightenedImg[i][j][k] = Img[i][j][k] + val
                if BrightenedImg[i][j][k] > 255:
                    BrightenedImg[i][j][k] = max(0, min(255, Img[i][j][k] + val))
    return BrightenedImg

#Setting a threshold for an image and whitening/blackening image based on it
def ThrImg(Img, val):
    ThresholdedImg = [[[0 for i in range(len(Img[0][0]))] for j in range(len(Img[0]))] for k in range(len(Img))]
    for i in range(len(Img)):
        for j in range(len(Img[i])):
            for k in range(len(Img[i][j])):
                if Img[i][j][k] >= val:
                    ThresholdedImg[i][j][k] = 255
                else:
                    ThresholdedImg[i][j][k] = 0
    return ThresholdedImg

#Flipping an image horizontally
def FliImg(Img):
    return [row[::-1] for row in Img]

#Rotating an image clockwise by 90 degrees
def RotImg(Img):
    RotatedImg = [[[0 for i in range(len(Img[0][0]))] for j in range(len(Img))] for k in range(len(Img[0]))]
    for i in range(len(Img)):
        for j in range(len(Img[i])):
            for k in range(len(Img[i][j])):
                RotatedImg[j][len(Img) - 1 - i][k] = Img[i][j][k]
    return RotatedImg

#Returns a cropped image
def CropImg(Img,left,up,right,down):
    CroppedImg = [[[0 for i in range(len(Img[0][0]))] for j in range(len(Img[0])-left-right)] for k in range(len(Img)-up-down)]
    for i in range(len(Img)-up-down):
        for j in range(len(Img[i])-left-right):
            for k in range(len(Img[i][j])): 
                CroppedImg[i][j][k]=Img[i+up][j+left][k]
    return CroppedImg

#Blurring an image using mean average of surrounding 3x3 pixels
def BluImg(Img):
    Img = PadImg(Img)
    BlurredImg = [[[0 for i in range(len(Img[0][0]))] for j in range(len(Img[0])-2)] for k in range(len(Img)-2)]
    for i in range(1, len(Img) - 1):
        for j in range(1, len(Img[0]) - 1):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    for m in range(len(Img[i][j])):
                        BlurredImg[i-1][j-1][m] += Img[i + k][j + l][m]
            for m in range(len(Img[i][j])):
                BlurredImg[i-1][j-1][m] = round(BlurredImg[i-1][j-1][m] / 9)
    return BlurredImg

def EdgImg(Img):
    Img = PadImg(Img)
    EdgeSharpenedImg = [[[0 for i in range(len(Img[0][0]))] for j in range(len(Img[0])-2)] for k in range(len(Img)-2)]
    for i in range(1, len(Img) - 1):
        for j in range(1, len(Img[0]) - 1):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    for m in range(len(Img[i][j])):
                        if k == 0 and l == 0:
                            EdgeSharpenedImg[i-1][j-1][m] += 8*Img[i + k][j + l][m]
                        else:
                            EdgeSharpenedImg[i-1][j-1][m] -= Img[i + k][j + l][m]
    EdgeSharpenedImg = [[[min(255,abs(k)) for k in j] for j in i] for i in EdgeSharpenedImg]
    return EdgeSharpenedImg

def LoadPPMP3(filename):
    with open(filename, "r") as file:
        data = []

        for line in file:
            line = line.split("#")[0]
            data.extend(line.split())

    #in PPM P3 format files, 1st element is P3, 2nd is width, 3rd is height and 4th is max value
    LoadedImg = [[[0 for i in range(0,3)] for j in range(int(data[1]))] for k in range(int(data[2]))]
    n=4
    
    for i in range(int(data[2])):
        for j in range(int(data[1])):
            for k in range(0,3):
                LoadedImg[i][j][k] = int(data[n])
                n+=1

    return LoadedImg
    
def SavePPMP3(filename, Img):

    with open(filename, "w") as file:
        file.write("P3\n")
        file.write(f"{len(Img[0])} {len(Img)}\n")
        file.write("255\n")

        for i in range(len(Img)):
            for j in range(len(Img[0])):
                for k in range(3):
                    file.write(f"{Img[i][j][k]} ")

            file.write("\n")

"""Img1=GreImg(5,5)
#Img1=RGBImg(5,5)
print("Randomly generated image")
PImg(Img1)
print('\nPadded Image\n')
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
print("\nCropped Image\n")
PImg(CropImg(Img1,1,1,1,1))
print("\nBlurred Image\n")
PImg(BluImg(Img1))
print("\nEdge Sharpened Image\n")
PImg(EdgImg(Img1))
SavePPMP3('NewPPMP3Img.ascii.ppm',RotImg(LoadPPMP3('snail.ascii.ppm')))"""