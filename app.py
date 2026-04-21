import streamlit as st
import time
from PIL import Image
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Kenangan Angkatan 6", page_icon="🎓", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    h1 { color: #00d4ff; text-align: center; }
    .stButton>button { width: 100%; border-radius: 25px; background-color: #1f77b4; color: white; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

# Fungsi untuk mencari file gambar secara otomatis (cek huruf besar/kecil)
def ambil_gambar(nama_file):
    # Daftar kemungkinan ekstensi
    ekstensi = ['.jpg', '.JPG', '.jpeg', '.png']
    nama_tanpa_ext = os.path.splitext(nama_file)[0]
    
    for ext in ekstensi:
        path = nama_tanpa_ext + ext
        if os.path.exists(path):
            return Image.open(path)
    return None

def ketik_pelan_st(teks, jeda=0.04):
    placeholder = st.empty()
    isi = ""
    for karakter in teks:
        isi += karakter
        placeholder.markdown(f"<div style='font-size:18px; line-height:1.7; text-align: justify;'>{isi}</div>", unsafe_allow_html=True)
        time.sleep(jeda)
    st.markdown("---")

def main():
    st.title("🎓 Jejak Langkah & Air Mata: Pamitnya Angkatan 6")
    st.markdown("<p style='text-align: center;'>Sebuah surat terbuka untuk rumah yang kita bangun bersama.</p>", unsafe_allow_html=True)
    st.divider()

    st.subheader("📸 Galeri Perjalanan Kita")
    col1, col2 = st.columns(2)
    
    # List gambar yang akan ditampilkan
    gambar_list = [
        ("sahabat.jpg", "Solidaritas Angkatan 6"),
        ("safari.jpg", "The Grand Taman Safari"),
        ("jatimpark.jpg", "Keceriaan Jatim Park 1"),
        ("museum.jpg", "Interactive Living Museum")
    ]

    for i, (fname, cap) in enumerate(gambar_list):
        img = ambil_gambar(fname)
        target_col = col1 if i % 2 == 0 else col2
        with target_col:
            if img:
                st.image(img, caption=cap, use_container_width=True)
            else:
                st.error(f"❌ {fname} tidak ditemukan di GitHub")

    st.divider()

    if st.button("✨ Klik untuk Membaca Pesan Terakhir"):
        st.snow()
        st.write("🎵 *Putar musik ini, baca pelan-pelan...*")
        st.audio("https://soundhelix.com")

        konten = [
            "**Assalamualaikum Warahmatullahi Wabarakatuh.**\n\nKepada Bapak dan Ibu guru yang kami muliakan, serta teman-teman seperjuangan Angkatan 6 yang luar biasa.",
            "Rasanya baru kemarin kita berdiri di lapangan ini dengan seragam yang masih kaku. Kita datang membawa mimpi masing-masing, namun takdir mempertemukan kita di sini sebagai keluarga.",
            "Di sekolah ini, kita belajar arti solidaritas saat tugas menumpuk dan tawa saat jam kosong. Foto-foto di atas adalah saksi bisu betapa indahnya perjalanan kita.",
            "Kami sadar langkah kami tak selalu lurus. Izinkan kami, Angkatan 6, memohon maaf yang sedalam-dalamnya atas segala khilaf.",
            "\"Perpisahan hanya untuk mereka yang mencintai dengan mata. Bagi yang mencintai dengan hati, tidak ada yang namanya perpisahan.\"",
            "Terima kasih untuk segalanya. Kami, Angkatan 6, pamit undur diri untuk terbang lebih tinggi.\n\n**Wassalamualaikum Warahmatullahi Wabarakatuh.**"
        ]

        for paragraf in konten:
            ketik_pelan_st(paragraf)
            time.sleep(0.5)

        st.balloons()
        st.success("✨ Angkatan 6 - Selamanya Keluarga ✨")

if __name__ == "__main__":
    main()

