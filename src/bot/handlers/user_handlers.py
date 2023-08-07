# Шаблон хендлера
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from src.bot.keyboards.user_keyboards import user_keyboards

router = Router()


@router.message(F.text == 'Текст кнопки 1')
async def answer_on_button_1(message: Message):
    await message.answer('Ответ на нажатие кнопки 1',
                         reply_markup=user_keyboards.create_inline_keyboard_on_button_1())


@router.callback_query(lambda c: c.data == 'test_inline')
async def answer_on_inline_button_1(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Ответ на нажатие инлайн кнопки 1')
