from viewBoard import mainGUI
from createBoard import mineboard
import tkinter as tk

def main():
    """
    Main function to run the Minesweeper game.
    """
    global root  

    def start_new_game(difficulty):
        """
        Starts a new game instance with the given difficulty.
        """
        nonlocal game, board_maker  # Declare these as nonlocal to modify the variables in the enclosing scope
        if game:
            # Destroy all widgets inside the root window without destroying the window itself
            for widget in root.winfo_children():
                widget.destroy()
        else:
            # If no game has started yet, hide the root window
            root.withdraw()

        # Create a new board and GUI
        board_maker = mineboard(difficulty=difficulty)
        game = mainGUI(root, board_maker)
        game.set_restart_callback(lambda: start_new_game(difficulty))
        root.deiconify()  # Show the root window again

    def get_difficulty(root):  
        """
        Creates a prompt to ask the user for the desired difficulty level.
        """
        def on_closing():
            """Handles the closing of the difficulty window."""
            if root.winfo_exists():
                root.deiconify()  # Show the root window if it was hidden
            difficulty_window.destroy()

        def handle_difficulty_selection(difficulty):
            """
            Handles the difficulty selection.
            """
            difficulty_window.destroy()
            start_new_game(difficulty)

        # Create a new difficulty selection window
        difficulty_window = tk.Toplevel(root)
        difficulty_window.title("Select Difficulty")
        window_width = 200
        window_height = 150
        screen_width = difficulty_window.winfo_screenwidth()
        screen_height = difficulty_window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        difficulty_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        tk.Button(difficulty_window, text="Easy", command=lambda: handle_difficulty_selection("Easy"), width=10).pack(pady=10)
        tk.Button(difficulty_window, text="Medium", command=lambda: handle_difficulty_selection("Medium"), width=10).pack(pady=5)
        tk.Button(difficulty_window, text="Hard", command=lambda: handle_difficulty_selection("Hard"), width=10).pack(pady=10)

        difficulty_window.protocol("WM_DELETE_WINDOW", on_closing)
        difficulty_window.grab_set()

    # Initialize game and difficulty window variables
    game = None
    board_maker = None

    if __name__ == "__main__":
        root = tk.Tk()
        root.withdraw()  # Start with the root window hidden

        get_difficulty(root) 

        root.mainloop()

main()
