import modules.create_bot as m_bot
import modules.downloads_image as m_load_img

def send_picture(message):
    if message.text.lower() == 'get picture':
        #знаходимо абсолютний шлях до файлу в папці images
        file_path = m_load_img.search_path("images/2.jpeg")
        # Бот відправляе повідомлення користувачеві, як фото
        m_bot.bot.send_photo(
            message.chat.id,
            open(file_path, "rb"), # Відкриваємо файл за абсолютним шляхом, який збережено в file_path
            "Горнятко кави!"
        )
    m_bot.bot.register_next_step_handler(message, send_picture)