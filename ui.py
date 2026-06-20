# ui.py
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import pyttsx3
from logic import get_bot_response

class TeacherBotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Professor Profile Assistant")
        self.root.geometry("850x650")
        self.root.configure(bg="#F4F6F9") # Soft academic background
        
        self.current_lang = "urdu"
        self.engine = pyttsx3.init()
        
        self.setup_styles()
        self.create_widgets()

    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # Professional Scholar Blue Styling
        self.style.configure("TFrame", background="#F4F6F9")
        self.style.configure("Header.TFrame", background="#1E3A8A") # Royal Blue Header
        self.style.configure("Sidebar.TFrame", background="#E5E7EB")
        
        self.style.configure("Action.TButton", background="#2563EB", foreground="white", font=("Helvetica", 10, "bold"))
        self.style.map("Action.TButton", background=[("active", "#1D4ED8")])
        
        self.style.configure("Lang.TButton", background="#4B5563", foreground="white", font=("Helvetica", 9, "bold"))
        self.style.map("Lang.TButton", background=[("active", "#374151")])

    def create_widgets(self):
        # Header Banner
        header_frame = ttk.Frame(self.root, style="Header.TFrame", height=80)
        header_frame.pack(fill="x", side="top")
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="🎓 PROF. SALEEM KHAN CHATBOT", bg="#1E3A8A", fg="white", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(header_frame, text="Mathematics Department | Layyah", bg="#1E3A8A", fg="#93C5FD", font=("Helvetica", 10, "italic"))
        subtitle_label.pack()

        # Main Layout split: Sidebar and Chat Area
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Sidebar for quick query links
        sidebar = ttk.Frame(main_frame, style="Sidebar.TFrame", width=220)
        sidebar.pack(fill="y", side="left", padx=(0, 10))
        sidebar.pack_propagate(False)
        
        side_title = tk.Label(sidebar, text="Quick Academic Links", bg="#E5E7EB", fg="#1F2937", font=("Helvetica", 11, "bold"))
        side_title.pack(pady=15)
        
        # Unique customized side buttons for a Teacher profile
        options = [
            ("📋 Service & Grade", "grade_rank"),
            ("📐 Math Specialization", "math_topics"),
            ("🏫 School Location", "school_details"),
            ("📜 Education Degree", "education"),
            ("👪 Family Relations", "family_children")
        ]
        
        for text, key in options:
            btn = ttk.Button(sidebar, text=text, command=lambda k=key: self.process_sidebar_query(k))
            btn.pack(fill="x", padx=10, pady=6)
            
        # Language Selector Button inside Sidebar
        self.lang_btn = ttk.Button(sidebar, text="🌐 Switch to English", style="Lang.TButton", command=self.toggle_language)
        self.lang_btn.pack(side="bottom", fill="x", padx=10, pady=20)

        # Chat and Input Content Area
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill="both", expand=True, side="right")
        
        # Chat Display Box
        self.chat_display = tk.Text(content_frame, bg="white", fg="#1F2937", font=("Helvetica", 11), wrap="word", bd=1, relief="solid")
        self.chat_display.pack(fill="both", expand=True, pady=(0, 10))
        self.chat_display.config(state="disabled")
        
        # Input Controls Frame
        input_frame = ttk.Frame(content_frame)
        input_frame.pack(fill="x", side="bottom")
        
        self.entry_box = tk.Entry(input_frame, font=("Helvetica", 12), bd=1, relief="solid")
        self.entry_box.pack(fill="x", side="left", expand=True, ipady=8, padx=(0, 5))
        self.entry_box.bind("<Return>", lambda event: self.handle_submit())
        
        submit_btn = ttk.Button(input_frame, text="Ask Bot 🔍", style="Action.TButton", command=self.handle_submit)
        submit_btn.pack(side="right", ipady=4)

        # Welcome Greetings
        self.append_message("System", "Welcome to Professor Saleem Ahmad Khan's Profile Assistant. Type your question below or click side buttons.")

    def append_message(self, sender, message):
        self.chat_display.config(state="normal")
        self.chat_display.insert(tk.END, f"[{sender}]: {message}\n\n")
        self.chat_display.see(tk.END)
        self.chat_display.config(state="disabled")

    def toggle_language(self):
        if self.current_lang == "urdu":
            self.current_lang = "english"
            self.lang_btn.config(text="🌐 Switch to Roman Urdu")
            self.append_message("System", "Language profile changed to English.")
        else:
            self.current_lang = "urdu"
            self.lang_btn.config(text="🌐 Switch to English")
            self.append_message("System", "Language profile changed to Roman Urdu.")

    def handle_submit(self):
        query = self.entry_box.get()
        if not query.strip():
            return
            
        self.append_message("You", query)
        self.entry_box.delete(0, tk.END)
        
        response = get_bot_response(query, self.current_lang)
        self.append_message("Bot", response)
        
        # Threaded Text-to-Speech execution to avoid freezing
        threading.Thread(target=self.speak_text, args=(response,), daemon=True).start()

    def process_sidebar_query(self, key_word):
        self.append_message("You [Quick Link]", f"Checking details for raw keyword: '{key_word}'")
        response = get_bot_response(key_word, self.current_lang)
        self.append_message("Bot", response)
        threading.Thread(target=self.speak_text, args=(response,), daemon=True).start()

    def speak_text(self, text):
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except:
            pass