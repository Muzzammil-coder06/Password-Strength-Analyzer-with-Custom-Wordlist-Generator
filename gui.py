import tkinter as tk
from tkinter import ttk
from analyzer import analyze_password
from wordlist_generator import generate_wordlist, export_wordlist
from PIL import Image, ImageTk

# ---------- Colors and Styles ----------
BG_COLOR = "#1e1e2f"
FG_COLOR = "#f5f5f5"
BTN_COLOR = "#3c3f58"
ENTRY_BG = "#2e2e3f"
HIGHLIGHT = "#ffa94d"
LIGHT_BG = "#f5f5f5"
LIGHT_FG = "#1e1e2f"

# ---------- App Window ----------
root = tk.Tk()
root.title("🔐 Password Strength Analyzer")
root.geometry("520x550")
root.configure(bg=BG_COLOR)

# ---------- App Icon ----------
try:
    root.iconbitmap("icon.ico")
except:
    pass

# ---------- Style ----------
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TFrame", background=BG_COLOR)
style.configure("TLabel", background=BG_COLOR, foreground=FG_COLOR, font=('Segoe UI', 11))
style.configure("TEntry", fieldbackground=ENTRY_BG, foreground=FG_COLOR)
style.configure("TButton", background=BTN_COLOR, foreground=FG_COLOR, padding=6)

# ---------- Strength Meter Colors ----------
style.configure("Red.Horizontal.TProgressbar", troughcolor=BG_COLOR, background="red")
style.configure("Orange.Horizontal.TProgressbar", troughcolor=BG_COLOR, background="orange")
style.configure("Yellow.Horizontal.TProgressbar", troughcolor=BG_COLOR, background="yellow")
style.configure("Green.Horizontal.TProgressbar", troughcolor=BG_COLOR, background="green")

# ---------- Main Frame ----------
frame = ttk.Frame(root, padding=20, style="TFrame")
frame.pack(expand=True, fill="both")

# ---------- Optional Banner ----------
try:
    img = Image.open("banner.png")
    img = img.resize((460, 80))
    photo = ImageTk.PhotoImage(img)
    img_label = ttk.Label(frame, image=photo)
    img_label.image = photo
    img_label.pack(pady=10)
except:
    pass

# ---------- Heading ----------
heading = ttk.Label(frame, text="Password Strength Analyzer", font=('Segoe UI', 16, 'bold'), foreground=HIGHLIGHT)
heading.pack(pady=10)

# ---------- Password Input ----------
ttk.Label(frame, text="Enter Password:").pack(anchor="w")
entry = ttk.Entry(frame, width=50)
entry.pack(pady=5)

# ---------- Output Text ----------
output = tk.StringVar()
output_label = ttk.Label(frame, textvariable=output, wraplength=450)
output_label.pack(pady=10)

# ---------- Password Strength Meter ----------
meter_label = ttk.Label(frame, text="Password Strength Meter:")
meter_label.pack(pady=(10, 0))

meter = ttk.Progressbar(frame, orient='horizontal', length=300, mode='determinate', maximum=4, style="Red.Horizontal.TProgressbar")
meter.pack(pady=5)

# ---------- Analyze Password ----------
def analyze():
    password = entry.get()
    result = analyze_password(password)
    output.set(f"Score: {result['score']}/4\nCrack Time: {result['crack_time']}\n{result['feedback']['warning']}")
    meter['value'] = result['score']

    # Change meter color based on score
    if result['score'] <= 1:
        meter.configure(style="Red.Horizontal.TProgressbar")
    elif result['score'] == 2:
        meter.configure(style="Orange.Horizontal.TProgressbar")
    elif result['score'] == 3:
        meter.configure(style="Yellow.Horizontal.TProgressbar")
    else:
        meter.configure(style="Green.Horizontal.TProgressbar")

ttk.Button(frame, text="Analyze Password", command=analyze).pack(pady=10)

# ---------- Wordlist Input ----------
ttk.Label(frame, text="Keywords for Wordlist (comma separated):").pack(anchor="w", pady=(10, 0))
entry_words = ttk.Entry(frame, width=50)
entry_words.pack(pady=5)

# ---------- Generate Wordlist ----------
def create_wordlist():
    base_words = entry_words.get().split(',')
    wordlist = generate_wordlist(base_words)
    export_wordlist(wordlist)
    output.set("\u2705 Wordlist generated and saved!")

ttk.Button(frame, text="Generate Wordlist", command=create_wordlist).pack(pady=10)

# ---------- Theme Toggle ----------
is_dark = True

def toggle_theme():
    global is_dark
    if is_dark:
        style.configure("TFrame", background=LIGHT_BG)
        style.configure("TLabel", background=LIGHT_BG, foreground=LIGHT_FG)
        style.configure("TEntry", fieldbackground="white", foreground="black")
        style.configure("TButton", background="#dcdcdc", foreground="black")
        frame.configure(style="TFrame")
        root.configure(bg=LIGHT_BG)
    else:
        style.configure("TFrame", background=BG_COLOR)
        style.configure("TLabel", background=BG_COLOR, foreground=FG_COLOR)
        style.configure("TEntry", fieldbackground=ENTRY_BG, foreground=FG_COLOR)
        style.configure("TButton", background=BTN_COLOR, foreground=FG_COLOR)
        frame.configure(style="TFrame")
        root.configure(bg=BG_COLOR)
    is_dark = not is_dark

ttk.Button(frame, text="Toggle Light/Dark Mode", command=toggle_theme).pack(pady=10)

# ---------- Mainloop ----------
root.mainloop()
