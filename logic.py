# logic.py

import re
from data import BOT_DATA


def get_bot_response(user_input, language="urdu"):

    cleaned_input = re.sub(r'[^\w\s]', '', user_input.lower().strip())

    for key, data_block in BOT_DATA.items():
        for keyword in data_block["keywords"]:
            if keyword in cleaned_input:
                return data_block[language]

    if language == "urdu":
        return "Mujhe is sawal ka direct jawab nahi mila. Please aasan keywords use karein."
    else:
        return "I could not find a direct answer. Please try using simpler keywords."