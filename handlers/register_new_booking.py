from random import random
from aiogram import Dispatcher, types
from create_bot import bot
from keyboards import kb_register
from aiogram.dispatcher.filters import Text
import re
import datetime
from database import insert_record, get_records_with_tg_id
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class BookingStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_email = State()
    waiting_for_check_in = State()
    waiting_for_check_out = State()

async def start(message: types.Message):
    bookings = []
    booking_list = get_records_with_tg_id(message.from_user.id)
    for booking in booking_list:
        bookings.append(booking)
        
    if bookings == []:
        await BookingStates.waiting_for_name.set()
        await bot.send_message(message.from_user.id, "Welcome to the hotel booking bot!\nPlease enter your name.", reply_markup=types.ReplyKeyboardRemove())
    else:
        message_data = ''
        for data in bookings:
            name = data['name']
            email = data['email']
            check_in = data['check_in']
            check_out = data['check_out']
            message_data += f'Name: {name}\nEmail: {email}\nCheck-in: {check_in}\nCheck-out: {check_out}\n\n'
        await bot.send_message(message.from_user.id, f"We have some of your bookings in our batabase:\n\n{message_data}\n\nDo you want to create new booking?", reply_markup=kb_register)
        print(bookings)
        
async def start_booking(message: types.Message):
    await BookingStates.waiting_for_name.set()
    await bot.send_message(message.from_user.id, "Please enter your name.", reply_markup=types.ReplyKeyboardRemove())

async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await BookingStates.next()
    await bot.send_message(message.from_user.id, "Please enter your email address.")

async def process_email(message: types.Message, state: FSMContext):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, message.text):
        await bot.send_message(message.from_user.id, "Please, send correct email address")
        return
    async with state.proxy() as data:
        data['email'] = message.text
    await BookingStates.next()
    await bot.send_message(message.from_user.id, "Please enter your check-in date (DD-MM-YYYY).")

async def process_check_in(message: types.Message, state: FSMContext):
    date_regex = r'^\d{2}-\d{2}-\d{4}$'
    if not re.match(date_regex, message.text):
        await bot.send_message(message.from_user.id, "Please, send correct check-in date")
        return
    async with state.proxy() as data:
        data['check_in'] = message.text
        data['tg_id'] = message.from_user.id
    await BookingStates.next()
    await bot.send_message(message.from_user.id, "Please enter your check-out date (DD-MM-YYYY).")

async def process_check_out(message: types.Message, state: FSMContext):
    date_regex = r'^\d{2}-\d{2}-\d{4}$'
    if not re.match(date_regex, message.text):
        await bot.send_message(message.from_user.id, "Please, send correct check-out date")
        return
    
    date_format = '%d-%m-%Y'
    data = await state.get_data()
    date1 = datetime.datetime.strptime(data['check_in'], date_format)
    date2 = datetime.datetime.strptime(message.text, date_format)
    if date1 > date2:
        await bot.send_message(message.from_user.id, "Please, send correct check-out date (after check-in date)")
        return
    
    async with state.proxy() as data:
        data['check_out'] = message.text
    insert_record(await state.get_data())
    # Process the booking
    async with state.proxy() as data:
        name = data['name']
        email = data['email']
        check_in = data['check_in']
        check_out = data['check_out']
        # Можно добавить логику с бронированиями
        booking_details = f"Booking details:\nName: {name}\nEmail: {email}\nCheck-in: {check_in}\nCheck-out: {check_out}"
        await bot.send_message(message.from_user.id, "Thank you for booking!\nHere are your booking details:\n" + booking_details)
        await bot.send_message(message.from_user.id, "Our consultant will call you back for confirmation and payment")
    await state.finish()