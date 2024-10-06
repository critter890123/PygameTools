import pygame

from PygameTools.modules.surface import Surface
from PygameTools.modules.slider import Slider

class PygameTools:
    """
        PygameTools is a custom framework made for the pygame python module. It was designed to
        streamline the creation of modular pygame programs using simple syntax.
    """
    def __init__(self, size: tuple[int, int], color: tuple[int, int, int] = (255, 255, 255)):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.running = True

        self.color = color
        self.surfaces = []
        self.scene = 0

    def createSurface(self, rect: tuple[int, int, int, int], scene: int, backgroundColor: tuple[int, int, int], scrollable: bool = False, height: int = 0):
        surface = Surface(rect, scene, backgroundColor, scrollable, height)
        self.surfaces.append(surface)
        return surface

    def update(self):
        update = {'type': 'None'}
        keyPressed = pygame.key.get_pressed()
        mousePressed = pygame.mouse.get_pressed()
        
        mousePosition = pygame.mouse.get_pos()
        mouseRect = pygame.Rect(mousePosition[0], mousePosition[1], 1, 1)
        
        for surface in self.surfaces:
            if surface.scene != self.scene:
                continue

            args = {}
            if True in keyPressed:
                args['keyPressed'] = keyPressed
            if pygame.Rect.colliderect(mouseRect, pygame.Rect(list(surface.position) + [surface.surface.get_rect().width, surface.surface.get_rect().height])):
                args['mouseRect'] = mouseRect
                args['offset'] = surface.offset
            if 1 in mousePressed:
                args['mousePressed'] = mousePressed
            if len(args.keys()) == 0:
                continue

            for obj in surface.objects:
                if hasattr(obj, 'toggle') and 1 in mousePressed:
                    obj.toggle({'mouseRect': mouseRect, 'offset': surface.offset})

                try:
                    result = obj.update(args)
                except Exception as error:
                    continue
                update = result if not result is None else update

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                update['type'] = 'quit'
                break

            if event.type == pygame.MOUSEWHEEL:
                for surface in self.surfaces:
                    if surface.scrollable and pygame.Rect.colliderect(mouseRect, surface.surface.get_rect()):
                        surface.offset[1] = max(min(surface.offset[1] + 10*event.y, 0), -surface.maxOffset)
                        slider = [type(obj) if type(obj) == Slider and obj.surfaceScroll else 0 for obj in surface.objects]
                        slider = slider.index(Slider) if Slider in slider else -1
                        if slider != -1:
                            surface.objects[slider].position = max(min(surface.objects[slider].position-10*event.y*(surface.objects[slider].scrollstep), surface.objects[slider].rect[3]), 0)

        return update

    def draw(self):
        self.screen.fill(self.color)

        for surface in self.surfaces:
            if surface.scene == self.scene:
                surface.draw(self.screen)

        update = self.update()
        if update['type'] == 'quit':
            self.running = False
            pygame.quit()
            return update

        if update['type'] == 'sceneChange':
            self.scene = update['scene']

        pygame.display.flip()

        self.clock.tick(60)  # limits FPS to 60

        return update






