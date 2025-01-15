import keyboard
import pyautogui
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import json
import threading
import os
import time

shortcuts = {}
file_name = os.path.join(os.path.expanduser("~"), "Documents", "shortcuts.json")  # Save in Documents folder
pressed_keys = set()
listener_running = True

# Save to file
def save_shortcuts():
    with open(file_name, "w") as file:
        json.dump(shortcuts, file)
    messagebox.showinfo("Success", f"Shortcuts saved to {file_name}")

# Load from file
def load_shortcuts():
    global shortcuts
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            shortcuts = json.load(file)
    else:
        shortcuts = {}

# Load from a specified file
def load_from_file():
    global shortcuts
    file_path = filedialog.askopenfilename(title="Select Shortcut File", filetypes=[("JSON Files", "*.json")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                shortcuts = json.load(file)
            update_listbox()
            messagebox.showinfo("Success", f"Shortcuts loaded from {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")

# Normalize key names
def normalize_key(key_name):
    if key_name in ['alt_l', 'alt_r']:
        return 'alt'
    elif key_name in ['ctrl_l', 'ctrl_r', 'control']:
        return 'ctrl'
    elif key_name in ['shift_l', 'shift_r']:
        return 'shift'
    return key_name

# Parse combination to standard format
def parse_combination(keys):
    normalized_keys = [normalize_key(key) for key in keys]
    combo = "+".join(sorted(normalized_keys))
    return combo

# Listen for shortcuts
def listen_shortcuts():
    def on_key_event(e):
        key_name = e.name if hasattr(e, 'name') else e.char
        if key_name:
            if e.event_type == keyboard.KEY_DOWN:
                normalized_key = normalize_key(key_name.lower())
                pressed_keys.add(normalized_key)
                combo = parse_combination(pressed_keys)

                # Check if the combination matches
                if combo in shortcuts:
                    action = shortcuts[combo]
                    if action.startswith("type:"):
                        wait_for_modifier_release()
                        execute_action(action)
                    else:
                        execute_action(action)
            elif e.event_type == keyboard.KEY_UP:
                normalized_key = normalize_key(key_name.lower())
                pressed_keys.discard(normalized_key)

    keyboard.hook(on_key_event)
    keyboard.wait()


# Wait for modifier keys released before executing
def wait_for_modifier_release():
    last_print_time = time.time()
    while keyboard.is_pressed('ctrl') or keyboard.is_pressed('shift') or keyboard.is_pressed('alt'):
        if time.time() - last_print_time >= 1:
            print("Modifier keys still pressed...")
            last_print_time = time.time()


# Execute action
def execute_action(action):
    if action.startswith("open:"):
        file_to_open = action[5:]
        file_to_open = file_to_open.replace("\\", "/")
        if " " in file_to_open:
            file_to_open = f'"{file_to_open}"'
            
        os.system(f'start "" {file_to_open}')
    elif action.startswith("type:"):
        text = action[5:]
        pyautogui.write(text)

# Validate key combination syntax
def is_valid_combo(combo):
    valid_keys = {'alt', 'ctrl', 'shift', 'cmd'}
    keys = combo.split("+")
    is_valid = all(key.isalnum() or key in valid_keys for key in keys)
    return is_valid

# Validate action syntax
def is_valid_action(action):
    is_valid = action.startswith("open:") or action.startswith("type:")
    return is_valid

# Add new shortcut
def add_shortcut():
    combo = simpledialog.askstring("Add Shortcut", "Enter key combination (e.g., ctrl+n):")
    if not combo or not is_valid_combo(combo.lower()):
        messagebox.showerror("Error", "Invalid key combination syntax. Use format like 'ctrl+n'.")
        return

    action = simpledialog.askstring("Add Shortcut", "Enter action (e.g., open:path or type:text):")
    if not action or not is_valid_action(action):
        messagebox.showerror("Error", "Invalid action syntax. Use 'open:path' or 'type:text'.")
        return

    shortcuts[combo.lower()] = action
    update_listbox()

# Update the listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for combo, action in shortcuts.items():
        listbox.insert(tk.END, f"{combo}: {action}")

# Delete selected shortcut
def delete_shortcut():
    selected = listbox.curselection()
    if selected:
        combo = listbox.get(selected[0]).split(":")[0]
        del shortcuts[combo]
        update_listbox()

# Tkinter GUI
root = tk.Tk()
root.title("Custom Shortcut Manager")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack(side=tk.LEFT, padx=5)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

btn_add = tk.Button(button_frame, text="Add Shortcut", command=add_shortcut)
btn_add.grid(row=0, column=0, padx=5)

btn_delete = tk.Button(button_frame, text="Delete Shortcut", command=delete_shortcut)
btn_delete.grid(row=0, column=1, padx=5)

btn_save = tk.Button(button_frame, text="Save Shortcuts", command=save_shortcuts)
btn_save.grid(row=0, column=2, padx=5)

btn_load = tk.Button(button_frame, text="Load from File", command=load_from_file)
btn_load.grid(row=0, column=3, padx=5)

load_shortcuts()
update_listbox()

listener_thread = threading.Thread(target=listen_shortcuts, daemon=True)
listener_thread.start()

root.mainloop()