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
        rect = [position+offset for position, offset in zip(self.rect[:2], offset)] + list(self.rect[2:])

        text_surface = self.font.render(self.text, False, self.color)
        text_rect = text_surface.get_rect(center=rect) if self.center else text_surface.get_rect(topleft=rect)
        surface = pygame.Surface((text_rect.width if self.maxWidth is None else self.maxWidth, text_rect.height), pygame.SRCALPHA, 32)
        surface = surface.convert_alpha()

        surface.blit(text_surface, (0, 0))
        screen.blit(surface, text_rect)
        return text_rect