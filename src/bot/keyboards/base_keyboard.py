# базовый класс создания клавиатуры
from aiogram import Bot
from aiogram.types import BotCommand

from src import conf
from src.bot.lexicon.lexicon_ru import lexicon


class BaseKeyboard:
    def __init__(self):
        self.reply_kb = None
        self.inline_kb = None


class BotMainMenu:
    def __init__(self, bot: Bot):
        self.bot = bot

    async def create_main_menu(self):
        commands_for_bot = [BotCommand(command=cmd,
                                       description=desc)
                            for cmd, desc in lexicon.menu.MAIN_MENU_COMMANDS.items()]

        await self.bot.set_my_commands(commands=commands_for_bot)
