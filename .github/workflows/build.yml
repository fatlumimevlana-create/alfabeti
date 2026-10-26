import datetime
import json
import random
import time
import tkinter as tk
from tkinter import messagebox


def llogarit_moshen(data_str):
    try:
        data_lindjes = datetime.datetime.strptime(data_str, "%d.%m.%Y")
        sot = datetime.datetime.now()
        return (
            sot.year
            - data_lindjes.year
            - ((sot.month, sot.day) < (data_lindjes.month, data_lindjes.day))
        )
    except ValueError:
        return None


def gjenero_kartelen():
    emri = entry_emri.get().strip()
    mbiemri = entry_mbiemri.get().strip()
    data_lindjes_str = entry_data.get().strip()
    gjinia = gjinia_var.get()

    if not emri or not mbiemri or not data_lindjes_str:
        messagebox.showwarning("Kujdes", "Ju lutem plotësoni të gjitha fushat!")
        return

    mosha = llogarit_moshen(data_lindjes_str)
    if mosha is None:
        messagebox.showerror(
            "Gabim", "Format i gabuar i datës! Përdorni: DD.MM.YYYY"
        )
        return

    try:
        pjesa_dates = datetime.datetime.strptime(
            data_lindjes_str, "%d.%m.%Y"
        ).strftime("%d%m%y")
        shifrat_rastesishme = str(random.randint(1000, 9999))
        nr_personal = pjesa_dates + shifrat_rastesishme
    except ValueError:
        nr_personal = str(random.randint(1000000000, 9999999999))

    # Përditësimi i kartelës
    lbl_rez_emri.config(text=f"Emri: {emri}")
    lbl_rez_mbiemri.config(text=f"Mbiemri: {mbiemri}")
    lbl_rez_gjinia.config(text=f"Gjinia: {gjinia}")
    lbl_rez_mosha.config(text=f"Mosha: {mosha} vjeç")
    lbl_rez_id.config(text=f"ID Personale: {nr_personal}")

    # Ruajtja në JSON
    data_personit = {
        "Emri": emri,
        "Mbiemri": mbiemri,
        "Data_Lindjes": data_lindjes_str,
        "Gjinia": gjinia,
        "Mosha": mosha,
        "ID_Personale": nr_personal,
    }

    try:
        with open("leternjoftimet.json", "a", encoding="utf-8") as f:
            json.dump(data_personit, f, ensure_ascii=False)
            f.write("\n")
        messagebox.showinfo(
            "Sukses", "Letërnjoftimi u gjenerua dhe u ruajt me sukses!"
        )
    except Exception as e:
        messagebox.showerror("Gabim", f"Nuk u ruajt dot: {e}")


def shiko_te_ruajturat():
    dritarja_listes = tk.Toplevel(root)
    dritarja_listes.title("Regjistri i Ruajtur")
    dritarja_listes.geometry("380x420")
    dritarja_listes.config(bg="#f4f6f9")

    tk.Label(
        dritarja_listes,
        text="Personat e Regjistruar",
        font=("Arial", 12, "bold"),
        bg="#0d47a1",
        fg="white",
        pady=8,
    ).pack(fill="x")

    text_box = tk.Text(
        dritarja_listes, font=("Arial", 9), bg="#ffffff", fg="#333333"
    )
    text_box.pack(fill="both", expand=True, padx=10, pady=10)

    try:
        with open("leternjoftimet.json", "r", encoding="utf-8") as f:
            for rresht in f:
                if rresht.strip():
                    p = json.loads(rresht)
                    info = f"Emri: {p.get('Emri')} {p.get('Mbiemri')}\nGjinia: {p.get('Gjinia', '-')}\nID: {p.get('ID_Personale')}\nMosha: {p.get('Mosha')}\n-----------------------------------\n"
                    text_box.insert(tk.END, info)
    except FileNotFoundError:
        text_box.insert(tk.END, "Nuk u gjet asnjë regjistrim i ruajtur ende!")

    text_box.config(state=tk.DISABLED)


# Dritarja Kryesore
root = tk.Tk()
root.title("Gjeneruesi i Letërnjoftimit")
root.geometry("420x660")
root.config(bg="#f4f6f9")

header_frame = tk.Frame(root, bg="#0d47a1", height=50)
header_frame.pack(fill="x")

lbl_titulli = tk.Label(
    header_frame,
    text="LETËRNJOFTIM DIGJITAL",
    font=("Arial", 13, "bold"),
    bg="#0d47a1",
    fg="white",
)
lbl_titulli.pack(pady=12)

# Korniza e inputeve
frame_input = tk.Frame(root, bg="#f4f6f9")
frame_input.pack(pady=5)

tk.Label(
    frame_input,
    text="Emri:",
    font=("Arial", 9, "bold"),
    bg="#f4f6f9",
    fg="#333333",
).grid(row=0, column=0, sticky="w", pady=3, padx=5)
entry_emri = tk.Entry(
    frame_input, font=("Arial", 10), relief="solid", bd=1, width=22
)
entry_emri.grid(row=0, column=1, pady=3, padx=5)

tk.Label(
    frame_input,
    text="Mbiemri:",
    font=("Arial", 9, "bold"),
    bg="#f4f6f9",
    fg="#333333",
).grid(row=1, column=0, sticky="w", pady=3, padx=5)
entry_mbiemri = tk.Entry(
    frame_input, font=("Arial", 10), relief="solid", bd=1, width=22
)
entry_mbiemri.grid(row=1, column=1, pady=3, padx=5)

tk.Label(
    frame_input,
    text="Data e Lindjes (DD.MM.YYYY):",
    font=("Arial", 9, "bold"),
    bg="#f4f6f9",
    fg="#333333",
).grid(row=2, column=0, sticky="w", pady=3, padx=5)
entry_data = tk.Entry(
    frame_input, font=("Arial", 10), relief="solid", bd=1, width=22
)
entry_data.grid(row=2, column=1, pady=3, padx=5)

# Fusha e Gjinisë
tk.Label(
    frame_input,
    text="Gjinia:",
    font=("Arial", 9, "bold"),
    bg="#f4f6f9",
    fg="#333333",
).grid(row=3, column=0, sticky="w", pady=3, padx=5)

gjinia_var = tk.StringVar(value="M")
frame_gjinise = tk.Frame(frame_input, bg="#f4f6f9")
frame_gjinise.grid(row=3, column=1, sticky="w", pady=3, padx=5)

tk.Radiobutton(
    frame_gjinise,
    text="Mashkull (M)",
    variable=gjinia_var,
    value="M",
    bg="#f4f6f9",
    font=("Arial", 9),
).pack(side="left", padx=(0, 10))
tk.Radiobutton(
    frame_gjinise,
    text="Femër (F)",
    variable=gjinia_var,
    value="F",
    bg="#f4f6f9",
    font=("Arial", 9),
).pack(side="left")

# Butonët
btn_gjenero = tk.Button(
    root,
    text="Gjenero Letërnjoftimin",
    command=gjenero_kartelen,
    bg="#1976d2",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="raised",
    bd=2,
    padx=10,
    pady=3,
)
btn_gjenero.pack(pady=4)

btn_shiko = tk.Button(
    root,
    text="Shiko të Ruajturat (Regjistri)",
    command=shiko_te_ruajturat,
    bg="#388e3c",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="raised",
    bd=2,
    padx=10,
    pady=3,
)
btn_shiko.pack(pady=4)

# Pamja e Kartelës
frame_kartela = tk.LabelFrame(
    root,
    text=" Të dhënat e Kartelës ",
    font=("Arial", 10, "bold"),
    bg="#ffffff",
    fg="#0d47a1",
    relief="groove",
    bd=2,
    padx=15,
    pady=8,
)
frame_kartela.pack(pady=5, fill="both", expand=True, padx=20)

lbl_rez_emri = tk.Label(
    frame_kartela,
    text="Emri: -",
    font=("Arial", 9, "bold"),
    bg="#ffffff",
    fg="#333333",
    anchor="w",
)
lbl_rez_emri.pack(fill="x", pady=2)

lbl_rez_mbiemri = tk.Label(
    frame_kartela,
    text="Mbiemri: -",
    font=("Arial", 9, "bold"),
    bg="#ffffff",
    fg="#333333",
    anchor="w",
)
lbl_rez_mbiemri.pack(fill="x", pady=2)

lbl_rez_gjinia = tk.Label(
    frame_kartela,
    text="Gjinia: -",
    font=("Arial", 9),
    bg="#ffffff",
    fg="#555555",
    anchor="w",
)
lbl_rez_gjinia.pack(fill="x", pady=2)

lbl_rez_mosha = tk.Label(
    frame_kartela,
    text="Mosha: -",
    font=("Arial", 9),
    bg="#ffffff",
    fg="#555555",
    anchor="w",
)
lbl_rez_mosha.pack(fill="x", pady=2)

lbl_rez_id = tk.Label(
    frame_kartela,
    text="ID Personale: -",
    font=("Arial", 9, "bold"),
    fg="#d32f2f",
    bg="#ffffff",
    anchor="w",
)
lbl_rez_id.pack(fill="x", pady=2)

root.mainloop()
