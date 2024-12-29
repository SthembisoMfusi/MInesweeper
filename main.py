from viewBoard import *
from createBoard import *
import tkinter as tk

def main():
    """
    Main function to run the Minesweeper game.
    """

    def get_difficulty():
        """
        Creates a prompt to ask the user for the desired difficulty level.
        """
        difficulty_window = tk.Toplevel(root)
        difficulty_window.title("Select Difficulty")

        window_width = 500
        window_height = 150
        screen_width = difficulty_window.winfo_screenwidth()
        screen_height = difficulty_window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        difficulty_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        def start_game(difficulty):
            """
            Starts the game with the selected difficulty.

            Args:
                difficulty (str): The chosen difficulty level ('Easy', 'Medium', or 'Hard').
            """
            difficulty_window.destroy()
            board_maker = mineboard(difficulty=difficulty)
            game = mainGUI(root, board_maker)
        def on_closing():
            """
            Handles the closing of the difficulty window.
            """
            root.destroy()  # Explicitly terminate the application

        tk.Button(difficulty_window, text="Easy", command=lambda: start_game("Easy"), width=10).pack(pady=10)
        tk.Button(difficulty_window, text="Medium", command=lambda: start_game("Medium"), width=10).pack(pady=5)
        tk.Button(difficulty_window, text="Hard", command=lambda: start_game("Hard"), width=10).pack(pady=10)
        
        difficulty_window.protocol("WM_DELETE_WINDOW", on_closing)
        difficulty_window.grab_set()

    if __name__ == "__main__":
        root = tk.Tk()
        root.withdraw()

        get_difficulty()

        root.mainloop()

main()
