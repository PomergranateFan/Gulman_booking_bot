from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.types.message import ContentType


from handlers.register_new_booking import (BookingStates,
                                        start,
                                        start_booking,
                                        process_name,
                                        process_email,
                                        process_check_in,
                                        process_check_out,
                                        )


def register_all_handlers(dp: Dispatcher):
    handle_register_new_user(dp)


def handle_register_new_user(dp : Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(start_booking, Text(equals='New booking'))
    dp.register_message_handler(process_name, state=BookingStates.waiting_for_name)
    dp.register_message_handler(process_email, state=BookingStates.waiting_for_email)
    dp.register_message_handler(process_check_in, state=BookingStates.waiting_for_check_in)
    dp.register_message_handler(process_check_out, state=BookingStates.waiting_for_check_out)
