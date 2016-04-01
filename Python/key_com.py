##The library of functions for keyboard commands, such as
##Typing letters and characters, holding modifier keys and Function keys
import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]
#####################################################
def splitString(phrase):
    typelist = list()
    for i in phrase:
        typelist.append(i)
    return typelist
    
def pressKey(key):
    if (key in keycodes):
        ckey = keycodes.get(key)
    else:
        try:
            ord(key)
        except:
            ckey = key
    
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(ckey, 0x48, 0, 0, ctypes.pointer(extra) )
    x = Input(ctypes.c_ulong(1), ii_ )
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
    
def releaseKey(key):
    if (key in keycodes):
        ckey = keycodes.get(key)
    else:
        try:
            ord(key)
        except:
            ckey = key

    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(ckey, 0x48, 0x0002, 0, ctypes.pointer(extra) )
    x = Input(ctypes.c_ulong(1), ii_ )
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
    
def ctrlMod(key):
    keylist = splitString(key)
    for i in keylist:
        #Press down ctrl
        pressKey(controlkey)
        #Press the key that will be modified by ctrl
        typeKey(i)
        #Release ctrl
        releaseKey(controlkey)
    
#Press a function key
def fKey(key):
    if (key not in functioncodes):
            return
    else:
        ckey = functioncodes.get(key)
        pressKey(ckey)
        releaseKey(ckey)
        time.sleep(0.05)
        
def shiftMod(key):
    #Press shift
    pressKey(shiftkey)
    #Type the key
    typeKey(key)
    #Release shift
    releaseKey(shiftkey)

def tabKey():
    pressKey(tabkey)
    releaseKey(tabkey)
    time.sleep(0.05)

def enterKey():
    pressKey(enterkey)
    releaseKey(enterkey)
    time.sleep(0.05)
    
def typeKey(key):
    keylist = splitString(key)
    for i in keylist:
        #If i is a capital letter
        if(ord(i) < 91 and ord(i) > 64):
            i = chr(ord(i)+32)
            shiftMod(i)
        #A number key modifier
        elif(i in shiftcodes):
            i = shiftcodes.get(i)
            shiftMod(i)
        else:
            pressKey(i)
            releaseKey(i)            
        time.sleep(0.05)

#The dictionary containing all of the keys and their hex code (Virtual Key-Codes)
keycodes = {' ':0x20,'a':0x41,'b':0x42,'c':0x43,'d':0x44,'e':0x45,'f':0x46,
            'g':0x47,'h':0x48,'i':0x49,'j':0x4A,'k':0x4B,'l':0x4C,'m':0x4D,
            'n':0x4E,'o':0x4F,'p':0x50,'q':0x51,'r':0x52,'s':0x53,'t':0x54,
            'u':0x55,'v':0x56,'w':0x57,'x':0x58,'y':0x59,'z':0x5A,'0':0x30,
            '1':0x31,'2':0x32,'3':0x33,'4':0x34,'5':0x35,'6':0x36,'7':0x37,
            '8':0x38,'9':0x39,'-':0x6D,'.':0x6E,'/':0xBF,';':0xBA,',':0xBC,'\'':0xDE,
            "\\":0xDC,'[':0xDB,']':0xDD,'-':0xBD}

functioncodes = {'F1':0x70,'F2':0x71,'F3':0x72,'F4':0x73,'F5':0x74,'F6':0x75,
                'F7':0x76,'F8':0x77,'F9':0x78,'F10':0x79,'F11':0x7A,'F12':0x7B}

shiftcodes = {'!':'1','@':'2','#':'3','$':'4','%':'5','^':'6','&':'7','*':'8',
              '(':'9',')':'0','?':'/','\"':'\'','|':'\\','{':'[','}':']','_':'-'}

shiftkey = 0x10
controlkey = 0x11
enterkey = 0x0D
tabkey = 0x09
