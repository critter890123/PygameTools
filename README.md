# Pygame Tools

Created By: **Christopher Carlo**

PygameTools is a custom framework made for the pygame python module. It was designed to
streamline the creation of modular pygame programs using simple syntax.

----------------------------------

## Getting started:

A basic program that will create a screen with size 500x500 is as follows:

	from PygameTools.main import PygameTools

	screen = PygameTools((500, 500))
	while screen.running:
		update = screen.draw()

`from PygameTools.main import PygameTools` -> 
This will import the PygameTools module.

`screen = PygameTools((width, height), color: tuple = (255, 255, 255))` ->
This will initialize the PygameTools module and create a screen
with a size of `width` pixels by `height` pixels where width and height
are both `int` values. In the above example, these values are `500` and `500`.

`while screen.running:` ->
PygameTools has a built in variable `self.running` that is initialized
as `True` and will become `False` in the event that the screen is closed.

`update = screen.draw()` ->
`screen.draw()` will handle the updating and drawing of all intialized scenes
as well as any screen updates.

------------------------------------

## Examples:

### Creating a scrollable Sidebar with a Slider:

	# Import PygameTools and pygame
	import pygame
	from PygameTools.main import PygameTools

	# Initialize PygameTools with a size of (500, 500)
	screen = PygameTools((500, 500))

	# Create a font for drawing text
	font = pygame.font.SysFont('Comic Sans MS', 20)

	# Create the scrollable sidebar
	# rect = (0, 0, 200, 500), scene = 0
	# backgroundColor = (100, 100, 100)
	# scrollable = True, height = 1000
	sideBar = screen.createSurface((0, 0, 200, 500), 0, (100, 100, 100), True, 1000)

	sideBar.createText(font, (100, 100), (0, 0, 0), "Scroll Me!")

	# Create the slider
	# rect = (170, 50, 10, 400)
	# barColor = (80, 80, 80), sliderColor = (60, 60, 60)
	slider = sideBar.createSlider((170, 50, 10, 400), (80, 80, 80), (60, 60, 60))
	
	# Bind the slider to the sideBar surface
	slider.bind_surface(sideBar)
	
	# Main loop
	while screen.running:
		update = screen.draw()

------------------------------------

## Documentation:

### PygameTools:
`PygameTools(size: tuple, color: tuple = (255, 255, 255))`

> Initializes `pygame` and creates the display. This is the base of
creating a program using PygameTools.

>`size` -> `(width, height)` -> 
Defines the width and height of the `pygame` display.

> `color` -> `(red, green, blue)` ->
Defines the background color of the display. Defaults to `(255, 255, 255)` or white.

`PygameTools.createSurface(rect: tuple, scene: int, backgroundColor: tuple, scrollable: bool = False, height: int = 0)`

> Creates a `Surface` that is a child of the `PygameTools` object.
This initializes a new `pygame.Surface` object and is where all `Surface` objects
(i.e. Button, Textbox, Slider, etc.) will be drawn.

>`rect` -> `(x, y, width, height)` -> 
Defines the parameters of drawing the `Surface` to the screen.

> `scene` -> `int` -> 
Defines which scene this Surface is a part of. Used for easily
switching between different menus/environments. `PygameTools` initially starts at
`self.scene = 0`.

> `backgroundColor` -> `(red, green, blue)` -> 
This is the color that will used to fill the `Surface`.

> `scrollable` -> `bool (True/False)` -> 
Defines whether or not scrolling with a mouse should affect this `Surface`. 
Defaults to `False`. Note: `height` should be greater than the `rect` height, 
otherwise this value will automatically be `False`.

> `height` -> `int` -> 
The true height of the `Surface`. This is used for scrolling the `Surface`. 
Defaults to `0`.

`PygameTools.draw()`

> This is used for updating any currently active `Surface` as well as drawing them to the display.
This will automatically handle any prebuilt `pygame` events (i.e. keyPressed, mousePressed, etc.) as
well custom events.

> returns a `dict` -> 
defaults to: `{'type': 'None'}`

---------------------------------------

### Surface:

`Surface.createButton(font: pygame.font, rect: tuple, text: str, buttonColor: tuple, textColor: tuple)`

> Creates a pressable `Button` on the current `Surface`.

> `font` -> `pygame.font` -> 
Defines the font used for displaying the `Text` in the `Button`.

> `rect` -> `(x, y, width, height)` ->
Defines the parameters of drawing the `Button` to the `Surface`.

> `text` -> `str` ->
The `Text` that will be displayed within the `Button`.

> `buttonColor` -> `(red, green, blue)` ->
Defines the background color of the `Button`.

> `textColor` -> `(red, green, blue)` ->
Defines the color of the `text` of the `Button`.

`Button.on_pressed = dict`

> Defines the behavior of the `Button` when pressed. The `dict` should
be in the format of `{'type': type, ...}`

> Built in behavior -> `{'type': 'sceneChange', 'scene': scene}` where `scene` is an `int`.
This will automatically change the `scene` when the `Button` is pressed.

`Surface.createSlider(rect: tuple, barColor: tuple, sliderColor: tuple, surfaceScroll: bool = True, vertical: bool = True)`

> Creates a `Slider` on the current `Surface`. This `Slider` can be used
for adjusting the scroll of the `Surface` if `surfaceScroll = True`.

> `rect` -> `(x, y, width, height)` ->
Defines the parameters of drawing the `Slider` to the `Surface`.

> `barColor` -> `(red, green, blue)` ->
Defines the color of the background bar of the `Slider`.

> `sliderColor` -> `(red, green, blue)` ->
Defines the color of the foreground slider of the `Slider`.

> `surfaceScroll` -> `boll (True/False` ->
Defines the bahvior of adjusting the `Slider`. Defaults to `True`.
When `surfaceScroll = True`, the `Slider` will not move when the `Surface` is scrolled
and the position of the `Slider` will be automatically adjusted.

> `vertical` -> `bool (True/False)` ->
Defines whether the `Slider` is vertical, `True`, or horizontal, `False`.

`Slider.bind_surface(surface)`

> Defines which `Surface` the `Slider` should ajust the scroll of.

>If the `Surface.scrollable` value is `True` the `Slider` will automatically
be adjusted when the `mousewheel` is scrolled and the `Surface` scroll
value will be automatically adjusted when the `Slider` is adjusted.

`Surface.createTextbox(font: pygame.font, rect: tuple, backgroundColor: tuple, textColor: tuple, placeholder: str = "")`

> Creates a `Textbox` on the current `Surface` used for getting `textInput`.
Any text is stored to `Textbox.text`.

> `font` -> `pygame.font` -> 
Defines the font used for displaying the `Text` in the `Button`.

> `rect` -> `(x, y, width, height)` ->
Defines the parameters of drawing the `Button` to the `Surface`.

> `backgroundColor` -> `(red, green, blue)` ->
Defines the background color for the `Textbox`. In most cases,
this will ideally be the background color of the `Surface` the `Textbox` is a part of.

> `textColor` -> `(red, green, blue)` ->
Defines the color of the `Text` displayed within the `Textbox`.

> `placeholder` -> `str` ->
Defines the `Text` that will be displayed within the `Textbox` when there
is no text inputted. Defaults to an empty `str`.

`Surface.createText(font: pygame.font, rect: tuple, color: tuple, text: str, center: bool = True, maxWidth: int = None)`

> Creates a `Text` object on the current `Surface`.

> `font` -> `pygame.font` ->
Defines the font used for displaying the `Text` to the `Surface`.

> `rect` -> `(x, y)` ->
Defines the parameters of drawing the `Text` to the `Surface`.

> `color` -> `(red, green, blue)` ->
Defines the color of the `Text`.

> `text` -> `str` ->
This is the text that will be displayed to the `Surface`.


`Surface.addObject(object)`

> Adds the ability to add a custom `object` to the current `Surface`.

> The `object` should have the following functions to work properly with `PygameTools`:
`Object.draw()` and `Object.update()`. Each of these functions will be automatically
called by `PygameTools.draw()`.

`Object.draw(screen: pygame.Surface, offset: list)`

> `screen` -> `pygame.Surface` ->
This is the `pygame.Surface` object of the `Surface` that the `object` is a part of.

> `offset` -> `[x, y]` -> 
This is the horizontal and vertical offsets of the `Surface` the `object` is a part of.
These values are only changed when the `Surface` is scrollable and the `mousewheel` is scrolled.

`Object.update(args: dict)`  

> `args` -> `dict` -> 
This `dict` is automatically created by `PygameTools.update()` and contains
the relevant event information. For example, if a mouse button is pressed and the mouse
is hovering above the `Surface` this object is a part of, `args` will be
`{'mousePressed': mousePressed, 'mouseRect': mouseRect, 'offset': surface.offset}`