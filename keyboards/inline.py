from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def addresses_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Address 1', callback_data='addresses_1'),
        InlineKeyboardButton(text='Address 2', callback_data='addresses_2'),
        InlineKeyboardButton(text='Address 3', callback_data='addresses_3'),
        width=1
    )
    return builder.as_markup()


links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='website', url='https://cactus.by/'),
            InlineKeyboardButton(text='Telegram', url='tg://resolve?domain=kaktus_mediakg')
        ]
    ]
)


def contacts_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Our Instagram', callback_data='contact_1'),
        InlineKeyboardButton(text='Number', callback_data='contact_2'),
        width=1
    )
    return builder.as_markup()




