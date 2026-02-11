from aiogram import Router, types, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from LuminTeamBot.keyboards.main_menu import main_menu_kb

callback_router = Router()


@callback_router.callback_query(F.data == "back_to_main")
async def back_to_main(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer()
    await callback.message.answer(
        "Вы вернулись в главное меню.",
        reply_markup=main_menu_kb
    )
