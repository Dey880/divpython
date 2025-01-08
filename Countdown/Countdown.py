import tkinter as tk
class CountdownApp:
    def __init__(self, master):
        self.master = master
        master.title("Countdown Timer")
        master.geometry("600x400")
        master.config(bg="#e3f2fd")
        
        self.label = tk.Label(master, text="Welcome to the Countdown Timer!", font=("Helvetica", 24, "bold"), fg="#01579b", bg="#e3f2fd")
        self.label.pack(pady=30)
        self.entry = tk.Entry(master, width=25, font=("Helvetica", 16), relief="solid", bd=2, justify="center")
        self.entry.pack(pady=15)
        self.countdown_label = tk.Label(master, text="", font=("Courier", 20), fg="#0288d1", bg="#e3f2fd")
        self.countdown_label.pack(pady=30)
        self.button = tk.Button(master, text="Submit / Start Countdown", font=("Helvetica", 16), bg="#0288d1", fg="white", relief="raised", command=self.start_countdown)
        self.button.pack(pady=15)
        self.button.config(borderwidth=3, highlightthickness=2, activebackground="#01579b", activeforeground="white")
        
        self.remaining_time = 0
        
    def start_countdown(self):
        try:
            user_input = self.entry.get().strip()
            
            if user_input == "":
                self.remaining_time = 300
            else:
                self.remaining_time = int(user_input)
                
            if self.remaining_time < 0:
                raise ValueError("Time must be a positive number.")
                
            self.entry.config(state="disabled")
            self.button.config(state="disabled")
            self.run_countdown()
            
        except ValueError:
            self.show_notification("Please enter a positive number")
            
    def run_countdown(self):
        if self.remaining_time > 0:
            hours, remainder = divmod(self.remaining_time, 3600)
            mins, secs = divmod(remainder, 60)
            
            if hours > 0:
                time_format = f"{hours:02d}:{mins:02d}:{secs:02d}"
            elif mins > 0:
                time_format = f"{mins:02d}:{secs:02d}"
            else:
                time_format = f"{secs:02d}"
                
            self.countdown_label.config(text=f"Time Remaining: {time_format}")
            self.remaining_time -= 1
            self.master.after(1000, self.run_countdown)
        else:
            self.countdown_label.config(text="Time's up!", fg="#d32f2f")
            self.show_notification("Countdown Timer", "Time's up!")
            self.entry.config(state="normal")
            self.button.config(state="normal")
            
    def show_notification(self, title, message):
        notification_window = tk.Toplevel(self.master)
        notification_window.title(title)
        notification_window.geometry("300x150")
        notification_window.config(bg="#e3f2fd")
        notification_window.attributes("-topmost", True)
        
        label = tk.Label(notification_window, text=message, font=("Helvetica", 14), fg="#01579b", bg="#e3f2fd")
        label.pack(pady=20)
        
        close_button = tk.Button(notification_window, text="OK", font=("Helvetica", 12), bg="#0288d1", fg="white", relief="raised", command=notification_window.destroy)
        close_button.pack(pady=10)
        
root = tk.Tk()
app = CountdownApp(root)
root.mainloop()