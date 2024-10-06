from cgitb import text
import pygame

from PygameTools.modules.button import Button
from PygameTools.modules.text import Text
from PygameTools.modules.slider import Slider
from PygameTools.modules.textbox import TextBox

class Surface:
    def __init__(self, rect: tuple[int, int, int, int], scene: int, backgroundColor: tuple[int, int, int], scrollable: bool = False, height: int = 0):
        self.position = rect[:2]
        self.surface = pygame.Surface(rect[2:])
        self.scene = scene
        self.backgroundColor = backgroundColor
        self.scrollable = scrollable if rect[3] < height else False
        self.maxOffset = abs(rect[3]-height)
        
        self.offset = [0, 0]
        self.objects = []

    def createButton(self, font: pygame.font, rect: tuple[int, int, int, int], text: str, buttonColor: tuple[int, int, int], textColor: tuple[int, int, int]):
        button = Button(font, rect, text, buttonColor, textColor)
        
        self.objects.append(button)
        return button

    def createSlider(self, rect: tuple[int, int, int, int], barColor: tuple[int, int, int], sliderColor: tuple[int, int, int], surfaceScroll: bool = True, vertical: bool = True):
        slider = Slider(rect, barColor, sliderColor, surfaceScroll, vertical)
        
        self.objects.append(slider)
        return slider

    def createTextbox(self, font: pygame.font, rect: tuple[int, int, int, int], backgroundColor: tuple[int, int, int], textColor: tuple[int, int, int], placeholder: str = ""):
        textbox = TextBox(font, rect, backgroundColor, textColor, placeholder)

        self.objects.append(textbox)
        return textbox

    def createText(self, font: pygame.font, rect: tuple[int, int], color: tuple[int, int, int], text: str, center: bool = True, maxWidth: int = None):
        text = Text(font, rect, color, text, center, maxWidth)

        self.objects.append(text)
        return text

    def addObject(self, object):
        self.objects.append(object)

    def draw(self, screen: pygame.Surface):
        self.surface.fill(self.backgroundColor)

        for obj in self.objects:
            obj.draw(self.surface, self.offset)

        screen.blit(self.surface, self.position)