from aiogram import Router, types
from aiogram.filters import Command
from LuminTeamBot.keyboards.main_menu import main_menu_kb

start_router = Router()


@start_router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "<b>Добро пожаловать в игру!</b>\n\n"
        "Я — официальный бот разработки. Здесь вы можете:\n"
        "• узнать текущий прогресс создания игры 📊\n"
        "• посмотреть концепт-арты 🎨\n"
        "• заглянуть за кулисы разработки 🎬\n"
        "• получить информацию о нас ℹ️\n\n"
        "Выберите раздел в меню ниже 👇",
        reply_markup=main_menu_kb,
        parse_mode="HTML"
    )
