import os
import tkinter as tk
from tkinter import ttk, messagebox
import qrcode

def generate_qr_code():
    ssid = ssid_entry.get()
    key = key_entry.get()
    encryption = encryption_var.get()

    if not ssid or not key or encryption not in ["WPA", "WPA2", "WPA3"]:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs correctement !")
        return

    wifi_data = f"WIFI:T:{encryption};S:{ssid};P:{key};;"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_data)
    qr.make(fit=True)

    output_folder = "Qrcode_générés"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    qr_code_filename = os.path.join(output_folder, f"{ssid}.png")
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(qr_code_filename)

    result_label.config(text="QR Code généré avec succès!")

def prevent_entry_edit(*args):
    encryption_combobox.set(encryption_var.get())

def on_closing():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter?"):
        window.destroy()

window = tk.Tk()
window.title("Générateur de QR Code Wi-Fi")

window.geometry("330x340")

ssid_label = ttk.Label(window, text="SSID du réseau :")
ssid_entry = ttk.Entry(window)

key_label = ttk.Label(window, text="Clé du réseau :")
key_entry = ttk.Entry(window, show="*")

encryption_label = ttk.Label(window, text="Sélectionnez le type de cryptage :")
encryption_var = tk.StringVar(value="WPA")

encryption_combobox = ttk.Combobox(window, textvariable=encryption_var, values=["WPA", "WPA2", "WPA3"])
encryption_combobox.bind("<<ComboboxSelected>>", prevent_entry_edit)

generate_button = ttk.Button(window, text="Générer QR Code", command=generate_qr_code)
result_label = ttk.Label(window, text="")

ssid_label.pack(pady=10)
ssid_entry.pack(pady=5)

key_label.pack(pady=10)
key_entry.pack(pady=5)

encryption_label.pack(pady=10)
encryption_combobox.pack(pady=5)

generate_button.pack(pady=20)
result_label.pack()

window.protocol("WM_DELETE_WINDOW", on_closing)

creator_label = ttk.Label(window, text="Create by M.N")
creator_label.pack()

window.mainloop()
