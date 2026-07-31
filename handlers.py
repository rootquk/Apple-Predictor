from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
import random

from keyboards import main_menu, predict_keyboard

router = Router()

# أمر /start
@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "👋 أهلاً وسهلاً بك في Apple Predictor Bot!\n\n"
        "هذا البوت يقدم توقعات عشوائية للمحاكاة والترفيه فقط.\n\n"
        "اختر من القائمة بالأسفل:",
        reply_markup=main_menu
    )

# عند الضغط على Apple Predictor
@router.message(F.text == "🍎 Apple Predictor")
async def predictor_menu(message: Message):
    await message.answer(
        "اضغط الزر بالأسفل للحصول على توقع عشوائي.",
        reply_markup=predict_keyboard
    )

# توليد التوقع
@router.callback_query(F.data == "generate_prediction")
async def generate_prediction(callback: CallbackQuery):
    predictions = [
        "🍎🍎🍎💣🍎",
        "🍎🍎💣🍎🍎",
        "🍎💣🍎🍎🍎",
        "💣🍎🍎🍎🍎",
        "🍎🍎🍎🍎💣"
    ]

    result = random.choice(predictions)

    await callback.message.answer(
        f"🎯 التوقع:\n\n{result}\n\n"
        "⚠️ هذا التوقع عشوائي وللمحاكاة فقط."
    )

    await callback.answer()
