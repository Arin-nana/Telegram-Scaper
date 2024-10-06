import unittest
from scripts.summarize_text import summarize_text, preprocess_text


class TestSummarizeText(unittest.TestCase):

    def log_summary(self, original_text, summarized_text):
        print("\nOriginal Text:")
        print(original_text)
        print("\nSummarized Text:")
        print(summarized_text)

    def test_long_text_english(self):
        text = """
        The United Nations (UN) is an intergovernmental organization tasked with maintaining international peace and security, 
        developing friendly relations among nations, achieving international cooperation, and being a center for harmonizing the actions of nations. 
        It is the world's largest and most familiar international organization. The UN is headquartered on international territory in New York City; 
        other main offices are in Geneva, Nairobi, Vienna, and The Hague. The UN was established after World War II with the aim of preventing future wars, 
        succeeding the ineffective League of Nations.
        """
        summary = summarize_text(text, language='en')
        self.log_summary(text, summary)
        self.assertIsInstance(summary, str)
        self.assertTrue(len(summary) < len(text))

    def test_medium_text_english(self):
        text = """
        The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. 
        It is named after the engineer Gustave Eiffel, whose company designed and built the tower. 
        Constructed from 1887 to 1889 as the entrance arch for the 1889 World's Fair, 
        it was initially criticized by some of France's leading artists and intellectuals for its design, 
        but it has become a global cultural icon of France and one of the most recognizable structures in the world.
        """
        summary = summarize_text(text, language='en')
        self.log_summary(text, summary)
        self.assertIsInstance(summary, str)
        self.assertTrue(len(summary) < len(text))

    def test_short_text_english(self):
        text = """
        The Mona Lisa is a half-length portrait painting by the Italian artist Leonardo da Vinci.
        """
        summary = summarize_text(text, language='en')
        self.log_summary(text, summary)
        self.assertEqual(summary, text)  # Ensure the original text is returned
        self.assertIsInstance(summary, str)

    def test_long_text_russian(self):
        text = """
        Организация Объединённых Наций (ООН) — это межправительственная организация, 
        отвечающая за поддержание международного мира и безопасности, 
        развитие дружеских отношений между нациями, достижение международного сотрудничества и 
        координацию действий государств. ООН является крупнейшей международной организацией в мире. 
        Штаб-квартира ООН находится на международной территории в Нью-Йорке; 
        другие главные офисы находятся в Женеве, Найроби, Вене и Гааге. 
        ООН была создана после Второй мировой войны с целью предотвращения будущих войн, 
        заменив неэффективную Лигу Наций.
        """
        summary = summarize_text(text, language='ru')
        self.log_summary(text, summary)
        self.assertIsInstance(summary, str)
        self.assertTrue(len(summary) < len(text))

    def test_medium_text_russian(self):
        text = """
        Эйфелева башня — это кованая решётчатая башня на Марсовом поле в Париже, Франция. 
        Она названа в честь инженера Густава Эйфеля, чья компания спроектировала и построила башню. 
        Построенная с 1887 по 1889 год как входная арка для Всемирной выставки 1889 года, 
        она изначально критиковалась некоторыми ведущими французскими художниками и интеллектуалами за свой дизайн, 
        но со временем стала глобальным культурным символом Франции и одним из самых узнаваемых сооружений в мире.
        """
        summary = summarize_text(text, language='ru')
        self.log_summary(text, summary)
        self.assertIsInstance(summary, str)
        self.assertTrue(len(summary) < len(text))

    def test_short_text_russian(self):
        text = """
        Мона Лиза — это портретная живопись Леонардо да Винчи.
        """
        summary = summarize_text(text, language='ru')
        self.log_summary(text, summary)
        self.assertEqual(summary, text)  # Ensure the original text is returned
        self.assertIsInstance(summary, str)

    def test_preprocess_text(self):
        text = "This is a test text with emoji 😊🚀 and other symbols ©™."
        expected = "This is a test text with emoji  and other symbols ."
        preprocessed_text = preprocess_text(text)
        self.assertEqual(preprocessed_text, expected)
        print("\nPreprocessed Text:")
        print(preprocessed_text)


if __name__ == '__main__':
    unittest.main()
