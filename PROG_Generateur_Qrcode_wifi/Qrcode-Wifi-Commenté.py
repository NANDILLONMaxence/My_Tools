# Importation des modules nécessaires
import os
import tkinter as tk
from tkinter import ttk, messagebox
import qrcode

# Fonction pour générer un QR Code à partir des informations du réseau Wi-Fi
def generate_qr_code():
    # Récupération des données du formulaire
    ssid = ssid_entry.get()
    key = key_entry.get()
    encryption = encryption_var.get()

    # Vérification des champs obligatoires
    if not ssid or not key or encryption not in ["WPA", "WPA2", "WPA3"]:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs correctement !")
        return

    # Construction des données du réseau Wi-Fi au format requis par le QR Code
    wifi_data = f"WIFI:T:{encryption};S:{ssid};P:{key};;"

    # Configuration du QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Ajout des données au QR Code
    qr.add_data(wifi_data)
    qr.make(fit=True)

    # Création du dossier de sortie s'il n'existe pas
    output_folder = "Qrcode_générés"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Sauvegarde du QR Code sous un nom de fichier basé sur le SSID du réseau
    qr_code_filename = os.path.join(output_folder, f"{ssid}.png")
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(qr_code_filename)

    # Mise à jour de l'étiquette de résultat
    result_label.config(text="QR Code généré avec succès!")

# Fonction pour empêcher l'édition de la combobox lors de la sélection
def prevent_entry_edit(*args):
    encryption_combobox.set(encryption_var.get())

# Fonction appelée lors de la fermeture de la fenêtre
def on_closing():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter?"):
        window.destroy()

# Création de la fenêtre principale
window = tk.Tk()
window.title("Générateur de QR Code Wi-Fi")
window.geometry("330x340")

# Création des éléments d'interface utilisateur
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

# Organisation des éléments dans la fenêtre
ssid_label.pack(pady=10)
ssid_entry.pack(pady=5)

key_label.pack(pady=10)
key_entry.pack(pady=5)

encryption_label.pack(pady=10)
encryption_combobox.pack(pady=5)

generate_button.pack(pady=20)
result_label.pack()

# Configuration de l'action de fermeture de la fenêtre
window.protocol("WM_DELETE_WINDOW", on_closing)

# Étiquette du créateur
creator_label = ttk.Label(window, text="Create by M.N")
creator_label.pack()

# Boucle principale de la fenêtre
window.mainloop()
