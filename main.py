from kivy.app import App
from kivy.uix.screenmanager import Screen

images = ["download (4).jpeg", "download.jfif"]
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



PhotoGalleryApp().run()
