from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# القائمة الرئيسية
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🍎 Apple Predictor")],
        [KeyboardButton(text="📊 Last Results"), KeyboardButton(text="ℹ️ Help")],
    ],
    resize_keyboard=True
)

# زر بدء التوقع
predict_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🎯 Generate Prediction",
                callback_data="generate_prediction"
            )
        ]
    ]
)

# زر الرجوع
back_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="⬅️ Back",
                callback_data="back_menu"
            )
        ]
    ]
)
