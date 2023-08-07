# Хендлер, обрабатывающий команду /start
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.bot.keyboards.start_keyboard import start_kb

router = Router()


# Базовый шаблон хендлера
@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer('Ответ бота на сообщение', reply_markup=start_kb.create__reply_start_keyboard())
