import os
import openai
from ..config import settings

openai.api_key = settings.OPENAI_API_KEY


async def generate_natal_card(prompt: str) -> str:
    """
    Запрос к OpenAI для генерации текста натальной карты.
    """
    # Заглушка: пока возвращаем простой текст
    # После получения ключа OpenAI можно раскомментировать реальный запрос
    # response = openai.Completion.create(
    #     model="text-davinci-003",
    #     prompt=prompt,
    #     max_tokens=300
    # )
    # return response.choices[0].text.strip()

    return f"[ЗАГЛУШКА OpenAI] Натальная карта по запросу: {prompt}"
