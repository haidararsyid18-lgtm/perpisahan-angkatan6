import streamlit as st
import time
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Kenangan Angkatan 6", page_icon="🎓", layout="centered")

# CSS untuk tampilan gelap dan animasi sederhana
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    h1 { color: #00d4ff; text-align: center; }
    .stButton>button { width: 100%; border-radius: 25px; background-color: #1f77b4; color: white; height: 3em; }
    /* Animasi fade in untuk gambar */
    .stImage { animation: fadeIn 2s; }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
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

    # --- BAGIAN MUSIK DI ATAS ---
    st.subheader("🎵 Putar musik ini dulu ya...")
    # Link audio lagu galau (Instrumen Piano Sedih)
    st.audio("https://soundhelix.com")
    st.caption("Disarankan: Putar musik di atas sebelum scroll ke bawah.")
    st.divider()

    # --- GALERI FOTO BERTAHAP ---
    st.subheader("📸 Menghidupkan Kenangan...")
    
    gambar_list = [
        {"file": "sahabat.jpg", "caption": "Solidaritas Tanpa Batas"},
        {"file": "safari.jpg", "caption": "Momen di Safari Prigen"},
        {"file": "jatimpark.jpg", "caption": "Tawa di Jatim Park 1"},
        {"file": "museum.jpg", "caption": "Interactive Living Museum"}
    ]

    col1, col2 = st.columns(2)
    
    # Proses pemunculan foto bertahap
    for i, item in enumerate(gambar_list):
        time.sleep(1.5) # Jeda 1.5 detik tiap foto muncul
        target_col = col1 if i % 2 == 0 else col2
        with target_col:
            if os.path.exists(item["file"]):
                try:
                    with open(item["file"], "rb") as f:
                        img_data = f.read()
                    st.image(img_data, caption=item["caption"], use_container_width=True)
                except:
                    st.error(f"⚠️ {item['file']} rusak.")
            else:
                st.warning(f"🔍 Menunggu {item['file']}...")

    st.divider()

    # --- PESAN PERPISAHAN TANPA EFEK SALJU/BALON ---
    if st.button("✨ Baca Pesan Terakhir"):
        # Efek visual dihilangkan sesuai permintaan
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

        st.success("✨ Angkatan 6 - Selamanya Keluarga ✨")
        st.markdown("<h3 style='text-align: center;'>See You on Top! 🚀</h3>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

