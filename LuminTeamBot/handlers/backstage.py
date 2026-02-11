import os
from aiogram import Router, types, F
from aiogram.filters import Command, or_f
from aiogram.types import FSInputFile
from LuminTeamBot.config import BACKSTAGE_DIR
from LuminTeamBot.services.file_manager import get_categories, get_images_in_category
from LuminTeamBot.keyboards.main_menu import categories_kb

backstage_router = Router()


@backstage_router.message(or_f(Command("backstage"),
                     lambda msg: msg.text == "🎬 Бэкстейдж"))
async def show_backstage_menu(message: types.Message):
    categories = get_categories(BACKSTAGE_DIR)
    if not categories:
        await message.answer("📁 Папка бэкстейджей пуста или не найдена.")
        return

    kb = categories_kb(categories, prefix="backstage")
    await message.answer(
        "<b>🎬 Закулисье разработки</b>\n\n"
        "Фото и моменты, оставшиеся за кадром:",
        reply_markup=kb,
        parse_mode="HTML"
    )


@backstage_router.callback_query(F.data.startswith("backstage_cat:"))
async def show_backstage_images(callback: types.CallbackQuery):
    category = callback.data.split(":", 1)[1]
    images = get_images_in_category(BACKSTAGE_DIR, category)

    if not images:
        await callback.answer("В этой категории пока нет материалов.")
        return

    await callback.answer()

    for img_path in images:
        photo = FSInputFile(img_path)
        name = os.path.splitext(os.path.basename(img_path))[0]
        caption = (
            f"<b>{category}</b>\n"
            f"📸 <i>{name}</i>\n"
            f"🗓 Дата: 2025-03-15\n"
            f"✏️ Автор: Команда разработки"
        )
        await callback.message.answer_photo(photo, caption=caption, parse_mode="HTML")