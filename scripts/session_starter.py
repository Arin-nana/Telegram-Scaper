from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Замените эти строки вашими данными
API_ID = 25997160  # Ваш настоящий API ID здесь
API_HASH = 'a52e3a0c9dadaf6a42533ee09c7638de'  # Ваш настоящий API Hash здесь
PHONE_NUMBER = '+79122714210'  # Ваш номер телефона


def create_session(phone_number):
    session = StringSession()
    client = TelegramClient(session, API_ID, API_HASH)

    # Начало сессии
    print("Начало сессии")
    client.start(phone=phone_number)

    if not client.is_user_authorized():
        print("Клиент не авторизован. Отправка кода подтверждения.")
        client.send_code_request(phone_number)
        try:
            code = input('Введите код подтверждения: ')
            client.sign_in(phone_number, code)
            print("Код подтверждения введен")
        except Exception as e:
            print(f"Ошибка при вводе кода: {e}")
            return None

    if not client.is_user_authorized():
        try:
            print("Запрос пароля.")
            password = input('Введите ваш пароль: ')
            client.sign_in(password=password)
            print("Пароль введен")
        except Exception as e:
            print(f"Ошибка при вводе пароля: {e}")
            return None

    # Сохранение строки сессии для последующего использования
    session_string = session.save()
    print("Сессия сохранена: ", session_string)
    return session_string
