import tkinter as tk
from PIL import ImageGrab
import threading

def get_mouse_coordinates():
    x, y = root.winfo_pointerxy()
    coordinates_label.config(text=f"X: {x}, Y: {y}")
    if capture_rgb_var.get():
        screenshot = ImageGrab.grab(bbox=(x, y, x + 1, y + 1))
        pixel = screenshot.getpixel((0, 0))
        rgb_label.config(text=f"RGB: {pixel}")

def update_info():
    if running_var.get():
        get_mouse_coordinates()
        root.after(100, update_info)

def start_update():
    if not capture_coordinates_var.get() and not capture_rgb_var.get():
        error_label.config(text="Veuillez cocher au moins une case.")
    else:
        error_label.config(text="")
        running_var.set(True)
        update_info()

def stop_update():
    running_var.set(False)

root = tk.Tk()
root.title("Mouse Cursor Info")
root.geometry("290x165")  # Définir la taille de la fenêtre à 290x165 pixels

coordinates_label = tk.Label(root, text="X: 0, Y: 0")
coordinates_label.pack()

rgb_label = tk.Label(root, text="RGB: N/A")
rgb_label.pack()

capture_coordinates_var = tk.BooleanVar()
capture_coordinates_checkbox = tk.Checkbutton(root, text="Capture Coordinates", variable=capture_coordinates_var)
capture_coordinates_checkbox.pack()

capture_rgb_var = tk.BooleanVar()
capture_rgb_checkbox = tk.Checkbutton(root, text="Capture RGB", variable=capture_rgb_var)
capture_rgb_checkbox.pack()

running_var = tk.BooleanVar()
start_button = tk.Button(root, text="Start", command=start_update)
start_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_update)
stop_button.pack()

error_label = tk.Label(root, text="", fg="red")
error_label.pack()

root.mainloop()
