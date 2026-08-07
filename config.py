# ============================================================
#  EgoDUBING Bot — Konfiguratsiya
# ============================================================
# 1) BOT_TOKEN endi shu faylga emas, Render'dagi "Environment"
#    bo'limiga kiritiladi (xavfsizlik uchun). Lokalda ishga
#    tushirish uchun terminalda quyidagini yozing:
#      export BOT_TOKEN="123456:ABC..."   (Linux/Mac)
#      set BOT_TOKEN=123456:ABC...        (Windows)
# 2) O'zingizning Telegram ID raqamingizni ADMIN_IDS ro'yxatiga qo'shing
#    (ID ni bilmasangiz @userinfobot ga /start yozing)
# ============================================================
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8977994406:AAF1AYuiR3gKJeQ84JzsR3Ji4Hx17eLycz0")

ADMIN_IDS = [
    8888728779,  # <-- shu yerga o'z Telegram ID raqamingizni yozing
]

DB_NAME = "uzumdub.db"

STUDIO_NAME = "EgoDUBING"

# Bosh menyudagi banner matni (ixtiyoriy, /start da chiqadi)
WELCOME_TEXT = (
    "🍥 <b>{studio}</b> ga xush kelibsiz!\n\n"
    "Bu yerda siz sevimli animelaringizni o'zbek tilidagi dublyajda "
    "topishingiz mumkin.\n\n"
    "🔎 Anime nomi yoki <b>ID</b> raqami orqali qidiring\n"
    "📋 Barcha animelar ro'yxatini ko'ring\n"
    "⭐ Sevimlilarga qo'shib qo'ying\n\n"
    "Quyidagi tugmalardan birini tanlang 👇"
)

# Har bir sahifada nechta anime/qism ko'rsatilsin
ANIME_PER_PAGE = 6
EPISODES_PER_PAGE = 12