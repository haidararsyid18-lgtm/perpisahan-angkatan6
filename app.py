import streamlit as st
import time

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Kenangan Angkatan 6", page_icon="🎓", layout="centered")

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
    st.divider()

    st.subheader("🎵 Putar musik perpisahan...")
    # Link lagu piano sedih yang stabil
    audio_url = "https://soundhelix.com"
    st.audio(audio_url, format="audio/mp3")
    
    st.divider()

    st.subheader("📸 Menghidupkan Kenangan...")
    
    # MENGGUNAKAN RAW URL GITHUB (Ganti username jika perlu)
    base_url = "https://githubusercontent.com"
    
    gambar_list = [
        {"url": base_url + "sahabat.jpg", "caption": "Solidaritas Angkatan 6"},
        {"url": base_url + "safari.jpg", "caption": "The Grand Taman Safari"},
        {"url": base_url + "jatimpark.jpg", "caption": "Keceriaan Jatim Park 1"},
        {"url": base_url + "museum.jpg", "caption": "Interactive Living Museum"}
    ]

    col1, col2 = st.columns(2)
    
    for i, item in enumerate(gambar_list):
        target_col = col1 if i % 2 == 0 else col2
        with target_col:
            # Gunakan try-except agar jika 1 gambar error, aplikasi TIDAK MATI
            try:
                st.image(item["url"], caption=item["caption"], use_container_width=True)
            except:
                st.warning(f"⚠️ Gambar '{item['caption']}' gagal dimuat. Coba cek file di GitHub.")

    st.divider()

    if st.button("✨ Klik untuk Membaca Pesan Terakhir"):
        konten = [
            "**Assalamualaikum Warahmatullahi Wabarakatuh.**",
            "Rasanya baru kemarin kita berdiri di lapangan ini dengan seragam yang masih kaku. Takdir mempertemukan kita sebagai keluarga.",
            "Izinkan kami memohon maaf yang sedalam-dalamnya atas segala khilaf.",
            "Terima kasih untuk segalanya. Kami, Angkatan 6, pamit undur diri untuk terbang lebih tinggi.\n\n**Wassalamualaikum Warahmatullahi Wabarakatuh.**"
        ]

        for paragraf in konten:
            ketik_pelan_st(paragraf)
            time.sleep(0.5)

        st.balloons()
        st.success("✨ Angkatan 6 - Selamanya Keluarga ✨")

if __name__ == "__main__":
    main()

