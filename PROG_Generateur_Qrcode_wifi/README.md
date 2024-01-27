# PROG générateur Qrcode wifi

## Instructions d'utilisation :

1. **Installation des dépendances :**
   - Assurez-vous d'avoir Python installé sur votre système.
   - Installez les bibliothèques nécessaires en exécutant la commande suivante dans votre terminal :
     ```
     pip install os-sys
     ```
	 ```
	 pip install Everything-Tkinter
	 ```
	 ```
	 pip install qrcode
	 ```
	 
2. **Exécution du script :**
   - Assurez-vous d'avoir Python installé sur votre système.
   - Exécutez le script en utilisant la commande suivante :
     ```
     python nom_du_script.py
     ```
	 ou en exécutant le `.exe`

3. **Interface Utilisateur :**
   - Saisissez le SSID du réseau Wi-Fi dans le champ correspondant.
   - Saisissez la clé du réseau dans le champ correspondant (le texte est masqué avec des astérisques).
   - Sélectionnez le type de cryptage (WPA, WPA2, ou WPA3) à l'aide de la combobox.
   - Cliquez sur le bouton "Générer QR Code" pour créer le QR Code.

4. **Génération du QR Code :**
   - Un QR Code contenant les informations du réseau Wi-Fi est généré.
   - Le QR Code est sauvegardé dans un dossier appelé "Qrcode_générés" à la racine du script.
   - Le nom du fichier est basé sur le SSID du réseau.

5. **Affichage du Résultat :**
   - Un message de succès est affiché sous la forme "QR Code généré avec succès!".

6. **Fermeture de la Fenêtre :**
   - La fenêtre peut être fermée en cliquant sur le bouton de fermeture.
   - Une confirmation sera demandée avant de quitter.

7. **Avertissement :**
   - Assurez-vous que les informations du réseau Wi-Fi sont correctes.
   - Le type de cryptage doit être sélectionné parmi les options proposées.
----
