from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Fronted"), KeyboardButton(text="Bakent"), KeyboardButton(text="Aloqa")]
    ],
)

html = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="HTML"),KeyboardButton(text="CSS")]
    ],
)

fron = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="PYTHON"), KeyboardButton(text="JAVASCRIPT"), KeyboardButton(text="C++")]
    ],
    resize_keyboard=True
)
Html=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1-dars"),KeyboardButton(text="2-dars"),KeyboardButton(text="5-dars"),KeyboardButton(text="6-dars"),KeyboardButton(text="7-dars")],
        [KeyboardButton(text="3-dars"),KeyboardButton(text="4-dars"),KeyboardButton(text="8-dars"),KeyboardButton(text="9-dars"),KeyboardButton(text="10-dars")],
    ],
)

csss = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1 -dars"),KeyboardButton(text="2 -dars"),KeyboardButton(text="5 -dars"),KeyboardButton(text="6 -dars"),KeyboardButton(text="7 -dars")],
        [KeyboardButton(text="3 -dars"),KeyboardButton(text="4 -dars"),KeyboardButton(text="8 -dars"),KeyboardButton(text="9 -dars")],
    ],
)

pyton = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1 - dars"),KeyboardButton(text="2 - dars"),KeyboardButton(text="3 - dars"),KeyboardButton(text="4 - dars"),KeyboardButton(text="5 - dars")]
    ],
)

java = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1--dars"),KeyboardButton(text="2--dars"),KeyboardButton(text="5--dars"),KeyboardButton(text="6--dars"),KeyboardButton(text="7 -dars")],
        [KeyboardButton(text="3--dars"),KeyboardButton(text="4--dars"),KeyboardButton(text="8--dars"),KeyboardButton(text="9--dars"),KeyboardButton(text="10--dars")],
    ],
)

ccc = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1-Dars"),KeyboardButton(text="2-Dars"),KeyboardButton(text="3-Dars"),KeyboardButton(text="4-Dars"),KeyboardButton(text="5-Dars")],
        [KeyboardButton(text="6-Dars"),KeyboardButton(text="7-Dars")],
    ],
)


