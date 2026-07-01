
# 🎮 VTuber Lite: Real-time 2D Avatar Controller

**Sistem Facial Emotion Recognition Realtime Untuk Mengendalikan Avatar 2D Berbasis Emosi Wajah**

VTuber Lite adalah sistem interaktif berbasis *Artificial Intelligence* yang memungkinkan siapa saja mengendalikan Avatar 2D secara *real-time* hanya menggunakan *webcam* laptop standar. Sistem ini dirancang sangat ringan, efisien, dan dapat berjalan lancar di CPU biasa tanpa memerlukan GPU kelas atas atau perangkat *motion capture* yang mahal.

## ✨ Fitur Utama
- **Zero-Training AI:** Mengeliminasi sepenuhnya kebutuhan dataset gambar eksternal. Program langsung siap pakai.
- **Presisi Spasial 3D:** Melacak 468 titik wajah dan gestur tangan secara akurat menggunakan teknologi Google MediaPipe.
- **Ultra-Ringan & Privat:** Pemrosesan 100% berjalan secara lokal (offline) di komputer Anda, tanpa merekam atau mengirim data video ke *server*.

## 📸 Demo
*(Catatan: Hapus teks ini dan masukkan gambar screenshot programmu atau file GIF saat kamu mencoba avatarnya di sini agar orang lain bisa melihat bentuknya)*

## 🚀 Cara Instalasi

### Prasyarat
Pastikan Anda sudah menginstal **Python (Disarankan versi 3.11.x)**. 
> **⚠️ PENTING:** Saat proses instalasi Python, pastikan Anda mencentang kotak **"Add Python to PATH"** (atau "Add Python.exe to PATH") di bagian paling bawah agar perintah terminal dapat berjalan!

### Langkah-langkah
1. **Download Repository ini**
   Anda bisa mengunduhnya dengan cara klik tombol hijau **"Code"** lalu pilih **"Download ZIP"**, atau gunakan perintah terminal (git clone) berikut:
   ```bash
   git clone [https://github.com/MohammadReyhanAretha/Sistem-Facial-Emotion-Recognition-Realtime-Untuk-Mengendalikan-Avatar-2D-Berbasis-Emosi-Wajah.git](https://github.com/MohammadReyhanAretha/Sistem-Facial-Emotion-Recognition-Realtime-Untuk-Mengendalikan-Avatar-2D-Berbasis-Emosi-Wajah.git)

```

2. **Masuk ke dalam Folder Proyek**
Jika Anda menggunakan `git clone`, Anda harus masuk ke dalam folder utama dan folder `FaceMesh` terlebih dahulu menggunakan perintah ini:
```bash
cd Sistem-Facial-Emotion-Recognition-Realtime-Untuk-Mengendalikan-Avatar-2D-Berbasis-Emosi-Wajah/FaceMesh

```


*(Jika Anda mendownload via ZIP, cukup ekstrak foldernya, lalu klik kanan di area kosong di dalam folder `FaceMesh` dan pilih "Open in Terminal").*
3. **Install *Library* yang Dibutuhkan**
Setelah terminal berada di dalam folder FaceMesh, jalankan perintah berikut untuk menginstal seluruh mesin AI yang dibutuhkan:
```bash
pip install -r requirements.txt

```



## 🎮 Cara Menjalankan Program

Setelah seluruh proses instalasi selesai, jalankan perintah ini di dalam terminal:

```bash
python main.py

```

*(Catatan: Jika di laptop Anda terdapat beberapa versi Python yang terinstal, Anda bisa memanggilnya secara spesifik menggunakan perintah `py -3.11 main.py`)*

## 🎭 Panduan Ekspresi & Gestur

Sistem kami menggunakan perpaduan deteksi rasio otot wajah dan gestur tubuh untuk mengatasi limitasi mikro-ekspresi. Berikut adalah cara memicu perubahan emosi pada Avatar Anda:

* 😐 **Neutral (Netral):** Kondisi titik koordinat otot wajah dalam keadaan normal dan rileks.
* 😄 **Happy (Senang):** Tersenyum lebar (sistem membaca rasio pelebaran jarak antara titik ujung bibir kiri dan kanan).
* 😨 **Fear (Takut/Kaget):** Membuka mulut lebar ke bawah / mangap (sistem membaca jarak bukaan antara bibir atas dan bawah).
* 😡 **Angry (Marah):** Angkat salah satu telapak tangan Anda hingga melampaui batas sumbu dahi atau di atas kepala.
* 😭 **Sad (Sedih):** Kepalkan atau dekatkan telapak tangan Anda hingga bersinggungan / menutupi area mata.

## 👥 Tim Pengembang

**KELOMPOK SUDAH BERUSAHA**
S1 Teknik Informatika - Telkom University

* **Ahmad Ruba'i** (103112400074) - *Lead Developer*
* **Mohammad Reyhan Aretha Fatin** (103112400078)
* **Puti Afifah Fairuzzana** (103112400194)
* **Mutiara Fauziah** (103112400197)
* **Eikel Prinst Sukatendel** (103112430232)
* **Adhe Yudho Satrio** (103112400234)
* **Maulana Malik Hidayat** (2211102228)

## 📄 Lisensi

Proyek ini bersifat *Open-Source*. Silakan diunduh, dipelajari, digunakan, dan dikembangkan lebih lanjut!

```

```
