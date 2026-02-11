from aiogram import Router, types
from aiogram.filters import Command, or_f
from LuminTeamBot.keyboards.main_menu import main_menu_kb

info_router = Router()


@info_router.message(or_f(Command("info"),
                          lambda msg: msg.text == "ℹ️ О нас"))
async def show_info(message: types.Message):
    text = (
        "<b>🎮 Наша студия — «DreamForge»</b>\n\n"
        "Мы — команда инди-разработчиков из трёх человек, создаём уютную RPG с элементами "
        "головоломок. Наша цель — подарить игрокам тёплую атмосферу и интересные механики.\n\n"
        "📍 Основана в 2024 году\n"
        "👥 Состав: программист, художник, композитор\n"
        "🌐 Сайт: https://dreamforge.dev\n"
        "📧 Контакт: support@dreamforge.dev\n\n"
        "Спасибо, что интересуетесь нашим проектом! ❤️"
    )
    await message.answer(text, parse_mode="HTML", reply_markup=main_menu_kb)
