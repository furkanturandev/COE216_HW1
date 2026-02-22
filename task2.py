import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk
import os

# ======================
# PARAMETRELER
# ======================

fs = 8000      # Sampling frequency
T = 0.3        # Ses süresi (saniye)

# ======================
# DTMF FREKANS TABLOSU
# ======================

dtmf = {
    "1": (697, 1209), "2": (697, 1336), "3": (697, 1477), "A": (697, 1633),
    "4": (770, 1209), "5": (770, 1336), "6": (770, 1477), "B": (770, 1633),
    "7": (852, 1209), "8": (852, 1336), "9": (852, 1477), "C": (852, 1633),
    "*": (941, 1209), "0": (941, 1336), "#": (941, 1477), "D": (941, 1633)
}

# ======================
# RENK PALETİ
# ======================

COLORS = {
    "bg":           "#1a1a2e",   # Koyu arka plan
    "panel":        "#16213e",   # Panel arka planı
    "btn_num":      "#0f3460",   # Rakam butonları
    "btn_num_hover":"#1a5276",   # Rakam hover
    "btn_letter":   "#e94560",   # Harf butonları (A,B,C,D)
    "btn_letter_hover":"#ff6b6b",# Harf hover
    "btn_special":  "#533483",   # Özel tuşlar (*,#)
    "btn_special_hover":"#7c3aed",
    "btn_text":     "#ffffff",   # Buton yazı rengi
    "title_text":   "#e0e0e0",  # Başlık yazı rengi
    "display_bg":   "#0a0a1a",  # Ekran arka planı
    "display_text": "#00d4ff",  # Ekran yazı rengi
    "accent":       "#00d4ff",  # Vurgu rengi
}

# =========================
# SİNYAL ÜRETME FONKSİYONU
# =========================

def play_tone(key):
    f_low, f_high = dtmf[key]
    t = np.arange(0, T, 1/fs)

    signal = 0.5 * (
        np.sin(2 * np.pi * f_low * t) +
        np.sin(2 * np.pi * f_high * t)
    )

    # Ekranı güncelle
    display_var.set(f"  {key}  →  {f_low} Hz + {f_high} Hz")

    # SES ÇAL
    sd.play(signal, fs)

    # GRAFİK GÖSTER (modern stil)
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(t, signal, color="#00d4ff", linewidth=0.8, alpha=0.9)
    ax.fill_between(t, signal, alpha=0.15, color="#00d4ff")
    ax.set_title(f"DTMF Signal — Key '{key}'  ({f_low} Hz + {f_high} Hz)",
                 fontsize=14, fontweight="bold", color="#e0e0e0", pad=15)
    ax.set_xlabel("Time (seconds)", fontsize=11, color="#aaaaaa")
    ax.set_ylabel("Amplitude", fontsize=11, color="#aaaaaa")
    ax.tick_params(colors="#888888")
    ax.grid(True, alpha=0.2, linestyle="--")
    fig.patch.set_facecolor("#1a1a2e")
    ax.set_facecolor("#0a0a1a")
    plt.tight_layout()
    plt.show()


# ======================
# HOVER EFEKT YARDIMCISI
# ======================

def on_enter(e, color):
    e.widget.config(bg=color)

def on_leave(e, color):
    e.widget.config(bg=color)

def get_btn_colors(key):
    """Tuş tipine göre renk döndürür."""
    if key in ("A", "B", "C", "D"):
        return COLORS["btn_letter"], COLORS["btn_letter_hover"]
    elif key in ("*", "#"):
        return COLORS["btn_special"], COLORS["btn_special_hover"]
    else:
        return COLORS["btn_num"], COLORS["btn_num_hover"]


# ======================
# GUI OLUŞTUR
# ======================

root = tk.Tk()
root.title("İSTÜN Keypad")
root.configure(bg=COLORS["bg"])
root.resizable(False, False)

# — Logo yükle —
script_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(script_dir, "istun_logo_red.png")
logo_img_original = Image.open(logo_path).convert("RGBA")
orig_w, orig_h = logo_img_original.size


# Pencere ikonu (32x32 şeffaf tuvalde ortalanmış, oran korunur)
icon_size = 32
icon_canvas = Image.new("RGBA", (icon_size, icon_size), (0, 0, 0, 0))
scale = min(icon_size / orig_w, icon_size / orig_h)
icon_w = int(orig_w * scale)
icon_h = int(orig_h * scale)
icon_img = logo_img_original.resize((icon_w, icon_h), Image.LANCZOS)
icon_x = (icon_size - icon_w) // 2
icon_y = (icon_size - icon_h) // 2
icon_canvas.paste(icon_img, (icon_x, icon_y), icon_img)
icon_photo = ImageTk.PhotoImage(icon_canvas)
root.iconphoto(True, icon_photo)

# Başlık logosu (36px yükseklik, oran korunur)
header_h = 36
header_w = int(orig_w * (header_h / orig_h))
header_logo_img = logo_img_original.resize((header_w, header_h), Image.LANCZOS)
header_logo_photo = ImageTk.PhotoImage(header_logo_img)

# — Fontlar —
title_font   = tkfont.Font(family="Segoe UI", size=18, weight="bold")
display_font = tkfont.Font(family="Consolas", size=14)
btn_font     = tkfont.Font(family="Segoe UI", size=16, weight="bold")
sub_font     = tkfont.Font(family="Segoe UI", size=8)

# — Başlık —
header = tk.Frame(root, bg=COLORS["bg"])
header.pack(fill="x", pady=(18, 5))

title_frame = tk.Frame(header, bg=COLORS["bg"])
title_frame.pack()

tk.Label(
    title_frame, image=header_logo_photo, bg=COLORS["bg"]
).pack(side="left", padx=(0, 8))

tk.Label(
    title_frame, text="İSTÜN Keypad", font=title_font,
    fg=COLORS["title_text"], bg=COLORS["bg"]
).pack(side="left")

tk.Label(
    header, text="Dual-Tone Multi-Frequency Generator", font=sub_font,
    fg="#666680", bg=COLORS["bg"]
).pack()

# — Dijital Ekran —
display_var = tk.StringVar(value="  Press a key…")

display_frame = tk.Frame(root, bg=COLORS["accent"], padx=2, pady=2)
display_frame.pack(padx=20, pady=(10, 15), fill="x")

display_label = tk.Label(
    display_frame, textvariable=display_var, font=display_font,
    fg=COLORS["display_text"], bg=COLORS["display_bg"],
    anchor="w", padx=15, pady=10
)
display_label.pack(fill="x")

# — Keypad Paneli —
keypad_frame = tk.Frame(root, bg=COLORS["panel"], padx=12, pady=12)
keypad_frame.pack(padx=20, pady=(0, 20))

keys = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]
]

# Küçük harfler (alt etiketler)
sub_labels = {
    "2": "ABC", "3": "DEF",
    "4": "GHI", "5": "JKL", "6": "MNO",
    "7": "PQRS", "8": "TUV", "9": "WXYZ",
    "0": "+"
}

for r in range(4):
    for c in range(4):
        key = keys[r][c]
        bg_color, hover_color = get_btn_colors(key)

        # Buton çerçevesi (boşluk için)
        cell = tk.Frame(keypad_frame, bg=COLORS["panel"])
        cell.grid(row=r, column=c, padx=4, pady=4)

        btn = tk.Button(
            cell,
            text=key,
            font=btn_font,
            width=4,
            height=2,
            fg=COLORS["btn_text"],
            bg=bg_color,
            activebackground=hover_color,
            activeforeground="#ffffff",
            bd=0,
            relief="flat",
            cursor="hand2",
            command=lambda k=key: play_tone(k)
        )
        btn.pack()

        # Hover efektleri
        btn.bind("<Enter>", lambda e, hc=hover_color: on_enter(e, hc))
        btn.bind("<Leave>", lambda e, bc=bg_color: on_leave(e, bc))

# — Alt bilgi —
tk.Label(
    root,
    text="fs = 8000 Hz  ·  T = 0.3 s",
    font=sub_font,
    fg="#555570",
    bg=COLORS["bg"]
).pack(pady=(0, 12))

# — Pencereyi ortala —
root.update_idletasks()
w = root.winfo_width()
h = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (w // 2)
y = (root.winfo_screenheight() // 2) - (h // 2)
root.geometry(f"+{x}+{y}")

root.mainloop()