import keyboard
import time
import tkinter as tk
from tkinter import ttk

class KeyboardClicker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("键盘连点器")
        self.root.geometry("300x200")
        
        # 创建样式
        style = ttk.Style()
        style.configure("TButton", padding=5)
        style.configure("TLabel", padding=5)
        style.configure("TEntry", padding=5)
        
        # 创建控件
        ttk.Label(self.root, text="点击间隔（秒）:").pack(pady=5)
        self.interval = ttk.Entry(self.root)
        self.interval.insert(0, "1.0")
        self.interval.pack(pady=5)
        
        ttk.Label(self.root, text="触发按键:").pack(pady=5)
        self.key = ttk.Entry(self.root)
        self.key.insert(0, "f")
        self.key.pack(pady=5)
        
        self.start_button = ttk.Button(self.root, text="开始", command=self.toggle)
        self.start_button.pack(pady=10)
        
        self.running = False
        
    def toggle(self):
        if not self.running:
            try:
                interval = float(self.interval.get())
                key = self.key.get()
                if not key:
                    raise ValueError("请输入触发按键")
                    
                self.running = True
                self.start_button.config(text="停止")
                keyboard.on_press_key(key, self.on_trigger)
                
            except ValueError as e:
                tk.messagebox.showerror("错误", str(e))
        else:
            self.running = False
            self.start_button.config(text="开始")
            keyboard.unhook_all()
            
    def on_trigger(self, e):
        if self.running:
            try:
                interval = float(self.interval.get())
                keyboard.press_and_release(e.name)
                time.sleep(interval)
            except ValueError:
                self.running = False
                self.start_button.config(text="开始")
                keyboard.unhook_all()
                tk.messagebox.showerror("错误", "无效的时间间隔")
                
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = KeyboardClicker()
    app.run()