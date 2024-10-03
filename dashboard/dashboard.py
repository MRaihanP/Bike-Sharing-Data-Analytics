import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates 

# Membaca data dari main_data.csv
df = pd.read_csv('dashboard/main_data.csv')

# Judul Dashboard
st.markdown("<h1 style='text-align: center;'>Dashboard Analisis Data: Bike Sharing</h1>", unsafe_allow_html=True)

# Identitas pembuat
st.markdown("**Nama**          : Muhammad Raihan Pradipta  \n"
            "**Email**         : mraihanpradipta@gmail.com  \n"
            "**ID Dicoding**   : raihanp  ")

# Menampilkan data
st.subheader('Data Penyewaan Sepeda')
st.write(df)

# Visualisasi Pengaruh Cuaca terhadap Penyewaan
weather_labels = {1: 'Clear/Cloudy', 2: 'Mist/Cloudy', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Ice'}
df['weathersit_label'] = df['weathersit'].map(weather_labels)

st.subheader('Pengaruh Cuaca terhadap Jumlah Penyewaan')
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='weathersit_label', y='cnt', data=df, ax=ax)
ax.set_title('Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda', fontsize=14)
ax.set_xlabel('Kondisi Cuaca', fontsize=12)
ax.set_ylabel('Jumlah Penyewaan Sepeda (cnt)', fontsize=12)
st.pyplot(fig)
st.markdown('**Kesimpulan: Cuaca memengaruhi jumlah penyewaan sepeda, terutama cuaca buruk yang mengurangi jumlah sewa.**')

# Visualisasi Tren Penyewaan berdasarkan Musim
season_labels = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
df['season_label'] = df['season'].map(season_labels)

st.subheader('Tren Penyewaan Sepeda Berdasarkan Musim')

# Membuat grafik terpisah untuk setiap musim
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
colors = {'Spring': 'green', 'Summer': 'orange', 'Fall': 'red', 'Winter': 'blue'}

for season in seasons:
    fig, ax = plt.subplots(figsize=(12, 6))
    season_data = df[df['season_label'] == season]
    
    season_data['dteday'] = pd.to_datetime(season_data['dteday'])
    
    sns.lineplot(data=season_data, x='dteday', y='cnt', color=colors[season], ax=ax)
    ax.set_title(f'Tren Penyewaan Sepeda di Musim {season}', fontsize=14)
    ax.set_xlabel('Tanggal', fontsize=12)
    ax.set_ylabel('Jumlah Penyewaan Sepeda (cnt)', fontsize=12)

    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

# Membuat grafik yang menggabungkan setiap musim
fig, ax = plt.subplots(figsize=(12, 6))
for season in seasons:
    season_data = df[df['season_label'] == season]
    season_data['dteday'] = pd.to_datetime(season_data['dteday'])
    sns.lineplot(data=season_data, x='dteday', y='cnt', label=season, color=colors[season], ax=ax)

ax.set_title('Tren Penyewaan Sepeda Seluruh Musim', fontsize=14)
ax.set_xlabel('Tanggal', fontsize=12)
ax.set_ylabel('Jumlah Penyewaan Sepeda (cnt)', fontsize=12)

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

plt.xticks(rotation=45)
plt.legend(title='Musim') 
plt.tight_layout()
st.pyplot(fig)
st.markdown('**Kesimpulan: Penyewaan sepeda meningkat selama musim panas dan puncaknya pada musim gugur, sementara jumlah penyewaan menurun selama musim dingin.**')\

# Clustering pengguna berdasarkan musim dan hari kerja
df['cluster'] = np.where((df['season'] == 3) & (df['workingday'] == 1), 'High-Demand-Workday', 'Other')

# Menampilkan subjudul untuk Clustering
st.subheader('Clustering Pengguna Berdasarkan Musim dan Hari Kerja')

# Menghitung jumlah hari untuk setiap kategori
high_demand_counts = df[ df['cluster'] == 'High-Demand-Workday'].groupby('season')['cluster'].count()
total_users_per_season = df.groupby('season')['cluster'].count()

# Membuat DataFrame untuk menampilkan hasil
summary = pd.DataFrame({
    'Musim': ['Spring', 'Summer', 'Fall', 'Winter'],
    'Holiday': [
        df[(df['season'] == 1) & (df['holiday'] == 1)].shape[0],
        df[(df['season'] == 2) & (df['holiday'] == 1)].shape[0],
        df[(df['season'] == 3) & (df['holiday'] == 1)].shape[0],
        df[(df['season'] == 4) & (df['holiday'] == 1)].shape[0]
    ],
    'Workingday': [
        df[(df['season'] == 1) & (df['workingday'] == 1)].shape[0],
        df[(df['season'] == 2) & (df['workingday'] == 1)].shape[0],
        df[(df['season'] == 3) & (df['workingday'] == 1)].shape[0],
        df[(df['season'] == 4) & (df['workingday'] == 1)].shape[0]
    ]
})

# Menampilkan tabel tanpa indeks di Streamlit
st.write("Jumlah Hari Berdasarkan Musim, Hari Kerja, dan Hari Libur:")
st.table(summary.reset_index(drop=True))  # Tampilkan tabel tanpa indeks

# Menghitung dan menampilkan hasil kesimpulan
high_demand_count = high_demand_counts.sum()  # Total pengguna pada 'High-Demand-Workday'
total_count = total_users_per_season.sum()    # Total pengguna di semua musim
percentage = (high_demand_count / total_count) * 100 if total_count > 0 else 0  # Menghindari pembagian dengan nol

# Melting DataFrame untuk mempermudah plotting
summary_melted = summary.melt(id_vars='Musim', value_vars=['Holiday', 'Workingday'],
                               var_name='Tipe Hari', value_name='Jumlah Hari')

# Menggambar bar plot
plt.figure(figsize=(12, 6))
sns.barplot(data=summary_melted, x='Musim', y='Jumlah Hari', hue='Tipe Hari', palette='Set2')

# Menambahkan judul dan label
plt.title('Jumlah Hari Berdasarkan Musim dan Tipe Hari')
plt.xlabel('Musim')
plt.ylabel('Jumlah Hari')
plt.legend(title='Tipe Hari')
plt.xticks(rotation=45)
plt.tight_layout()

# Menampilkan grafik di Streamlit
st.pyplot(plt)

# Menampilkan kesimpulan
st.markdown(f'**Kesimpulan: Pengguna pada hari kerja di musim gugur memiliki permintaan tinggi, '
            f'mencapai {high_demand_count} pengguna ({percentage:.2f}%).**')