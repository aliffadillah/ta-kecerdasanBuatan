import tkinter as tk
from tkinter import ttk, messagebox

# Definisikan nilai-nilai yang tersedia
KG1_Kerusakan_Mesin_DOHC = {  # kerusakan mesin
    "G01 - Rantai Mesin Kendor": 0.40,
    "G02 - Knalpot berubah menjadi berwarna kekuningan": 0.7,
    "G03 - Setelan klep (shim klep) yang mulai aus": 0.8,
    "G04 - Mesin brebet (bersuara kasar) di RPM rendah": 0.45,
    "G05 - Mesin mengeluarkan suara berisik dan tidak normal": 0.43
}

KG2_Kerusakan_Sistem_Mesin_Performa_Lemah = {
    "G06 - Sistem pendingin tidak maksimal": 0.6,
    "G07 - Mesin panas": 0.70,
    "G08 - Kompresi bocor": 0.8
}

KG3_Kerusakan_Mesin_Gampang_Mogok = {
    "G04 - Mesin brebet (bersuara kasar) di RPM rendah": 0.40,
    "G05 - Mesin mengeluarkan suara berisik dan tidak normal": 0.38,
    "G09 - Busi kemasukan air": 0.65,
    "G10 - Banyak kotoran di lubang pembuangan / knalpot": 0.75,
    "G11 - Sistem bahan bakar rusak/sumbat": 0.8
}

def tampilkan_nilai(nilai_dict):
    return "\n".join([f"{kunci}: {nilai}" for kunci, nilai in nilai_dict.items()])

def jumlahkan_nilai(nilai_dict, kunci_dipilih):
    nilai_dipilih = {}
    total = 0
    for kunci in kunci_dipilih:
        if kunci in nilai_dict:
            nilai_dipilih[kunci] = nilai_dict[kunci]
            total += nilai_dict[kunci]
    return total, nilai_dipilih

def bagi_nilai_dengan_total(nilai_dipilih, total):
    hasil_bagi = {}
    for kunci, nilai in nilai_dipilih.items():
        hasil_bagi[kunci] = nilai / total if total != 0 else "Tidak dapat dibagi dengan 0"
    return hasil_bagi

def kalikan_dan_jumlahkan(nilai_dipilih, hasil_bagi):
    total_kalikan = 0
    hasil_kalikan = {}
    for kunci, nilai in hasil_bagi.items():
        if nilai != "Tidak dapat dibagi dengan 0":
            hasil_kalikan[kunci] = nilai * nilai_dipilih[kunci]
            total_kalikan += hasil_kalikan[kunci]
        else:
            hasil_kalikan[kunci] = nilai
    return total_kalikan, hasil_kalikan

def kalikan_dan_bagi(nilai_dipilih, hasil_bagi, total_kalikan):
    hasil_akhir = {}
    for kunci, nilai in hasil_bagi.items():
        if total_kalikan != 0 and nilai != "Tidak dapat dibagi dengan 0":
            hasil_akhir[kunci] = (nilai_dipilih[kunci] * nilai) / total_kalikan
        else:
            hasil_akhir[kunci] = "Tidak dapat dibagi dengan 0 atau total perkalian adalah 0"
    return hasil_akhir

def langkah_6(nilai_dipilih, hasil_akhir):
    hasil_l6 = {}
    total_l6 = 0
    for kunci, nilai in hasil_akhir.items():
        if nilai != "Tidak dapat dibagi dengan 0 atau total perkalian adalah 0":
            hasil_l6[kunci] = nilai_dipilih[kunci] * nilai
            total_l6 += hasil_l6[kunci]
        else:
            hasil_l6[kunci] = nilai
    return total_l6, hasil_l6

def konversi_ke_persen(nilai):
    return int(nilai * 100)

def tampilkan_hasil(nilai_dipilih, total, hasil_bagi, total_kalikan, hasil_akhir, total_l6, persen):
    hasil = (
        f"Nilai yang dipilih:\n{tampilkan_nilai(nilai_dipilih)}\n\n"
        f"Total nilai yang dipilih: {total}\n\n"
        f"Hasil pembagian:\n{tampilkan_nilai(hasil_bagi)}\n\n"
        f"Total perkalian: {total_kalikan}\n\n"
        f"Hasil akhir:\n{tampilkan_nilai(hasil_akhir)}\n\n"
        f"Total langkah 6: {total_l6}\n\n"
        f"Hasil dalam persen: {persen}%\n"
    )
    messagebox.showinfo("Hasil", hasil)

def proses_perhitungan(nilai_dict, nilai_pilihan):
    total, nilai_dipilih = jumlahkan_nilai(nilai_dict, nilai_pilihan)
    hasil_bagi = bagi_nilai_dengan_total(nilai_dipilih, total)
    total_kalikan, hasil_kalikan = kalikan_dan_jumlahkan(nilai_dipilih, hasil_bagi)
    hasil_akhir = kalikan_dan_bagi(nilai_dipilih, hasil_bagi, total_kalikan)
    total_l6, hasil_l6 = langkah_6(nilai_dipilih, hasil_akhir)
    persen = konversi_ke_persen(total_l6)
    tampilkan_hasil(nilai_dipilih, total, hasil_bagi, total_kalikan, hasil_akhir, total_l6, persen)

def main():
    root = tk.Tk()
    root.title("Perhitungan Nilai")

    nilai_dict = tk.StringVar(value="KG1_Kerusakan_Mesin_DOHC")

    nilai_dicts = {
        "KG1_Kerusakan_Mesin_DOHC": KG1_Kerusakan_Mesin_DOHC,
        "KG2_Kerusakan_Sistem_Mesin_Performa_Lemah": KG2_Kerusakan_Sistem_Mesin_Performa_Lemah,
        "KG3_Kerusakan_Mesin_Gampang_Mogok": KG3_Kerusakan_Mesin_Gampang_Mogok
    }

    def update_nilai_options(*args):
        kategori = nilai_dict.get()
        nilai_combo['values'] = list(nilai_dicts[kategori].keys())

    kategori_frame = ttk.Frame(root, padding="10")
    kategori_frame.grid(row=0, column=0, sticky="W")

    ttk.Label(kategori_frame, text="Pilih kategori:").grid(row=0, column=0, sticky="W")
    kategori_combo = ttk.Combobox(kategori_frame, textvariable=nilai_dict)
    kategori_combo['values'] = ('KG1_Kerusakan_Mesin_DOHC', 'KG2_Kerusakan_Sistem_Mesin_Performa_Lemah', 'KG3_Kerusakan_Mesin_Gampang_Mogok')
    kategori_combo.grid(row=0, column=1, sticky="W")
    kategori_combo.bind("<<ComboboxSelected>>", update_nilai_options)

    nilai_frame = ttk.Frame(root, padding="10")
    nilai_frame.grid(row=1, column=0, sticky="W")

    ttk.Label(nilai_frame, text="Pilih nilai yang dipilih:").grid(row=0, column=0, sticky="W")
    nilai_combo = ttk.Combobox(nilai_frame)
    nilai_combo.grid(row=0, column=1, sticky="W")

    def tambah_nilai():
        nilai = nilai_combo.get()
        if nilai and nilai not in listbox.get(0, tk.END):
            listbox.insert(tk.END, nilai)

    tambah_button = ttk.Button(nilai_frame, text="Tambah", command=tambah_nilai)
    tambah_button.grid(row=0, column=2, sticky="W")

    listbox_frame = ttk.Frame(root, padding="10")
    listbox_frame.grid(row=2, column=0, sticky="W")

    listbox = tk.Listbox(listbox_frame, selectmode=tk.MULTIPLE, width=50, height=10)
    listbox.grid(row=0, column=0, sticky="W")

    def reset():
        listbox.delete(0, tk.END)

    reset_button = ttk.Button(listbox_frame, text="Reset", command=reset)
    reset_button.grid(row=1, column=0, sticky="W")

    button_frame = ttk.Frame(root, padding="10")
    button_frame.grid(row=3, column=0, sticky="W")

    def hitung():
        kategori = nilai_dict.get()
        nilai_pilihan = listbox.get(0, tk.END)
        proses_perhitungan(nilai_dicts[kategori], nilai_pilihan)

    hitung_button = ttk.Button(button_frame, text="Hitung", command=hitung)
    hitung_button.grid(row=0, column=0, sticky="W")

    root.mainloop()

if __name__ == "__main__":
    main()
