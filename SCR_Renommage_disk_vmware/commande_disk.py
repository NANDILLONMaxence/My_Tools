import tkinter as tk
from tkinter import filedialog
import os

# Liste pour stocker les commandes
commandes = []

def envoyer_commande():
    banque = banque_entry.get()
    dossier_machine = dossier_machine_entry.get()
    commande_cd = f"cd /vmfs/volumes/{banque}/{dossier_machine}/"
    commande_mv = ""
    commande_vi = ""
    if utiliser_mv.get():
        ancien_nom = ancien_nom_entry.get()
        nouveau_nom = nouveau_nom_entry.get()
        ancien_nom += ".vmdk"  # Ajouter l'extension ".vmdk" à l'ancien nom
        nouveau_nom += ".vmdk"  # Ajouter l'extension ".vmdk" au nouveau nom
        commande_mv = f"mv {ancien_nom} {nouveau_nom}"
    if utiliser_vi.get():
        nom_machine = dossier_machine
        commande_vi = f"vi {nom_machine}.vmx"
    commande_complete = commande_cd + "\n" + commande_mv + "\n" + commande_vi
    resultat_text.delete(1.0, tk.END)
    resultat_text.insert(tk.END, commande_complete)
    commandes.append(commande_complete)  # Ajouter la commande à la liste

def creer_liste_commande():
    if len(commandes) > 0:
        contenu = "\n".join(commandes)
        nom_fichier = dossier_machine_entry.get() + ".txt"
        chemin_fichier = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichier texte", "*.txt")], initialfile=nom_fichier)
        if chemin_fichier:
            with open(chemin_fichier, "w") as fichier:
                fichier.write(contenu)
            resultat_text.delete(1.0, tk.END)
            resultat_text.insert(tk.END, f"Liste de commandes créée : {chemin_fichier}")
    else:
        resultat_text.delete(1.0, tk.END)
        resultat_text.insert(tk.END, "Aucune commande à enregistrer")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Création de commande")
fenetre.geometry("400x450")

# Labels
banque_label = tk.Label(fenetre, text="Banque:")
banque_label.pack()

# Entrée de texte pour Banque
banque_entry = tk.Entry(fenetre)
banque_entry.pack()

dossier_machine_label = tk.Label(fenetre, text="Dossier machine:")
dossier_machine_label.pack()

# Entrée de texte pour Dossier machine
dossier_machine_entry = tk.Entry(fenetre)
dossier_machine_entry.pack()

# Option mv
utiliser_mv = tk.BooleanVar()
mv_checkbox = tk.Checkbutton(fenetre, text="Utiliser mv", variable=utiliser_mv)
mv_checkbox.pack()

# Labels et Entrées de texte pour mv
ancien_nom_label = tk.Label(fenetre, text="Ancien nom:")
ancien_nom_entry = tk.Entry(fenetre)

nouveau_nom_label = tk.Label(fenetre, text="Nouveau nom:")
nouveau_nom_entry = tk.Entry(fenetre)

# Fonction pour activer/désactiver les champs mv en fonction de l'état de la checkbox
def toggle_mv_fields():
    if utiliser_mv.get():
        ancien_nom_label.pack()
        ancien_nom_entry.pack()
        nouveau_nom_label.pack()
        nouveau_nom_entry.pack()
    else:
        ancien_nom_label.pack_forget()
        ancien_nom_entry.pack_forget()
        nouveau_nom_label.pack_forget()
        nouveau_nom_entry.pack_forget()

mv_checkbox.config(command=toggle_mv_fields)

# Option vi
utiliser_vi = tk.BooleanVar()
vi_checkbox = tk.Checkbutton(fenetre, text="Utiliser vi", variable=utiliser_vi)
vi_checkbox.pack()

# Bouton Envoyer
envoyer_button = tk.Button(fenetre, text="Envoyer", command=envoyer_commande)
envoyer_button.pack()

# Bouton Créer liste_commande
creer_liste_commande_button = tk.Button(fenetre, text="Créer liste_commande", command=creer_liste_commande)
creer_liste_commande_button.pack()

# Zone de texte pour afficher le résultat
resultat_text = tk.Text(fenetre, height=6)
resultat_text.pack()

# Lancement de la boucle principale
fenetre.mainloop()
