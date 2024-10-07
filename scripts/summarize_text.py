import re
import emoji
from transformers import pipeline

print("Loading Hugging Face summarizer pipelines...")
# Initialize the Hugging Face summarizer pipelines
summarizer_en = pipeline('summarization', model='facebook/bart-large-cnn')
summarizer_ru = pipeline('summarization', model='IlyaGusev/mbart_ru_sum_gazeta')


def preprocess_text(text: str) -> str:
    """
    Preprocess the input text by removing emojis and unwanted characters,
    except for the following symbols: :-'";/*@#$%^&(){}[]<>|№—.

    Args:
        text (str): The input text to preprocess.

    Returns:
        str: The preprocessed text with emojis and unwanted characters removed.
    """
    # Remove emojis
    text = emoji.replace_emoji(text, replace='')

    # Remove unwanted characters except specified symbols
    text = re.sub(r'[^a-zA-Zа-яА-Я0-9\s,.\-\'\";/*@#$%^&(){}[\]<>|№—]', '', text)

    return text


def summarize_text(text: str, language: str = 'en') -> str:
    """
    Summarize the input text using Hugging Face's summarization pipeline
    based on the selected language and length of the text.
    If the text is less than 50 tokens, return the original text.

    Args:
        text (str): The input text to summarize.
        language (str): The language of the text ('en' for English, 'ru' for Russian).

    Returns:
        str: The summarized text.
    """
    print(f"Summarizing text for language: {language}")

    # Split text into tokens to count them
    tokens = text.split()
    num_tokens = len(tokens)

    # Return original text if it's less than 50 tokens
    if num_tokens < 50:
        print(f"Text has {num_tokens} tokens, returning original text.")
        return text

    # Preprocess the text
    text = preprocess_text(text)

    # Determine max_length and min_length based on the length of the text
    if num_tokens < 500:
        max_length = 100
        min_length = 50
    else:
        max_length = 150
        min_length = 50

    print(f"Text length: {num_tokens} tokens, Max length: {max_length}, Min length: {min_length}")

    # Perform summarization based on language
    if language == 'ru':
        summary = summarizer_ru(text, max_length=max_length, min_length=min_length, do_sample=False)
    else:
        summary = summarizer_en(text, max_length=max_length, min_length=min_length, do_sample=False)

    summarized_text = summary[0]['summary_text']
    print(f"Summarized text: {summarized_text}")

    return summarized_text
