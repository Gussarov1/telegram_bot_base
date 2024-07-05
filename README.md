# Telegram Bot with Scheduled Tasks - Starter Template

This project is a basic template for creating a Telegram bot using the `aiogram` library. The bot can handle basic commands, echo messages, and perform scheduled tasks using the `aioschedule` library. This template serves as a starting point for developers to build their own Telegram bots with additional functionality.

## Features

- Responds to the `/start` command with a greeting message.
- Responds to the `/id` command with the chat ID.
- Echoes back any received messages.
- Schedules tasks to send messages to specified chats at specified times.
- Allows adding new scheduled tasks via the `/schedule` command.

## Requirements

- Python 3.7+
- Telegram bot token from [BotFather](https://t.me/BotFather)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Gussarov1/telegram_bot_base.git
   cd telegram_bot_base
   ```
   
2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
4. Create a .env file in the root directory of the project and add your Telegram bot token and chat IDs:
    ```env
    BOT_TOKEN=your_bot_token_here
    CHAT_ID=your_chat_id_here
    CHAT_ID_1=your_chat_id_1
    CHAT_ID_2=your_chat_id_2
    LOGGING_LEVEL=DEBUG
    ```

## Usage

1. Run the bot:
    ```sh
    python bot.py
    ```

2. Interact with the bot on Telegram: 
   - Send /start to receive a greeting message.
   - Send /id to get the chat ID.
   - Send any message to have it echoed back to you.
   - Send /schedule <time> <message> to add a new scheduled task. The <time> should be in HH:MM format.

## Project Structure

- bot.py: Main entry point of the bot. Initializes the bot and starts the event loop.
- handlers.py: Contains all the command and message handlers.
- scheduler.py: Manages the scheduling of tasks.
- logging_config.py: Configures logging for the project.
- README.md: Project documentation.

## Logging Configuration

Logging is configured to separate logs based on their severity levels:

-	Logs with levels below ERROR are written to stdout.
-	Logs with level ERROR and above are written to stderr.

You can set the logging level via the LOGGING_LEVEL environment variable in the .env file.

## Customization

This template provides a basic structure for a Telegram bot. You can customize and extend the functionality by:

-	Adding new command and message handlers in handlers.py.
-	Defining additional scheduled tasks in scheduler.py.
-	Configuring different logging settings in logging_config.py.

## Contributing

1.	Fork the repository.
2.	Create a new branch
    ```sh
    git checkout -b feature-branch
    ```

3.	Commit your changes 
    ```
    git commit -am 'Add new feature'
    ```

4.	Push to the branch 
    ```
    git push origin feature-branch
    ```

5.	Create a new Pull Request.