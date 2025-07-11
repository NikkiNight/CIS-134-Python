"""
images.py

Revised for Python 3.2, 2011.

This module,  written by Kenneth Lambert, supports simple image processing.  
The Image class represents either an image loaded from a GIF file or a 
blank image.  

To instantiate an image from a file, enter

image = Image(aGifFileName)                   

To instantiate a blank image, enter

image = Image(aWidth, aHeight)

Image methods:

draw()                          Displays the image in a window 
getWidth()  -> anInt            The width in pixels
getHeight() -> anInt            The height in pixels
getPixel(x, y)  -> (r, g, b)    The RGB values of pixel at x, y
setPixel(x, y, (r, g, b))       Resets pixel at x, y to (r, g, b)
save()                          Saves the image to the current file name
save(aFileName)                 Saves the image to fileName

LICENSE: This is open-source software released under the terms of the
GPL (http://www.gnu.org/licenses/gpl.html).
"""

import tkinter
import os, os.path
tk = tkinter

_root = None

""" Edited from:

Program: posterize.py (CIS 134 Ch7 Assignment 5)
Author: Nicola Ward
Last Date Modified: 3/29/2024

The purpose of this program is to prompt the user to enter a value up to 255 for
each red, green and blue prompt. The program clones the image, then uses the entered
RGB values and shades the black pixel with the custom color.

"""

from images import Image

image = Image("smokey.gif")
print("Please close the image to continue.")
image.draw()

# Input/Prompt The User For RGB Values
while True:    
    red = int(input("Please enter a custom value up to 255 for red: "))
    if red > 0 and red < 255:
        break
    print("Error.")

while True:
    green = int(input("Please enter a custom value up to 255 for green: "))
    if green > 0 and green < 255:
        break
    print("Error.")
    
while True:
    blue = int(input("Please enter a custom value up to 255 for blue: "))
    if blue > 0 and blue < 255:
        break
    print("Error.")    

# Tuple
newRGB = (red, green, blue)

# Clone Image
dupe = image.clone()

# Function
def posterize(dupe, newRGB):    
        
    red, green, blue = newRGB # Unpack tuple
        
    whitePixel = (255, 255, 255)
    customPixel = (red, green, blue)

    for y in range(dupe.getHeight()):
        for x in range(dupe.getWidth()):
            (r, g, b) = dupe.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                dupe.setPixel(x, y, customPixel)
            else:
                dupe.setPixel(x, y, whitePixel)

posterize(dupe, newRGB) # Call posterize Function     
dupe.draw() # Draw New Image

""" Rest Of Program Code: """
class ImageView(tk.Canvas):
    def __init__(self, image,
                 title = "New Image",
                 autoflush=False):
        master = tk.Toplevel(_root)
        master.protocol("WM_DELETE_WINDOW", self.close)
        tk.Canvas.__init__(self, master,
                           width = image.getWidth(),
                           height = image.getHeight())
        self.master.title(title)
        self.pack()
        master.resizable(0,0)
        self.image = image
        self.height = image.getHeight()
        self.width = image.getWidth()
        self.autoflush = autoflush
        self.closed = False

    def close(self):
        """Close the window"""
        self.closed = True
        self.master.destroy()
        self.image.canvas = None
        _root.quit()

    def isClosed(self):
        return self.closed

    def getHeight(self):
        """Return the height of the window"""
        return self.height

    def getWidth(self):
        """Return the width of the window"""
        return self.width

class Image:
        
    def __init__(self, *args):
        self.canvas = None
        if len(args) == 1:
            name = args[0]
            if type(name) != str:
                raise Exception('Must be a file name')
            if name[-4:].upper() != '.GIF':
                raise Exception('File must be a GIF')
            if not os.path.exists(args[0]):
                raise Exception('File not in current directory')
            self.image = tk.PhotoImage(file = args[0], master = _root)
            self.filename = args[0]
            self.width = self.image.width()
            self.height = self.image.height()
        else: # arguments are width and height
            self.width, self.height = args
            self.image = tk.PhotoImage(master =_root,
                                       width = self.width,
                                       height = self.height)
            self.filename = ""
            		
    def getWidth(self):
        """Returns the width of the image in pixels"""
        return self.width

    def getHeight(self):
        """Returns the height of the image in pixels"""
        return self.height

    def getPixel(self, x, y):
        """Returns a tuple (r,g,b) with the RGB color values for pixel (x,y)
        r,g,b are in range(256)

        """
        value = self.image.get(x, y)
        if type(value) == int:
            return (value, value, value)
        elif type(value) == tuple:
            return value
        else:
            return tuple(map(int, value.split()))

    def setPixel(self, x, y, color):
        """Sets pixel (x,y) to the color given by RGB values r, g, and b.
        r,g,b should be in range(256)

        """
        (r, g, b) = color
        r = round(r)
        g = round(g)
        b = round(b)
        color = (r, g, b)
        self.image.put("{#%02x%02x%02x}" % color, (x, y))

    def draw(self):
        """Creates and opens a window on an image.
        The user must close the window to return control to
        the caller."""
        if not self.canvas:
            self.canvas = ImageView(self,
                                    self.filename)
        self.canvas.create_image(self.width // 2,
                                 self.height // 2,
                                 image = self.image)
        _root.mainloop()

    def save(self, filename = ""):
        """Saves the image to filename.  If no file name
        is provided, uses the image's file name if there
        is one; otherwise, simply returns.
        If the .gif extension is not present, it is added.
        """
        if filename == "":
            return
        else:
            self.filename = filename
        path, name = os.path.split(filename)
        ext = name.split(".")[-1]
        if ext != "gif":
            filename += ".gif"
            self.filename = filename
        self.image.write(self.filename, format = "gif")

    def clone(self):
        new = Image(self.width, self.height)
        new.image = self.image.copy()
        return new

    def __str__(self):
        rep = ""
        if self.filename:
            rep += ("File name: " + self.filename + "\n")
        rep += ("Width:  " + str(self.width) + \
                "\nHeight: " + str(self.height))
        return rep
    		
_root = tk.Tk()
_root.withdraw()



  

   
