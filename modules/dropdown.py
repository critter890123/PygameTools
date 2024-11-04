import pygame

from PygameTools.modules.button import Button

class Dropdown:
    def __init__(self, font: pygame.font, rect: tuple[int,int,int,int], options: list[str], backgroundColor: tuple[int,int,int], textColor: tuple[int,int,int], placeholder: str = None, borderWidth: int = 0, borderColor: tuple[int, int, int] = (0, 0, 0)):
        self.font = font
        self.rect = rect
        self.placeholder = placeholder if placeholder else options[0]
        self.selectedOption = None if not placeholder in options else placeholder
        self.options = options
        self.backgroundColor = backgroundColor
        self.textColor = textColor

        self.borderWidth = borderWidth
        self.borderColor = borderColor

        self.selected = False

    def toggle(self, args: dict):
        rect = [self.rect[0] + (args['position'][0] + args['offset'][0]), self.rect[1] + (args['position'][1] + args['offset'][1]), self.rect[2], self.rect[3]]

        if pygame.Rect.colliderect(args['mouseRect'], rect):
            self.selected = True
        else:
            self.selected = False

    def update(self, args: dict):
        index = 0
        for option in self.options:
            if option == self.selectedOption:
                    continue
            rect = [self.rect[0] + (args['position'][0] + args['offset'][0]), ((index+1)*self.rect[3]) + self.rect[1] + (args['position'][1] + args['offset'][1]), self.rect[2], self.rect[3]]
            if pygame.Rect.colliderect(args['mouseRect'], rect) and args['mousePressed'][0] and self.selected:
                self.selectedOption = option
                return True
            index += 1

    def draw(self, screen: pygame.Surface, offset: list[int, int]):
        Button(self.font, self.rect, self.placeholder if not self.selectedOption else self.selectedOption, self.backgroundColor, self.textColor, self.borderWidth, self.borderWidth).draw(screen, offset)

        if self.selected:
            index = 0
            for option in self.options:
                if option == self.selectedOption:
                    continue
                rect = [self.rect[0], ((index+1)*self.rect[3]) + self.rect[1], self.rect[2], self.rect[3]]
                Button(self.font, rect, option, self.backgroundColor, self.textColor, self.borderWidth, self.borderWidth).draw(screen, offset)
                if self.borderWidth:
                    pygame.draw.line(screen, self.borderColor, (self.rect[0], ((index+1)*self.rect[3]) + self.rect[1]), (self.rect[0]+self.rect[2]-1, ((index+1)*self.rect[3]) + self.rect[1]))
                index += 1