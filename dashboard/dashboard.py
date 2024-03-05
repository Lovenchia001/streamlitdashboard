import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Memuat data
all_data = pd.read_csv("all_data.csv")

# Menampilkan nama kolom untuk memeriksa strukturnya
st.write("Nama kolom dalam dataset:", all_data.columns)

# Memeriksa apakah kolom 'Datetimes' ada
if 'Datetimes' in all_data.columns:
    # Mengonversi kolom 'Date' ke dalam tipe datetime
    all_data['Datetimes'] = pd.to_datetime(all_data['Datetimes'])

# Mengonversi kolom 'Date' ke dalam tipe datetime
all_data['Datetimes'] = pd.to_datetime(all_data['Datetimes'])

# Analisis Data Eksploratif (EDA)
def eda_all_data():
    """
    Melakukan Analisis Data Eksploratif (EDA) pada dataset yang digabungkan (all_data.csv).
    """

    # Menampilkan beberapa baris pertama dataset
    st.subheader("Analisis Data Eksploratif untuk all_data")
    st.write("Beberapa baris pertama dari dataset:")
    st.write(all_data.head())
    
    # Statistik deskriptif
    st.write("Statistik deskriptif dari dataset:")
    st.write(all_data.describe())
    
    # Distribusi Count per Bulan
    st.write("Distribusi peminjaman sepeda per bulan:")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='Month', y='Count', data=all_data, estimator=sum, ci=None, palette='muted', ax=ax)
    ax.set_title('Distribusi Jumlah Peminjaman Sepeda pada Setiap Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Total Jumlah Peminjaman Sepeda')
    st.pyplot(fig)

    # Matriks korelasi
    st.write("Matriks korelasi antara fitur numerik:")
    corr = all_data.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, ax=ax)
    ax.set_title('Matriks Korelasi')
    st.pyplot(fig)

# Dashboard Streamlit
def main():
    """
    Dashboard Streamlit untuk menampilkan hasil EDA.
    """

    st.title("Dashboard Analisis Data Eksploratif")

    # Membuat sidebar untuk navigasi
    st.sidebar.title("Navigasi")

    # Sidebar untuk informasi pengguna
    st.sidebar.subheader("Lovenchia Warouw")
    st.sidebar.write("Bangkit Academy - Machine Learning")

    # Sidebar untuk media sosial
    st.sidebar.subheader("Media Sosial")
    st.sidebar.write("Instagram: [eeeeren_](https://www.instagram.com/eeeeren_/)")
    st.sidebar.write("GitHub: [Lovenchia001](https://github.com/Lovenchia001)")

    # Hapus deklarasi ganda dari selection
    # selection = st.sidebar.radio("Pergi ke:", ["Analisis Data Eksploratif"])

    # Menampilkan EDA untuk all_data
    if st.sidebar.radio("Pergi ke:", ["Analisis Data Eksploratif"]) == "Analisis Data Eksploratif":
        eda_all_data()

if __name__ == "__main__":
    main()
