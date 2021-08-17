import json
from typing import List

import requests
from requests import Response

from Settings import DeepL_Token


class DeepL:
    def __init__(self):
        self.__url: str = "https://api-free.deepl.com/v2/translate"
        self.__token: str = DeepL_Token


    def translate(self, source: List[str], lang: str) -> str:
        lang = lang.upper()
        payload = {
            "auth_key": self.__token,
            "text": source,
            "source_lang": lang,
        }
        if lang == "zh":
            payload.setdefault("target_lang", "EN-US")
        else:
            payload.setdefault("target_lang", "ZH")

        response: Response = requests.post(self.__url, data=payload)
        return json.loads(response.text)['translations'][0]['text']
