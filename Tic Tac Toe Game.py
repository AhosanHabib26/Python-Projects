import tkinter as tk
from tkinter import messagebox
import random

# Initialize the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")
window.geometry("400x450")

# Game variables
current_player = "X"
buttons = []

# All 8 possible winning combinations
winning_combos = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

def check_winner():
    # Check each combination
    for combo in winning_combos:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            # Highlight the winning buttons green
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            
            # Show win message box
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            reset_game()
            return True
            
    # Check for a tie
    if all(btn["text"] != "" for btn in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a Tie!")
        reset_game()
        return True
        
    return False

def computer_move():
    global current_player
    
    # Gather all indexes that are currently empty
    empty_cells = [i for i, btn in enumerate(buttons) if btn["text"] == ""]
    
    if empty_cells:
        # Pick a random available square
        move = random.choice(empty_cells)
        buttons[move]["text"] = "O"
        
        if not check_winner():
            current_player = "X"
            turn_label.config(text="Player X's turn")

def btn_click(index):
    global current_player
    
    # Player X's turn logic
    if buttons[index]["text"] == "" and current_player == "X":
        buttons[index]["text"] = "X"
        
        if not check_winner():
            current_player = "O"
            turn_label.config(text="Computer (O) is thinking...")
            # Wait 500 milliseconds (0.5 seconds) before the computer moves
            window.after(500, computer_move)

def reset_game():
    global current_player
    current_player = "X"
    turn_label.config(text="Player X's turn")
    for btn in buttons:
        btn.config(text="", bg="SystemButtonFace")

# Create the 3x3 button grid frame
grid_frame = tk.Frame(window)
grid_frame.pack(fill="both", expand=True)

# Generate the 9 buttons dynamically
for i in range(9):
    btn = tk.Button(grid_frame, text="", font=("Arial", 24, "bold"), 
                    command=lambda idx=i: btn_click(idx))
    btn.grid(row=i//3, column=i%3, sticky="nsew")
    buttons.append(btn)

# Make the grid rows and columns scale/expand evenly
for i in range(3):
    grid_frame.rowconfigure(i, weight=1)
    grid_frame.columnconfigure(i, weight=1)

# Status label at the bottom
turn_label = tk.Label(window, text="Player X's turn", font=("Arial", 14), pady=10)
turn_label.pack()

# Start the application loop
window.mainloop()