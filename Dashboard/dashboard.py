import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
url = "https://drive.google.com/uc?export=download&id=1HZEZbPwCWqI2bAo3U0y7SacHdrED51sw"
day_data = pd.read_csv(url)

# Membuat dataframe baru untuk menyimpan total pengguna casual dan registered
users_type = day_data[['casual', 'registered']].sum()

# Mengatur parameter visualisasi
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Visualisasi diagram batang
users_type.plot(kind='bar', ax=axes[0], color=['skyblue', 'salmon'], rot=0)
axes[0].set_title('Perbandingan Jumlah Pengguna Sepeda Casual dan Registered')
axes[0].set_xlabel('Tipe Pengguna')
axes[0].set_ylabel('Jumlah Pengguna (x 1.000.000)')
axes[0].legend(title='')

# Visualisasi diagram lingkaran
users_type.plot(kind='pie', autopct='%1.1f%%', ax=axes[1], colors=['skyblue', 'salmon'])
axes[1].set_title('Proporsi Pengguna Sepeda Casual dan Registered')

# Menampilkan visualisasi
plt.tight_layout()

# Membuat dashboard streamlit
st.title("Analisis Penggunaan Sepeda")
st.write("Total Pengguna Casual dan Registered")
st.pyplot(fig)

# Membuat dropdown untuk memilih tahun
tahun = day_data['year'].unique()
tahun_selected = st.selectbox("Pilih Tahun", tahun)

# Membuat plot total pengguna per bulan
users_by_month = day_data.groupby(by=["year", "month"]).agg({
    "casual": "sum",
    "registered": "sum",
    "count": "sum",  
}).reset_index()

data_year = users_by_month[users_by_month['year'] == tahun_selected]
plt.figure(figsize=(12, 6))
plt.plot(data_year['month'], data_year['count'])
plt.xlabel("Bulan")
plt.ylabel("Jumlah Pengguna Registered")
plt.title("Total Pengguna Registered Sepeda per Bulan")
plt.xticks(range(1, 13), ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
plt.grid(True)
st.pyplot(plt.gcf())

# Membuat plot penggunaan bike-sharing berdasarkan musim
season_order = ["Spring", "Summer", "Fall", "Winter"]
users_by_season = day_data.groupby(by="season").agg({
    "casual": "sum",
    "registered": "sum",
    "count": "sum",
})
print(users_by_season)  # Periksa data untuk memastikan bahwa data untuk musim tersedia
plt.figure(figsize=(10, 6))
sns.barplot(x=users_by_season.index, y="count", data=users_by_season, order=season_order, palette="autumn")
plt.title("Penggunaan Bike-sharing berdasarkan Musim")
plt.xlabel("Season")
plt.ylabel("Total Pengguna (x1.000.0000)")
plt.xticks(rotation=45)
st.pyplot(plt.gcf())