import tkinter as tk

class NiceDayReminderApp:
    def __init__(self, master):
        self.master = master
        master.title("Nice day reminder")
        master.geometry("400x300")
        
        self.label = tk.Label(master, text="Remember to have a nice day!", font=("Arial", 20), fg="black")
        self.label.pack()
        
        self.button_yes = tk.Button(master,
                                    text="Yes",
                                    font=("Helvetica", 14, "bold"),
                                    fg="white",
                                    bg="green",
                                    padx=20,
                                    pady=10,
                                    relief=tk.RAISED,
                                    command=self.handle_yes_response)
                                    
        self.button_no = tk.Button(master,
                                    text="No",
                                    font=("Helvetica", 14, "bold"),
                                    fg="white",
                                    bg="red",
                                    padx=20,
                                    pady=10,
                                    relief=tk.RAISED,
                                    command=self.handle_no_response)
        
        self.label.pack(pady=20)
        self.button_yes.pack(pady=20)
        self.button_no.pack(pady=20)
        
        self.label1 = tk.Label(master, text="sending good vibes", font=("Arial", 20), fg="black")
        self.update_text_state = ["sending good vibes .", "sending good vibes ..", "sending good vibes ..."]
        self.current_text_index = 0
        
        master.bind("<BackSpace>", lambda e: self.reset())
        
    def handle_yes_response(self):
        self.label.config(text="Nice!")
        self.button_yes.pack_forget()
        self.button_no.pack_forget()
        self.label1.pack()
        self.update_text()
        
    def update_text(self):
        self.label1.config(text=self.update_text_state[self.current_text_index])
        self.current_text_index = (self.current_text_index + 1) % len(self.update_text_state)
        self.label1.after(500, self.update_text)
        
    def handle_no_response(self):
        self.label.config(text="ok")
        self.button_yes.pack_forget()
        self.button_no.pack_forget()
        
    def reset(self):
        self.label.config(text="Remember to have a nice day")
        self.label.pack()
        self.button_yes.pack(pady=20)
        self.button_no.pack(pady=20)
        self.label1.pack_forget()
        self.current_text_index = 0
        
root = tk.Tk()
app = NiceDayReminderApp(root)
root.mainloop()