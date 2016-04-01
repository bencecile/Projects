import ctypes
import time

def leftClick(seconds=0.1):
    """
    Use the x and y coordinates as where you want to click.
    """
    leftDown()
    leftUp()
    time.sleep(seconds)

def leftDown():
    """
    The x and y coordinates are where it will start to press
    """
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down

def leftUp():
    """
    Only lets the mouse button up
    """
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

def move(xcoord, ycoord):
    ctypes.windll.user32.SetCursorPos(xcoord, ycoord)

def scrollWheelDown():
    #Move the mouse wheel down one click
    ctypes.windll.user32.mouse_event(0x0800, 0, 0, -120,0)

def scrollWheelUp():
    #Move the mouse wheel up one click
    ctypes.windll.user32.mouse_event(0x0800, 0, 0, 120,0)
