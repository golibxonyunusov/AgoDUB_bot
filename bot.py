import asyncio
import logging
import os

from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN, STUDIO_NAME
import database as db
from handlers import user, admin


# ---------------------------------------------------------------
# RENDER UCHUN MINIMAL HTTP SERVER
# ---------------------------------------------------------------
# Render'ning bepul "Web Service" rejasi ishlashi uchun konteyner
# ichida biror port tinglanishini talab qiladi, aks holda deploy
# "no open ports detected" xatosi bilan yiqiladi. Shu portga
# UptimeRobot ham har 5 daqiqada so'rov yuborib, xizmatni
# "uxlab qolishdan" saqlab turadi.
async def handle_health(request):
    return web.Response(text=f"{STUDIO_NAME} bot ishlayapti ✅")


async def run_web_server():
    app = web.Application()
    app.router.add_get("/", handle_health)
    app.router.add_get("/health", handle_health)

    runner = web.AppRunner(app)
    await runner.setup()

    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, host="0.0.0.0", port=port)
    await site.start()
    print(f"🌐 HTTP server {port}-portda ishga tushdi (Render/UptimeRobot uchun)")


async def main():
    logging.basicConfig(level=logging.INFO)

    if not BOT_TOKEN or BOT_TOKEN == "PASTE_YOUR_BOT_TOKEN_HERE":
        print("❗️ BOT_TOKEN to'g'ri kiritilmagan! Environment variable yoki config.py ni tekshiring.")
        return

    await db.init_db()

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())

    # Admin router birinchi ulanadi (admin tugmalari user routerdagi
    # umumiy matn handlerlaridan oldin ushlanishi uchun)
    dp.include_router(admin.router)
    dp.include_router(user.router)

    await bot.delete_webhook(drop_pending_updates=True)

    # HTTP server va Telegram polling parallel ishga tushadi
    await run_web_server()

    print(f"🍥 {STUDIO_NAME} bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi.")