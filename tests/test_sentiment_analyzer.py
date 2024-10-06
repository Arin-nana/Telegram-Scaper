import unittest
from scripts.sentiment_analyzer import SentimentAnalyzer
from entities.text_data import TextData

class TestSentimentAnalyzer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analyzer = SentimentAnalyzer()  # Создаем экземпляр SentimentAnalyzer один раз для всех тестов

    def test_positive_sentiment(self):
        text_data = TextData("Этот сотрудник великолепен в своей работе!", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "positive")  # Ожидаемый результат - positive

    def test_negative_sentiment(self):
        text_data = TextData("Этот сотрудник совершенно не справляется со своими обязанностями.", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")  # Ожидаемый результат - negative

    def test_neutral_sentiment(self):
        text_data = TextData("Сотрудник выполняет свою работу на таком себе уровне.", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")  # Ожидаемый результат - neutral

    def test_long_text(self):
        text_data = TextData(
            ("Этот сотрудник действительно удивителен! Он всегда выполняет задачи вовремя, "
             "его навыки и профессионализм на высшем уровне. Я бы хотел, чтобы у нас было больше таких сотрудников. "
             "Единственное, что меня немного смущает, это его стремление к идеалу, иногда он слишком скрупулезен. "
             "Но в целом, работать с ним - незабываемое впечатление."),
            "http://example.com"
        )
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "positive")  # Ожидаемый результат - positive для длинного текста

    def test_special_characters(self):
        text_data = TextData("!!!???", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")  # Ожидаемый результат - neutral для строки с особыми символами

    def test_mixed_sentiments(self):
        text_data = TextData("Сотрудник хорошо справляется со своей работой, но иногда опаздывает на совещания.", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertIn(result, ["positive", "negative", "neutral"])  # Проверка, что результат находится в ожидаемых диапазонах

    def test_positive_sentiment_2(self):
        text_data = TextData("Этот сотрудник просто великолепен!", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "positive")

    def test_positive_sentiment_3(self):
        text_data = TextData("Я в восторге от работы этого сотрудника!", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "positive")

    def test_positive_sentiment_4(self):
        text_data = TextData("Этот сотрудник - лучший, с кем я когда-либо работал!", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "positive")

    def test_positive_sentiment_5(self):
        text_data = TextData("Сотрудник просто шикарный!", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "positive")

    def test_positive_sentiment_6(self):
        text_data = TextData("Навыки этого сотрудника на высоте!", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "positive")

    def test_positive_sentiment_7(self):
        text_data = TextData("Я был потрясен, насколько этот сотрудник хорош!", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "positive")

    def test_positive_sentiment_8(self):
        text_data = TextData("Это был незабываемый опыт работы с этим сотрудником!", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "positive")

    def test_positive_sentiment_9(self):
        text_data = TextData("Я обязательно порекомендую этого сотрудника другим!", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "positive")

    def test_positive_sentiment_10(self):
        text_data = TextData("Этот сотрудник оставил у меня только положительные он эмоции!", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "positive")

    def test_positive_sentiment_11(self):
        text_data = TextData("Сотрудник был просто супер!", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "positive")

    def test_negative_sentiment_2(self):
        text_data = TextData("Я разочарован работой этого сотрудника.", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")

    def test_negative_sentiment_3(self):
        text_data = TextData("Это худший сотрудник, с которым я когда-либо работал.", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")

    def test_negative_sentiment_4(self):
        text_data = TextData("Сотрудник слишком медленно выполняет задачи.", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")

    def test_negative_sentiment_5(self):
        text_data = TextData("Я жалею, что нанял этого сотрудника.", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")

    def test_negative_sentiment_6(self):
        text_data = TextData("Его навыки оставляют желать лучшего.", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")

    def test_negative_sentiment_7(self):
        text_data = TextData("Сотрудник часто ошибается в работе.", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")

    def test_negative_sentiment_8(self):
        text_data = TextData("Этот сотрудник - полное разочарование.", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")

    def test_negative_sentiment_9(self):
        text_data = TextData("Сотрудник оказался совершенно не таким, как я ожидал.", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")

    def test_negative_sentiment_10(self):
        text_data = TextData("Это было ужасное зрелище.", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")

    def test_negative_sentiment_11(self):
        text_data = TextData("Работа сотрудника была просто ужасна.", "http://example.com")
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")

    def test_positive_sentiment_69(self):
        text_data = TextData(
            ("Этот сотрудник действительно удивителен! Он всегда выполняет задачи вовремя, "
             "его навыки и профессионализм на высшем уровне. Я бы хотел, чтобы у нас было больше таких сотрудников."),
            "http://example.com"
        )
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "positive")

    def test_positive_sentiment_79(self):
        text_data = TextData(
            ("Сотрудник проявляет высокий уровень ответственности и трудолюбия. "
             "Его внимание к деталям и качество работы просто восхитительны."),
            "http://example.com"
        )
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "positive")

    def test_positive_sentiment_89(self):
        text_data = TextData(
            ("Это был незабываемый опыт работы с этим сотрудником! Его вклад в команду неоценим, "
             "и его позитивное отношение мотивирует остальных."),
            "http://example.com"
        )
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "positive")

    def test_positive_sentiment_99(self):
        text_data = TextData(
            ("Я обязательно порекомендую этого сотрудника другим! Его профессионализм и навыки "
             "вызывают уважение и восхищение."),
            "http://example.com"
        )
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "positive")

    def test_positive_sentiment_190(self):
        text_data = TextData(
            ("Этот сотрудник оставил у меня только положительные эмоции! Его работа всегда на высшем уровне, "
             "и он превосходно справляется с любыми задачами."),
            "http://example.com"
        )
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "positive")

    def test_positive_sentiment_119(self):
        text_data = TextData(
            ("Сотрудник был просто супер! Его подход к работе и взаимодействие с коллегами заслуживают только похвалы."),
            "http://example.com"
        )
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "positive")

    def test_negative_sentiment_29(self):
        text_data = TextData(
            ("Я разочарован работой этого сотрудника. Он часто не успевает выполнить задачи в срок, "
             "и его подход к работе оставляет желать лучшего."),
            "http://example.com"
        )
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")

    def test_negative_sentiment_39(self):
        text_data = TextData(
            ("Это худший сотрудник, с которым я когда-либо работал. Его работа полна ошибок, "
             "и он часто отсутствует на рабочем месте."),
            "http://example.com"
        )
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")

    def test_negative_sentiment_49(self):
        text_data = TextData(
            ("Сотрудник слишком медленно выполняет задачи и часто делает ошибки. "
             "Его навыки явно недостаточны для этой должности."),
            "http://example.com"
        )
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")

    def test_negative_sentiment_59(self):
        text_data = TextData(
            ("Я жалею, что нанял этого сотрудника. Его работа вызывает только разочарование, "
             "и его вклад в команду минимален."),
            "http://example.com"
        )
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")

    def test_negative_sentiment_69(self):
        text_data = TextData(
            ("Его навыки оставляют желать лучшего. Он часто ошибается, "
             "и его работа требует постоянной проверки и корректировки."),
            "http://example.com"
        )
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")

    def test_negative_sentiment_79(self):
        text_data = TextData(
            ("Сотрудник часто ошибается в работе, и его производительность ниже ожидаемой. "
             "Его необходимо обучать и контролировать на каждом этапе."),
            "http://example.com"
        )
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")

    def test_negative_sentiment_89(self):
        text_data = TextData(
            ("Этот сотрудник - полное разочарование. Он не способен справляться с задачами, "
             "и его поведение на рабочем месте вызывает вопросы."),
            "http://example.com"
        )
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")

    def test_negative_sentiment_99(self):
        text_data = TextData(
            ("Сотрудник оказался совершенно не таким, как я ожидал. Его производительность низка, "
             "и он не проявляет инициативы в работе."),
            "http://example.com"
        )
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")

    def test_negative_sentiment_109(self):
        text_data = TextData(
            ("Это было ужасное зрелище. Сотрудник не справляется со своими обязанностями и постоянно делает ошибки."),
            "http://example.com"
        )
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")

    def test_negative_sentiment_119(self):
        text_data = TextData(
            ("Работа сотрудника была просто ужасна. Он не только не выполняет задачи в срок, "
             "но и делает много ошибок, которые приходится исправлять."),
            "http://example.com"
        )
        result = self.analyzer.analyze_sentiment(text_data)
        self.assertEqual(result, "negative")

if __name__ == '__main__':
    unittest.main()
