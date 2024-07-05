from aiogram import Dispatcher, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from scheduler import add_schedule


def register_handlers(dp: Dispatcher) -> None:
    @dp.message(CommandStart())
    async def command_start_handler(message: Message) -> None:
        """
        This handler receives messages with the `/start` command
        """
        await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

    @dp.message(Command(commands=['id']))
    async def command_id_handler(message: Message) -> None:
        """
        This handler receives messages with the `/id` command and returns the chat ID
        """
        chat_id = message.chat.id
        await message.answer(f"Chat ID: {chat_id}")

    @dp.message(Command(commands=['schedule']))
    async def command_schedule_handler(message: Message) -> None:
        """
        This handler receives messages with the `/schedule` command and adds a new scheduled task
        """
        args = message.get_args().split()
        if len(args) != 2:
            await message.answer("Usage: /schedule <time> <message>")
            return

        time, text = args
        chat_id = message.chat.id
        add_schedule(dp.bot, chat_id, time, text)
        await message.answer(f"Scheduled message '{text}' at {time} for chat {chat_id}")

    @dp.message()
    async def echo_handler(message: Message) -> None:
        """
        This handler will forward received messages back to the sender
        """
        try:
            await message.send_copy(chat_id=message.chat.id)
        except TypeError:
            await message.answer("Nice try!")
