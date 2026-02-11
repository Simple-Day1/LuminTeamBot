import os
from aiogram import Router, types
from aiogram.filters import Command, or_f
from aiogram.types import FSInputFile
from LuminTeamBot.config import PROGRESS_IMAGE

progress_router = Router()


@progress_router.message(or_f(Command("progress"), 
                              lambda msg: msg.text == "📊 Прогресс"))
async def show_progress(message: types.Message):
    if os.path.exists(PROGRESS_IMAGE):
        photo = FSInputFile(PROGRESS_IMAGE)
        caption = (
            "<b>Текущий прогресс разработки</b>\n\n"
            "• Геймплей: 75%\n"
            "• Арт: 60%\n"
            "• Звук: 40%\n"
            "• Оптимизация: 30%\n\n"
            "✨ Примерная дата релиза: декабрь 2025"
        )
        await message.answer_photo(photo, caption=caption, parse_mode="HTML")
    else:
        await message.answer("❌ Изображение прогресса временно недоступно.")