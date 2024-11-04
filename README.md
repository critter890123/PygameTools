# Pygame Tools

Created By: **Christopher Carlo**

PygameTools is a custom framework made for the pygame python module. It was designed to
streamline the creation of modular pygame programs using simple syntax.

----------------------------------

## Table of Contents

- [Getting Started](#getting-started)
- [Examples](#examples)
- [Documentation](#documentation)
	- [PygameTools](#pygametools)
	- [Surface](#surface)
	- [PygameTools Object](#object)
	- [Button](#button)
	- [Slider](#slider)
	- [Textbox](#textbox)
	- [Text](#text)
	- [Dropdown](#dropdown)

---

## Getting started:

A basic program that will create a screen with size 500x500 is as follows:

	from PygameTools.main import PygameTools

	screen = PygameTools((500, 500))
	while screen.running:
		update = screen.draw()

	pygame.quit()

`from PygameTools.main import PygameTools` -> 
This will import the PygameTools module.

`screen = PygameTools((width, height), color: tuple = (255, 255, 255))` ->
This will initialize the PygameTools module and create a screen
with a size of `width` pixels by `height` pixels where width and height
are both `int` values. In the above example, these values are `500` and `500`.

`while screen.running:` ->
`screen.running` is a built in variable that is initialized as `True` 
and will become `False` in the event that the screen is closed.

`update = screen.draw()` ->
`screen.draw()` will handle the updating and drawing of all intialized `Surfaces`
as well as any screen updates and user input.

`pygame.quit()` ->
Ensures `pygame` is cleanly closed to prevent errors.

---

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

[`PygameTools.createSurface(rect: tuple, scene: int, backgroundColor: tuple, scrollable: bool = False, height: int = 0, borderWidth: int = 0, borderColor: tuple = (0, 0, 0))`](#surface)

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

> `borderWidth` -> `int` ->
Defines the width of the border of the `Surface`.

> `borderColor` -> `(red, green, blue)` ->
Defines the color of the border of the `Surface`.
Defaults to `BLACK`.

`PygameTools.draw()`

> This is used for updating any currently active `Surface` as well as drawing them to the display.
This will automatically handle any prebuilt `pygame` events (i.e. keyPressed, mousePressed, etc.) as
well custom events.

> returns a `dict` -> 
defaults to: `{'type': 'None'}`

---------------------------------------

### Surface:

`Surface.updateHeight(newHeight: int)`

> Updates the true height of the `Surface` and the `scrollable` flag.

> `newHeight` -> `int` -> 
Defines the new height of the `Surface`.

[`Surface.createButton(font: pygame.font, rect: tuple, text: str, buttonColor: tuple, textColor: tuple = (0, 0, 0), borderWidth: int = 0, borderColor: tuple = (0, 0, 0))`](#button)

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
Defines the color of the `text` of the `Button`. Defaults to `BLACK`.

> `borderWidth` -> `int` ->
Defines the width of the border of the `Button`.

> `borderColor` -> `(red, green, blue)` ->
Defines the color of the border of the `Button`.
Defaults to `BLACK`.

[`Surface.createSlider(rect: tuple, barColor: tuple, sliderColor: tuple, surfaceScroll: bool = True, vertical: bool = True)`](#slider)

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

[`Surface.createTextbox(font: pygame.font, rect: tuple, backgroundColor: tuple, textColor: tuple = (0, 0, 0), placeholder: str = "")`](#textbox)

> Creates a `Textbox` on the current `Surface` used for getting `textInput`.
Any text is stored to `Textbox.text`.

> `font` -> `pygame.font` -> 
Defines the font used for displaying the `Text` in the `Textbox`.

> `rect` -> `(x, y, width, height)` ->
Defines the parameters of drawing the `Textbox` to the `Surface`.

> `backgroundColor` -> `(red, green, blue)` ->
Defines the background color for the `Textbox`. In most cases,
this will ideally be the background color of the `Surface` the `Textbox` is a part of.

> `textColor` -> `(red, green, blue)` ->
Defines the color of the `Text` displayed within the `Textbox`. Defaults to `BLACK`.

> `placeholder` -> `str` ->
Defines the `Text` that will be displayed within the `Textbox` when there
is no text inputted. Defaults to an empty `str`.

[`Surface.createText(font: pygame.font, rect: tuple, color: tuple, text: str, center: bool = True, maxWidth: int = None)`](#text)

> Creates a `Text` object on the current `Surface`. Supports the use of newline characters `\n`.

> `font` -> `pygame.font` ->
Defines the font used for displaying the `Text` to the `Surface`.

> `rect` -> `(x, y)` ->
Defines the parameters of drawing the `Text` to the `Surface`.

> `color` -> `(red, green, blue)` ->
Defines the color of the `Text`.

> `text` -> `str` ->
This is the text that will be displayed to the `Surface`.

[`Surface.createDropdown(font: pygame.font, rect: tuple, options: list, backgroundColor: tuple, textColor: tuple = (0, 0, 0), placeholder: str = None, borderWidth: int = 0, borderColor: tuple = (0, 0, 0))`](#dropdown)

> Creates a vertical `Dropdown` menu that displays a list of pressable options. 

> `font` -> `pygame.font` -> 
Defines the font used for displaying the `Text` to the `Dropdown`.

> `rect` -> `(x, y, width, height)` ->
Defines the parameters of drawing the `Dopdown` to the `Surface`.

> `options` -> `[option1, option2, ...]` ->
Defines the `list` of selectable options displayed in the `Dropdown`. 
Each of the options should be a `str` value.

> `backgroundColor` -> `(red, green, blue)` ->
Defines the background color for the `Dropdown` menu. 

> `textColor` -> `(red, green, blue)` -> 
Defines the color of the `Text` displayed within the `Dropdown`.

> `placeholder` -> `str` ->
Defines the `Text` that will be displayed on top of the `Dropdown` when there
is no option selected. Defaults to the first entry in `options`.

> `borderWidth` -> `int` ->
Defines the width of the border of the `Dropdown`.

> `borderColor` -> `(red, green, blue)` ->
Defines the color of the border of the `Dropdown`.
Defaults to `BLACK`.

[`Surface.addObject(object)`](#object)

> Adds the ability to add a custom `object` to the current `Surface`.

> The `object` should have the following functions to work properly with `PygameTools`:
`Object.draw()` and `Object.update()`. Each of these functions will be automatically
called by `PygameTools.draw()`.

---

### Object:

`Object.update(args: dict)`  

> The base function responsible for updating the object in the event of an update
such as user input. This function is automatically called by `PygameTools.update()`
as long as the `Surface` it is a part of is not `deactivated` or out of `scene`.

> `args` -> `dict` -> 
This `dict` is automatically created by `PygameTools.update()` and contains
the relevant event information. For example, if a mouse button is pressed and the mouse
is hovering above the `Surface` this object is a part of, `args` will be equal to
`{'mouseRect': mouseRect, 'offset': surface.offset, 'position': surface.position, 'mousePressed': mousePressed}`

`Object.toggle(args: dict)`

> This function is only called by `PygameTools.update()` when a `mouseButton` is pressed.
Helpful for `Objects` that contain elements that should stay activated until manually deactivated,
such as a `Textbox` or a `Dropdown`.

> `args` -> `dict` -> 
This `dict` is automatically created by `PygameTools.update()` and contains
the relevant event information.

`Object.draw(screen: pygame.Surface, offset: list)`

> The base function for drawing the object to the `screen`. This function is automatically called
by `PygameTools.draw()` as long as the `Surface` it is a part of is not `deactivated` or out of `scene`.

> `screen` -> `pygame.Surface` ->
This is the `pygame.Surface` object of the `Surface` that the `object` is a part of.

> `offset` -> `[x, y]` -> 
This is the horizontal and vertical offsets of the `Surface` the `object` is a part of.
These values are only changed when the `Surface` is scrollable and the `mousewheel` is scrolled
or a `Slider` is binded to the `Surface` and it is adjusted.

---

### Button:

Useful variables:

`Button.on_pressed`

> `dict` -> Defines the behavior of the `Button` when pressed. 
This should be in the format of `{'type': type, ...}`.

> Built in behavior -> Changing scene: `{'type': 'changeScene', 'scene': scene}` where `scene` is an `int`.
This will automatically change the `scene` when the `Button` is pressed.

> Built in behavior -> Disabling Surface: `{'type': 'disableSurface', 'surface': surface}` where `surface` is a `<PygameTools.Surface> object`.
This will automatically disable a `surface` when the `Button` is pressed. That `surface` will not longer be drawn or updated
until it is enabled again.

> Built in behavior -> Enabling Surface: `{'type': 'enableSurface', 'surface': surface}` where `surface` is a `<PygameTools.Surface> object`.
This will automatically enable a `surface` when the `Button` is pressed. 

---

### Slider:

Useful variables:

`Slider.position`

> `int` ->
Defines the vertical or horizontal position of the `Slider`. Can be used for getting
user input from a `Slider`.

Useful functions:

`Slider.bind_surface(surface)`

> Defines which `Surface` the `Slider` should ajust the scroll of.

>If the `Surface.scrollable` value is `True` the `Slider` will automatically
be adjusted when the `mousewheel` is scrolled and the `Surface` scroll
value will be automatically adjusted when the `Slider` is adjusted.

---

### Textbox:

Useful variables:

`Textbox.text`

> `str` ->
Defines the current `Text` in the `Textbox`. Can be used for reading user input
from a `Textbox`.

---

### Text:

Useful variables:

`Text.text`

> `str` ->
Defines the current `Text` displayed. Can be used for creating dynamic `Text`.

---

### Dropdown:

Useful Variables:

`Dropdown.selectedOption`

> `str` ->
Defines the current selected option in the `Dropdown`. Can be used for reading user input
from a `Dropdown`.

`Dropdown.options`

> `[option1, option2, ...]` ->
Defines the list of pressable options in the `Dropdown`. Can be used for creating a dynamic
list of options in a `Dropdown`.

---