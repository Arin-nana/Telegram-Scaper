from scripts.fetch_messages import fetch_messages
from scripts.session_starter import create_session

if __name__ == "__main__":
    # Запускаем создание сессии и получаем строку сессии
    session_string = create_session('+79122714210')
    if session_string:
        # Сохраняем строку сессии в файл для последующего использования
        with open('session_string.txt', 'w') as file:
            file.write(session_string)

        n_hours = 1  # Укажите количество часов
        channel = r'https://t.me/tb_invest_official'  # Укажите канал или чат

        # Чтение строки сессии из файла
        with open('session_string.txt', 'r') as file:
            session_string = file.read()

        # Использование строки сессии для извлечения сообщений
        messages = fetch_messages(n_hours, channel, session_string)
        for msg in messages:
            print(msg)
