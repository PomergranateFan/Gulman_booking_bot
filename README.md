Hotel Booking Bot

This is a Telegram bot for hotel booking. It allows users to book rooms for a specific period.

Requirements

This project uses the following packages:

aiogram
PyMySQL
You can install them via pip:

Copy code
pip install aiogram pymysql
Usage

Start the bot by running create_bot.py:
Copy code
python create_bot.py
Interact with the bot via Telegram.
Use the following commands to interact with the bot:
/start - starts the bot and shows previous bookings if any.
/book - starts the booking process.
/cancel - cancels the current booking process.
States

The bot uses the aiogram.dispatcher.filters.state module to keep track of the user's progress in the booking process. The following states are used:

BookingStates.waiting_for_name - waiting for the user's name.
BookingStates.waiting_for_email - waiting for the user's email address.
BookingStates.waiting_for_check_in - waiting for the user's check-in date.
BookingStates.waiting_for_check_out - waiting for the user's check-out date.
Regex

The bot uses regular expressions to validate user input. The following regex patterns are used:

r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' - validates email addresses.
r'^\d{2}-\d{2}-\d{4}$' - validates date strings in the format DD-MM-YYYY.
Database

The bot uses a MySQL database to store booking data. The database.py module handles database connection and data insertion.

Keyboard

The bot uses a custom keyboard with the following options:

Book - starts the booking process.
Cancel - cancels the current booking process.
The keyboards.py module handles keyboard creation.
