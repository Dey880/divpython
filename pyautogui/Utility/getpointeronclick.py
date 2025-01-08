from pynput import mouse, keyboard

def on_click(x, y, key, pressed):
    if pressed:
        print(f'Pointer position on click: ({x}, {y})')
        
def on_press(key):
    if key == keyboard.Key.esc:
        print("\nExiting...")
        listener.stop()
        return False
        
listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)

listener.start()
keyboard_listener.start()
listener.join()