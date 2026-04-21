import streamlit as st
import time
from PIL import Image

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Kenangan Angkatan 6", page_icon="🎓", layout="centered")

# CSS untuk tampilan gelap yang estetik
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    h1 { color: #00d4ff; text-align: center; }
    .stButton>button { width: 100%; border-radius: 25px; background-color: #1f77b4; color: white; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

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

    # --- GALERI FOTO ---
    st.subheader("📸 Galeri Perjalanan Kita")
    col1, col2 = st.columns(2)
    
    with col1:
        try:
            st.image("sahabat.jpg", caption="Solidaritas Angkatan 6", use_container_width=True)
        except: st.warning("sahabat.jpg tidak ditemukan")
        try:
            st.image("safari.jpg", caption="The Grand Taman Safari", use_container_width=True)
        except: st.warning("safari.jpg tidak ditemukan")

    with col2:
        try:
            st.image("jatimpark.jpg", caption="Keceriaan Jatim Park 1", use_container_width=True)
        except: st.warning("jatimpark.jpg tidak ditemukan")
        try:
            st.image("museum.jpg", caption="Interactive Living Museum", use_container_width=True)
        except: st.warning("museum.jpg tidak ditemukan")

    st.divider()

    # --- PESAN PERPISAHAN ---
    if st.button("✨ Klik untuk Membaca Pesan Terakhir"):
        st.snow()
        # Audio Player (Lagu Galau Instrumen)
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
