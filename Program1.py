import random as r

def GenImg(n):
    Img=[[r.randint(0,255) for i in range(n)] for j in range(n)]
    return Img
Img1 = GenImg(5)

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

print(ThrImg(Img1,100))