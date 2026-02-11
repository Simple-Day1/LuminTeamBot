from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📊 Прогресс"), KeyboardButton(text="🎨 Галерея")],
        [KeyboardButton(text="🎬 Бэкстейдж"), KeyboardButton(text="ℹ️ О нас")]
    ],
    resize_keyboard=True
)


def categories_kb(categories: list, prefix: str) -> InlineKeyboardMarkup:
    buttons = []
    for cat in categories:
        buttons.append([InlineKeyboardButton(
            text=cat,
            callback_data=f"{prefix}_cat:{cat}"
        )])
    buttons.append([InlineKeyboardButton(text="◀️ Назад", callback_data="back_to_main")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)
