import os
from aiogram import Router, types, F
from aiogram.filters import Command, or_f
from aiogram.types import FSInputFile
from LuminTeamBot.config import GALLERY_DIR
from LuminTeamBot.services.file_manager import get_categories, get_images_in_category
from LuminTeamBot.keyboards.main_menu import categories_kb


gallery_router = Router()


@gallery_router.message(or_f(Command("gallery"),
                     lambda msg: msg.text == "🎨 Галерея"))
async def show_gallery_menu(message: types.Message):
    categories = get_categories(GALLERY_DIR)
    if not categories:
        await message.answer("📁 Папка галереи пуста или не найдена.")
        return

    kb = categories_kb(categories, prefix="gallery")
    await message.answer(
        "<b>🖼 Галерея концепт-артов</b>\n\n"
        "Выберите категорию для просмотра:",
        reply_markup=kb,
        parse_mode="HTML"
    )


@gallery_router.callback_query(F.data.startswith("gallery_cat:"))
async def show_category_images(callback: types.CallbackQuery):
    category = callback.data.split(":", 1)[1]
    images = get_images_in_category(GALLERY_DIR, category)

    if not images:
        await callback.answer("В этой категории пока нет изображений.")
        return

    await callback.answer()

    for img_path in images:
        photo = FSInputFile(img_path)
        name = os.path.splitext(os.path.basename(img_path))[0]
        caption = f"<b>{category}</b>\n<i>{name}</i>"
        await callback.message.answer_photo(photo, caption=caption, parse_mode="HTML")