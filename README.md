# Hotel Booking Bot

## Description

This is a Telegram bot for hotel booking. It allows users to book rooms for a specific period.

## Requirements

This project uses the following packages:

* aiogram
* pymongo
* loguru

##  How to use:

You can install libs via pip:

Copy code: 
* `pip install aiogram pymongo loguru`


Start the bot:
Copy code:
* `python3 main.py`
## Interact with the bot via Telegram.
Use the following commands to interact with the bot:
* `/start` - starts the bot and shows previous bookings if any.

## States

The bot uses the aiogram.dispatcher.filters.state module to keep track of the user's progress in the booking process. The following states are used:

* `BookingStates.waiting_for_name` - waiting for the user's name.
* `BookingStates.waiting_for_email` - waiting for the user's email address.
* `BookingStates.waiting_for_check_in` - waiting for the user's check-in date.
* `BookingStates.waiting_for_check_out` - waiting for the user's check-out date.

## Regex

The bot uses regular expressions to validate user input. The following regex patterns are used:

* `r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'` - validates email addresses.

* `r'^\d{2}-\d{2}-\d{4}$'` - validates date strings in the format DD-MM-YYYY.

## Database

The bot uses a MongoDB database to store booking data. The `database.py` module handles database connection and data insertion.

## Keyboard

The bot uses a custom keyboard with the following options:

* Start - create new booking or check your previous booking(if you have same) 
* New booking(if you press /start and want to create new booking 

The `keyboards.py` module handles keyboard creation.
