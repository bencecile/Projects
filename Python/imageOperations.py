from PIL import Image
import os.path

def getLuminance(red, green, blue):
    #The percieved RGB luminance formula
    #https://www.w3.org/TR/AERT#color-contrast
    return (0.299*red+0.587*green+0.114*blue)/255

#Prompts the user for the image path
#Returns the path to the file
def getFile ():
    fileName = input("Enter the path to the image: ")
    while (not os.path.isfile(fileName)):
        print("That file does not exist")
        fileName = input("Enter the path to the image: ")

    return fileName

def getOutline():
    outImage = Image.open(getFile())
    width, height = outImage.size
    completed = set()
    contrastMin = 0.07 #Can be changed to produce different results
    outlined = False
    #Go through the entire outImage each pixel at a time
    for i in range(width):
        for j in range(height):
            #Skip the pixel if it has been changed
            if ((i, j) in completed):
                continue
            outLined = False
            pixelStart = outImage.getpixel((i, j)) #Returns an (R, G, B) tuple
            startL = getLuminance(*pixelStart)
            for x in range(2):
                for y in range(2):
                    #Make sure the pixel to check is within the image
                    if (i+x <= width-1 and j+y <= height-1):
                        pixelCheck = outImage.getpixel((i+x, j+y))
                        checkL = getLuminance(*pixelCheck)
                        #Check the difference in luminance (contrast)
                        if (abs(startL-checkL) > contrastMin):
                            #Replace the less bright pixel with black and the other with white
                            if (startL > checkL):
                                outImage.putpixel((i, j), (255, 255, 255))
                                outImage.putpixel((i+x, j+y), (0, 0, 0))
                            else:
                                outImage.putpixel((i+x, j+y), (255, 255, 255))
                                outImage.putpixel((i, j), (0, 0, 0))
                            completed.add((i+x, j+y))
                            outlined = True

            #Default a pixel to white
            if (outLined == False):
                outImage.putpixel((i, j), (255, 255, 255))
    outImage.show()
    outImage.close()


def getGreyScale():
    outImage = Image.open(getFile())
    width, height = outImage.size
    for i in range(width):
        for j in range(height):
            pixelStart = outImage.getpixel((i, j))
            startL = getLuminance(*pixelStart)
            #Get the greyscale with the same luminance of the original pixel
            outImage.putpixel((i, j), (int(startL*255), int(startL*255), int(startL*255)))
    outImage.show()
    outImage.close()

#Currently unused
def getAverageRGB(outImage, x, y, width, height):
    allPixels = [0, 0, 0]
    count = 0
    for i in range(x, width):
        for j in range(y, height):
            count += 1
            toAdd = outImage.getpixel((i, j))
            allPixels[0] += toAdd[0]
            allPixels[1] += toAdd[1]
            allPixels[2] += toAdd[2]
    return (allPixels[0]/count, allPixels[1]/count, allPixels[2]/count)

#Get user input
choice = input("Enter [0] for the outline of an image, [1] for the grey scale of an image: ")

while (choice != "0" and choice != "1"):
    print("That is not a valid option.")
    choice = input("Enter [0] for the outline of an image, [1] for the grey scale of an image: ")

if (choice == "0"):
    getOutline()
else:
    getGreyScale()
