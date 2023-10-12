from kivy.app import App
from kivy.uix.screenmanager import Screen
from PIL import Image, ImageDraw
import random

images = ["download (4).jpeg", "download.jfif", "download (2).jfif"]
index= 0
class PhotoGalleryApp(App):
    pass

class Display(Screen):
    def display_image(self):
        return images[index]
    def advance(self):
        global index, images
        index= (index+1)%len(images)
        self.ids.image.source = images[index]
class PhotoEditorApp(App):
    pass

class MainScreen(Screen):


    def render(self):
        self.ids.image.source = self.ids.filename.text
        return(self.ids.filename.text)

    def pointillism(self,image, name):
        img = Image.open(image)
        pixels = img.load()
        canvas = Image.new("RGB", (img.size[0], img.size[1]), "white")
        for i in range(200000):
            x = random.randint(0, img.size[0] - 1)
            y = random.randint(0, img.size[1] - 1)
            size = random.randint(3, 5)
            ellipsebox = [(x, y), (x + size, y + size)]
            draw = ImageDraw.Draw(canvas)
            draw.ellipse(ellipsebox, fill=(pixels[x, y][0], pixels[x, y][1], pixels[x, y][2]))
            del draw
        canvas.save(name)
        self.ids.image.source = "pointillism " + self.ids.filename.text
    def invert(self, image, name):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = 255 - pixels[x, y][0]
                green = 255 - pixels[x, y][1]
                blue = 255 - pixels[x, y][2]
                pixels[x, y] = (red, green, blue)
        img.save(name)
        self.ids.image.source = "invert " + self.ids.filename.text
    def sepia(self, image, name):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red1 = pixels[x, y][0]
                green1 = pixels[x, y][1]
                blue1 = pixels[x, y][2]
                red = int(red1 * .393 + green1 * 0.769 + blue1 * 0.189)
                green = int(red1 * .349 + green1 * 0.686 + blue1 * 0.168)
                blue = int(red1 * .272 + green1 * 0.534 + blue1 * 0.131)

                pixels[x, y] = (red, green, blue)
        img.save(name)
        self.ids.image.source = "Sepia "+self.ids.filename.text
    def lighten_darken(self, image, name, difference):
        img = Image.open(image)
        pixels = img.load()

        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = pixels[x, y][0] + difference
                green = pixels[x, y][1] + difference
                blue = pixels[x, y][2] + difference
                pixels[x, y] = (red, green, blue)

        img.save(name)
        self.ids.image.source = image["Lighten/darken "+self.ids.filename.text]

    def red_filter(self, image, name):
      img = Image.open(image)
      pixels = img.load()
      for y in range(img.size[1]):
        for x in range(img.size[0]):
          red = 255
          green = pixels[x, y][1]
          blue = pixels[x, y][2]
          pixels[x,y] = (red, green, blue)
      img.save(name)
      self.ids.image.source = image["red_filter " + self.ids.filename.text]


# PhotoGalleryApp().run()
PhotoEditorApp().run()