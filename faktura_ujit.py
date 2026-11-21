1import tkinter as tk
from tkinter import messagebox

def llogarit_faturen_sakte():
    try:
        kubiket = float(entry_kubiket.get())
        
        if kubiket < 0:
            messagebox.showerror("Gabim", "Kubikët nuk mund të jenë negativë!")
            return
            
        # Tarifat e sakta sipas KRU Gjakova
        cmimi_uji = 0.52
        cmimi_kanalizimi = 0.18
        tarifa_fikse = 1.30
        
        # Llogaritja
        shuma_uji = kubiket * cmimi_uji
        shuma_kanalizimi = kubiket * cmimi_kanalizimi
        
        shuma_neto = shuma_uji + shuma_kanalizimi + tarifa_fikse
        tvsh = shuma_neto * 0.08
        totali = shuma_neto + tvsh
        
        rezultat_teksti = (
            f"Për {kubiket} kubikë:\n"
            f"• Uji ({cmimi_uji}€): {shuma_uji:.2f} €\n"
            f"• Kanalizimi ({cmimi_kanalizimi}€): {shuma_kanalizimi:.2f} €\n"
            f"• Tarifa fikse: {tarifa_fikse:.2f} €\n"
            f"• Shuma Neto: {shuma_neto:.2f} €\n"
            f"• TVSH (8%): {tvsh:.2f} €\n"
            f"----------------------------------\n"
            f"TOTALI PËR T'U PAGUAR: {totali:.2f} €"
        )
        label_rezultati.config(text=rezultat_teksti)
        
    except ValueError:
        messagebox.showerror("Gabim", "Të lutem shkruaj vetëm një numër!")

app = tk.Tk()
app.title("Llogaritësi - KRU Gjakova")
app.geometry("340x360")

tk.Label(app, text="Shkruaj sa kubikë ke hargjuar:", font=("Arial", 10, "bold")).pack(pady=10)
entry_kubiket = tk.Entry(app, font=("Arial", 12), justify="center", width=15)
entry_kubiket.pack(pady=5)
entry_kubiket.focus()

btn = tk.Button(app, text="Llogarit Faturën", command=llogarit_faturen_sakte, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn.pack(pady=10)

label_rezultati = tk.Label(app, text="", font=("Arial", 10), justify="left", fg="#333")
label_rezultati.pack(pady=10)

app.mainloop()
