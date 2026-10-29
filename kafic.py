import tkinter as tk
from tkinter import messagebox
from collections import Counter

MENYJA = {
    "Kafe Espresso": 0.50,
    "Makijato e vogël": 0.50,
    "Makijato e madhe": 0.80,
    "Ujë i gazuar": 0.50,
    "Kokakolla (kanacë)": 1.00,
    "Birrë": 1.00
}

class KafeneApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menaxhimi i Kafenesë")
        self.root.geometry("400x600")
        self.root.config(bg="#f0f0f0")

        # Ruajtja e porosive për secilën nga 10 tavolinat veç e veç
        self.tavolinat = {i: {"porosia": [], "totali": 0.0} for i in range(1, 11)}
        self.tavolina_aktuale = 1

        # Titulli
        tk.Label(root, text="☕ Sistemi i Kafenesë", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#d32f2f").pack(pady=5)

        # Tavolinat (Zgjedhja)
        tk.Label(root, text="Zgjidhni Tavolinën:", font=("Arial", 10, "bold"), bg="#f0f0f0").pack(anchor="w", padx=15)
        
        frame_tav = tk.Frame(root, bg="#f0f0f0")
        frame_tav.pack(pady=5, padx=10)

        self.butona_tav = {}
        for i in range(1, 11):
            rreshti = (i - 1) // 5
            kolona = (i - 1) % 5
            btn = tk.Button(
                frame_tav, 
                text=f"Tav. {i}\n(E lirë)", 
                width=7, height=2,
                bg="lightgreen",
                font=("Arial", 9, "bold"),
                command=lambda t=i: self.ndryshoTavolinen(t)
            )
            btn.grid(row=rreshti, column=kolona, padx=3, pady=3)
            self.butona_tav[i] = btn

        # Info se cila tavolinë është e zgjedhur aktualisht
        self.lbl_info = tk.Label(root, text="Duke porositur për: Tavolina 1", font=("Arial", 11, "bold"), bg="#ffeb3b", fg="#333")
        self.lbl_info.pack(fill="x", padx=10, pady=5)

        # Menyja për të shtuar artikuj
        tk.Label(root, text="Shto Pije:", font=("Arial", 10, "bold"), bg="#f0f0f0").pack(anchor="w", padx=15)
        
        frame_meny = tk.Frame(root, bg="#f0f0f0")
        frame_meny.pack(pady=2, padx=10, fill="x")

        for emri, cmimi in MENYJA.items():
            btn_pije = tk.Button(
                frame_meny, 
                text=f"{emri} - {cmimi:.2f}€", 
                font=("Arial", 9, "bold"),
                bg="white",
                anchor="w",
                padx=10,
                command=lambda e=emri: self.shtoArtikull(e)
            )
            btn_pije.pack(pady=2, fill="x")

        # Lista e porosive për tavolinën aktuale
        tk.Label(root, text="Porosia Aktuale e Tavolinës:", font=("Arial", 10, "bold"), bg="#f0f0f0").pack(anchor="w", padx=15, pady=(5, 0))
        
        self.listbox = tk.Listbox(root, width=40, height=5, font=("Arial", 10))
        self.listbox.pack(padx=10, pady=2)

        # Totali dhe butonat
        self.lbl_totali = tk.Label(root, text="Totali: 0.00€", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="darkblue")
        self.lbl_totali.pack(pady=5)

        frame_veprime = tk.Frame(root, bg="#f0f0f0")
        frame_veprime.pack(pady=5, fill="x", padx=10)

        tk.Button(frame_veprime, text="Fshi Fundit", bg="#ffcccc", font=("Arial", 9), command=self.fshiArtikullin).pack(side="left", expand=True, fill="x", padx=2)
        tk.Button(frame_veprime, text="Paguaj / Liro", bg="#4CAF50", fg="white", font=("Arial", 9, "bold"), command=self.paguajFaturen).pack(side="right", expand=True, fill="x", padx=2)

    def ndryshoTavolinen(self, nr):
        # Kur ndryshon tavolina, shfaqet porosia e ruajtur për atë tavolinë
        self.tavolina_aktuale = nr
        self.lbl_info.config(text=f"Duke porositur për: Tavolina {nr}")
        self.rifreskoPamjen()

    def shtoArtikull(self, emri):
        cmimi = MENYJA[emri]
        tav = self.tavolina_aktuale
        # Shton pijen te tavolina aktuale
        self.tavolinat[tav]["porosia"].append((emri, cmimi))
        self.rifreskoPamjen()
        self.peditButoninTavolines(tav)

    def fshiArtikullin(self):
        tav = self.tavolina_aktuale
        porosia = self.tavolinat[tav]["porosia"]
        if porosia:
            porosia.pop()
            self.rifreskoPamjen()
            self.peditButoninTavolines(tav)

    def rifreskoPamjen(self):
        self.listbox.delete(0, tk.END)
        tav = self.tavolina_aktuale
        porosia = self.tavolinat[tav]["porosia"]
        
        shumarica = Counter(porosia)
        totali = 0
        for item, sasia in shumarica.items():
            emri, cmimi = item
            cmimi_total = cmimi * sasia
            self.listbox.insert(tk.END, f"{sasia}x {emri} - {cmimi_total:.2f}€")
            totali += cmimi_total
            
        self.tavolinat[tav]["totali"] = totali
        self.lbl_totali.config(text=f"Totali: {totali:.2f}€")

    def peditButoninTavolines(self, nr):
        totali = self.tavolinat[nr]["totali"]
        if totali > 0:
            self.butona_tav[nr].config(text=f"Tav. {nr}\n({totali:.2f}€)", bg="lightcoral")
        else:
            self.butona_tav[nr].config(text=f"Tav. {nr}\n(E lirë)", bg="lightgreen")

    def paguajFaturen(self):
        tav = self.tavolina_aktuale
        totali = self.tavolinat[tav]["totali"]
        if totali == 0:
            messagebox.showinfo("Kujdes", f"Tavolina {tav} nuk ka porosi aktive!")
            return
        
        messagebox.showinfo("Pagesa", f"Fatura për Tavolinën {tav} u pagua!\nTotali: {totali:.2f}€")
        
        # Fshin totalisht llogarinë dhe e liron tavolinën
        self.tavolinat[tav]["porosia"] = []
        self.tavolinat[tav]["totali"] = 0.0
        self.rifreskoPamjen()
        self.peditButoninTavolines(tav)

if __name__ == "__main__":
    root = tk.Tk()
    app = KafeneApp(root)
    root.mainloop()
