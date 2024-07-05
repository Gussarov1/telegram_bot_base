import asyncio
from os import getenv

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import register_handlers
from scheduler import schedule_jobs, scheduler
from logging_config import setup_logging

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

setup_logging()

dp = Dispatcher()

async def main() -> None:
    """
    Main function to initialize the bot and start handlers
    """
    bot = Bot(token=TOKEN)

    register_handlers(dp)

    asyncio.create_task(schedule_jobs(bot))
    asyncio.create_task(scheduler())

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())