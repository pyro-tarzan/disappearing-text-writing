import tkinter as tk

class TextDisappear(tk.Tk):
    def __init__(self):
        super().__init__()
        self.gui = self.create_gui()
        self.clear_time = 5
        self.remaining_time = self.clear_time
        self.clear_timer = None 
        self.text_cleared = False

    def create_gui(self) -> None:
        self.title("Text Disappear App")
        self.geometry("600x600")

        self.timer_label = tk.Label(self, text="", font=("Arial", 14))
        self.timer_label.pack(pady=10)

        self.text_field = tk.Text(
            self,
            wrap="word",
            height=25,
            width=55,
            bd=0,
            bg=self.cget("bg"),
            highlightthickness=0,
            font=("Arial", 12)
            )

        self.text_field.pack(pady=10)
        self.text_field.bind("<KeyRelease>", self.on_text_modified)
    
    def on_text_modified(self, event) -> None:
        if self.text_cleared:
            self.text_cleared = False

        if self.clear_timer:
            self.after_cancel(self.clear_timer)

        self.remaining_time = self.clear_time
        self.update_timer_label()
    
    def clear_text(self):
        self.text_cleared = True
        self.text_field.delete(1.0, tk.END)
        self.timer_label.config(text="0")
        self.clear_timer = None        

    def update_timer_label(self):
        if self.remaining_time > 0:
            self.timer_label.config(text=f"{self.remaining_time}")
            self.remaining_time -= 1
            
            self.clear_timer = self.after(1000, self.update_timer_label)
        else:
            self.clear_text()


