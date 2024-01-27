Start-Process "microsoft-edge:"
Start-Sleep -Seconds 2
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait('%f')
1..4 | ForEach-Object { [System.Windows.Forms.SendKeys]::SendWait('{UP}') }
[System.Windows.Forms.SendKeys]::SendWait('{ENTER}')
Start-Sleep -Seconds 2
[System.Windows.Forms.SendKeys]::SendWait('Compatibilit')
Start-Sleep -Seconds 1.5
1..4 | ForEach-Object { [System.Windows.Forms.SendKeys]::SendWait('{TAB}') }
[System.Windows.Forms.SendKeys]::SendWait('{ENTER}')
Start-Sleep -Seconds 1
[System.Windows.Forms.SendKeys]::SendWait('https://www.youtube.com')
[System.Windows.Forms.SendKeys]::SendWait('{ENTER}')
Start-Sleep -Seconds 0.5
[System.Windows.Forms.SendKeys]::SendWait('^l')
[System.Windows.Forms.SendKeys]::SendWait('https://www.youtube.com')
[System.Windows.Forms.SendKeys]::SendWait('{ENTER}')