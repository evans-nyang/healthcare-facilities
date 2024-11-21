from aiogram import Bot, Dispatcher, Router, F
from aiogram.enums import ParseMode, ChatAction
from aiogram.types import CallbackQuery, Message
import uuid
import logging

from rag import rag
from db import init_db, save_conversation, save_feedback
# from utils.logger import logger  # Assuming you've set up a logger
from keyboards import get_feedback_keyboard, get_disabled_feedback_keyboard

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize bot and dispatcher
router = Router()
bot = Bot(token="YOUR_BOT_TOKEN_HERE")
dp = Dispatcher(bot)

# Initialize database on startup
@dp.startup
async def on_startup():
    try:
        logger.info("Initializing database...")
        init_db()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Error initializing database: {str(e)}")
        raise RuntimeError("Database initialization failed")

# Handle /start command
@router.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer(
        "Hello! I'm here to answer questions. Just ask me anything!",
        parse_mode=ParseMode.MARKDOWN,
    )

# Handle questions
@router.message(F.text)
async def ask_question(message: Message):
    question = message.text
    user_id = message.from_user.id

    if not question:
        await message.answer("Please provide a question.")
        return

    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)

    try:
        # Generate the answer with the RAG function
        answer_data = rag(question)
        
        # Generate a unique conversation ID (UUID)
        conversation_id = str(uuid.uuid4())

        # Save the conversation in the database
        save_conversation(
            conversation_id=conversation_id,
            question=question,
            answer_data=answer_data
        )

        # Respond with the answer and feedback options
        await message.answer(
            answer_data["answer"],
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_feedback_keyboard(conversation_id)
        )

        logger.info(f"Question processed for user {user_id}, conversation ID: {conversation_id}")

    except Exception as e:
        logger.error(f"Error processing question for user {user_id}: {str(e)}")
        await message.answer("Sorry, an error occurred while processing your question.")

# Handle feedback callback
@router.callback_query(F.data.startswith("feedback:"))
async def handle_feedback(callback_query: CallbackQuery):
    _, conversation_id, feedback = callback_query.data.split(":")
    is_positive = feedback == "positive"
    user_id = callback_query.from_user.id

    logger.info(f"Received feedback from user {user_id} for conversation {conversation_id}: {feedback}")

    try:
        # Save feedback in the database
        save_feedback(conversation_id, 1 if is_positive else -1)
        
        response = (
            "👍 Thank you for your positive feedback!"
            if is_positive
            else "👎 Thank you for your feedback. We'll try to improve!"
        )

        # Update the feedback button to disabled
        await callback_query.message.edit_reply_markup(
            reply_markup=get_disabled_feedback_keyboard(feedback)
        )

        await callback_query.answer(response)

        logger.info(f"Feedback processed successfully for user {user_id}, conversation {conversation_id}")

    except Exception as e:
        logger.error(f"Error saving feedback for user {user_id}, conversation {conversation_id}: {str(e)}")
        await callback_query.answer("Sorry, there was an error processing your feedback.")

# Handle already disabled feedback
@router.callback_query(F.data == "disabled")
async def handle_disabled_feedback(callback_query: CallbackQuery):
    await callback_query.answer("You've already provided feedback for this response.")

# Run the bot
if __name__ == "__main__":
    dp.include_router(router)
    dp.start_polling(bot)
