from viewBoard import mainGUI
from createBoard import mineboard
import tkinter as tk

def main():
    """
    Main function to run the Minesweeper game.
    """
    global root  # Declare root as global in main

    def start_new_game(difficulty):
        nonlocal game, board_maker
        """
        Starts a new game instance with the given difficulty.
        """
        if game:
            for widget in root.winfo_children():
                widget.destroy()
        else:
            root.withdraw()

        board_maker = mineboard(difficulty=difficulty)
        game = mainGUI(root, board_maker)
        game.set_restart_callback(lambda: start_new_game(difficulty))
        root.deiconify()

    def get_difficulty(root):  # Accept root as an argument
        """
        Creates a prompt to ask the user for the desired difficulty level.
        """
        nonlocal difficulty_window

        difficulty_window = tk.Toplevel(root)
        difficulty_window.title("Select Difficulty")
        window_width = 200
        window_height = 150
        screen_width = difficulty_window.winfo_screenwidth()
        screen_height = difficulty_window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        difficulty_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        def on_closing():
            """Handles the closing of the difficulty window."""
            if root.winfo_exists():
                root.destroy()

        def handle_difficulty_selection(difficulty):
            """
            Handles the difficulty selection.
            """
            difficulty_window.destroy()
            start_new_game(difficulty)

        tk.Button(difficulty_window, text="Easy", command=lambda: handle_difficulty_selection("Easy"), width=10).pack(pady=10)
        tk.Button(difficulty_window, text="Medium", command=lambda: handle_difficulty_selection("Medium"), width=10).pack(pady=5)
        tk.Button(difficulty_window, text="Hard", command=lambda: handle_difficulty_selection("Hard"), width=10).pack(pady=10)

        difficulty_window.protocol("WM_DELETE_WINDOW", on_closing)
        difficulty_window.grab_set()

    game = None
    board_maker = None
    difficulty_window = None

    if __name__ == "__main__":
        root = tk.Tk()
        root.withdraw()

        get_difficulty(root)  # Pass root to get_difficulty

        root.mainloop()

main()