__________________________________________________
⚡ Terminal Racer

Terminal Racer is een simpele Python racing game die volledig in de terminal wordt gespeeld.
De speler ontwijkt obstakels op een weg terwijl de snelheid van het spel constant doorgaat.

Het project bevat een startmenu, player systeem, car customizer en een racing game loop.

__________________________________________________
🎮 Features

1 👤 Player systeem:

    - Maak spelers aan met een unieke naam
    - Spelers worden opgeslagen in een players.json bestand

2 🚗 Car Customizer:

    - Kies verschillende car models
    - Kies verschillende car kleuren

3 🏁 Racing Game:

    - Obstakels verschijnen willekeurig
    - Bestuur je auto met toetsen
    - Botsingen beëindigen de race

4 💾 Data opslag:

    -Spelers worden automatisch opgeslagen en geladen via JSON

__________________________________________________
🕹 Controls:

Tijdens de race:

    Key	Actie:

    A of ←	| Ga naar links
    D of →	| Ga naar rechts

__________________________________________________
📂 Project Structure:

    terminal-racer
    │
    ├── start_menu.py     # Startmenu + player management
    ├── race_logic.py     # Racing game logic
    ├── players.json      # Opgeslagen spelers (wordt automatisch gemaakt)
    └── README.md

__________________________________________________
⚙️ Requirements:
    
Je hebt nodig:
    
    Python 3.8+
    
    Python library:
    - keyboard

    Installeren:
    - pip install keyboard
    
    ⚠️ Op Linux moet je de game mogelijk met sudo runnen vanwege keyboard input.

__________________________________________________
▶️ How To Run:

Start de game met:

    python start_menu.py

Je krijgt daarna het startmenu:
    
    1. Create a new player
    2. Car customizer
    3. Play
    4. Quit

__________________________________________________
🧠 How The Game Works:

1. De weg bestaat uit 5 lanes

2. De speler staat altijd onderaan

3. Nieuwe rijen worden bovenaan gegenereerd

4. Obstakels (11) verschijnen willekeurig

5. Als de speler een obstakel raakt → Game Over

Speler:

    oo

Obstacle:

    11

Road tile:

    []

__________________________________________________
🔮 Possible Future Features:
    Ideeën om het project verder uit te breiden:
    
verschillende auto sprites

hogere snelheid naarmate je langer overleeft

verschillende obstacle types

score systeem

leaderboard

betere terminal graphics

geluiden

__________________________________________________
👨‍💻 Authors:

Roy (Game logic) & Nico (Menu logic)