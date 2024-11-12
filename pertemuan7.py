import tkinter as tk  # Impor modul tkinter dengan alias "tk" agar lebih singkat saat menulis kode
from tkinter import messagebox  # Mengimpor messagebox untuk menampilkan pesan pop-up

def show_prediction():  # Fungsi ini akan dipanggil saat tombol "Hasil Prediksi" diklik
    for entry in entries:  # Mengecek setiap kolom input (entry) dalam daftar entries
        if not entry.get():  # Jika kolom input kosong
            messagebox.showerror("Error", "Semua nilai mata pelajaran harus diisi.")  # Tampilkan pesan error
            return  # Hentikan fungsi jika ada kolom yang kosong

    result_text = "Prediksi Prodi: Teknologi Informasi"  # Set hasil prediksi ke "Teknologi Informasi"
    result_label.config(text=result_text)  # Tampilkan hasil prediksi pada label result_label
    messagebox.showinfo("Hasil Prediksi", result_text)  # Menampilkan hasil prediksi dalam kotak pesan informasi

root = tk.Tk()  # Membuat jendela utama aplikasi
root.title("Aplikasi Prediksi Prodi Pilihan")  # Memberi judul pada jendela utama
root.geometry("400x400")  # Menentukan ukuran jendela utama 400x400 piksel
root.configure(bg="light blue")  # Mengatur warna background jendela utama menjadi biru muda

title_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 14, "bold"), bg="light blue")  
# Membuat label untuk judul aplikasi dengan font Arial ukuran 14 dan tebal (bold) dengan latar belakang biru muda
title_label.pack(pady=10)  # Menampilkan label judul dan memberi jarak vertikal 10 piksel

input_frame = tk.Frame(root, bg="light blue")  # Membuat frame sebagai wadah untuk kolom-kolom input dengan latar belakang biru muda
input_frame.pack(pady=10)  # Menempatkan frame di jendela utama dengan jarak vertikal 10 piksel

subject_labels = ["Nilai Mata Pelajaran " + str(i+1) for i in range(10)]  # Membuat daftar nama-nama label mata pelajaran
entries = []  # Membuat daftar kosong untuk menyimpan kolom input (Entry) setiap nilai mata pelajaran

for i, subject in enumerate(subject_labels):  # Loop untuk membuat label dan kolom input setiap mata pelajaran
    label = tk.Label(input_frame, text=subject, bg="light blue")  # Membuat label untuk setiap mata pelajaran dengan latar belakang biru muda
    label.grid(row=i, column=0, padx=5, pady=5, sticky="w")  # Menempatkan label di grid, kolom 0, dengan sedikit jarak
    entry = tk.Entry(input_frame)  # Membuat kolom input (Entry) untuk nilai mata pelajaran
    entry.grid(row=i, column=1, padx=5, pady=5)  # Menempatkan kolom input di grid, kolom 1, dengan sedikit jarak
    entries.append(entry)  # Menambahkan kolom input ke daftar entries

predict_button = tk.Button(root, text="Hasil Prediksi", command=show_prediction)  
# Membuat tombol "Hasil Prediksi" yang menjalankan fungsi show_prediction saat diklik
predict_button.pack(pady=10)  # Menambahkan tombol ke jendela utama dengan jarak vertikal 10 piksel

result_label = tk.Label(root, text="", font=("Arial", 12, "italic"), bg="light blue")  
# Membuat label kosong untuk menampilkan hasil prediksi, dengan font italic dan background biru muda
result_label.pack(pady=20)  # Menampilkan label hasil prediksi di jendela utama dengan jarak vertikal 20 piksel

root.mainloop()  # Memulai loop utama untuk menjalankan aplikasi GUI
