# =========================================================
# IMPORT & KONFIGURASI
# =========================================================

import streamlit as st
import os
import re
from collections import Counter

ICON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ai_tutor_icon.png")

st.set_page_config(
    page_title="AI Tutor Bahasa Indonesia",
    page_icon=ICON_PATH if os.path.exists(ICON_PATH) else "🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# DESAIN WEBSITE / CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@500;600;700;800&display=swap');

:root {
    --biru: #159BD3;
    --biru-tua: #087FC1;
    --toska: #20AAA8;
    --toska-tua: #138E8C;
    --navy: #153B50;
    --teks: #334155;
}

/* =========================================================
   BACKGROUND GLOBAL
========================================================= */

.stApp {
    background:
        radial-gradient(circle at 0% 15%, rgba(21,155,211,.18) 0 12%, transparent 28%),
        radial-gradient(circle at 100% 18%, rgba(32,170,168,.18) 0 12%, transparent 30%),
        radial-gradient(circle at 15% 100%, rgba(89,128,255,.12) 0 10%, transparent 28%),
        linear-gradient(135deg, #f5fcff 0%, #ffffff 48%, #effcfb 100%);
    min-height: 100vh;
}

.main .block-container {
    max-width: 1400px !important;
    padding-top: 1.2rem !important;
    padding-bottom: 3rem !important;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Poppins', sans-serif !important;
}

/* =========================================================
   BUTTON DASAR
========================================================= */

div.stButton > button {
    font-family: 'Poppins', sans-serif !important;
    font-weight: 600 !important;
    border-radius: 14px !important;
    min-height: 46px !important;
    transition: all .25s ease !important;
}

div.stButton > button:hover {
    transform: translateY(-2px) !important;
}


/* =========================================================
   NAVBAR
========================================================= */

.header-box {
    background: linear-gradient(90deg, #119BD3 0%, #159BD3 45%, #20AAA8 100%);
    padding: 10px 12px;
    border-radius: 0 0 22px 22px;
    box-shadow: 0 8px 25px rgba(20, 158, 209, .20);
    margin-bottom: 25px;
}

.header-box div.stButton > button {
    min-height: 48px !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255,255,255,.30) !important;
    background: rgba(255,255,255,.10) !important;
    color: white !important;
    font-family: 'Poppins', sans-serif !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    transition: all .25s ease !important;
    box-shadow: none !important;
}

.header-box div.stButton > button:hover {
    background: rgba(255,255,255,.24) !important;
    border-color: rgba(255,255,255,.65) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 18px rgba(0,0,0,.10) !important;
}

.logo-mark {
    width: 48px;
    height: 48px;
    margin: 0 auto;
    position: relative;
}

.logo-one, .logo-two, .logo-three {
    position: absolute;
    width: 25px;
    height: 25px;
    border-radius: 6px;
    box-shadow: 0 4px 10px rgba(0,0,0,.12);
}

.logo-one {
    background: #7ED957;
    left: 2px;
    top: 5px;
}

.logo-two {
    background: #F7C948;
    left: 10px;
    top: 11px;
}

.logo-three {
    background: #3AA9FF;
    left: 18px;
    top: 17px;
}

/* Tombol di luar navbar: AI Tutor & kembali */
div.stButton > button {
    background: linear-gradient(135deg, #159BD3, #20AAA8) !important;
    color: white !important;
    border: none !important;
    box-shadow: 0 7px 18px rgba(21,155,211,.18) !important;
}

div.stButton > button:hover {
    background: linear-gradient(135deg, #087FC1, #138E8C) !important;
    color: white !important;
    box-shadow: 0 10px 22px rgba(21,155,211,.25) !important;
}


/* =========================================================
   BERANDA / HERO
========================================================= */

.home-hero {
    background: linear-gradient(135deg, #0F9FE0 0%, #159BD3 48%, #20AAA8 100%);
    border-radius: 30px;
    padding: 58px 30px 52px 30px;
    margin-top: 12px;
    text-align: center;
    position: relative;
    overflow: hidden;
    box-shadow: 0 18px 45px rgba(21,155,211,.24);
}

.home-hero:before,
.home-hero:after {
    content: "";
    position: absolute;
    border-radius: 50%;
    background: rgba(255,255,255,.10);
}

.home-hero:before {
    width: 260px;
    height: 260px;
    left: -100px;
    top: -110px;
}

.home-hero:after {
    width: 340px;
    height: 340px;
    right: -130px;
    bottom: -180px;
}

.home-logo {
    position: relative;
    z-index: 2;
    font-size: 62px;
    line-height: 1;
    margin-bottom: 10px;
}

.home-title {
    position: relative;
    z-index: 2;
    color: white;
    font-family: 'Poppins', sans-serif;
    font-size: 54px;
    line-height: 1.05;
    font-weight: 800;
    text-align: center;
}

.home-subtitle {
    position: relative;
    z-index: 2;
    color: #e9ffff;
    font-family: 'Poppins', sans-serif;
    font-size: 23px;
    font-weight: 600;
    margin-top: 8px;
    text-align: center;
}

.home-welcome {
    text-align: center;
    padding: 32px 20px 12px 20px;
}

.home-welcome-title {
    color: var(--navy);
    font-family: 'Poppins', sans-serif;
    font-size: 30px;
    font-weight: 800;
}

.home-welcome-text {
    color: #607784;
    font-size: 16px;
    line-height: 1.7;
    margin-top: 8px;
}

/* =========================================================
   KARTU FITUR
========================================================= */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,.90) !important;
    border: 1px solid rgba(21,155,211,.15) !important;
    border-radius: 20px !important;
    box-shadow: 0 8px 24px rgba(21,155,211,.09) !important;
}

/* =========================================================
   JUDUL HALAMAN
========================================================= */

.page-title {
    color: var(--biru-tua);
    font-family: 'Poppins', sans-serif;
    font-size: 38px;
    font-weight: 800;
    margin-top: 20px;
    margin-bottom: 8px;
}

.page-text {
    color: #5B7180;
    font-size: 16px;
    line-height: 1.7;
}

/* =========================================================
   AI TUTOR - HALAMAN KHUSUS
========================================================= */

.ai-page-top {
    background: linear-gradient(135deg, #0D9FDE 0%, #159BD3 50%, #20AAA8 100%);
    border-radius: 28px;
    padding: 42px 30px 36px;
    text-align: center;
    box-shadow: 0 16px 38px rgba(21,155,211,.22);
    position: relative;
    overflow: hidden;
}

.ai-page-top:before,
.ai-page-top:after {
    content: "";
    position: absolute;
    border-radius: 50%;
    background: rgba(255,255,255,.10);
}

.ai-page-top:before {
    width: 210px;
    height: 210px;
    left: -80px;
    top: -80px;
}

.ai-page-top:after {
    width: 260px;
    height: 260px;
    right: -100px;
    bottom: -130px;
}

.ai-icon {
    position: relative;
    z-index: 2;
    font-size: 58px;
}

.ai-heading {
    position: relative;
    z-index: 2;
    color: white;
    font-family: 'Poppins', sans-serif;
    font-size: 42px;
    font-weight: 800;
    text-align: center;
    margin-top: 6px;
}

.ai-tagline {
    position: relative;
    z-index: 2;
    color: #eaffff;
    font-size: 16px;
    text-align: center;
    margin-top: 5px;
}

.ai-question-card {
    background: rgba(255,255,255,.95);
    border-radius: 24px;
    padding: 28px 30px 24px;
    margin-top: 25px;
    border: 1px solid rgba(21,155,211,.16);
    box-shadow: 0 12px 32px rgba(21,155,211,.12);
}

.ai-section-title {
    color: var(--navy);
    font-family: 'Poppins', sans-serif;
    font-size: 24px;
    font-weight: 800;
    text-align: left;
}

.ai-section-text {
    color: #637784;
    font-size: 14px;
    margin-top: 5px;
    margin-bottom: 14px;
}

div[data-testid="stTextArea"] textarea {
    background: #f7fbfd !important;
    border: 2px solid #d4edf5 !important;
    border-radius: 15px !important;
    color: #253746 !important;
    font-size: 15px !important;
}

div[data-testid="stTextArea"] textarea:focus {
    border-color: #159BD3 !important;
    box-shadow: 0 0 0 3px rgba(21,155,211,.10) !important;
}

.ai-ask-button button {
    background: linear-gradient(135deg, #159BD3, #20AAA8) !important;
    color: white !important;
    border: none !important;
    border-radius: 14px !important;
    min-height: 48px !important;
    font-family: 'Poppins', sans-serif !important;
    font-weight: 700 !important;
    box-shadow: 0 7px 18px rgba(21,155,211,.22) !important;
}

.ai-ask-button button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 23px rgba(21,155,211,.30) !important;
}

.ai-result-card {
    background: rgba(255,255,255,.96);
    border-radius: 22px;
    padding: 24px 28px;
    margin-top: 20px;
    border-left: 6px solid #20AAA8;
    box-shadow: 0 8px 25px rgba(21,155,211,.10);
}

/* =========================================================
   TENTANG KAMI
========================================================= */

.team-title {
    color: var(--biru-tua);
    font-family: 'Poppins', sans-serif;
    font-size: 40px;
    font-weight: 800;
    text-align: center;
}

.team-subtitle {
    color: #627884;
    font-size: 16px;
    text-align: center;
    margin-bottom: 25px;
}

.team-card-native {
    text-align: center;
}

/* =========================================================
   EXPANDER / ALERT
========================================================= */

[data-testid="stExpander"] {
    border-radius: 16px !important;
    border: 1px solid rgba(21,155,211,.14) !important;
    background: rgba(255,255,255,.88) !important;
}

[data-testid="stAlert"] {
    border-radius: 15px !important;
}

/* =========================================================
   FOOTER
========================================================= */

.footer-text {
    text-align: center;
    color: #71838C;
    font-size: 13px;
    padding: 12px;
}

/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 768px) {
    .home-title {
        font-size: 38px;
    }

    .home-subtitle {
        font-size: 19px;
    }

    .ai-heading {
        font-size: 32px;
    }

    .page-title {
        font-size: 30px;
    }
}

/* =========================================================
   TAMPILAN TERPUSAT + LIGHT/DARK MODE
========================================================= */

.stApp {
    color: #243746;
}

.main .block-container {
    text-align: center;
}

[data-testid="stMarkdownContainer"],
[data-testid="stText"],
[data-testid="stCaptionContainer"],
[data-testid="stHeader"] {
    color: #243746;
}

[data-testid="stVerticalBlockBorderWrapper"] {
    text-align: center !important;
}

[data-testid="stVerticalBlockBorderWrapper"] [data-testid="stMarkdownContainer"],
[data-testid="stVerticalBlockBorderWrapper"] p {
    text-align: center;
}

[data-testid="stTextArea"] label {
    text-align: center !important;
    width: 100%;
}

[data-testid="stTextArea"] textarea {
    color: #243746 !important;
}

/* Navbar lebih hidup */
div.stButton > button {
    background: linear-gradient(135deg, #159BD3, #20AAA8) !important;
    color: #ffffff !important;
    border: 1px solid rgba(255,255,255,.45) !important;
    box-shadow: 0 6px 16px rgba(21,155,211,.18) !important;
}

div.stButton > button:hover {
    background: linear-gradient(135deg, #087FC1, #138E8C) !important;
    color: #ffffff !important;
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
    .stApp {
        background:
            radial-gradient(circle at 0% 15%, rgba(21,155,211,.16) 0 12%, transparent 30%),
            radial-gradient(circle at 100% 18%, rgba(32,170,168,.14) 0 12%, transparent 30%),
            linear-gradient(135deg, #08141d 0%, #0d1822 48%, #0b2021 100%) !important;
        color: #e8f4f7 !important;
    }

    [data-testid="stMarkdownContainer"],
    [data-testid="stText"],
    [data-testid="stCaptionContainer"],
    .main .block-container,
    label, p, li {
        color: #e8f4f7 !important;
    }

    .home-welcome-title,
    .page-title,
    .team-title,
    .ai-section-title {
        color: #e8fbff !important;
    }

    .home-welcome-text,
    .page-text,
    .team-subtitle,
    .ai-tagline,
    .ai-section-text {
        color: #b9d0d8 !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(18, 35, 46, .92) !important;
        border-color: rgba(83, 190, 211, .22) !important;
        box-shadow: 0 10px 28px rgba(0,0,0,.24) !important;
    }

    [data-testid="stExpander"] {
        background: rgba(18,35,46,.92) !important;
        border-color: rgba(83,190,211,.22) !important;
    }

    [data-testid="stTextArea"] textarea {
        background: #16232d !important;
        color: #f0f8fa !important;
        border-color: #315967 !important;
    }

    [data-testid="stTextArea"] textarea::placeholder {
        color: #91aab4 !important;
    }

    .ai-question-card, .ai-result-card {
        background: rgba(18,35,46,.94) !important;
        color: #e8f4f7 !important;
    }

    .ai-section-title {
        color: #e8fbff !important;
    }

    .ai-section-text {
        color: #b9d0d8 !important;
    }

    .footer-text, .stCaption {
        color: #9db4bd !important;
    }
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SISTEM NAVIGASI
# =========================================================

if "menu" not in st.session_state:
    st.session_state.menu = "Beranda"

def pilih_menu(nama_menu):
    st.session_state.menu = nama_menu

# =========================================================
# KONFIGURASI DATABASE
# =========================================================

FOLDER_DATABASE = "database"


# =========================================================
# FUNGSI MEMBACA DATABASE TXT
# =========================================================

def baca_database():

    data = []

    if not os.path.exists(FOLDER_DATABASE):

        os.makedirs(FOLDER_DATABASE)

    daftar_file = os.listdir(
        FOLDER_DATABASE
    )

    for nama_file in daftar_file:

        if nama_file.lower().endswith(".txt"):

            lokasi_file = os.path.join(
                FOLDER_DATABASE,
                nama_file
            )

            try:

                with open(
                    lokasi_file,
                    "r",
                    encoding="utf-8"
                ) as file:

                    isi = file.read()

                data.append({
                    "nama_file": nama_file,
                    "isi": isi
                })

            except Exception as error:

                st.error(
                    f"Gagal membaca {nama_file}: {error}"
                )

    return data


# =========================================================
# MEMBERSIHKAN TEKS & NORMALISASI PERTANYAAN
# =========================================================

def bersihkan_teks(teks):
    """Normalisasi teks untuk pencarian tanpa mengubah makna."""
    teks = str(teks).lower()
    teks = teks.replace("–", "-").replace("—", "-")
    teks = re.sub(r"[^a-zA-ZÀ-ÿ0-9\s-]", " ", teks)
    teks = teks.replace("-", " ")
    teks = re.sub(r"\s+", " ", teks)
    return teks.strip()


# Kata umum yang tidak membantu menentukan topik pertanyaan.
STOPWORDS = {
    "yang", "dan", "di", "ke", "dari", "pada", "dengan", "untuk", "dalam",
    "adalah", "ialah", "itu", "ini", "atau", "apa", "apakah", "bagaimana",
    "mengapa", "sebutkan", "jelaskan", "jelaskanlah", "tentang", "suatu",
    "sebuah", "secara", "merupakan", "dapat", "akan", "sebagai", "oleh",
    "lebih", "juga", "tidak", "tersebut", "utama", "saja", "kah", "nya",
    "disebut", "dimaksud", "maksud", "pengertian", "jelas", "jelaskan"
}

# Istilah yang sering diketik siswa tanpa spasi/tanda hubung.
ALIAS_PERTANYAAN = {
    "teksprosedur": "teks prosedur",
    "teksproseduradalah": "teks prosedur adalah",
    "tekseksplanasi": "teks eksplanasi",
    "tekseksposisi": "teks eksposisi",
    "teksdeskripsi": "teks deskripsi",
    "teksnegosiasi": "teks negosiasi",
    "tekspersuasif": "teks persuasif",
    "ciri-ciri": "ciri ciri",
    "ciri2": "ciri ciri",
    "langkah-langkah": "langkah langkah",
    "langkah2": "langkah langkah",
}


def normalisasi_pertanyaan(pertanyaan, database=None):
    """Merapikan pertanyaan dan memperbaiki bentuk yang umum diketik siswa."""
    teks = str(pertanyaan).lower().strip()
    teks = teks.replace("–", "-").replace("—", "-")
    teks = re.sub(r"[^a-zA-ZÀ-ÿ0-9\s-]", " ", teks)

    # Alias harus diproses sebelum tanda hubung dihapus.
    for sumber, target in sorted(ALIAS_PERTANYAAN.items(), key=lambda x: len(x[0]), reverse=True):
        teks = teks.replace(sumber, target)

    teks = teks.replace("-", " ")
    teks = re.sub(r"\s+", " ", teks).strip()

    # Pemecahan token yang menempel, misalnya "teksprosedur".
    # Alias di atas menangani contoh umum; bagian ini menjadi cadangan
    # jika siswa menulis gabungan istilah lain yang memang ada di database.
    if database:
        kosakata = set()
        for data in database:
            kosakata.update(
                k for k in bersihkan_teks(data.get("isi", "")).split()
                if len(k) >= 3
            )
        tokens = teks.split()
        hasil = []
        for token in tokens:
            if token in kosakata or len(token) < 7:
                hasil.append(token)
                continue
            pecahan = None
            for i in range(3, len(token) - 2):
                kiri = token[:i]
                kanan = token[i:]
                if kiri in kosakata and kanan in kosakata:
                    pecahan = [kiri, kanan]
                    break
            hasil.extend(pecahan if pecahan else [token])
        teks = " ".join(hasil)

    return teks


def ambil_kata_kunci(pertanyaan, database=None):
    teks = normalisasi_pertanyaan(pertanyaan, database)
    kata = teks.split()
    hasil = []
    for item in kata:
        if len(item) > 2 and item not in STOPWORDS and item not in hasil:
            hasil.append(item)
    return hasil


def buat_frasa_kunci(pertanyaan, database=None):
    teks = normalisasi_pertanyaan(pertanyaan, database)
    kata = [k for k in teks.split() if len(k) > 2 and k not in STOPWORDS]
    frasa = []
    for n in (2, 3, 4):
        for i in range(len(kata) - n + 1):
            frasa.append(" ".join(kata[i:i+n]))
    return frasa


def klasifikasi_pertanyaan(pertanyaan, database=None):
    """Menentukan fokus pertanyaan supaya jawaban tidak keluar topik."""
    q = normalisasi_pertanyaan(pertanyaan, database)

    # DEFINISI harus diperiksa lebih dulu.
    if (
        "apa itu" in q
        or "pengertian" in q
        or "definisi" in q
        or "dimaksud" in q
        or re.search(r"\b(adalah|ialah|merupakan)\s*\??$", q)
    ):
        return "definisi"

    if "ciri ciri" in q or re.search(r"\bciri\b", q):
        return "ciri"
    if any(x in q for x in ["tujuan", "fungsi"]):
        return "tujuan"
    if any(x in q for x in ["struktur", "bagian bagian"]):
        return "struktur"
    if any(x in q for x in ["langkah", "tahapan", "cara"]):
        return "langkah"
    if any(x in q for x in ["jenis", "macam"]):
        return "jenis"
    if any(x in q for x in ["contoh", "misalnya"]):
        return "contoh"
    if any(x in q for x in ["unsur kebahasaan", "kebahasaan", "kalimat perintah", "kalimat ajakan", "konjungsi"]):
        return "kebahasaan"
    if any(x in q for x in ["bentuk sajian", "disajikan", "media"]):
        return "bentuk_sajian"
    return "umum"


def _blok_teks(isi):
    """Membagi materi menjadi blok yang tetap mempertahankan urutan database."""
    isi = isi.replace("\r\n", "\n")
    return [b.strip() for b in re.split(r"\n\s*\n+", isi) if b.strip()]


def _cari_blok_definisi(isi, pertanyaan):
    """Ambil blok tepat setelah heading definisi, bila tersedia."""
    blok = _blok_teks(isi)
    q = normalisasi_pertanyaan(pertanyaan)

    for i, b in enumerate(blok):
        b_norm = bersihkan_teks(b)
        # Materi pengguna memiliki heading "APA ITU TESK PROSEDUR?".
        # Kita sengaja mencari "apa itu" + topik, bukan exact spelling,
        # agar typo "tesk" di judul database tidak mengganggu.
        if "apa itu" in b_norm and "prosedur" in b_norm:
            if i + 1 < len(blok):
                return blok[i + 1]

    # Cadangan: cari blok yang benar-benar mendefinisikan topik.
    kata_topik = [k for k in ambil_kata_kunci(pertanyaan) if k not in {"apa", "itu"}]
    kandidat = []
    for i, b in enumerate(blok):
        n = bersihkan_teks(b)
        if not all(k in set(n.split()) for k in kata_topik):
            continue
        if any(x in n for x in [" adalah ", " merupakan ", " ialah ", " disebut ", " yaitu "]):
            skor = 100
            if i > 0 and "apa itu" in bersihkan_teks(blok[i-1]):
                skor += 100
            kandidat.append((skor, i, b))
    if kandidat:
        kandidat.sort(reverse=True)
        return kandidat[0][2]
    return ""


def _cari_blok_berdasarkan_intent(isi, pertanyaan, intent):
    """Mengambil bagian materi yang memang menjawab jenis pertanyaan."""
    blok = _blok_teks(isi)
    q = normalisasi_pertanyaan(pertanyaan)
    topik = [k for k in ambil_kata_kunci(pertanyaan) if k not in {"ciri", "tujuan", "fungsi", "struktur", "langkah", "tahapan", "cara", "jenis", "macam", "contoh"}]

    if intent == "definisi":
        return _cari_blok_definisi(isi, pertanyaan)

    pola = {
        "tujuan": ["tujuan utama teks prosedur", "fungsi dan tujuan spesifik", "bertujuan"],
        "ciri": ["ciri-ciri teks prosedur", "ciri ciri teks prosedur", "CIRI 1", "CIRI 2", "CIRI 3", "CIRI 4", "CIRI 5"],
        "struktur": ["struktur teks prosedur"],
        "langkah": ["langkah-langkah", "langkah langkah", "tahapan"],
        "jenis": ["jenis-jenis teks prosedur", "jenis jenis teks prosedur", "teks prosedur sederhana", "teks prosedur kompleks", "teks prosedur protokol"],
        "kebahasaan": ["unsur kebahasaan", "kalimat perintah", "kalimat ajakan", "konjungsi temporal"],
        "bentuk_sajian": ["bentuk sajian teks prosedur", "visual / infografik", "audio-visual"],
        "contoh": ["contoh", "misalnya"],
    }

    # Untuk pertanyaan tujuan/fungsi, ambil blok yang memang menjadi jawaban.
    if intent == "tujuan":
        # Jika pengguna menanyakan FUNGSI, prioritaskan bagian fungsi.
        if "fungsi" in q:
            for b in blok:
                n = bersihkan_teks(b)
                if "fungsi dan tujuan spesifik" in n:
                    return b
        # Jika pengguna menanyakan TUJUAN, ambil definisi tujuan yang eksplisit.
        for b in blok:
            n = bersihkan_teks(b)
            if "tujuan utama teks prosedur" in n:
                return b

    kandidat = []
    for i, b in enumerate(blok):
        n = bersihkan_teks(b)
        if not all(k in set(n.split()) for k in topik) if topik else False:
            continue
        skor = 0
        for p in pola.get(intent, []):
            if bersihkan_teks(p) in n:
                skor += 80
        if intent == "tujuan" and any(x in n for x in ["tujuan", "bertujuan", "fungsi"]):
            skor += 70
        if intent == "ciri" and "ciri" in n:
            skor += 70
        if intent == "struktur" and "struktur" in n:
            skor += 70
        if intent == "langkah" and "langkah" in n:
            skor += 70
        if intent == "jenis" and "teks prosedur" in n:
            skor += 50
        if intent == "kebahasaan" and any(x in n for x in ["kalimat", "konjungsi", "keterangan"]):
            skor += 50
        if intent == "bentuk_sajian" and "sajian" in n:
            skor += 70
        if intent == "contoh" and any(x in n for x in ["contoh", "misalnya"]):
            skor += 50
        if skor:
            kandidat.append((skor, -i, b))

    if not kandidat:
        return ""

    kandidat.sort(reverse=True)
    terbaik = kandidat[0][2]

    # Untuk pertanyaan jenis/ciri, satu blok saja kadang terlalu sempit.
    # Tambahkan blok berikutnya hanya jika masih merupakan bagian yang sama.
    idx = next((i for i, b in enumerate(blok) if b == terbaik), 0)
    tambahan = []
    if intent in {"ciri", "jenis"}:
        for b in blok[idx + 1:idx + 4]:
            n = bersihkan_teks(b)
            if intent == "ciri" and ("ciri" in n or "kalimat" in n or "konjungsi" in n):
                tambahan.append(b)
            elif intent == "jenis" and "teks prosedur" in n:
                tambahan.append(b)

    return "\n\n".join([terbaik] + tambahan)


# =========================================================
# AI TUTOR - PENCARIAN BERDASARKAN BAGIAN MATERI
# =========================================================
#
# Prinsip penting:
# 1. Jawaban TIDAK dibuat/diarang oleh program.
# 2. Program hanya mengambil teks yang memang ada di database TXT.
# 3. Pertanyaan "Apa itu X?" dipaksa mencari heading "APA ITU X?"
#    atau paragraf definisi X, bukan paragraf lain yang kebetulan
#    mengandung kata X.
# 4. Jika bagian yang tepat tidak ditemukan, program TIDAK menjawab
#    dengan materi yang tidak jelas.
# =========================================================

def _normalisasi_blok(teks):
    return bersihkan_teks(teks)


def _kata_set(teks):
    return set(_normalisasi_blok(teks).split())


def _topik_pertanyaan(pertanyaan, database=None):
    """
    Mengambil topik utama dari pertanyaan.

    Contoh:
    'apa itu teks prosedur?'       -> ['teks', 'prosedur']
    'teksprosedur adalah?'         -> ['teks', 'prosedur']
    'apa ciri ciri teks prosedur'  -> ['teks', 'prosedur']
    """
    q = normalisasi_pertanyaan(pertanyaan, database)

    intent_words = {
        "apa", "itu", "adalah", "ialah", "merupakan", "dimaksud",
        "pengertian", "definisi", "ciri", "ciri-ciri", "tujuan",
        "fungsi", "struktur", "bagian", "langkah", "langkah-langkah",
        "tahapan", "cara", "jenis", "macam", "contoh", "jelaskan",
        "sebutkan", "bagaimana", "mengapa", "tentang", "yang"
    }

    return [
        kata for kata in q.split()
        if len(kata) >= 3 and kata not in intent_words
    ]


def _intent_pertanyaan(pertanyaan, database=None):
    q = normalisasi_pertanyaan(pertanyaan, database)

    # Definisi HARUS diperiksa paling awal.
    if (
        "apa itu" in q
        or "pengertian" in q
        or "definisi" in q
        or "dimaksud" in q
        or re.search(r"\b(adalah|ialah|merupakan)\s*$", q)
    ):
        return "definisi"

    if "ciri ciri" in q or re.search(r"\bciri\b", q):
        return "ciri"

    if "tujuan" in q:
        return "tujuan"

    if "fungsi" in q:
        return "fungsi"

    if "struktur" in q or "bagian bagian" in q:
        return "struktur"

    if "langkah langkah" in q or "tahapan" in q:
        return "langkah"

    if "jenis" in q or "macam" in q:
        return "jenis"

    if "contoh" in q or "misalnya" in q:
        return "contoh"

    if (
        "unsur kebahasaan" in q
        or "kebahasaan" in q
        or "kalimat perintah" in q
        or "kalimat ajakan" in q
        or "konjungsi" in q
    ):
        return "kebahasaan"

    return "umum"


def _cari_heading(isi, topik, kata_heading):
    """
    Mencari blok yang berfungsi sebagai heading.

    Tidak menggunakan substring sembarangan.
    Semua kata topik harus benar-benar menjadi token.
    """
    blok = _blok_teks(isi)

    for i, blok_saat_ini in enumerate(blok):
        n = _normalisasi_blok(blok_saat_ini)
        token = set(n.split())

        # Heading harus pendek agar paragraf biasa tidak dianggap heading.
        if len(n) > 180:
            continue

        topik_cocok = all(k in token for k in topik) if topik else False
        heading_cocok = all(k in token for k in kata_heading)

        if topik_cocok and heading_cocok:
            return i, blok

    return None, blok


def _ambil_definisi_dari_database(pertanyaan, isi, database=None):
    """
    Untuk pertanyaan DEFINISI, cari heading 'APA ITU ...'
    lalu ambil blok tepat setelah heading tersebut.

    Ini adalah aturan utama untuk kasus:
    'APA ITU TEKS PROSEDUR?'
    'TEKSPROSEDUR ADALAH?'
    """
    topik = _topik_pertanyaan(pertanyaan, database)

    if not topik:
        return ""

    blok = _blok_teks(isi)

    # PRIORITAS 1:
    # Heading 'APA ITU ...' yang memiliki seluruh topik.
    for i, b in enumerate(blok):
        n = _normalisasi_blok(b)
        token = set(n.split())

        # Database yang kamu kirim memiliki typo pada heading:
        # "APA ITU TESK PROSEDUR?"
        # Pertanyaan siswa boleh memakai "teks prosedur".
        token_cocok = set(token)
        if "tesk" in token_cocok:
            token_cocok.add("teks")

        if (
            "apa" in token
            and "itu" in token
            and all(k in token_cocok for k in topik)
        ):
            if i + 1 < len(blok):
                # Blok sesudah heading adalah jawaban definisi
                # pada database yang diberikan pengguna.
                return blok[i + 1].strip()

    # PRIORITAS 2:
    # Cari paragraf yang mengandung topik + pola definisi.
    kandidat = []

    for i, b in enumerate(blok):
        n = _normalisasi_blok(b)
        token = set(n.split())

        if not all(k in token for k in topik):
            continue

        pola_definisi = (
            " adalah " in f" {n} "
            or " merupakan " in f" {n} "
            or " ialah " in f" {n} "
            or " disebut " in f" {n} "
            or " yaitu " in f" {n} "
        )

        if pola_definisi:
            skor = 100

            # Jika blok sebelumnya adalah heading "apa itu",
            # naikkan prioritas secara sangat tinggi.
            if i > 0:
                prev = _normalisasi_blok(blok[i - 1])
                if "apa" in prev.split() and "itu" in prev.split():
                    skor += 1000

            kandidat.append((skor, -i, b))

    if kandidat:
        kandidat.sort(reverse=True)
        return kandidat[0][2].strip()

    return ""


def _ambil_bagian_intent(pertanyaan, isi, database=None):
    """
    Mengambil bagian materi berdasarkan jenis pertanyaan.
    """
    intent = _intent_pertanyaan(pertanyaan, database)

    if intent == "definisi":
        return _ambil_definisi_dari_database(
            pertanyaan,
            isi,
            database
        )

    topik = _topik_pertanyaan(pertanyaan, database)
    blok = _blok_teks(isi)

    # =====================================================
    # ATURAN KHUSUS UNTUK PERTANYAAN YANG MEMILIKI BAGIAN
    # JAWABAN YANG SUDAH JELAS DI DATABASE.
    # =====================================================
    # Ini sengaja diletakkan SEBELUM pencarian umum supaya
    # "Apa tujuan teks prosedur?" tidak mengambil paragraf
    # definisi hanya karena kata "tujuan" kebetulan muncul.

    if intent == "tujuan":
        for i, b in enumerate(blok):
            n = _normalisasi_blok(b)
            if "tujuan utama teks prosedur" in n:
                return b.strip()

    if intent == "fungsi":
        for i, b in enumerate(blok):
            n = _normalisasi_blok(b)
            if "fungsi dan tujuan spesifik" in n:
                bagian = [b]
                # Ambil rincian fungsi 1-4 yang langsung mengikuti heading.
                for j in range(i + 1, min(i + 5, len(blok))):
                    bagian.append(blok[j])
                return "\\n\\n".join(bagian).strip()

    if intent == "langkah":
        for i, b in enumerate(blok):
            n = _normalisasi_blok(b)
            if "langkah langkah" in n and len(n) < 100:
                bagian = [b]
                for j in range(i + 1, min(i + 8, len(blok))):
                    berikutnya = _normalisasi_blok(blok[j])
                    # Berhenti ketika masuk ke bagian baru.
                    if (
                        berikutnya.startswith("4 penutup")
                        or berikutnya.startswith("unsur kebahasaan")
                    ):
                        break
                    bagian.append(blok[j])
                return "\\n\\n".join(bagian).strip()

    # Kata heading yang dicari sesuai jenis pertanyaan.
    heading_map = {
        "ciri": ["ciri"],
        "tujuan": ["tujuan"],
        "fungsi": ["fungsi"],
        "struktur": ["struktur"],
        "langkah": ["langkah"],
        "jenis": ["jenis"],
        "kebahasaan": ["kebahasaan"],
        "contoh": ["contoh"],
    }

    kata_heading = heading_map.get(intent, [])

    kandidat = []

    for i, b in enumerate(blok):
        n = _normalisasi_blok(b)
        token = set(n.split())

        # Heading harus cukup pendek.
        if len(n) > 180:
            continue

        if not kata_heading:
            continue

        if not all(k in token for k in kata_heading):
            continue

        # Jika ada topik, topik harus muncul sebagai token.
        if topik and not all(k in token for k in topik):
            continue

        skor = 100

        # Topik lengkap.
        skor += len(topik) * 50

        # Heading yang sangat spesifik mendapatkan prioritas.
        if "teks" in token and "prosedur" in token:
            skor += 200

        kandidat.append((skor, -i, i))

    if not kandidat:
        # Cadangan: cari paragraf yang memiliki semua topik
        # dan kata intent.
        for i, b in enumerate(blok):
            n = _normalisasi_blok(b)
            token = set(n.split())

            if topik and not all(k in token for k in topik):
                continue

            cocok_intent = any(
                kata in token
                for kata in kata_heading
            )

            if cocok_intent:
                kandidat.append((80, -i, i))

    if not kandidat:
        return ""

    kandidat.sort(reverse=True)
    indeks = kandidat[0][2]

    # Untuk heading seperti "Ciri-Ciri Teks Prosedur",
    # ambil heading + beberapa blok sesudahnya yang masih
    # membahas topik tersebut.
    hasil = [blok[indeks]]

    if intent in {"ciri", "jenis", "struktur", "kebahasaan"}:
        for j in range(indeks + 1, min(indeks + 8, len(blok))):
            berikutnya = _normalisasi_blok(blok[j])

            # Berhenti jika menemukan heading besar baru.
            if (
                len(berikutnya) < 120
                and (
                    berikutnya.startswith("jenis jenis")
                    or berikutnya.startswith("struktur teks")
                    or berikutnya.startswith("unsur kebahasaan")
                    or berikutnya.startswith("cara membuat")
                )
            ):
                break

            hasil.append(blok[j])

    return "\n\n".join(hasil).strip()


def _skor_materi(pertanyaan, data, database=None):
    """
    Skor file.

    Bagian yang tepat menjawab pertanyaan diberi skor sangat tinggi.
    Kemunculan kata yang kebetulan sama diberi skor jauh lebih rendah.
    """
    isi = data["isi"]
    nama_file = data["nama_file"]

    intent = _intent_pertanyaan(pertanyaan, database)
    topik = _topik_pertanyaan(pertanyaan, database)

    skor = 0

    # =====================================================
    # PRIORITAS TERTINGGI: BAGIAN JAWABAN YANG TEPAT
    # =====================================================
    jawaban_tepat = _ambil_bagian_intent(
        pertanyaan,
        isi,
        database
    )

    if jawaban_tepat:
        skor += 5000

    # =====================================================
    # KHUSUS DEFINISI:
    # HEADING "APA ITU ..." ADALAH PRIORITAS ABSOLUT
    # =====================================================
    if intent == "definisi" and topik:
        blok = _blok_teks(isi)

        for i, b in enumerate(blok):
            n = _normalisasi_blok(b)
            token = set(n.split())

            token_cocok = set(token)
            if "tesk" in token_cocok:
                token_cocok.add("teks")

            if (
                "apa" in token
                and "itu" in token
                and all(k in token_cocok for k in topik)
            ):
                skor += 10000

                # File yang benar-benar memiliki definisi
                # diberi bonus tambahan.
                if i + 1 < len(blok):
                    sesudah = _normalisasi_blok(blok[i + 1])
                    if any(
                        pola in f" {sesudah} "
                        for pola in [
                            " adalah ",
                            " merupakan ",
                            " ialah ",
                            " disebut ",
                            " yaitu "
                        ]
                    ):
                        skor += 5000

                break

    # =====================================================
    # SKOR CADANGAN: KECocokan TOPIK
    # =====================================================
    teks = _normalisasi_blok(isi)
    token_isi = set(teks.split())

    cocok = [k for k in topik if k in token_isi]

    if topik:
        coverage = len(cocok) / len(topik)
        skor += int(coverage * 500)

    # Bonus kecil untuk nama file.
    nama_norm = _normalisasi_blok(nama_file)
    skor += sum(20 for k in cocok if k in set(nama_norm.split()))

    return skor


def cari_materi(pertanyaan, database):
    """
    Mengembalikan materi yang benar-benar relevan.

    Jika tidak ada bagian yang cukup meyakinkan,
    kembalikan [] agar AI Tutor tidak blunder.
    """
    if not pertanyaan.strip() or not database:
        return []

    hasil = []

    for data in database:
        skor = _skor_materi(
            pertanyaan,
            data,
            database
        )

        if skor > 0:
            hasil.append({
                "nama_file": data["nama_file"],
                "isi": data["isi"],
                "skor": skor
            })

    if not hasil:
        return []

    hasil.sort(
        key=lambda x: x["skor"],
        reverse=True
    )

    # =====================================================
    # BATAS KEAMANAN
    # =====================================================
    # Jika pertanyaan punya bagian jawaban yang tepat,
    # hanya kandidat yang sama-sama memiliki jawaban tepat
    # yang boleh menjadi materi terkait.
    utama = hasil[0]

    intent = _intent_pertanyaan(
        pertanyaan,
        database
    )

    jawaban_utama = _ambil_bagian_intent(
        pertanyaan,
        utama["isi"],
        database
    )

    if not jawaban_utama:
        return []

    hasil_final = [utama]

    for item in hasil[1:]:
        jawaban_item = _ambil_bagian_intent(
            pertanyaan,
            item["isi"],
            database
        )

        if not jawaban_item:
            continue

        # Materi kedua harus sangat dekat dengan skor utama.
        if item["skor"] >= utama["skor"] * 0.80:
            hasil_final.append(item)

    return hasil_final[:4]


# =========================================================
# FUNGSI JAWABAN
# =========================================================

def ambil_potongan_relevan(
    pertanyaan,
    isi,
    jumlah_maksimal=2000,
    database=None
):
    """
    Jawaban FINAL.

    Tidak melakukan pencarian ulang secara longgar.
    Hanya mengembalikan bagian database yang sesuai
    dengan intent pertanyaan.
    """
    jawaban = _ambil_bagian_intent(
        pertanyaan,
        isi,
        database
    )

    if not jawaban:
        return ""

    if len(jawaban) <= jumlah_maksimal:
        return jawaban.strip()

    # Potong di batas kalimat agar tidak memotong
    # penjelasan secara kasar.
    potongan = jawaban[:jumlah_maksimal]
    titik = potongan.rfind(".")

    if titik >= int(jumlah_maksimal * 0.60):
        potongan = potongan[:titik + 1]

    return potongan.strip()


# LOAD DATABASE
# =========================================================

database = baca_database()


# =========================================================
# HEADER / NAVBAR
# AI TUTOR DAN MATERI TIDAK ADA DI NAVBAR
# =========================================================

if st.session_state.menu != "AI Tutor":
    col_logo, col1, col2, col3, col4, col5, col6 = st.columns(
        [0.50, 0.95, 1.65, 1.25, 1.55, 1.55, 1.20]
    )

    with col_logo:
        st.markdown("## 📚")

    with col1:
        if st.button("Beranda", key="nav_beranda", use_container_width=True):
            pilih_menu("Beranda")
            st.rerun()

    with col2:
        if st.button("Video Pembelajaran", key="nav_video", use_container_width=True):
            pilih_menu("Video Pembelajaran")
            st.rerun()

    with col3:
        if st.button("Kuis / Latihan", key="nav_kuis", use_container_width=True):
            pilih_menu("Kuis / Latihan")
            st.rerun()

    with col4:
        if st.button("Pengumpulan Tugas", key="nav_tugas", use_container_width=True):
            pilih_menu("Pengumpulan Tugas")
            st.rerun()

    with col5:
        if st.button("Panduan Penggunaan", key="nav_panduan", use_container_width=True):
            pilih_menu("Panduan Penggunaan")
            st.rerun()

    with col6:
        if st.button("Tentang Kami", key="nav_tentang", use_container_width=True):
            pilih_menu("Tentang Kami")
            st.rerun()


# =========================================================
# HALAMAN BERANDA
# AI TUTOR TETAP TAMPIL LANGSUNG DI BERANDA
# =========================================================

if st.session_state.menu == "Beranda":
    st.write("")

    # HEADER BERANDA
    kiri, tengah, kanan = st.columns([1, 4, 1])
    with tengah:
        st.markdown("# 📚")
        st.title("AI TUTOR")
        st.subheader("Bahasa Indonesia")
        st.write(
            "Teman belajar digital untuk memahami Bahasa Indonesia "
            "dengan lebih mudah, interaktif, dan menyenangkan."
        )

    st.write("")
    st.divider()
    st.write("")

    # AI TUTOR DI BERANDA
    kiri_ai, tengah_ai, kanan_ai = st.columns([1, 6, 1])
    with tengah_ai:
        with st.container(border=True):
            st.title("🤖 AI Tutor Bahasa Indonesia")
            st.write(
                "Tanyakan materi Bahasa Indonesia dan AI Tutor akan "
                "mencari jawaban hanya dari database pembelajaran."
            )
            st.write("")
            st.subheader("💬 Tanyakan Sesuatu")

            pertanyaan_beranda = st.text_area(
                "Masukkan pertanyaan Anda:",
                placeholder="Contoh: Apa ciri-ciri teks prosedur?",
                height=130,
                key="pertanyaan_beranda"
            )

            tombol_beranda = st.button(
                "🔍 TANYAKAN",
                key="btn_tanyakan_beranda",
                use_container_width=True
            )

        if tombol_beranda:
            if pertanyaan_beranda.strip() == "":
                st.warning("Silakan masukkan pertanyaan terlebih dahulu.")
            elif len(database) == 0:
                st.error("Database TXT belum ditemukan.")
            else:
                with st.spinner("Sedang mencari materi yang paling sesuai..."):
                    hasil_beranda = cari_materi(pertanyaan_beranda, database)

                if hasil_beranda:
                    hasil_utama = hasil_beranda[0]
                    jawaban = ambil_potongan_relevan(
                        pertanyaan_beranda,
                        hasil_utama["isi"],
                        database=database
                    )

                    if jawaban:
                        st.success("Materi yang relevan ditemukan.")
                        with st.container(border=True):
                            st.subheader("💡 Jawaban")
                            st.info(jawaban)

                        with st.container(border=True):
                            st.subheader("📚 Sumber Materi")
                            st.write(hasil_utama["nama_file"])

                        # Hanya tampilkan materi tambahan yang cukup dekat
                        # dengan skor utama. Materi yang jauh tidak ditampilkan.
                        skor_utama = hasil_utama["skor"]
                        terkait = [
                            item for item in hasil_beranda[1:4]
                            if item["skor"] >= max(12, int(skor_utama * 0.60))
                        ]

                        if terkait:
                            st.subheader("📑 Materi Terkait")
                            for item in terkait:
                                potongan = ambil_potongan_relevan(
                                    pertanyaan_beranda,
                                    item["isi"],
                                    800,
                                    database
                                )
                                if potongan:
                                    with st.expander(item["nama_file"]):
                                        st.write(potongan)
                    else:
                        st.warning(
                            "Materi yang benar-benar sesuai dengan pertanyaan belum ditemukan."
                        )
                else:
                    st.warning(
                        "Materi yang sesuai dengan pertanyaan belum ditemukan dalam database."
                    )
                    st.info(
                        "Coba gunakan kata kunci yang lebih spesifik, misalnya "
                        "ciri-ciri, tujuan, struktur, fungsi, atau langkah-langkah."
                    )

    st.write("")

    # MENU PEMBELAJARAN: URUTAN SESUAI PERMINTAAN
    st.subheader("✨ Menu Pembelajaran")

    fitur1, fitur2, fitur3 = st.columns(3)

    with fitur1:
        with st.container(border=True):
            st.markdown("## 🎥")
            st.markdown("### Video Pembelajaran")
            st.write("Belajar melalui video yang menarik dan mudah dipahami.")
            if st.button(
                "▶️ Lihat Video",
                key="home_video",
                use_container_width=True
            ):
                pilih_menu("Video Pembelajaran")
                st.rerun()

    with fitur2:
        with st.container(border=True):
            st.markdown("## 📝")
            st.markdown("### Kuis / Latihan")
            st.write("Uji pemahaman melalui kuis dan latihan soal.")
            if st.button(
                "🎯 Buka Kuis / Latihan",
                key="home_kuis",
                use_container_width=True
            ):
                pilih_menu("Kuis / Latihan")
                st.rerun()

    with fitur3:
        with st.container(border=True):
            st.markdown("## 📤")
            st.markdown("### Pengumpulan Tugas")
            st.write("Kirim tugas melalui Google Classroom.")
            if st.button(
                "📤 Buka Pengumpulan Tugas",
                key="home_tugas",
                use_container_width=True
            ):
                pilih_menu("Pengumpulan Tugas")
                st.rerun()

# =========================================================
# HALAMAN PANDUAN PENGGUNAAN
# =========================================================

elif st.session_state.menu == "Panduan Penggunaan":

    st.write("")
    st.title("📖 Panduan Penggunaan")
    st.write(
        "Ikuti langkah berikut untuk menggunakan website AI Tutor Bahasa Indonesia."
    )
    st.write("")

    langkah_panduan = [
        ("1️⃣", "Membuka Beranda", "Gunakan halaman Beranda untuk melihat fitur utama website dan AI Tutor."),
        ("2️⃣", "Menggunakan AI Tutor", "Ketik pertanyaan Bahasa Indonesia pada kotak pertanyaan di Beranda, lalu tekan tombol TANYAKAN."),
        ("3️⃣", "Menulis Pertanyaan", "Gunakan pertanyaan yang jelas dan spesifik, misalnya: “Apa yang dimaksud dengan teks prosedur?” atau “Apa ciri-ciri teks prosedur?”"),
        ("4️⃣", "Membaca Jawaban", "AI Tutor akan mengambil jawaban dari materi yang tersedia di database. Jika materi yang sesuai tidak ditemukan, website tidak akan menampilkan jawaban yang tidak didukung database."),
        ("5️⃣", "Video Pembelajaran", "Buka menu Video Pembelajaran untuk melihat video yang telah disediakan sebagai media belajar tambahan."),
        ("6️⃣", "Kuis / Latihan", "Buka menu Kuis / Latihan untuk mengerjakan kuis dan latihan soal Bahasa Indonesia."),
        ("7️⃣", "Pengumpulan Tugas", "Buka menu Pengumpulan Tugas untuk mengakses Google Classroom dan mengirimkan tugas."),
        ("8️⃣", "Tentang Kami", "Buka menu Tentang Kami untuk melihat anggota tim pengembang AI Tutor Bahasa Indonesia."),
    ]

    for ikon, judul, isi in langkah_panduan:
        with st.container(border=True):
            st.markdown(f"## {ikon}")
            st.markdown(f"### {judul}")
            st.write(isi)

# =========================================================
# HALAMAN VIDEO
# =========================================================

elif st.session_state.menu == "Video Pembelajaran":

    st.title("🎥 Video Pembelajaran")
    st.write(
        "Berikut beberapa video pembelajaran Bahasa Indonesia."
    )

    with st.container(border=True):
        st.markdown("### 🎬 Video Pembelajaran 1")
        st.markdown(
            "[▶️ Tonton Video Pembelajaran](https://youtu.be/OZAdSVoMnh4?si=BsV1gCVb7HjUstqQ)"
        )

    with st.container(border=True):
        st.markdown("### 🎬 Video Contoh Animasi Prosedur")
        st.markdown(
            "[▶️ Tonton Video](https://youtu.be/FRnY3ZReGnM?si=9e668MZOm6Yh1ajK)"
        )


# =========================================================
# HALAMAN KUIS / LATIHAN
# =========================================================

elif st.session_state.menu == "Kuis / Latihan":

    st.title("📝 Kuis / Latihan Soal")
    st.write(
        "Uji pemahaman kamu melalui kuis dan latihan soal."
    )

    with st.container(border=True):
        st.markdown("### 🎯 Kuis")
        st.write("Kerjakan kuis untuk menguji pemahamanmu.")
        st.markdown(
            "[🚀 Mulai Kuis](https://play.blooket.com/play?id=488472)"
        )

    with st.container(border=True):
        st.markdown("### 📄 Latihan Soal")
        st.write("Buka dokumen latihan soal Bahasa Indonesia.")
        st.markdown(
            "[📖 Buka Latihan Soal](https://docs.google.com/document/d/1erD9R-nhl9_GgVOEAXQYQ3IH1GkzxkQe/edit?pli=1)"
        )


# =========================================================
# HALAMAN PENGUMPULAN TUGAS
# =========================================================

elif st.session_state.menu == "Pengumpulan Tugas":

    st.title("📤 Pengumpulan Tugas")
    st.write(
        "Gunakan Google Classroom untuk mengumpulkan tugas pembelajaran."
    )

    with st.container(border=True):
        st.markdown("### 📄 Pengumpulan Tugas")
        st.write(
            "Klik tombol berikut untuk membuka halaman pengumpulan tugas."
        )
        st.link_button(
            "📤 Buka Google Classroom",
            "https://classroom.google.com/c/ODczODc3NTc0MjQ1?cjc=x7nzkr5k",
            use_container_width=True
        )


# =========================================================
# HALAMAN TENTANG KAMI
# =========================================================

elif st.session_state.menu == "Tentang Kami":

    st.write("")
    st.markdown("# 👥 Tentang Kami")
    st.write("Tim Pengembang AI Tutor Bahasa Indonesia")
    st.write("")

    anggota = [
        ("👩‍💻", "Claudia Ratna"),
        ("👩‍💻", "Ezra Natasya"),
        ("👨‍💻", "Kevin Pardede"),
        ("👨‍💻", "Samuel Simamora"),
        ("👩‍💻", "Siti Fadilah"),
        ("👩‍💻", "Yasinta Theresya"),
    ]

    for awal in range(0, len(anggota), 3):
        cols = st.columns(3)
        for kolom, (ikon, nama) in zip(cols, anggota[awal:awal + 3]):
            with kolom:
                with st.container(border=True):
                    st.markdown(f"## {ikon}")
                    st.markdown(f"### {nama}")
                    st.caption("Anggota Tim")
                    st.write("Program Studi PBSI D 2023")


# =========================================================
# HALAMAN AI TUTOR
# NAVBAR TIDAK DITAMPILKAN DI HALAMAN INI
# =========================================================

elif st.session_state.menu == "AI Tutor":

    if st.button("← Kembali ke Beranda", key="kembali_ai", use_container_width=False):
        pilih_menu("Beranda")
        st.rerun()

    st.write("")

    # Header AI Tutor menggunakan komponen Streamlit
    with st.container(border=True):
        st.markdown("# 🤖")
        st.title("AI Tutor Bahasa Indonesia")
        st.write(
            "Tanyakan apa saja tentang materi Bahasa Indonesia "
            "berdasarkan database pembelajaran."
        )

    st.write("")

    # Form pertanyaan
    with st.container(border=True):
        st.subheader("💬 Tanyakan Sesuatu")
        st.write(
            "Masukkan pertanyaanmu. AI Tutor akan mencari materi "
            "yang paling relevan dari database."
        )

        pertanyaan = st.text_area(
            "Masukkan pertanyaan Anda:",
            placeholder="Contoh: Apa tujuan utama teks prosedur?",
            height=140,
            key="pertanyaan_ai"
        )

        tombol = st.button(
            "🔍 TANYAKAN",
            key="btn_tanyakan_ai",
            use_container_width=True
        )

    if tombol:

        if pertanyaan.strip() == "":
            st.warning(
                "Silakan masukkan pertanyaan terlebih dahulu."
            )

        elif len(database) == 0:
            st.error(
                "Database TXT belum ditemukan."
            )

        else:
            with st.spinner("Sedang mencari materi..."):
                hasil = cari_materi(
                    pertanyaan,
                    database
                )

            if len(hasil) > 0:
                hasil_utama = hasil[0]

                st.success(
                    "Materi yang paling relevan ditemukan."
                )

                with st.container(border=True):
                    st.subheader("💡 Jawaban")

                    jawaban = ambil_potongan_relevan(
                        pertanyaan,
                        hasil_utama["isi"],
                        database=database
                    )

                    st.info(jawaban)

                with st.container(border=True):
                    st.subheader("📚 Sumber Materi")
                    st.write(
                        f"**{hasil_utama['nama_file']}**"
                    )

                skor_utama = hasil_utama["skor"]
                terkait = [
                    item for item in hasil[1:4]
                    if item["skor"] >= max(35, int(skor_utama * 0.60))
                ]

                if terkait:
                    st.subheader("📑 Materi Terkait")
                    for item in terkait:
                        potongan = ambil_potongan_relevan(
                            pertanyaan,
                            item["isi"],
                            800,
                            database
                        )
                        if potongan:
                            with st.expander(item["nama_file"]):
                                st.write(potongan)

            else:
                st.warning(
                    "Maaf, materi yang Anda tanyakan belum ditemukan dalam database."
                )
                st.info(
                    "Coba gunakan kata kunci yang lebih spesifik, "
                    "misalnya nama materi atau istilah penting."
                )


# =========================================================
# FOOTER
# =========================================================

st.divider()
st.caption(
    "AI Tutor Bahasa Indonesia | Python + Streamlit + TXT Knowledge Base"
)