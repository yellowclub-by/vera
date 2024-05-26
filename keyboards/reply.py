from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Catalog'),
            KeyboardButton(text='About')
        ],
        [
            KeyboardButton(text='Contacts'),
            KeyboardButton(text='Addresses')
        ]

    ],
    resize_keyboard=True,
    input_field_placeholder='meow'

)


catalog_kb = ReplyKeyboardMarkup(
    keyboard=[
        [

            KeyboardButton(text='cactus'),
            KeyboardButton(text='mini cactus'),
            KeyboardButton(text='coloured cactus')
        ],
        [
            KeyboardButton(text='succulent'),
            KeyboardButton(text='ripsalis'),
            KeyboardButton(text='opuntia')
        ]
    ],
    resize_keyboard=True
)


