import spacy
from spacy.tokens import Doc
import re
from typing import List, Set

class StreamProcessor:
    def __init__(self, target_entities: List[str]) -> None:
        """
        Инициализация класса StreamProcessor.

        :param target_entities: Список целевых имен и названий компаний для поиска.
        """
        self.nlp = spacy.load("ru_core_news_sm")  # Загружаем модель spaCy для русского языка
        self.target_entities = self.lemmatize_entities(target_entities)  # Лемматизируем целевые сущности

    def lemmatize_entities(self, entities: List[str]) -> Set[str]:
        """
        Лемматизация целевых имен и названий компаний.

        :param entities: Список целевых имен и названий компаний.
        :return: Множество лемматизированных целевых сущностей.
        """
        lemmatized_entities: Set[str] = set()
        for entity in entities:
            doc: Doc = self.nlp(entity)  # Пропускаем каждую сущность через модель spaCy для получения токенов
            lemmas: List[str] = [token.lemma_ for token in doc]  # Преобразуем каждый токен в его лемму (базовая форма)
            lemmatized_entities.add(' '.join(lemmas))  # Объединяем леммы в строку и добавляем в множество
        return lemmatized_entities

    def process_text(self, text: str) -> bool:
        """
        Обработка текста для поиска целевых имен и названий компаний.

        :param text: Текст для обработки.
        :return: True, если целевая сущность найдена в тексте, иначе False.
        """
        doc: Doc = self.nlp(text)  # Пропускаем текст через модель spaCy для получения токенов
        lemmas: List[str] = [token.lemma_ for token in doc]  # Преобразуем каждый токен в его лемму
        lemmatized_text: str = ' '.join(lemmas)  # Объединяем леммы в строку

        for entity in self.target_entities:
            # Ищем лемматизированную целевую сущность в лемматизированном тексте
            if re.search(r'\b' + re.escape(entity) + r'\b', lemmatized_text):
                return True  # Возвращаем True, если сущность найдена
        return False  # Возвращаем False, если сущность не найдена

if __name__ == "__main__":
    target_entities: List[str] = ["Иван Иванов", "Компания ABC"]  # Список имен и названий компаний для поиска
    processor: StreamProcessor = StreamProcessor(target_entities)

    # Пример потока текстов
    text_stream: List[str] = [
        "Иван Иванов сегодня подписал новый контракт.",
        "Сегодня Компания ABC объявила о выпуске нового продукта.",
        "Этот текст не содержит нужных имен и названий."
    ]

    for text in text_stream:
        if processor.process_text(text):
            print(f"Найдено упоминание в тексте: {text}")
        else:
            print("Упоминание не найдено.")