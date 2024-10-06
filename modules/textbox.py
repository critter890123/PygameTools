import pygame, time, math

from PygameTools.modules.text import Text

def getKeys(keyPressed: list[bool]):
    keys_pressed = []
        
    for i, key in enumerate(keyPressed):
        if key:
            if i >= 4 and i <= 29:
                keys_pressed.append(keys["letters"][i-4])
            elif i >= 30 and i <= 39:
                keys_pressed.append(keys["nums"][i-30])
            elif str(i) in keys.keys():
                keys_pressed.append(keys[str(i)])
                
    return keys_pressed

keys = {
    "letters": ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
    "nums": ["1","2","3","4","5","6","7","8","9","0"],
    "42": "backspace",
    "44": "space",
    "225": "shift"
    }


class TextBox:
    def __init__(self, font: pygame.font, rect: tuple[int, int, int, int], backgroundColor: tuple[int, int, int], textColor: tuple[int, int, int], placeholder: str = ""):
        self.placeholder = placeholder
        self.text = ""
        self.font = font
        self.textColor = textColor
        self.backgroundColor = backgroundColor
        self.rect = rect
            
        self.selected = False
        self.timer = time.time()

        self.keyTimer = time.time()
        self.lastKey = None

    def toggle(self, args: dict):
        args['mouseRect'].x -= args['offset'][0]
        args['mouseRect'].y -= args['offset'][1]

        if pygame.Rect.colliderect(pygame.Rect(self.rect), args['mouseRect']):
            self.selected = True
        else:
            self.selected = False

    def update(self, args: dict):
        keys = getKeys(args['keyPressed'])
        if len(keys) == 0:
            self.keyTimer -= 0.15
            return

        if self.selected and (self.lastKey is None or self.lastKey != keys[0] or (time.time() - self.keyTimer > 0.15)):
            self.keyTimer = time.time()
            self.lastKey = keys[0]

            caps = True if "shift" in keys else False
                
            if keys[0] == "shift":
                return
            if keys[0] == "backspace":
                if len(self.text) > 0:
                    self.text = self.text[:-1]
            elif keys[0] == "space":
                self.text += " "
            else:
                self.text += keys[0] if not caps else keys[0].upper()

    def timerUpdate(self):
        self.timer = time.time()
        if math.floor(self.timer) % 2 == 0:
            return True
        else:
            return False

    def draw(self, screen: pygame.Surface, offset: list[int, int]):
        textRect = (self.rect[0]+5, self.rect[1]+5)
        text = (self.text if self.text != "" else self.placeholder) + (" |" if self.selected and self.timerUpdate() else "")

        rect = [position+offset for position, offset in zip(self.rect[:2], offset)] + list(self.rect[2:])
        
        pygame.draw.rect(screen, self.backgroundColor, rect)
        pygame.draw.rect(screen, (0, 0, 0) if not self.backgroundColor == ("black" or (0, 0, 0)) else (255, 255, 255), rect, 2)

        Text(self.font, self.textColor, text, textRect, False, self.rect[2]-20).draw(screen, offset)


        