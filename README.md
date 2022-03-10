# HPI-Scrapper

Dieses Programm wurde geschrieben, um Schülern zu helfen die HPI-Cloud leichter zu benutzen und Ihre Datein sortiert zu behalten.

## Installation

Lade dir diese Datei herunter: ```https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe``` und führe den Installationsprozess durch.

Drücke nun ```Win + R``` und tippe in das Fenster ```cmd``` ein.

Führe jetzt folgende Befehle aus:

```CMD
pip install progressbar2
pip install Selenium
pip install python-docx
```

Extrahiere nun die Datein aus dem Kompriemiertem Ordner.
Trage nun deine HPI-Cloud Daten in die Informations.py ein. (```Rechtsklick``` auf die ```Informations.py``` Datei und ```Öffnen mit``` und dann ```Andere App Auswählen``` nun  ```Weitere Apps``` auswählen und ```Editor``` auswählen)
Danach sollte die Datei so aussehen:
```
hpiEmail = "deineEmail@gmail.com"
hpiPassword = "deinPasswort"
```

Wenn du möchtest, dass das Programm nach jedem Neustart nach neuen Aufgaben sucht musst du folgendes machen:

Drücke ```Win + R``` und kopiere da folgendes hinein: ```%appdata%/microsoft/windows/Start Menu/Programs/Startup``` nun sollte sich ein Ordner öffnen. Drücke nun Rechtsklick und erstelle eine neue Verknüpfung.
Diese Verknüpfung muss nun zu deiner ```main.py``` Datei führen. Wenn du das geschaft hast bist du fertig. Nun wird jedes mal nach neuen Aufgaben gesucht und wenn du welche hast wird dir eine Benachrichtigung geschickt.  

## Optional für Todoist

Als erstes musst du dir ein Todoist Konto anlegen. Dies ist Gratis. Dabei musst du aber beachten, dass du nicht einfach dein Google Konto verknüpfen kannst. Da dies sonst nicht funktionieren wird.
Wenn du deine Aufgaben automatisch in Todoist Laden möchtest, trage ```toDo = True``` ein, wenn nicht trage ```toDo = False``` ein.
Nun musst bei Todoist ein Projekt erstellen. Es ist egal wie es heißt und wird danach gelöscht. 
Am ende sollte dein Todoist so aussehen wie in der Todoist.png Datei.
Trage nun deine Todist Nutzerdaten in die Informations.py Datei ein.
 
## Usage

Führe nun die main.py Datei aus.
Nun dauert es wenig Sekunden (Meist zwischen 10-60 Sekunden) und ein ```Aufgaben``` Ordner sollte erscheinen.
In diesem befinden sich nun geordnet Ihre Aufgaben.

## Contributing

Bei Fragen oder Ähnlichem bitte an jabbekeipert@gmail.com wenden.
