import tkinter as tk
from tkinter import messagebox

def tampilkan_rayuan():
    """Fungsi yang dipanggil ketika tombol diklik untuk memunculkan rayuan gombal."""
    nama = entry_nama.get().strip()
    if not nama:
        nama = "Cantik"
        
    # Pesan rayuan manis
    pesan = (
        f"Halo, {nama}! 💕\n\n"
        "Kamu tahu enggak bedanya kamu sama soal ujian?\n"
        "Kalau soal ujian susah untuk dipecahkan...\n"
        "Tapi kalau kamu, senyumanmu justru sukses memecahkan hatiku "
        "tiap detik!\n\n"
        "Tetap jadi matahari di hariku ya! ✨"
    )
    
    # Mengubah teks di label luaran
    label_hasil.config(
        text=f"Pesan Spesial untuk {nama}:\n" + "Kamu adalah pemenang di hatiku! 💖",
        fg="#880e4f",
        bg="#f8bbd0"
    )
    
    # Memunculkan pop-up romantis
    messagebox.showinfo("Spesial Buat Kamu ❤️", pesan)

# ==========================================
# Konfigurasi Window Utama (Tkinter)
# ==========================================
root = tk.Tk()
root.title("Aplikasi Penakluk Hati v1.0")
root.geometry("450x450")
root.configure(bg="#ffebee")

# ==========================================
# 1. Judul Aplikasi (Label Widget)
# ==========================================
label_judul = tk.Label(
    root, 
    text="❤️ APLIKASI SPESIAL ❤️", 
    font=("Helvetica", 14, "bold"),
    bg="#ffebee",
    fg="#c2185b"
)
label_judul.pack(pady=20)

# ==========================================
# 2. Container (Frame Widget)
# ==========================================
frame_utama = tk.Frame(root, bg="#ffffff", padx=20, pady=20, relief=tk.RIDGE, bd=2)
frame_utama.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Label Nama Cewek
lbl_nama = tk.Label(frame_utama, text="Masukkan Nama Kamu:", font=("Arial", 10), bg="#ffffff", fg="#333333")
lbl_nama.pack(anchor="w", pady=(0, 5))

# Input Nama (Entry Widget)
entry_nama = tk.Entry(frame_utama, font=("Arial", 11), width=25, bd=2, relief=tk.GROOVE)
entry_nama.pack(anchor="w", pady=(0, 15))

# ==========================================
# 3. Tombol Eksekusi (Button Widget)
# ==========================================
btn_rayu = tk.Button(
    frame_utama, 
    text="Klik untuk Lihat Rayuan", 
    command=tampilkan_rayuan,
    bg="#e91e63", 
    fg="white", 
    font=("Arial", 11, "bold"),
    padx=10, 
    pady=5,
    cursor="hand2"
)
btn_rayu.pack(pady=10)

# ==========================================
# 4. Label Luaran / Output (Label Widget)
# ==========================================
label_hasil = tk.Label(
    frame_utama, 
    text="Hasil rayuan akan muncul di sini...", 
    font=("Arial", 10, "italic"),
    bg="#fce4ec",
    fg="#ad1457",
    width=35,
    height=3,
    relief=tk.SUNKEN
)
label_hasil.pack(pady=15)

# Menjalankan aplikasi
root.mainloop()