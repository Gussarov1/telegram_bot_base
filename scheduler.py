import logging
import aioschedule as schedule
import asyncio
from os import getenv
from aiogram import Bot


async def scheduled_task(bot: Bot, chat_id: int, message_text: str) -> None:
    """
    Example of a scheduled task
    """
    try:
        await bot.send_message(chat_id, message_text)
    except Exception as e:
        logging.error(f"Failed to send message: {e}")


async def schedule_jobs(bot: Bot) -> None:
    """
    Configure scheduled tasks
    """
    # Example schedule for multiple chats
    schedule.every().day.at("12:00").do(scheduled_task, bot, getenv("CHAT_ID_1"), "Daily message for chat 1")
    schedule.every().day.at("12:05").do(scheduled_task, bot, getenv("CHAT_ID_2"), "Daily message for chat 2")
    schedule.every(1).minutes.do(scheduled_task, bot, getenv("CHAT_ID"), "Message every minute")


def add_schedule(bot: Bot, chat_id: int, time: str, message_text: str) -> None:
    """
    Add a new scheduled task
    """
    schedule.every().day.at(time).do(scheduled_task, bot, chat_id, message_text)
    logging.info(f"Scheduled new task for chat {chat_id} at {time} with message: {message_text}")


async def scheduler() -> None:
    """
    Run the scheduled tasks
    """
    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)
