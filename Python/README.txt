General installation and running:
- Python 3 is required and all libraries must be python 3 compatible
- Library dependencies:
  - Pillow
- All libraries can be obtained easily from the pip command (https://pypi.python.org/pypi/pip)
  - Any Unix package should be able to find pip (sudo apt-get install pip)
- All of the python programs can be run from the command line with "python3 <File Name>" or "python <File Name" (if python 3 is default).

Descriptions for each of the files:
### imageOperations.py ###
Requires a base image and makes a new image either outlined or grey scaled.
Prompts the user for the operation to be performed and then the path to the image.

### mouse_com.py ###
Windows only.
This is a library that automates mouse button pressing.
Possible functions to call:
  leftClick(seconds) (Clicks the left mouse button with a default 0.1 second delay)
  leftDown()         (Holds the left mouse button down until leftUp is called)
  leftUp()           (Lifts up the left mouse button)
  move(x, y)         (Moves the mouse to the specified x,y coordinate on the screen)
  scrollWheelDown()  (Moves the mouse wheel down one click)
  scrollWheelUp()    (Moves the mouse wheel up one click)


### key_com.py ###
Windows only.
This is a library that automates keyboard key strokes.
Possible functions to call:
  typeKey(key)  (Types the string specified by key)
  ctrlMod(key)  (Same as typeKey, but holds the control key down as well)
  fKey(key)     (Presses a single function key using F1 to F12)
  shiftMod(key) (Same as typeKey, but holds the shift key down as well)
  tabKey()      (Presses the tab key)
  enterKey()    (Presses the enter key)

*Note: Both of the command libraries can be easily tested by giving the -i option on the command line.
