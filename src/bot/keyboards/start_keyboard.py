from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from src.bot.keyboards.base_keyboard import BaseKeyboard


class StartKB(BaseKeyboard):
    def create__reply_start_keyboard(self):
        self.reply_kb = [
            [KeyboardButton(text='Текст кнопки 1'), KeyboardButton(text='Текст кнопки 2')],
            [KeyboardButton(text='Текст кнопки 3')]
        ]
        return ReplyKeyboardMarkup(keyboard=self.reply_kb,
                                   resize_keyboard=True,
                                   input_field_placeholder='placeholder',
                                   one_time_keyboard=True)


start_kb = StartKB()
