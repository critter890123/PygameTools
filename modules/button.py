import pygame

from PygameTools.modules.text import Text

class Button:
    def __init__(self, rect: tuple[int,int,int,int], font: pygame.font, text: str, buttonColor: tuple[int,int,int], textColor: tuple[int,int,int]):
        self.font = font
        self.rect = rect
        self.text = text
        self.buttonColor = buttonColor
        self.pressedColor = (self.buttonColor[0]*.9, self.buttonColor[1]*.9, self.buttonColor[2]*.9) # 10% darker than buttonColor
        self.textColor = textColor

        self.pressed = False
        self.onPressed = None

    def update(self, args: dict):
        args['mouseRect'].x -= args['offset'][0]
        args['mouseRect'].y -= args['offset'][1]

        if pygame.Rect.colliderect(args['mouseRect'], pygame.Rect(self.rect)):
            self.pressed = True

        else:
            self.pressed = False

        if type(self.onPressed) is dict and self.pressed:
            return self.onPressed

    def draw(self, screen: pygame.Surface, offset: list[int, int]):
        rect = [position+offset for position, offset in zip(self.rect[:2], offset)] + list(self.rect[2:])
        pygame.draw.rect(screen, self.buttonColor if not self.pressed else self.pressedColor, rect)
        # rect value for text = ((x + width/2), (y + height/2))
        Text(self.font, (int(self.rect[0] + (self.rect[2]/2)), int(self.rect[1] + (self.rect[3]/2))), self.textColor, self.text).draw(screen, offset)
        self.pressed = False