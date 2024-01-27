import tkinter as tk
import paramiko
from tkinter import messagebox
from tkinter.ttk import Progressbar

def connect_ssh():
    # Récupérer les valeurs des champs de saisie
    hostname = hostname_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Établir une connexion SSH
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(hostname, username=username, password=password)

        # Exécuter la commande pour récupérer les informations système
        stdin, stdout, stderr = ssh_client.exec_command('wmic csproduct get *')
        output_system = stdout.read().decode()

        # Exécuter la commande pour récupérer les informations réseau
        stdin, stdout, stderr = ssh_client.exec_command('ipconfig /all')
        output_network = stdout.read().decode('latin-1')

        # Afficher les informations système et réseau récupérées
        print('Informations système du Wyse 5070:')
        print(output_system)

        print('Informations réseau du Wyse 5070:')
        print(output_network)
    # Message d'erreur
    except paramiko.AuthenticationException:
        messagebox.showerror('Erreur', 'Échec de l\'authentification SSH.')
    except paramiko.SSHException as ssh_ex:
        messagebox.showerror('Erreur', 'Erreur lors de l\'établissement de la connexion SSH: ' + str(ssh_ex))
    finally:
        # Fermer la connexion SSH
        ssh_client.close()

# Créer la fenêtre principale
window = tk.Tk()
window.title('Connexion SSH')
window.geometry('400x200')

# Créer les étiquettes et les champs de saisie pour hostname, username et password
hostname_label = tk.Label(window, text='Hostname:')
hostname_label.pack()
hostname_entry = tk.Entry(window)
hostname_entry.pack()

username_label = tk.Label(window, text='Username:')
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text='Password:')
password_label.pack()
password_entry = tk.Entry(window, show='*')
password_entry.pack()

# Créer le bouton de validation
connect_button = tk.Button(window, text='Valider', command=connect_ssh)
connect_button.pack()

# Créer la barre de progression
progress_bar = Progressbar(window, length=200, mode='indeterminate')
progress_bar.pack()

# Démarrer la boucle principale Tkinter
window.mainloop()

