import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from handlers.start import start_router
from handlers.progress import progress_router
from handlers.gallery import gallery_router
from handlers.backstage import backstage_router
from handlers.info import info_router
from handlers.callbacks import callback_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(start_router)
    dp.include_router(progress_router)
    dp.include_router(gallery_router)
    dp.include_router(backstage_router)
    dp.include_router(info_router)
    dp.include_router(callback_router)

    logger.info("Бот запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
