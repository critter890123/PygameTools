import pygame

class Text:
    def __init__(self, font: pygame.font, rect: tuple[int,int], color: tuple, text: str, center: bool = True, maxWidth: int = None):
        self.font = font
        self.color = color
        self.text = text
        self.rect = rect
        self.center = center
        self.maxWidth = maxWidth

    def draw(self, screen: pygame.Surface, offset: list[int, int]):
        maxWidth = 0
        text_rects = []
        text_surfaces = []
        rect = [position+offset for position, offset in zip(self.rect, offset)]

        for index, text in enumerate(self.text.split("\n")):
            text_surface = self.font.render(text, False, self.color)
            text_rect = text_surface.get_rect(center=rect) if self.center else text_surface.get_rect(topleft=rect)
            
            if self.maxWidth and text_rect.width > self.maxWidth:
                cropped_text_rect = text_surface.get_rect()
                cropped_text_rect.width = self.maxWidth
                cropped_text_surface = text_surface.subsurface(cropped_text_rect)
                cropped_text_rect = cropped_text_surface.get_rect(center=rect) if self.center else cropped_text_surface.get_rect(topleft=rect)

                screen.blit(cropped_text_surface, cropped_text_rect)
            else:
                screen.blit(text_surface, text_rect)

            rect[1] += self.font.size("")[1]