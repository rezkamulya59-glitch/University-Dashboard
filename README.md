# 🎓 Dashboard Analitik Universitas

> Dashboard interaktif untuk analisis dan monitoring data mahasiswa 

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📊 Sumber Data

Dashboard ini menggunakan tiga dataset utama:

### 1. **students.csv**
Dataset mahasiswa yang berisi informasi:
- `student_id`: ID unik mahasiswa
- `name`: Nama lengkap mahasiswa
- `faculty`: Nama fakultas
- `major`: Program studi
- `year_enrolled`: Tahun masuk/pendaftaran
- `gender`: Jenis kelamin (Male/Female)
- `age`: Usia mahasiswa
- `gpa`: Indeks Prestasi Kumulatif (0.00-4.00)
- `status`: Status mahasiswa (Active/Graduated/Inactive)

### 2. **academic_performance.csv**
Dataset performa akademik mahasiswa per semester

### 3. **faculty.csv**
Dataset informasi detail fakultas dan program studi

> **Catatan**: Data yang digunakan adalah data dummy/sampel untuk keperluan demonstrasi dashboard

---

## 🌐 Akses Dashboard

Dashboard dapat diakses secara online melalui:
🔗 hhttps://university-dashboard-rezka.streamlit.app/

---

## 📝 Deskripsi Dashboard
Dashboard Analitik Universitas adalah aplikasi visualisasi data berbasis web yang dirancang untuk membantu administrator universitas, dosen, dan stakeholder dalam memantau dan menganalisis data mahasiswa secara real-time. Dashboard ini menyediakan berbagai visualisasi interaktif untuk memahami distribusi mahasiswa, performa akademik, dan tren penerimaan mahasiswa.

- 📊 **Memantau data mahasiswa** secara real-time
- 📈 **Menganalisis tren penerimaan** mahasiswa dari tahun ke tahun
- 🎯 **Melihat distribusi mahasiswa** per fakultas dan program studi
- 💯 **Mengevaluasi performa akademik** melalui IPK rata-rata
- 👥 **Memahami demografi mahasiswa** berdasarkan gender dan usia
- 📉 **Mengidentifikasi pola** dalam status keaktifan mahasiswa

---

### 🎯 Tujuan Dashboard

1. **Memudahkan Pengambilan Keputusan** - Menyajikan data dalam format visual yang mudah dipahami
2. **Meningkatkan Efisiensi** - Mengurangi waktu analisis data manual
3. **Monitoring Real-time** - Memantau KPI (Key Performance Indicators) secara langsung
4. **Data-Driven Insights** - Memberikan insight berbasis data untuk strategi akademik

---

## ✨ Fitur Utama Dashboard

### 🔍 **1. Filter Interaktif**
Dashboard dilengkapi dengan sidebar filter yang memungkinkan pengguna untuk:
- **Filter Tahun**: Pilih rentang tahun pendaftaran mahasiswa (slider)
- **Filter Fakultas**: Pilih satu atau beberapa fakultas (multi-select)
- **Filter Gender**: Filter berdasarkan jenis kelamin (dropdown)

Filter ini bekerja secara **real-time** dan langsung memperbarui seluruh visualisasi.

### 📊 **2. KPI Metrics Cards**
Empat metrik utama yang ditampilkan di bagian atas dashboard:
- **Total Mahasiswa** - Jumlah total mahasiswa sesuai filter
- **IPK Rata-rata** - Nilai rata-rata IPK dengan indikator perubahan
- **Jumlah Fakultas** - Total fakultas yang tersedia
- **Mahasiswa Aktif** - Jumlah mahasiswa dengan status aktif

Setiap metric dilengkapi dengan **delta indicator** (↑↓) untuk menunjukkan perubahan.

### 📈 **3. Visualisasi Data Interaktif**
Enam visualisasi utama yang dapat berinteraksi dengan filter:

#### a. **Distribusi Mahasiswa per Fakultas** (Bar Chart)
- Menampilkan jumlah mahasiswa di setiap fakultas
- Tooltip interaktif saat hover
- Warna biru konsisten untuk branding

#### b. **Tren Jumlah Mahasiswa per Tahun** (Line Chart)
- Menunjukkan pola penerimaan mahasiswa dari tahun ke tahun
- Membantu identifikasi tren naik/turun
- Ideal untuk perencanaan kapasitas

#### c. **Status Mahasiswa** (Pie Chart)
- Distribusi status: Active, Graduated, Inactive
- Persentase dan jumlah absolut
- Warna-warna soft & modern

#### d. **IPK Rata-rata per Fakultas** (Horizontal Bar Chart)
- Perbandingan performa akademik antar fakultas
- Menampilkan IPK dan jumlah mahasiswa
- Sorted dari tertinggi ke terendah

#### e. **Distribusi Gender** (Pie Chart)
- Proporsi mahasiswa berdasarkan gender
- Membantu analisis keseimbangan gender

#### f. **Top 5 Program Studi** (Bar Chart)
- Menampilkan 5 program studi dengan mahasiswa terbanyak
- Membantu identifikasi program studi populer

### 📋 **4. Tabel Data Mahasiswa**
- Tabel interaktif dengan **scrolling vertikal**
- Menampilkan semua kolom data mahasiswa
- **Height fixed** (500px) untuk UX yang lebih baik
- Search dan sort capability

### 📥 **5. Export Data**
- **Download button** untuk export data ke CSV
- File otomatis diberi nama dengan timestamp
- Format: `data_mahasiswa_YYYYMMDD_HHMMSS.csv`

### 📊 **6. Statistik Ringkasan**
Tabel statistik yang menampilkan:
- Jumlah Total Mahasiswa
- IPK Rata-rata
- IPK Tertinggi
- IPK Terendah
- Rata-rata Umur Mahasiswa

---

## 📈 Visualisasi Data

Dashboard ini menggunakan kombinasi library visualisasi untuk hasil optimal:

### 🎨 **Library yang Digunakan**

| Library | Fungsi | Visualisasi |
|---------|--------|-------------|
| **Plotly** | Interactive charts | Bar Chart (Fakultas & Prodi) |
| **Streamlit** | Built-in charts | Line Chart (Tren Tahunan) |
| **Matplotlib** | Static charts | Pie Chart (Status & Gender), Horizontal Bar (IPK) |

### 📊 **Jenis Visualisasi**

#### 1. **Bar Chart** - Perbandingan Kategori
- Distribusi Mahasiswa per Fakultas
- Top 5 Program Studi
- **Cocok untuk**: Membandingkan nilai antar kategori

#### 2. **Line Chart** - Tren Waktu
- Tren Jumlah Mahasiswa per Tahun
- **Cocok untuk**: Melihat perubahan dari waktu ke waktu

#### 3. **Pie Chart** - Proporsi
- Status Mahasiswa
- Distribusi Gender
- **Cocok untuk**: Menunjukkan bagian dari keseluruhan

#### 4. **Horizontal Bar Chart** - Ranking
- IPK Rata-rata per Fakultas
- **Cocok untuk**: Membandingkan dan ranking nilai
---

## 📸 Tampilan Dashboard

### 1. **KPI Metrics Cards**
Empat metrik utama di bagian atas dashboard dengan delta indicators.
<p align="center">
  <img src="https://raw.githubusercontent.com/rezkamulya59-glitch/Dashboard-Universitas/main/ringkasan-data.png" 
       alt="KPI Metrics" 
       width="800"
       style="border: 2px solid #ddd; border-radius: 8px; padding: 10px;"/>
</p>

### 2. **Visualisasi Data - Distribusi & Tren**
Dua visualisasi side-by-side: distribusi per fakultas dan tren tahunan.
<p align="center">
  <img src="https://github.com/rezkamulya59-glitch/Dashboard-Universitas/blob/main/distribusi-dan-tren-mhs.png"
       alt="distribusi dan tren" 
       width="800"
       style="border: 2px solid #ddd; border-radius: 8px; padding: 10px;"/>
</p>


### 3. **Visualisasi Data - Status Mahasiswa**
Pie chart interaktif menampilkan proporsi status mahasiswa (Active/Graduated/Inactive).
<p align="center">
  <img src="https://github.com/rezkamulya59-glitch/Dashboard-Universitas/blob/main/status-mhs.png"
       alt="status mahasiswa" 
       width="800"
       style="border: 2px solid #ddd; border-radius: 8px; padding: 10px;"/>
</p>

### 4. **Visualisasi Data - IPK per Fakultas**
Horizontal bar chart membandingkan IPK rata-rata antar fakultas dengan jumlah mahasiswa.
<p align="center">
  <img src="https://github.com/rezkamulya59-glitch/Dashboard-Universitas/blob/main/jumlah-mhs-perprodi.png"
       alt="distribusi dan tren" 
       width="800"
       style="border: 2px solid #ddd; border-radius: 8px; padding: 10px;"/>
</p>


### 5. **Visualisasi Data - Distribusi Gender**
Pie chart menunjukkan proporsi mahasiswa laki-laki dan perempuan.
<p align="center">
  <img src="https://github.com/rezkamulya59-glitch/Dashboard-Universitas/blob/main/gender-mhs.png"
       alt="gender" 
       width="800"
       style="border: 2px solid #ddd; border-radius: 8px; padding: 10px;"/>
</p>

### 6. **Tabel Data Mahasiswa**
Tabel interaktif dengan scrolling vertikal dan semua informasi mahasiswa.
<p align="center">
  <img src="https://github.com/rezkamulya59-glitch/Dashboard-Universitas/blob/main/data-mhs.png"
       alt="data mhs" 
       width="800"
       style="border: 2px solid #ddd; border-radius: 8px; padding: 10px;"/>
</p>

### 7. **Statistik & Top Program Studi**
Statistik ringkasan dan bar chart top 5 program studi terpopuler.
<p align="center">
  <img src="https://github.com/rezkamulya59-glitch/Dashboard-Universitas/blob/main/ringkasan-topProdi.png"
       alt="top prodi" 
       width="800"
       style="border: 2px solid #ddd; border-radius: 8px; padding: 10px;"/>
</p>

### 8. **Filter Sidebar**
Sidebar dengan tiga filter utama: Tahun, Fakultas, dan Gender.
<p align="center">
  <img src="https://github.com/rezkamulya59-glitch/Dashboard-Universitas/blob/main/filter-data.png"
       alt="filter data" 
       width="800"
       style="border: 2px solid #ddd; border-radius: 8px; padding: 10px;"/>
</p>

---

## 🛠️ Teknologi yang Digunakan

```python
streamlit==1.28.0      # Web framework
pandas==2.0.3          # Data manipulation
numpy==1.24.3          # Numerical computing
matplotlib==3.7.2      # Static visualization
plotly==5.17.0         # Interactive visualization
```
