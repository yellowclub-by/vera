from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def addresses_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='address1', callback_data='addresses_1'),
        InlineKeyboardButton(text='address2', callback_data='addresses_2'),
        InlineKeyboardButton(text='address3', callback_data='addresses_3'),
        width=1
    )
    return builder.as_markup()



