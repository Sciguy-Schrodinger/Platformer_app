# 🏃 Platformer

A classic platformer game built with **Pygame** and **Tkinter**.  
Jump between platforms, collect coins, avoid enemies, and escape through the exit door!

---

## 🎮 Features

- **3 unique levels** — each with different layouts and challenges
- **Coin collection** — collect 5 coins per level to unlock the exit
- **Enemy AI** — enemies patrol platforms and chase the player
- **Smooth animations** — left/right movement with sprite animation
- **Sound effects** — coin collection, death, level unlock, and background music
- **Rich UI** — custom main menu with info, restart, and quit options
- **Persistent game state** — tracks levels, coins, and progress

---

## 🛠️ Technologies Used

- **Python 3** — core logic
- **Pygame** — 2D rendering, input handling, audio
- **Tkinter** — main menu interface

---

## 🚀 How to Run

### Requirements

Install dependencies:

bash
pip install pygame Pillow

### Run

python3 platformer.py

🎮 Controls
Key	Action
Arrow Keys	Move the player (left, right, up)
Close Window	Exit the game

🧠 How It Works

   1. Player — moves with arrow keys

   2. Coins — collect 5 coins per level to unlock the exit

   3. Enemies — patrol platforms and move left/right

   4. Exit — appears after collecting all coins

   5. Level progression — reach the exit to advance

   6. Death — touching an enemy or falling off the screen ends the game
