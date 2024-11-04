import pygame, time

from PygameTools.modules.surface import Surface
from PygameTools.modules.slider import Slider

class PygameTools:
    """
        PygameTools is a custom framework made for the pygame python module. It was designed to
        streamline the creation of modular pygame programs using simple syntax.
    """
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (100, 100, 100)
    LIGHTGRAY = (200, 200, 200)

    def __init__(self, size: tuple[int, int], color: tuple[int, int, int] = (255, 255, 255)):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.running = True

        self.color = color
        self.surfaces = []
        self.scene = 0
        
        self.mousePressed = False

    def createSurface(self, rect: tuple[int, int, int, int], scene: int, backgroundColor: tuple[int, int, int], scrollable: bool = False, height: int = 0, borderWidth: int = 0, borderColor: tuple[int, int, int] = (0, 0, 0)):
        surface = Surface(rect, scene, backgroundColor, scrollable, height, borderWidth, borderColor)
        self.surfaces.append(surface)
        return surface

    def update(self):
        update = {'type': 'None'}
        keyPressed = pygame.key.get_pressed()
        mousePressed = pygame.mouse.get_pressed()
        
        mousePosition = pygame.mouse.get_pos()
        mouseRect = pygame.Rect(mousePosition[0], mousePosition[1], 1, 1)
        
        
        for surface in reversed(self.surfaces):
            if surface.scene != self.scene or surface.disabled:
                continue

            args = {}
            if True in keyPressed:
                args['keyPressed'] = keyPressed
            if pygame.Rect.colliderect(mouseRect, pygame.Rect(list(surface.position) + [surface.surface.get_rect().width, surface.surface.get_rect().height])):
                args['mouseRect'] = mouseRect
                args['offset'] = surface.offset
                args['position'] = surface.position
            if 1 in mousePressed:
                args['mousePressed'] = mousePressed
            else:
                self.mousePressed = False
            if len(args.keys()) == 0:
                continue

            for obj in reversed(surface.objects):
                try:
                    if hasattr(obj, 'update') and not self.mousePressed:
                        result = obj.update(args)
                    else:
                        result = None
                    if hasattr(obj, 'toggle') and 1 in mousePressed and not self.mousePressed:
                        obj.toggle(args)
                except KeyError:
                    continue
                except Exception as error:
                    raise(error)

                update = result if type(result) is dict else update
                if result:
                    self.mousePressed = True

            if 'mouseRect' in args:
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                update['type'] = 'quit'
                break

            if event.type == pygame.MOUSEWHEEL:
                for surface in self.surfaces:
                    if surface.scrollable and pygame.Rect.colliderect(mouseRect, pygame.Rect(list(surface.position) + [surface.surface.get_rect().width, surface.surface.get_rect().height])):
                        surface.offset[1] = max(min(surface.offset[1] + 10*event.y, 0), -surface.maxOffset)
                        slider = [type(obj) if type(obj) == Slider and obj.surfaceScroll else 0 for obj in surface.objects]
                        slider = slider.index(Slider) if Slider in slider else -1
                        if slider != -1:
                            surface.objects[slider].position = max(min(surface.objects[slider].position-10*event.y*(surface.objects[slider].scrollstep), surface.objects[slider].rect[3]), 0)
        return update

    def draw(self):
        self.screen.fill(self.color)

        for surface in self.surfaces:
            if surface.scene != self.scene or surface.disabled:
                continue
            surface.draw(self.screen)

        update = self.update()
        if update['type'] == 'quit':
            self.running = False
            pygame.quit()
            return update

        if update['type'] == 'changeScene':
            self.scene = update['scene']

        if update['type'] == 'disableSurface':
            update['surface'].disabled = True

        if update['type'] == 'enableSurface':
            update['surface'].disabled = False

        pygame.display.flip()

        self.clock.tick(60)

        return update






