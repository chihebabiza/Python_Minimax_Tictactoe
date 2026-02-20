# Tic-Tac-Toe AI

An unbeatable Tic-Tac-Toe game built with **Python** and **Pygame**, featuring an AI opponent powered by the **Minimax algorithm**.

## 🚀 Features

* **Unbeatable AI:** The computer uses the Minimax decision theory to calculate all possible outcomes and play optimally. You can at best tie, but never win!
* **Interactive GUI:** A clean, responsive interface built with Pygame.
* **Play as X or O:** Choose your side. In Tic-Tac-Toe, X always goes first.
* **Real-time Decision Making:** Watch the "Computer thinking..." state as the AI calculates its next move.

---

## 🧠 How the AI Works: Minimax

The AI is implemented using the **Minimax algorithm**, a recursive strategy used in decision-making and game theory.

* **Maximizing Player (X):** Tries to choose the move that results in the highest possible score ().
* **Minimizing Player (O):** Tries to choose the move that results in the lowest possible score ().
* **Base Case:** If the game is a tie, the score is .

---

## 🛠️ Getting Started

### Prerequisites

* Python 3.x
* Pygame library

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/chihebabiza/Python_Minimax_Tictactoe.git
cd Tic-Tac-Toe-AI

```


2. **Install dependencies:**
```bash
pip install pygame

```



### How to Play

1. **Run the game:**
```bash
python runner.py

```


2. **Choose your player:** Select "Play as X" or "Play as O" on the starting screen.
3. **Make your move:** If it's your turn, click on an empty tile on the 3x3 grid.
4. **Restart:** Once the game ends (Win/Lose/Tie), click the **Play Again** button to reset.

## 📂 Project Structure

* `runner.py`: The main GUI code using Pygame to handle rendering and user input.
* `tictactoe.py`: The game logic, including the board state, legal actions, and the Minimax AI.
* `OpenSans-Regular.ttf`: Font file for the interface.

---
