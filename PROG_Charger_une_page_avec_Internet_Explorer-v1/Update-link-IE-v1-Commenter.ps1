# Ouvre le navigateur Microsoft Edge
Start-Process "microsoft-edge:"
Start-Sleep -Seconds 2

# Importe la classe SendKeys de System.Windows.Forms pour simuler des frappes clavier
Add-Type -AssemblyName System.Windows.Forms

# Appuie sur la combinaison de touches 'Alt + F' pour ouvrir le menu d'options
[System.Windows.Forms.SendKeys]::SendWait('%f')

# Appuie quatre fois sur la touche 'Haut' pour sélectionner 'Paramètres'
1..4 | ForEach-Object { [System.Windows.Forms.SendKeys]::SendWait('{UP}') }

# Appuie sur la touche 'Entrée' pour ouvrir les paramètres
[System.Windows.Forms.SendKeys]::SendWait('{ENTER}')
Start-Sleep -Seconds 1.5

# Tape 'Compatibilit' pour rechercher Compatibilité d'Internet Explorer
[System.Windows.Forms.SendKeys]::SendWait('Compatibilit')
Start-Sleep -Seconds 1

# Appuie quatre fois sur la touche 'Tab' pour sélectionner le bouton 'Ajouter'
1..4 | ForEach-Object { [System.Windows.Forms.SendKeys]::SendWait('{TAB}') }

# Appuie sur la touche 'Entrée' pour ouvrir ouvrir la fenêtre de l'option
[System.Windows.Forms.SendKeys]::SendWait('{ENTER}')
Start-Sleep -Seconds 0.5

# Tape 'https://www.youtube.com' dans la barre d'adresse
[System.Windows.Forms.SendKeys]::SendWait('https://www.youtube.com')
[System.Windows.Forms.SendKeys]::SendWait('{ENTER}')

# Appuie sur 'Ctrl + L' pour sélectionner la barre d'adresse
[System.Windows.Forms.SendKeys]::SendWait('^l')

# Tape à nouveau 'https://www.youtube.com' dans la barre d'adresse pour vérifier l'ouverture de youtube avec IE
[System.Windows.Forms.SendKeys]::SendWait('https://www.youtube.com')
[System.Windows.Forms.SendKeys]::SendWait('{ENTER}')
