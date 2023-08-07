# Главный файл запуска бота
import asyncio
import logging

from aiogram import Dispatcher, Bot

from src import conf
from src.bot.handlers import start_handler, user_handlers
from src.bot.keyboards.base_keyboard import BotMainMenu
from src.bot.middlewares.base_middleware import Middleware
from src.db.database import async_engine, create_session_maker


# Функция запуска бота
async def start_bot():
    bot: Bot = Bot(token=conf.bot.token, parse_mode='HTML')

    # Создание главного меню с коиандами бота
    main_menu = BotMainMenu(bot)
    await main_menu.create_main_menu()

    dp: Dispatcher = Dispatcher()

    # инитиализируем middleware для всех хендлеров
    dp.message.middleware(Middleware())
    dp.callback_query.middleware(Middleware())

    # инициализация хендлеров
    dp.include_router(start_handler.router)
    dp.include_router(user_handlers.router)

    # Запуск сессии для базы данных и передача сессии в бота
    engine = async_engine(url=conf.db.build_database_url())
    session_maker = create_session_maker(engine=engine)

    # Удаление обновлений после перезапуска бота
    await bot.delete_webhook(drop_pending_updates=True)

    # запуск бота
    await dp.start_polling(bot, session_maker=session_maker)


if __name__ == '__main__':
    logging.basicConfig(level=conf.logging.logging_level)
    asyncio.run(start_bot())
