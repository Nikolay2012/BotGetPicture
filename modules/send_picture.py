import modules.create_bot as m_bot
def send_picture(message):
    if message.text.lower() == 'get picture':
        m_bot.bot.send_photo(
            message.chat.id,
            "https://i.pinimg.com/736x/55/36/c8/5536c8edc514d16064a65f3e20d8e181.jpg"
        )
    m_bot.bot.register_next_step_handler(message, send_picture)