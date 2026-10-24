This is a project about doing image operations on images represented as a 3D nested list. A list can either be randomly generated or imported and exported in PPM P3/PPM ASCII format.

Following are the operations/functions available to do in the code:

0)PImg(Img): Prints the image's 3D list in a more readable format

1)GreImg(m,n): Generates a grayscale Image of size mxn

2)RGBImg(m,n): Generates a RGB Image of size mxn

3)PadImg(Img): Adds a layer of padding to given Image

4)InvImg(Img): Inverts value of each pixel, by subtracting its value from 255

5)BriImg(Img,val): Brightens/increases value of each pixel by given amount upto 255

6)ThrImg(Img,val): Changes pixels whose value is above/equal to given threshold to 255 and rest to 0

7)FliImg(Img): Flips each row's pixel's values horizontally (Mirror Image)

8)RotImg(Img): Rotates Image by 90 degrees clockwise

9)CroImg(Img,left,up,right,down): Crops image

9)BluImg(Img): Blurs pixels of Image by taking mean of 3x3 pixels around it.

10)EdgImg(Img): Detects edges of an image using a laplacian style kerner [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]] to be exact

11)LoadPPMP3(filename): Converts PPM P3 file formats into a 3D list compatible with above functions

12)SavePPMP3(filename,Img): Converts 3D lists above functions give as output back to a PPM P3 file format and save it as a file
