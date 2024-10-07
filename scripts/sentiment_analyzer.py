import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from entities.text_data import TextData

# Создаем класс для анализа сентимента (эмоциональной окраски) текста
class SentimentAnalyzer:
    def __init__(self):
        # Загружаем предобученный токенизатор и модель для анализа сентимента на русском языке
        self.dictionary = {'LABEL_0': 'negative', 'LABEL_1': 'negative', 'LABEL_2': 'positive'}
        self.tokenizer = AutoTokenizer.from_pretrained("sismetanin/rubert-ru-sentiment-rusentiment")
        self.model = AutoModelForSequenceClassification.from_pretrained("sismetanin/rubert-ru-sentiment-rusentiment")

    def analyze_sentiment(self, text_data):
        # Токенизируем входной текст, приводим его к формату, подходящему для модели
        inputs = self.tokenizer(text_data.text, return_tensors="pt")

        # Используем модель для получения логитов (результатов) без обновления градиентов
        with torch.no_grad():
            logits = self.model(**inputs).logits

        # Определяем класс сентимента
        predicted_class_id = logits.argmax().item()

        # Получаем текстовое описание сентимента из конфигурации модели
        sentiment = self.model.config.id2label[predicted_class_id]

        # Возвращаем текстовое описание сентимента
        return self.dictionary[sentiment]


# Пример использования созданного класса
if __name__ == "__main__":
    analyzer = SentimentAnalyzer()  # Создаем экземпляр класса SentimentAnalyzer
    text_data = TextData("Мне очень понравился этот фильм!", "http://example.com")  # Экземпляр класса TextData
    print(analyzer.analyze_sentiment(text_data))  # Выводим результат анализа сентимента
