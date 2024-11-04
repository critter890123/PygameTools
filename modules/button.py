import pygame

from PygameTools.modules.text import Text

class Button:
    def __init__(self, font: pygame.font, rect: tuple[int,int,int,int], text: str, buttonColor: tuple[int,int,int], textColor: tuple[int,int,int] = (0, 0, 0), borderWidth: int = 0, borderColor: tuple[int,int,int] = (0, 0, 0)):
        self.font = font
        self.rect = rect
        self.text = text
        self.buttonColor = buttonColor
        self.pressedColor = (self.buttonColor[0]*.9, self.buttonColor[1]*.9, self.buttonColor[2]*.9) # 10% darker than buttonColor
        self.textColor = textColor

        self.borderWidth = borderWidth
        self.borderColor = borderColor

        self.pressed = False
        self.onPressed = None

    def update(self, args: dict):
        rect = [self.rect[0] + (args['position'][0] + args['offset'][0]), self.rect[1] + (args['position'][1] + args['offset'][1]), self.rect[2], self.rect[3]]

        if pygame.Rect.colliderect(args['mouseRect'], pygame.Rect(rect)) and args['mousePressed'][0]:
            self.pressed = True

        else:
            self.pressed = False

        if type(self.onPressed) is dict and self.pressed:
            return self.onPressed

    def draw(self, screen: pygame.Surface, offset: list[int, int]):
        rect = [position+offset for position, offset in zip(self.rect[:2], offset)] + list(self.rect[2:])
        pygame.draw.rect(screen, self.buttonColor if not self.pressed else self.pressedColor, rect)
        if self.borderWidth > 0:
            pygame.draw.rect(screen, self.borderColor, rect, self.borderWidth)
        # rect value for text = ((x + width/2), (y + height/2))
        Text(self.font, (int(self.rect[0] + (self.rect[2]/2)), int(self.rect[1] + (self.rect[3]/2) - self.text.count('\n')*(self.font.size("")[1]/2))), self.textColor, self.text).draw(screen, offset)
        self.pressed = False