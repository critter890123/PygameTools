import pygame

class Slider:
    def __init__(self, rect: tuple[int, int, int, int], barColor: tuple[int, int, int], sliderColor: tuple[int, int, int], surfaceScroll: bool = True, vertical: bool = True):
        self.barColor = barColor
        self.sliderColor = sliderColor
        self.rect = rect
        self.vertical = vertical
        self.surfaceScroll = surfaceScroll

        self.bind = False
        self.position = 0

    def bind_surface(self, surface):
        self.bind = True
        self.step = surface.maxOffset/self.rect[3]
        self.scrollstep = self.rect[3]/surface.maxOffset
        self.scene = surface

    def update(self, args: dict):
        if not self.surfaceScroll:
            args['mouseRect'].x += args['offset'][0]
            args['mouseRect'].y += args['offset'][1]

        if pygame.Rect.colliderect(args['mouseRect'], (self.rect[0]-self.rect[2], self.rect[1], self.rect[2]*3, self.rect[3])) and args['mousePressed'][0]:
            self.position = args['mouseRect'].y - self.rect[1] if self.vertical else args['mouseRect'].x - self.rect[0]

            if self.bind:
                self.scene.offset[1] = (-self.step)*self.position

    def draw(self, screen: pygame.Surface, offset: list[int, int]):
        sliderRect = (
            (self.rect[0]-self.rect[2], self.rect[1]+self.position, self.rect[2]*3, self.rect[2]*2)
            if self.vertical else
            (self.rect[0]+self.position, self.rect[1]-self.rect[3], self.rect[3]*2, self.rect[3]*3)
            )

        sliderRect = [position+offset for position, offset in zip(sliderRect[:2], offset)] + list(sliderRect[2:]) if not self.surfaceScroll else sliderRect
        rect = [position+offset for position, offset in zip(self.rect[:2], offset)] + list(self.rect[2:])

        pygame.draw.rect(screen, self.barColor, rect if not self.surfaceScroll else self.rect)
        pygame.draw.rect(screen, self.sliderColor, sliderRect)