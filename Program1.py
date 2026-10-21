import random as r

def GenImg(n):
    Img=[[r.randint(0,255) for i in range(n)] for j in range(n)]
    return Img
Img1 = GenImg(5)
print(Img1)

def InvImg(Img):
    for i in range(0,len(Img)):
        for j in range(0,len(Img[i])):
            Img[i][j]=255-Img[i][j]
    return Img
print(InvImg(Img1))