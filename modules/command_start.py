import modules.create_bot as m_bot
import modules.create_keyboard_get_picture as m_c_key_get_picture
import modules.send_picture as m_send_picture

@m_bot.bot.message_handler(commands=["start"])
def bot_start(message):
    m_bot.bot.send_message(
        message.chat.id, # 
        "Hello, user!", # 
        reply_markup= m_c_key_get_picture.keyboard_get_picture #
    )
    m_bot.bot.register_next_step_handler(message, m_send_picture.send_picture)