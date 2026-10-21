import random as r

def PImg(Img):
    for row in Img:
        print(row)

def GenImg(n):
    Img=[[r.randint(0,255) for i in range(n)] for j in range(n)]
    return Img
Img1 = GenImg(5)
PImg(Img1)

def InvImg(Img):
    for i in range(0,len(Img)):
        for j in range(0,len(Img[i])):
            Img[i][j]=255-Img[i][j]
    return Img

def  BriImg(Img,val):
    for i in range(0,len(Img)):
        for j in range(0,len(Img[i])):
            Img[i][j]+=val
            if Img[i][j]>255:
                Img[i][j]=255
    return Img

def ThrImg(Img,val):
    for i in range(0,len(Img)):
        for j in range(0,len(Img[i])):
                if Img[i][j]>=val:
                    Img[i][j]=255
                else:
                    Img[i][j]=0
    return Img

def FliImg(Img):
    return [row[::-1] for row in Img]

def RotImg(Img):
    RotatedImg = [[None for i in range(len(Img))] for i in range(len(Img[0]))]
    for i in range(len(Img)):
        for j in range(len(Img[0])):
            RotatedImg[j][len(Img)-1-i]=Img[i][j]
    return RotatedImg
            