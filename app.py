import streamlit as st
import time
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Kenangan Angkatan 6", page_icon="🎓", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    h1 { color: #00d4ff; text-align: center; }
    .stButton>button { 
        width: 100%; 
        border-radius: 25px; 
        background-image: linear-gradient(to right, #1f77b4, #00d4ff); 
        color: white; 
        height: 3em; 
        font-weight: bold;
        border: none;
    }
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
    st.divider()

    st.subheader("🎵 Putar musik perpisahan ini...")
    # Menggunakan link MP3 direct agar musik bisa langsung diputar
    audio_url = "https://soundhelix.com" 
    st.audio(audio_url, format="audio/mp3")
    st.info("Setelah musik berputar, scroll pelan-pelan ke bawah...")
    
    st.divider()

    st.subheader("📸 Menghidupkan Kenangan...")
    
    gambar_list = [
        {"file": "sahabat.jpg", "caption": "Solidaritas Angkatan 6"},
        {"file": "safari.jpg", "caption": "The Grand Taman Safari"},
        {"file": "jatimpark.jpg", "caption": "Keceriaan Jatim Park 1"},
        {"file": "museum.jpg", "caption": "Interactive Living Museum"}
    ]

    col1, col2 = st.columns(2)
    
    for i, item in enumerate(gambar_list):
        target_col = col1 if i % 2 == 0 else col2
        with target_col:
            if os.path.exists(item["file"]):
                st.image(item["file"], caption=item["caption"], use_container_width=True)
            else:
                st.warning(f"🔍 File {item['file']} tidak terbaca.")

    st.divider()

    if st.button("✨ Klik untuk Membaca Pesan Terakhir"):
        konten = [
            "**Assalamualaikum Warahmatullahi Wabarakatuh.**\n\nKepada Bapak dan Ibu guru yang kami muliakan, serta teman-teman seperjuangan Angkatan 6 yang luar biasa.",
            "Rasanya baru kemarin kita berdiri di lapangan ini dengan seragam yang masih kaku. Takdir mempertemukan kita di sini sebagai keluarga.",
            "Di sekolah ini, kita belajar arti solidaritas dan tawa. Foto-foto di atas adalah saksi bisu perjalanan kita.",
            "Kami sadar langkah kami tak selalu lurus. Izinkan kami memohon maaf yang sedalam-dalamnya atas segala khilaf.",
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
