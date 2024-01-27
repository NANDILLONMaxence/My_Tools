# SCR Renommage disk vmware

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

2. **Exécution du script :**
   - Assurez-vous d'avoir Python installé sur votre système.
   - Exécutez le script en utilisant la commande suivante :
     ```
     python nom_du_script.py
     ```
	 ou en exécutant le `.exe`

3. **Interface Utilisateur :**
   - Saisissez la banque et le dossier de la machine virtuelle dans les champs correspondants.
   - Cochez les cases "Utiliser mv" et/ou "Utiliser vi" selon vos besoins.
   - Si "Utiliser mv" est coché, saisissez l'ancien et le nouveau nom dans les champs appropriés.
   - Cliquez sur le bouton "Envoyer" pour générer et afficher les commandes.
   - Cliquez sur le bouton "Créer liste_commande" pour sauvegarder la liste des commandes dans un fichier texte.

4. **Génération des Commandes :**
   - Les commandes générées seront affichées dans la zone de texte.
   - Si "Utiliser mv" est sélectionné, une commande `mv` sera générée.
   - Si "Utiliser vi" est sélectionné, une commande `vi` sera générée.

5. **Sauvegarde de la Liste de Commandes :**
   - Cliquez sur "Créer liste_commande" pour sauvegarder la liste des commandes dans un fichier texte.
   - Sélectionnez l'emplacement et le nom du fichier texte dans la fenêtre de sauvegarde.

6. **Notes :**
   - Assurez-vous d'avoir les autorisations nécessaires pour effectuer les opérations spécifiées par les commandes.
   - Si aucune des options "Utiliser mv" ou "Utiliser vi" n'est cochée, aucune commande ne sera générée.
----
