# main.py
import tkinter as tk
from ui import TeacherBotUI

def main():
    root = tk.Tk()
    app = TeacherBotUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()