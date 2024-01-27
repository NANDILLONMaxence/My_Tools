# SCR Recuperation d'information Wyse beta test

## Instructions d'utilisation :

1. **Installation des dépendances :**
   - Assurez-vous d'avoir Python installé sur votre système.
   - Installez les bibliothèques nécessaires en exécutant la commande suivante dans votre terminal :
     ```
     pip install paramiko
     ```
	 ```
	 pip install Everything-Tkinter
	 ```

2. **Exécution du script :**
   - Exécutez le script en utilisant la commande suivante :
     ```
     python nom_du_script.py
     ```
	 ou en exécutant le `.exe`
	 
3. **Interface Utilisateur :**
   - Saisissez le hostname, le nom d'utilisateur et le mot de passe dans les champs correspondants.
   - Cliquez sur le bouton "Valider" pour établir la connexion SSH.

4. **Résultats :**
   - Les informations système et réseau du Wyse 5070 seront affichées dans la console.

## Notes :

- Assurez-vous d'avoir une connexion réseau valide pour établir la connexion SSH.
- Si l'authentification SSH échoue, assurez-vous que les informations fournies sont correctes.
- Le mot de passe est masqué pour des raisons de sécurité.
- Le script utilise la politique `AutoAddPolicy` pour ajouter automatiquement le host key du serveur SSH à la liste des clés connues si nécessaire.

**Avertissement :** 
Le stockage de mots de passe en clair dans le code peut présenter des risques de sécurité. Considérez l'utilisation de méthodes plus sécurisées, comme la gestion de clés SSH.

N'hésitez pas à me contacter en cas de problème ou de question.
----
