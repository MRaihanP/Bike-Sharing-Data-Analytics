# Dashboard Analisis Data: Bike Sharing

## Deskripsi
Dashboard ini adalah aplikasi analisis data untuk penyewaan sepeda, yang menyajikan analisis data interaktif menggunakan **Streamlit**. Dashboard ini menyajikan berbagai visualisasi dan analisis yang membantu dalam memahami pola penyewaan sepeda berdasarkan faktor-faktor seperti cuaca, musim, dan jenis hari.

## Struktur Direktori
Berikut adalah struktur direktori proyek:
submission/
├───dashboard/
│   ├───main_data.csv        # Data bersih yang digunakan untuk dashboard
│   └───dashboard.py          # Skrip untuk menjalankan dashboard
├───data/
│   └───day.csv              # Dataset mentah
├───notebook.ipynb  # Jupyter Notebook untuk analisis
├───README.md                # Penjelasan cara menggunakan dashboard
└───requirements.txt         # Daftar pustaka yang dibutuhkan


## Setup Environment - Shell/Terminal

1. **Buka terminal**.

2. **Navigasikan ke direktori proyek:**
    ```bash
    cd \go\to\files\path
    ```
    Ubah \go\to\files\path menjadi path penyimpanan file submission

3. **Buat lingkungan virtual menggunakan venv:**
    ```bash
    python -m venv bike-sharing-analytics
    ```

4. **Aktifkan lingkungan virtual:**
   - **Di Windows**:
     ```bash
     bike-sharing-analytics\Scripts\activate
     ```
   - **Di Mac/Linux**:
     ```bash
     source bike-sharing-analytics/bin/activate
     ```

5. **Instal semua dependensi dari `requirements.txt`:**
    ```bash
    pip install -r requirements.txt
    ```

## Menjalankan Aplikasi Streamlit

Untuk menjalankan aplikasi **Streamlit**, gunakan perintah berikut di terminal:

```bash
streamlit run dashboard/dashboard.py
```

## Catatan
- Pastikan Anda telah menginstal Python (versi 3.6 atau lebih baru)
- Aplikasi ini dirancang dan diuji menggunakan Python versi 3.11.5.
