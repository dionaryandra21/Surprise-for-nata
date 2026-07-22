import streamlit as st
import streamlit.components.v1 as components
import random
import time
import os
import base64

# --- Pelacak Folder Otomatis ---
DIR_SAAT_INI = os.path.dirname(os.path.abspath(__file__))
FILE_LAGU = os.path.join(DIR_SAAT_INI, "lagu.mp3")
FILE_LEVELUP = os.path.join(DIR_SAAT_INI, "levelup.mp3")

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

# ---------------- LOGIKA STATE PENYIMPANAN ----------------
if 'tahap' not in st.session_state:
    st.session_state.tahap = 1

# Indikator urutan foto (1 sampai 10)
if 'foto_index' not in st.session_state:
    st.session_state.foto_index = 1

# --- LOGIKA MUSIK AMAN (Dimulai setelah kue/saat surat muncul) ---
if st.session_state.tahap >= 5:
    if os.path.exists(FILE_LAGU):
        st.audio(FILE_LAGU, format="audio/mpeg", autoplay=True)

layar_utama = st.empty()

with layar_utama.container():
    # ================= HALAMAN 1 =================
    if st.session_state.tahap == 1:
        st.markdown("<div style='text-align: center; font-family: \"Press Start 2P\", cursive; font-size: 20px; margin-top: 5vh; line-height: 1.8; color: #ff1493; text-shadow: 2px 2px 0px #ffffff;'>SURPRISE....ADA SESUATU NIH BUAT WYNTER !!!</div>", unsafe_allow_html=True)
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
            st.markdown("<div style='text-align: center; font-family: \"Press Start 2P\", cursive; font-size: 18px; color: #ff1493; text-shadow: 2px 2px 0px #ffffff; line-height: 1.8;'>KAMU SAYANG DION GA?</div>", unsafe_allow_html=True)
            st.write("")
            jawaban = st.radio("Pilih:", ["IYAAAAAA DONGGG", "IYAAAAAA BANGET"], index=None, label_visibility="collapsed")
            st.write("") 
            
            if jawaban:
                if st.button("START >", use_container_width=True):
                    st.session_state.tahap = 3 
                    st.rerun() 
            else:
                st.button("LOCKED X", disabled=True, use_container_width=True)

    # ================= HALAMAN 3 (LILIN & KUE OTOMATIS) =================
    elif st.session_state.tahap == 3:
        st.markdown("<div style='text-align: center; font-family: \"Press Start 2P\", cursive; font-size: 24px; color: #ff1493; text-shadow: 3px 3px 0px #ffffff; margin-top: 2vh;'>MAKE A WISH & TIUP LILINNYA!</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; font-family: \"Press Start 2P\", cursive; font-size: 10px; color: #c71585; margin-bottom: 5px;'>(Izinkan akses mikrofon lalu tiup speaker bawah HP-mu)</div>", unsafe_allow_html=True)

        st.markdown("""
        <style>
        div[data-testid="stButton"] {
            display: none !important;
        }
        </style>
        """, unsafe_allow_html=True)

        html_kue = """
        <!DOCTYPE html>
        <html>
        <head>
        <style>
          body { text-align: center; background-color: transparent; overflow: hidden; margin: 0; padding: 0; font-family: 'Courier New', Courier, monospace;}
          .party-container { position: relative; margin-top: 100px; display: inline-block; }
          
          .cake {
            width: 180px; height: 90px; background: #ffb6c1; position: relative; margin: 0 auto;
            border-radius: 10px 10px 5px 5px; border: 4px solid #c71585; box-shadow: 0 8px 0 #c71585;
          }
          .icing {
            width: 100%; height: 40px; background: #ffffff; border-radius: 5px 5px 25px 25px;
            position: absolute; top: -2px; left: 0; border-bottom: 4px solid #c71585;
          }
          .plate {
            width: 220px; height: 15px; background: #f8f9fa; border: 4px solid #c71585; 
            border-radius: 20px; position: absolute; bottom: -15px; left: 50%; transform: translateX(-50%); box-shadow: 0 5px 0 #dcdcdc;
          }
          .sprinkle { width: 8px; height: 4px; border-radius: 4px; position: absolute; }
          .s1 { background: #ff69b4; top: 15px; left: 20px; transform: rotate(30deg); }
          .s2 { background: #00ced1; top: 10px; left: 60px; transform: rotate(-20deg); }
          .s3 { background: #ffd700; top: 20px; left: 100px; transform: rotate(45deg); }
          .s4 { background: #32cd32; top: 12px; left: 140px; transform: rotate(-45deg); }
          
          .candle {
            width: 20px; height: 50px;
            background: repeating-linear-gradient(45deg, #ffffff, #ffffff 5px, #ff1493 5px, #ff1493 10px);
            border: 3px solid #c71585; border-radius: 4px; 
            position: absolute; left: 50%; top: -50px; transform: translateX(-50%); z-index: 3;
          }
          .wick {
            width: 4px; height: 12px; background: #333; position: absolute; top: -12px; left: 50%; transform: translateX(-50%); border-radius: 2px;
          }
          .flame {
            width: 18px; height: 35px;
            background: radial-gradient(ellipse at bottom, #fff 10%, #fde08b 30%, #ff8c00 70%, transparent 100%);
            border-radius: 50% 50% 20% 20%; position: absolute; top: -42px; left: 50%; transform: translateX(-50%);
            animation: flicker 0.1s infinite alternate; box-shadow: 0 0 20px #ffaa00, 0 0 40px #ffaa00; transform-origin: bottom center;
          }
          @keyframes flicker {
            0% { transform: translateX(-50%) scale(1) rotate(-2deg); opacity: 0.9; }
            100% { transform: translateX(-50%) scale(1.05) rotate(2deg); opacity: 1; }
          }
          .smoke {
            width: 10px; height: 10px; background: rgba(100,100,100,0.5); border-radius: 50%;
            position: absolute; top: -15px; left: 50%; transform: translateX(-50%); opacity: 0;
          }
          
          .blow-out .flame { display: none; }
          .blow-out .smoke { animation: floatUp 2s ease-out forwards; }
          @keyframes floatUp {
            0% { transform: translate(-50%, 0) scale(1); opacity: 1; }
            100% { transform: translate(-50%, -100px) scale(4); opacity: 0; }
          }
          
          #status { color: #d81b60; font-weight: bold; font-size: 14px; border: 2px dashed #d81b60; padding: 10px; display: inline-block; border-radius: 10px; background-color: rgba(255,255,255,0.7); margin-top: 50px;}
        </style>
        </head>
        <body>
          <div class="party-container" id="candle-wrap">
            <div class="candle">
              <div class="wick"></div>
              <div class="flame" id="flame"></div>
              <div class="smoke"></div>
            </div>
            <div class="cake">
              <div class="icing">
                <div class="sprinkle s1"></div>
                <div class="sprinkle s2"></div>
                <div class="sprinkle s3"></div>
                <div class="sprinkle s4"></div>
              </div>
            </div>
            <div class="plate"></div>
          </div>
          <br>
          <div id="status">⏳ Menunggu akses mikrofon...</div>

          <script>
            navigator.mediaDevices.getUserMedia({ audio: true })
              .then(function(stream) {
                document.getElementById('status').innerText = "🎤 Mic aktif! Ayo tiup kenceng-kenceng!";
                let audioContext = new (window.AudioContext || window.webkitAudioContext)();
                let analyser = audioContext.createAnalyser();
                let microphone = audioContext.createMediaStreamSource(stream);
                let scriptProcessor = audioContext.createScriptProcessor(2048, 1, 1);

                analyser.smoothingTimeConstant = 0.8;
                analyser.fftSize = 1024;
                microphone.connect(analyser);
                analyser.connect(scriptProcessor);
                scriptProcessor.connect(audioContext.destination);

                scriptProcessor.onaudioprocess = function() {
                  let array = new Uint8Array(analyser.frequencyBinCount);
                  analyser.getByteFrequencyData(array);
                  let values = 0;
                  for (let i = 0; i < array.length; i++) { values += (array[i]); }
                  let average = values / array.length;
                  
                  if (average > 60) { 
                    document.getElementById('candle-wrap').classList.add('blow-out');
                    document.getElementById('status').innerText = "✨ YAY! LILIN MATI! TUNGGU BENTAR...";
                    stream.getTracks().forEach(track => track.stop()); 
                    
                    setTimeout(function() {
                        let buttons = window.parent.document.querySelectorAll('button');
                        buttons.forEach(b => {
                            if(b.textContent.includes('LANJUTKAN')) {
                                b.click();
                            }
                        });
                    }, 2000);
                  }
                }
              })
              .catch(function(err) {
                document.getElementById('status').innerText = "Mic tidak diizinkan. Mohon refresh web ini dan izinkan microphone!";
              });
          </script>
        </body>
        </html>
        """
        components.html(html_kue, height=450)
        
        st.markdown("<div style='opacity: 0; position: absolute; z-index: -1;'>", unsafe_allow_html=True)
        if st.button("LANJUTKAN"):
            st.session_state.tahap = 4
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # ================= HALAMAN 4 (ANIMASI LEVEL UP) =================
    elif st.session_state.tahap == 4:
        st.markdown("<div style='text-align: center; font-family: \"Press Start 2P\", cursive; font-size: 28px; color: #ff1493; margin-top: 35vh; text-shadow: 4px 4px 0px #ffffff;'>LEVEL 25...</div>", unsafe_allow_html=True)
        time.sleep(1.5) 
        
        layar_utama.empty()
        
        with layar_utama.container():
            st.markdown("<div style='text-align: center; font-family: \"Press Start 2P\", cursive; font-size: 40px; color: #ff1493; margin-top: 30vh; text-shadow: 5px 5px 0px #ffffff; line-height: 1.5;'>LEVEL UP!<br><br>⭐ 26 ⭐</div>", unsafe_allow_html=True)
            if os.path.exists(FILE_LEVELUP):
                st.audio(FILE_LEVELUP, format="audio/mpeg", autoplay=True) 
        time.sleep(3) 
        
        st.session_state.tahap = 5
        st.rerun()

    # ================= HALAMAN 5 (SURAT UTAMA) =================
    elif st.session_state.tahap == 5:
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
            <p>happy level up day!!! make a wish for u b'day, tahun ini umur kamu bertambah satu tahun dan jatah hidup kamu berkurang satu tahun juga semoga kamu sehat, kmu skrg makin dewasa, apapun yang kamu inginkan bisa terjadi. terimakasih udh lahir di dunia ini dan bertahan hidup, banyak hal yang sudah kmu laluin dan masih bnyk hal yng blm km laluin, semakin kamu dewasa semkin bnyk juga rintangannya but its okayy karna masih bnyk orang yg sayang sma kmu salah satunya aku ><, apapun susahnya apapun sedihnya apapun senangnya kamu nikmatin dn brsyukur. semoga banyak kebahagiaan yang kembali dari hari ini semoga semua harapan yg diinginkan menjadi kenyataan semoga akan ada banyak kebahagiaan yang datang ke dalam hidupmu semoga harimu jauh lebih menyenangkan sesuai dng harapan mu. sekali lagi selamat ulang tahun ya, terimakasih sudah menjadi kuat selama ini walaupun awalnya dikuat2in aj dan slnjutnya harus slalu kuat, ceria bahagia yaa!! I LOVE YOU SO MUCH NATAREL PRISQILLA RIANDINI HIMAWAN <3 </p>
            <div class="blinking-cursor">▼</div>
        </div>
        """
        st.markdown(pesan_surat, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("NEXT STAGE >", use_container_width=True):
                st.session_state.tahap = 6
                st.rerun()

    # ================= HALAMAN 6 (MENU PILIHAN) =================
    elif st.session_state.tahap == 6:
        st.markdown("<div style='text-align: center; font-family: \"Press Start 2P\", cursive; font-size: 28px; color: #ff1493; text-shadow: 4px 4px 0px #ffffff; margin-top: 10vh; margin-bottom: 40px; line-height: 1.5;'>PILIH STAGE 🎮</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.link_button("💬 CHAT DION", "https://wa.me/6281234567890?text=Halo%20sayang,%20aku%20udah%20siap%20nih%20buat%20ambil%20kuenya!", use_container_width=True)
            st.write("")
            
            if st.button("📸 KENANGAN KITA", use_container_width=True):
                st.session_state.tahap = 7
                st.rerun()
                
            st.write("")
            st.write("")
            
            if st.button("< KEMBALI", use_container_width=True):
                st.session_state.tahap = 5
                st.rerun()

    # ================= HALAMAN 7 (KONSOL FOTO - SLIDESHOW 10 FOTO) =================
    elif st.session_state.tahap == 7:
        
        st.markdown("""
        <style>
        /* Memastikan hanya ada 1 area grid yang ditarik ke dalam konsol */
        div[data-testid="stHorizontalBlock"] {
            position: relative;
            z-index: 10;
            width: 270px !important;
            margin-left: auto !important;
            margin-right: auto !important;
            margin-top: -190px !important;
        }
        /* Style untuk tombol-tombol agar ukurannya pas dan tersusun rapi */
        div[data-testid="stHorizontalBlock"] button {
            border-radius: 15px !important; 
            box-shadow: 4px 4px 0px #c71585 !important;
            margin-bottom: 12px !important;
            padding: 10px 5px !important;
        }
        div[data-testid="stHorizontalBlock"] button p {
            font-size: 11px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Mengecek dan memuat foto sesuai index saat ini
        nama_file_sekarang = f"foto{st.session_state.foto_index}.jpg"
        path_foto = os.path.join(DIR_SAAT_INI, nama_file_sekarang)
        
        img_html = ""
        if os.path.exists(path_foto):
            with open(path_foto, "rb") as image_file:
                encoded_img = base64.b64encode(image_file.read()).decode()
            img_html = f'<img src="data:image/jpeg;base64,{encoded_img}" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0; z-index: 2;">'
        else:
            img_html = f'<div style="width: 100%; height: 100%; position: absolute; top: 0; left: 0; z-index: 2; display: flex; align-items: center; justify-content: center; background-color: #222; color: #fff; font-family: \'Press Start 2P\', cursive; font-size: 10px; text-align: center;">{nama_file_sekarang}<br><br>KOSONG</div>'

        gameboy_html = f"""
<div style="background-color: #d8d8d8; border: 5px solid #ffffff; border-radius: 10px 10px 40px 10px; padding: 20px; width: 320px; height: 500px; margin: 5vh auto 0 auto; box-shadow: 8px 8px 0px rgba(255,105,180,0.5); position: relative; z-index: 1;">
<div style="background-color: #555555; border-radius: 10px 10px 30px 10px; padding: 15px; width: 100%; box-sizing: border-box; height: 200px; position: relative;">
<div style="background-color: #8bac0f; border: 4px solid #0f380f; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; padding: 5px; box-sizing: border-box; box-shadow: inset 4px 4px 0px rgba(0,0,0,0.2); overflow: hidden; position: relative;">
<div style="text-align: center; color: #0f380f; z-index: 1;">
<div style="font-family: 'Press Start 2P', cursive; font-size: 14px; margin-bottom: 15px; line-height: 1.5;">STAGE<br>KENANGAN</div>
</div>
{img_html}
</div>
</div>
<!-- Indikator 1/10 disisipkan ke dalam HTML agar aman dari tabrakan CSS -->
<div style="text-align: center; margin-top: 15px; font-family: 'Press Start 2P', cursive; font-size: 12px; color: #ff1493;">{st.session_state.foto_index}/10</div>

<div style="position: absolute; bottom: 25px; left: 20px; font-family: 'Press Start 2P', cursive; font-size: 9px; color: #9c9c9c; font-weight: bold; letter-spacing: 1px;">1 JUNI 2026</div>
<div style="position: absolute; bottom: 20px; right: 20px; display: flex; gap: 6px; transform: rotate(-25deg);">
<div style="width: 5px; height: 35px; background-color: #9c9c9c; border-radius: 5px; box-shadow: inset 1px 1px 2px rgba(0,0,0,0.2);"></div>
<div style="width: 5px; height: 35px; background-color: #9c9c9c; border-radius: 5px; box-shadow: inset 1px 1px 2px rgba(0,0,0,0.2);"></div>
<div style="width: 5px; height: 35px; background-color: #9c9c9c; border-radius: 5px; box-shadow: inset 1px 1px 2px rgba(0,0,0,0.2);"></div>
<div style="width: 5px; height: 35px; background-color: #9c9c9c; border-radius: 5px; box-shadow: inset 1px 1px 2px rgba(0,0,0,0.2);"></div>
</div>
<div style="position: absolute; bottom: 10px; left: 50%; transform: translateX(-50%); display: flex; gap: 4px;">
<div style="width: 20px; height: 3px; background-color: #b0b0b0; border-radius: 2px;"></div>
<div style="width: 20px; height: 3px; background-color: #b0b0b0; border-radius: 2px;"></div>
</div>
</div>
"""
        st.markdown(gameboy_html, unsafe_allow_html=True)
        
        # Grid 2 Kolom untuk semua tombol agar rapi dan tidak tumpang tindih
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⏪ FOTO", use_container_width=True):
                st.session_state.foto_index = st.session_state.foto_index - 1 if st.session_state.foto_index > 1 else 10
                st.rerun()
            if st.button("< BACK", use_container_width=True):
                st.session_state.tahap = 6
                st.rerun()
        with col2:
            if st.button("FOTO ⏩", use_container_width=True):
                st.session_state.foto_index = st.session_state.foto_index + 1 if st.session_state.foto_index < 10 else 1
                st.rerun()
            if st.button("NEXT >", use_container_width=True):
                st.session_state.tahap = 8 
                st.rerun()
                
    # ================= HALAMAN 8 =================
    elif st.session_state.tahap == 8:
        st.markdown("<div style='text-align: center; font-family: \"Press Start 2P\", cursive; font-size: 24px; color: #ff1493; text-shadow: 3px 3px 0px #ffffff; margin-top: 15vh; margin-bottom: 30px; line-height: 1.5;'>TO BE CONTINUED... ✨</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("< KEMBALI", use_container_width=True):
                st.session_state.tahap = 7
                st.rerun()
