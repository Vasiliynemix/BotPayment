from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.bot.keyboards.base_keyboard import BaseKeyboard


class UserKeyboards(BaseKeyboard):
    def create_inline_keyboard_on_button_1(self):
        self.inline_kb = InlineKeyboardBuilder()
        self.inline_kb.button(text='Тест инлайн кнопки', callback_data='test_inline')
        self.inline_kb.adjust(2)
        return self.inline_kb.as_markup(resize_keyboard=True,
                                        one_time_keyboard=True)


user_keyboards = UserKeyboards()
