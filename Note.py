import tkinter as tk
from tkinter import messagebox

def llogarit_mesataren():
    try:
        notat_pjesa_1 = []
        notat_pjesa_2 = []
        
        ka_pjesen_2 = False
        
        for i in range(len(lendet)):
            # Kontrollojmë Pjesën e I (është e detyrueshme për vitin e parë)
            val1 = entries_p1[i].get().strip()
            if not val1:
                messagebox.showerror("Gabim", f"Ju lutem plotësoni notën e Pjesës I për lëndën '{lendet[i]}'!")
                return
            n1 = float(val1)
            if not (1 <= n1 <= 5):
                messagebox.showerror("Gabim", f"Nota te Pjesa I për '{lendet[i]}' duhet të jetë nga 1 deri në 5!")
                return
            notat_pjesa_1.append(n1)
            
            # Kontrollojmë Pjesën e II (është opsionale / nëse lihet bosh pranohet)
            val2 = entries_p2[i].get().strip()
            if val2:
                n2 = float(val2)
                if not (1 <= n2 <= 5):
                    messagebox.showerror("Gabim", f"Nota te Pjesa II për '{lendet[i]}' duhet të jetë nga 1 deri në 5!")
                    return
                notat_pjesa_2.append(n2)
                
        # Kontrollojmë nëse e gjithë Pjesa e II është e plotësuar
        if len(notat_pjesa_2) == len(lendet):
            ka_pjesen_2 = True

        # Llogaritjet
        mes_p1 = sum(notat_pjesa_1) / len(lendet)
        
        teksti_rezultati = f"Mesatarja Pjesa I: {mes_p1:.2f}\n"
        
        if ka_pjesen_2:
            mes_p2 = sum(notat_pjesa_2) / len(lendet)
            mes_vjetore = (mes_p1 + mes_p2) / 2
            teksti_rezultati += f"Mesatarja Pjesa II: {mes_p2:.2f}\nMesatarja Përgjithshme: {mes_vjetore:.2f}"
        else:
            teksti_rezultati += "Mesatarja Pjesa II: (E pambushur)\nMesatarja Përgjithshme: (Viti i I - Vetëm Pjesa I)"

        rezultat_label.config(text=teksti_rezultati, fg="#2e7d32")
        
    except ValueError:
        messagebox.showerror("Gabim", "Ju lutem kontrolloni që të gjitha fushat e plotësuara të kenë vetëm numra nga 1 deri në 5!")

# Krijimi i dritares kryesore me dizajnin e bukur
root = tk.Tk()
root.title("Kalkulatori i Mesatares - Dëftesa")
root.geometry("480x650")
root.config(bg="#f4f6f9")

lendet = [
    "Gjuhë shqipe", "Gjuhë angleze", "Gjuhë gjermane", "Art muzikor", 
    "Art figurativ", "Matematikë", "Fizikë", "Kimi", "Biologji", 
    "Histori", "Gjeografi", "Ed,qytetare", "Ed,fizike", "TIK", "Mësim zgjedhor"
]

header_frame = tk.Frame(root, bg="#1976d2", pady=10)
header_frame.pack(fill=tk.X)

title_lbl = tk.Label(header_frame, text="Kalkulatori i Notave & Mesatares", font=("Arial", 14, "bold"), fg="white", bg="#1976d2")
title_lbl.pack()

sub_title_lbl = tk.Label(header_frame, text="Plotësoni notat nga 1 deri në 5", font=("Arial", 10), fg="#e3f2fd", bg="#1976d2")
sub_title_lbl.pack()

container = tk.Frame(root, bg="#f4f6f9")
container.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

canvas = tk.Canvas(container, bg="#f4f6f9", highlightthickness=0)
scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#f4f6f9")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

tk.Label(scrollable_frame, text="Lënda", font=("Arial", 10, "bold"), width=16, anchor="w", bg="#f4f6f9", fg="#333").grid(row=0, column=0, padx=5, pady=8)
tk.Label(scrollable_frame, text="Pjesa I", font=("Arial", 10, "bold"), width=7, bg="#f4f6f9", fg="#1976d2").grid(row=0, column=1, padx=5, pady=8)
tk.Label(scrollable_frame, text="Pjesa II", font=("Arial", 10, "bold"), width=7, bg="#f4f6f9", fg="#1976d2").grid(row=0, column=2, padx=5, pady=8)

entries_p1 = []
entries_p2 = []

for i, lenda in enumerate(lendet):
    lbl = tk.Label(scrollable_frame, text=lenda, anchor="w", width=16, font=("Arial", 10), bg="#f4f6f9", fg="#222")
    lbl.grid(row=i+1, column=0, padx=5, pady=4, sticky="w")
    
    e1 = tk.Entry(scrollable_frame, width=7, justify="center", font=("Arial", 10), relief="solid", bd=1)
    e1.grid(row=i+1, column=1, padx=5, pady=4, ipady=3)
    entries_p1.append(e1)
    
    e2 = tk.Entry(scrollable_frame, width=7, justify="center", font=("Arial", 10), relief="solid", bd=1)
    e2.grid(row=i+1, column=2, padx=5, pady=4, ipady=3)
    entries_p2.append(e2)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

bottom_frame = tk.Frame(root, bg="#ffffff", bd=1, relief="solid", padx=10, pady=10)
bottom_frame.pack(fill=tk.X, padx=15, pady=15)

btn_llogarit = tk.Button(bottom_frame, text="Llogarit Mesataren", bg="#2e7d32", fg="white", font=("Arial", 11, "bold"), relief="flat", padx=10, pady=8, command=llogarit_mesataren)
btn_llogarit.pack(fill=tk.X, pady=5)

rezultat_label = tk.Label(bottom_frame, text="Mesatarja Pjesa I: - \nMesatarja Pjesa II: - \nMesatarja Përgjithshme: -", font=("Arial", 10, "bold"), bg="#ffffff", fg="#333", justify="left")
rezultat_label.pack(pady=5, anchor="w")

root.mainloop()
