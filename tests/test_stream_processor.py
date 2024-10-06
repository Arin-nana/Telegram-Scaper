import unittest
from scripts.stream_processor import StreamProcessor

class TestStreamProcessor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        target_entities = ["Иван Иванов", "Компания ABC"]
        cls.processor = StreamProcessor(target_entities)

    # Проверка простого положительного совпадения
    def test_positive_match_simple(self):
        text = "Иван Иванов сегодня подписал новый контракт."
        self.assertTrue(self.processor.process_text(text))

    # Проверка совпадения с вариацией упоминания компании
    def test_positive_match_variation(self):
        text = "Компания ABC объявила о выпуске нового продукта."
        self.assertTrue(self.processor.process_text(text))

    # Проверка текста без упоминаний нужных имен и названий
    def test_negative_match(self):
        text = "Этот текст не содержит нужных имен и названий."
        self.assertFalse(self.processor.process_text(text))

    # Проверка текста без учета регистра символов
    def test_case_insensitivity(self):
        text = "ИВАН ИВАНОВ сегодня подписал новый контракт."
        self.assertTrue(self.processor.process_text(text))

    # Проверка частичного совпадения с упоминанием компании
    def test_partial_match(self):
        text = "Сегодня компания abc объявила о выпуске нового продукта."
        self.assertTrue(self.processor.process_text(text))

    # Проверка текста с несколькими упоминаниями
    def test_multiple_mentions(self):
        text = "Иван Иванов и Компания ABC сегодня подписали новый контракт."
        self.assertTrue(self.processor.process_text(text))

    # Проверка работы с различными формами имен и названий (лемматизация)
    def test_lemmas(self):
        text = "Ивану Иванову очень понравилось работать в компании ABC."
        self.assertTrue(self.processor.process_text(text))

    # Проверка длинного текста с упоминаниями
    def test_long_text(self):
        text = ("Этот сотрудник действительно удивителен! Он всегда выполняет задачи вовремя, "
                "его навыки и профессионализм на высшем уровне. Иван Иванов был особенно полезен. "
                "Сегодня Компания ABC объявила о выпуске нового продукта.")
        self.assertTrue(self.processor.process_text(text))

    # Проверка текста с особыми символами
    def test_special_characters(self):
        text = "Иван Иванов!!!???"
        self.assertTrue(self.processor.process_text(text))

    # Проверка текста, содержащего только особые символы
    def test_no_match_special_characters(self):
        text = "!!!???"
        self.assertFalse(self.processor.process_text(text))

    # Проверка текста с общими фразами (без упоминаний)
    def test_mixed_sentiments(self):
        text = "Сотрудник хорошо справляется со своей работой, но иногда опаздывает на совещания."
        self.assertFalse(self.processor.process_text(text))

    # Проверка текста с несколькими упоминаниями в одном предложении
    def test_multiple_entities(self):
        text = "Иван Иванов работает в компании ABC. Он достиг больших успехов."
        self.assertTrue(self.processor.process_text(text))

    # Проверка текста с измененными формами имен и названий
    def test_non_lemmas(self):
        text = "Иван Иванова очень удивил всех."
        self.assertFalse(self.processor.process_text(text))

    # Проверка текста без нужных имен и названий
    def test_no_entities(self):
        text = "Этот текст не содержит нужных имен и названий."
        self.assertFalse(self.processor.process_text(text))

    # Проверка именительного падежа имени
    def test_inflected_name_nominative(self):
        text = "Иван Иванов - наш лучший сотрудник."
        self.assertTrue(self.processor.process_text(text))

    # Проверка родительного падежа имени
    def test_inflected_name_genitive(self):
        text = "Достижения Ивана Иванова впечатляют."
        self.assertTrue(self.processor.process_text(text))

    # Проверка дательного падежа имени
    def test_inflected_name_dative(self):
        text = "Мы доверили проект Ивану Иванову."
        self.assertTrue(self.processor.process_text(text))

    # Проверка винительного падежа имени
    def test_inflected_name_accusative(self):
        text = "Все благодарили Ивана Иванова за его труд."
        self.assertTrue(self.processor.process_text(text))

    # Проверка творительного падежа имени
    def test_inflected_name_instrumental(self):
        text = "Мы гордимся Иваном Ивановым."
        self.assertTrue(self.processor.process_text(text))

    # Проверка предложного падежа имени
    def test_inflected_name_prepositional(self):
        text = "Мы говорим об Иване Иванове."
        self.assertTrue(self.processor.process_text(text))

    # Проверка именительного падежа названия компании
    def test_inflected_company_nominative(self):
        text = "Компания ABC расширяет свои границы."
        self.assertTrue(self.processor.process_text(text))

    # Проверка родительного падежа названия компании
    def test_inflected_company_genitive(self):
        text = "Это новое достижение компании ABC."
        self.assertTrue(self.processor.process_text(text))

    # Проверка дательного падежа названия компании
    def test_inflected_company_dative(self):
        text = "Мы доверили проект компании ABC."
        self.assertTrue(self.processor.process_text(text))

    # Проверка винительного падежа названия компании
    def test_inflected_company_accusative(self):
        text = "Мы уважаем компанию ABC."
        self.assertTrue(self.processor.process_text(text))

    # Проверка творительного падежа названия компании
    def test_inflected_company_instrumental(self):
        text = "Мы сотрудничаем с компанией ABC."
        self.assertTrue(self.processor.process_text(text))

    # Проверка предложного падежа названия компании
    def test_inflected_company_prepositional(self):
        text = "Мы говорим о компании ABC."
        self.assertTrue(self.processor.process_text(text))

if __name__ == '__main__':
    unittest.main()
