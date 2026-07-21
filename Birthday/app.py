import streamlit as st
import random
import time
import os
import base64

# --- Pelacak Folder Otomatis ---
DIR_SAAT_INI = os.path.dirname(os.path.abspath(__file__))
FILE_LAGU = os.path.join(DIR_SAAT_INI, "lagu.mp3")
FILE_LEVELUP = os.path.join(DIR_SAAT_INI, "levelup.mp3")
FILE_FOTO = os.path.join(DIR_SAAT_INI, "foto.jpg")

# Mengatur konfigurasi halaman
st.set_page_config(page_title="Surat Spesial", page_icon="💌")

# Memasukkan CSS Retro Hardcore
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&display=swap');

html, body, [class*="css"], p, div, label, h1, h2, h3 {
    font-family: 'Press Start 2P', cursive !important;
    color: #d81b60 !important;
}

.stApp {
    background-color: #ffc0cb;
    background-image: 
        linear-gradient(rgba(255, 105, 180, 0.3) 2px, transparent 2px),
        linear-gradient(90deg, rgba(255, 105, 180, 0.3) 2px, transparent 2px);
    background-size: 40px 40px; 
}

.scanlines {
    position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
    background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.05) 50%);
    background-size: 100% 4px; z-index: 999999; pointer-events: none; 
}

.stButton>button {
    background-color: #ff69b4 !important;
    border: 4px solid #ffffff !important;
    border-radius: 0px !important; 
    padding: 15px 24px !important;
    box-shadow: 6px 6px 0px #c71585 !important; 
    width: 100%;
    transition: none !important; 
}
.stButton>button, .stButton>button p, .stButton>button div {
    color: white !important;
    font-family: 'Press Start 2P', cursive !important;
    font-size: 16px !important;
    text-shadow: 2px 2px 0px #c71585 !important;
}
.stButton>button:hover, .stButton>button:active {
    background-color: #ff1493 !important;
    transform: translate(6px, 6px) !important; 
    box-shadow: 0px 0px 0px #c71585 !important; 
}

.stLinkButton > a {
    background-color: #ff69b4 !important;
    border: 4px solid #ffffff !important;
    border-radius: 0px !important; 
    padding: 15px 24px !important;
    box-shadow: 6px 6px 0px #c71585 !important; 
    width: 100%;
    text-align: center;
    display: inline-block;
    text-decoration: none;
}
.stLinkButton > a, .stLinkButton > a p, .stLinkButton > a div {
    color: white !important;
    font-family: 'Press Start 2P', cursive !important;
    font-size: 16px !important;
    text-shadow: 2px 2px 0px #c71585 !important;
}
.stLinkButton > a:hover, .stLinkButton > a:active {
    background-color: #ff1493 !important;
    transform: translate(6px, 6px) !important; 
    box-shadow: 0px 0px 0px #c71585 !important; 
}

.stRadio > div { gap: 15px; }

.stRadio [role="radio"] div:first-child,
.stRadio [role="radio"] svg,
.stRadio [role="radio"] input,
.stRadio span[data-baseweb="radio"] > div:first-child { 
    display: none !important; 
}
.stRadio [data-baseweb="radio"] { background: transparent !important; border: none !important; }

.stRadio [role="radio"] {
    background-color: #ffb6c1 !important;
    border: 4px solid #ffffff !important;
    border-radius: 0px !important; 
    padding: 15px !important;
    box-shadow: 6px 6px 0px #ff1493 !important;
    margin-bottom: 15px;
}
.stRadio [role="radio"] p {
    font-family: 'Press Start 2P', cursive !important;
    font-size: 14px !important;
    color: #c71585 !important;
    text-align: center;
    line-height: 1.5;
}

.stRadio [role="radio"][aria-checked="true"] {
    background-color: #ff1493 !important;
    transform: translate(6px, 6px) !important;
    box-shadow: 0px 0px 0px #ff1493 !important;
    border-color: #ffb6c1 !important;
}
.stRadio [role="radio"][aria-checked="true"] p {
    color: white !important;
    text-shadow: 2px 2px 0px #c71585 !important;
}

.block-container {
    animation: fadeInPage 1.2s ease-in-out;
    position: relative;
    z-index: 1;
}
@keyframes fadeInPage {
    0% { opacity: 0; transform: scale(0.95); }
    100% { opacity: 1; transform: scale(1); }
}

.hujan-love {
    position: fixed; top: -10vh; font-size: 30px;
    animation: fall linear forwards; z-index: 99999; pointer-events: none;
}
@keyframes fall { to { transform: translateY(110vh); } }

audio { display: none !important; }

.kertas-surat {
    background-color: #ffffff; padding: 30px; 
    border: 5px solid #ff1493; border-radius: 0px; 
    box-shadow: 10px 10px 0px #ffb6c1; text-align: justify; margin-top: 20px; margin-bottom: 30px;
}
.kertas-surat p { 
    font-family: 'VT323', monospace !important; 
    font-size: 26px !important; color: #880e4f !important; line-height: 1.4;
}
.kertas-surat b {
    font-family: 'Press Start 2P', cursive !important;
    font-size: 16px !important; color: #ff1493 !important;
}

.blinking-cursor {
    font-size: 14px; color: #ff1493; text-align: right; margin-top: 15px;
    animation: blink 1s step-end infinite;
}
@keyframes blink { 50% { opacity: 0; } }

.bg-clouds {
    position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
    z-index: 0; pointer-events: none; overflow: hidden;
}
.cloud {
    position: absolute; color: white; opacity: 0.8;
    animation: moveClouds linear infinite; filter: drop-shadow(4px 4px 0px rgba(255,105,180,0.5));
}
.c1 { top: 5%; font-size: 80px; animation-duration: 35s; animation-delay: -5s; }
.c2 { top: 20%; font-size: 50px; animation-duration: 45s; animation-delay: -25s; }
.c3 { top: 55%; font-size: 110px; animation-duration: 40s; animation-delay: -15s; }
.c4 { top: 75%; font-size: 40px; animation-duration: 60s; animation-delay: -40s; }
.c5 { top: 15%; font-size: 70px; animation-duration: 50s; animation-delay: -35s; }
.c6 { top: 10%; font-size: 60px; animation-duration: 38s; animation-delay: -12s; }
.c7 { top: 35%; font-size: 90px; animation-duration: 32s; animation-delay: -20s; }
.c8 { top: 45%; font-size: 45px; animation-duration: 55s; animation-delay: -2s; }
.c9 { top: 65%; font-size: 75px; animation-duration: 38s; animation-delay: -28s; }
.c10 { top: 85%; font-size: 55px; animation-duration: 48s; animation-delay: -50s; }
.c11 { top: 30%; font-size: 100px; animation-duration: 30s; animation-delay: -45s; }
.c12 { top: 70%; font-size: 85px; animation-duration: 36s; animation-delay: -8s; }
.c13 { top: 90%; font-size: 40px; animation-duration: 65s; animation-delay: -30s; }
.c14 { top: 40%; font-size: 120px; animation-duration: 28s; animation-delay: -35s; }
.c15 { top: 80%; font-size: 65px; animation-duration: 42s; animation-delay: -18s; }
.c16 { top: 12%; font-size: 75px; animation-duration: 40s; animation-delay: -10s; }
.c17 { top: 25%; font-size: 55px; animation-duration: 45s; animation-delay: -30s; }
.c18 { top: 50%; font-size: 95px; animation-duration: 35s; animation-delay: -5s; }
.c19 { top: 70%; font-size: 45px; animation-duration: 55s; animation-delay: -20s; }
.c20 { top: 90%; font-size: 70px; animation-duration: 50s; animation-delay: -15s; }

@keyframes moveClouds {
    0% { transform: translateX(-15vw); }
    100% { transform: translateX(110vw); }
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)
st.markdown("<div class='scanlines'></div>", unsafe_allow_html=True)

awan_html = f"""
<div class="bg-clouds">
    {''.join([f'<div class="cloud c{i}">☁️</div>' for i in range(1, 21)])}
</div>
"""
st.markdown(awan_html, unsafe_allow_html=True)

# ---------------- LOGIKA PINDAH HALAMAN ----------------
if 'tahap' not in st.session_state:
    st.session_state.tahap = 1

# --- LOGIKA MUSIK AMAN ---
if st.session_state.tahap >= 4:
    if os.path.exists(FILE_LAGU):
        st.audio(FILE_LAGU, format="audio/mpeg", autoplay=True)

layar_utama = st.empty()

with layar_utama.container():
    # ================= HALAMAN 1 =================
    if st.session_state.tahap == 1:
        st.markdown("<div style='text-align: center; font-family: \"Press Start 2P\", cursive; font-size: 20px; margin-top: 5vh; line-height: 1.8; color: #ff1493; text-shadow: 2px 2px 0px #ffffff;'>SURPRISE....
        ADA SESUATU NIH BUAT WYNTER !!!</div>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; font-size: 100px; margin-top: 20px; filter: drop-shadow(5px 5px 0px #c71585);'>💌</h1>", unsafe_allow_html=True)
        
        st.write("")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("BUKA SURAT", use_container_width=True):
                st.session_state.tahap = 2
                st.rerun() 

    # ================= HALAMAN 2 =================
    elif st.session_state.tahap == 2:
        st.markdown("<h1 style='text-align: center; font-size: 80px; margin-top: 2vh; filter: drop-shadow(5px 5px 0px #c71585);'>🫣</h1>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("<div style='text-align: center; font-family: \"Press Start 2P\", cursive; font-size: 18px; color: #ff1493; text-shadow: 2px 2px 0px #ffffff; line-height: 1.8;'>KAMU SAYANG DION GA? 👀</div>", unsafe_allow_html=True)
            st.write("")
            jawaban = st.radio("Pilih:", ["IYAAAAAA", "IYAAAAAA BANGET"], index=None, label_visibility="collapsed")
            st.write("") 
            
            if jawaban:
                if st.button("START >", use_container_width=True):
                    st.session_state.tahap = 3
                    st.rerun() 
            else:
                st.button("LOCKED X", disabled=True, use_container_width=True)

    # ================= HALAMAN 3 =================
    elif st.session_state.tahap == 3:
        st.markdown("<div style='text-align: center; font-family: \"Press Start 2P\", cursive; font-size: 28px; color: #ff1493; margin-top: 35vh; text-shadow: 4px 4px 0px #ffffff;'>LEVEL 25...</div>", unsafe_allow_html=True)
        time.sleep(1.5) 
        
        layar_utama.empty()
        
        with layar_utama.container():
            st.markdown("<div style='text-align: center; font-family: \"Press Start 2P\", cursive; font-size: 40px; color: #ff1493; margin-top: 30vh; text-shadow: 5px 5px 0px #ffffff; line-height: 1.5;'>LEVEL UP!<br><br>⭐ 26 ⭐</div>", unsafe_allow_html=True)
            if os.path.exists(FILE_LEVELUP):
                st.audio(FILE_LEVELUP, format="audio/mpeg", autoplay=True) 
        time.sleep(3) 
        
        st.session_state.tahap = 4
        st.rerun()

    # ================= HALAMAN 4 =================
    elif st.session_state.tahap == 4:
        st.markdown("<div style='text-align: center; font-family: \"Press Start 2P\", cursive; font-size: 24px; color: #ff1493; text-shadow: 3px 3px 0px #ffffff; margin-bottom: 20px; line-height: 1.5;'>STAGE CLEAR:<br><br>LEVEL UP!!! 💖🥳</div>", unsafe_allow_html=True)
        
        st.balloons()
        
        elemen_love = ""
        for _ in range(40): 
            left = random.randint(2, 95) 
            delay = random.uniform(0, 3) 
            duration = random.uniform(3, 6) 
            elemen_love += f"<div class='hujan-love' style='left: {left}vw; animation-delay: {delay}s; animation-duration: {duration}s;'>💖</div>"
        st.markdown(elemen_love, unsafe_allow_html=True)
        
        pesan_surat = """
        <div class="kertas-surat">
            <p><b>Hai BABE ku CAYAANGGGGGGGGGGGGG!</b></p>
            <p>happy level up day!!! make a wish for u b'day, tahun ini umur kamu bertambah satu tahun dan jatah hidup kamu berkurang satu tahun juga semoga kamu sehat, kmu skrg makin dewasa, apapun yang kamu inginkan bisa terjadi. terimakasih udh lahir di dunia ini dan bertahan hidup, banyak hal yang sudah kmu laluin dan masih bnyk hal yng blm km laluin, semakin kamu dewasa semkin bnyk juga rintangannya but its okayy karna masih bnyk orang yg sayang sma kmu salah satunya aku ><, apapun susahnya apapun sedihnya apapun senangnya kamu nikmatin dn brsyukur. semoga banyak kebahagiaan yang kembali dari hari ini semoga semua harapan yg diinginkan menjadi kenyataan semoga akan ada banyak kebahagiaan yang datang ke dalam hidupmu semoga harimu jauh lebih menyenangkan sesuai dng harapan mu. sekali lagi selamat ulang tahun ya, terimakasih sudah menjadi kuat selama ini walaupun awalnya dikuat2in aj dan slnjutnya harus slalu kuat, ceria bahagia yaa!!</p>
            <div class="blinking-cursor">▼</div>
        </div>
        """
        st.markdown(pesan_surat, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("NEXT STAGE >", use_container_width=True):
                st.session_state.tahap = 5
                st.rerun()

    # ================= HALAMAN 5 =================
    elif st.session_state.tahap == 5:
        st.markdown("<div style='text-align: center; font-family: \"Press Start 2P\", cursive; font-size: 28px; color: #ff1493; text-shadow: 4px 4px 0px #ffffff; margin-top: 10vh; margin-bottom: 40px; line-height: 1.5;'>PILIH STAGE 🎮</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.link_button("💬 CHAT DION", "https://wa.me/6281234567890?text=Halo%20sayang,%20aku%20udah%20siap%20nih%20buat%20ambil%20kuenya!", use_container_width=True)
            st.write("")
            
            if st.button("📸 KENANGAN KITA", use_container_width=True):
                st.session_state.tahap = 6
                st.rerun()
                
            st.write("")
            st.write("")
            
            if st.button("< KEMBALI", use_container_width=True):
                st.session_state.tahap = 4
                st.rerun()

    # ================= HALAMAN 6 =================
    elif st.session_state.tahap == 6:
        
        st.markdown("""
        <style>
        div[data-testid="stHorizontalBlock"] {
            margin-top: -180px !important;
            position: relative;
            z-index: 10;
            width: 280px !important;
            margin-left: auto !important;
            margin-right: auto !important;
        }
        div[data-testid="stHorizontalBlock"] button {
            border-radius: 20px !important; 
            box-shadow: 4px 4px 0px #c71585 !important;
            margin-bottom: 15px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # --- LOGIKA BACA FOTO ---
        img_html = ""
        if os.path.exists(FILE_FOTO):
            with open(FILE_FOTO, "rb") as image_file:
                encoded_img = base64.b64encode(image_file.read()).decode()
            img_html = f'<img src="data:image/jpeg;base64,{encoded_img}" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0; z-index: 2;">'

        # --- HTML Konsol TANPA Spasi di Awal ---
        gameboy_html = f"""
<div style="background-color: #d8d8d8; border: 5px solid #ffffff; border-radius: 10px 10px 40px 10px; padding: 20px; width: 320px; height: 430px; margin: 5vh auto 0 auto; box-shadow: 8px 8px 0px rgba(255,105,180,0.5); position: relative; z-index: 1;">
<div style="background-color: #555555; border-radius: 10px 10px 30px 10px; padding: 15px; width: 100%; box-sizing: border-box; height: 200px;">
<div style="background-color: #8bac0f; border: 4px solid #0f380f; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; padding: 5px; box-sizing: border-box; box-shadow: inset 4px 4px 0px rgba(0,0,0,0.2); overflow: hidden; position: relative;">
<div style="text-align: center; color: #0f380f; z-index: 1;">
<div style="font-family: 'Press Start 2P', cursive; font-size: 14px; margin-bottom: 15px; line-height: 1.5;">STAGE<br>KENANGAN</div>
<div style="font-family: 'Press Start 2P', cursive; font-size: 8px;">(UNDER CONSTRUCTION 🚧)</div>
</div>
{img_html}
</div>
</div>
<div style="position: absolute; bottom: 25px; left: 20px; font-family: 'Press Start 2P', cursive; font-size: 8px; color: #a0a0a0; text-shadow: 1px 1px 0px #ffffff; letter-spacing: 1px;">1 JUNI 2026</div>
<div style="position: absolute; bottom: 20px; right: 20px; display: flex; gap: 6px; transform: rotate(-25deg);">
<div style="width: 5px; height: 35px; background-color: #b0b0b0; border-radius: 5px; box-shadow: inset 1px 1px 2px rgba(0,0,0,0.2);"></div>
<div style="width: 5px; height: 35px; background-color: #b0b0b0; border-radius: 5px; box-shadow: inset 1px 1px 2px rgba(0,0,0,0.2);"></div>
<div style="width: 5px; height: 35px; background-color: #b0b0b0; border-radius: 5px; box-shadow: inset 1px 1px 2px rgba(0,0,0,0.2);"></div>
<div style="width: 5px; height: 35px; background-color: #b0b0b0; border-radius: 5px; box-shadow: inset 1px 1px 2px rgba(0,0,0,0.2);"></div>
</div>
<div style="position: absolute; bottom: 10px; left: 50%; transform: translateX(-50%); display: flex; gap: 4px;">
<div style="width: 20px; height: 3px; background-color: #c0c0c0; border-radius: 2px;"></div>
<div style="width: 20px; height: 3px; background-color: #c0c0c0; border-radius: 2px;"></div>
</div>
</div>
"""
        st.markdown(gameboy_html, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 0.1, 1])
        with col1:
            if st.button("< BACK", use_container_width=True):
                st.session_state.tahap = 5
                st.rerun()
        with col3:
            if st.button("NEXT >", use_container_width=True):
                st.session_state.tahap = 7 
                st.rerun()
                
    # ================= HALAMAN 7 =================
    elif st.session_state.tahap == 7:
        st.markdown("<div style='text-align: center; font-family: \"Press Start 2P\", cursive; font-size: 24px; color: #ff1493; text-shadow: 3px 3px 0px #ffffff; margin-top: 15vh; margin-bottom: 30px; line-height: 1.5;'>TO BE CONTINUED... ✨</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("< KEMBALI", use_container_width=True):
                st.session_state.tahap = 6
                st.rerun()
