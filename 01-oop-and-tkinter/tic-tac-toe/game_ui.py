import tkinter as tk
import tkinter.font as font
from game import Game


class BoardCell:
    def __init__(self, window, row, col, callback):
        self.callback = callback
        frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        frame.grid(row=row, column=col, padx=1, pady=1)
        self.button = tk.Button(master=frame, text=' ', height=4, width=8,
                                command=lambda r=row, c=col: self.callback(r, c))
        self.button.pack()

    def set_played(self, symbol):
        self.button.config(state=tk.DISABLED, text=symbol)

    def deactivate(self):
        self.button.config(state=tk.DISABLED)

    def reset(self):
        self.button.config(state=tk.ACTIVE, text=' ')


class MessageFrame:
    def __init__(self, window, callback):
        frame = tk.Frame(master=window)
        frame.grid(row=4, column=0, columnspan=3)
        self.label = tk.Label(master=frame, text='X plays')
        self.label.pack()
        self.button = tk.Button(master=frame, text='Play again', command=callback)
        self.button.pack()
        self.disable_button()

    def disable_button(self):
        self.button.pack_forget()

    def enable_button(self):
        self.button.pack()

    def display_message(self, message):
        self.label.config(text=message)

    def reset(self, symbol):
        self.display_message(symbol + " plays")
        self.disable_button()


class ScoreFrame:
    def __init__(self, window):
        frame = tk.Frame(master=window)
        frame.grid(row=5, column=0, columnspan=3)
        self.label = tk.Label(master=frame, text='X: 0 - O: 0')
        self.label.pack()

    def display_score(self, score):
        self.label.config(text=f"X: {score[0]} - O: {score[1]}")


class GameFrame:
    def __init__(self):
        self.game = Game()
        self.window = tk.Tk()
        self.cells = [[], [], []]
        self.window.title("tic-tac-toe")
        for row in range(3):
            for col in range(3):
                slot = BoardCell(self.window, row, col, self.play)
                self.cells[row].append(slot)
        self.msg_frame = MessageFrame(self.window, self.new_game)
        self.score_frame = ScoreFrame(self.window)
        self.window.mainloop()

    def reset(self):
        for row in range(3):
            for col in range(3):
                self.cells[row][col].reset()
        if not self.game.is_tie():
            self.msg_frame.reset(self.game.get_winner().get_symbol())
        else:
            self.msg_frame.reset(self.game.get_current_symbol())

    def deactivate_all(self):
        for row in range(3):
            for col in range(3):
                self.cells[row][col].deactivate()

    def play(self, row, col):
        self.cells[row][col].set_played(self.game.get_current_symbol())
        self.game.play(row, col)
        winner = self.game.get_winner()
        if winner is not None:
            self.deactivate_all()
            self.msg_frame.display_message(self.game.get_winner().get_symbol() + " WINS!")
            self.msg_frame.enable_button()
            self.score_frame.display_score(self.game.get_score())
        elif self.game.is_tie():
            self.deactivate_all()
            self.msg_frame.display_message("IT'S A TIE ...")
            self.msg_frame.enable_button()
        else:
            self.msg_frame.display_message(self.game.get_current_symbol() + " plays")

    def new_game(self):
        self.reset()
        self.game.reset()





