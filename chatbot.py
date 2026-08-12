import re
import random

# Define a dictionary with intents and responses

possible_inputs = {
    'salutation': ['hello', 'hi', 'hey'],
    'depature': ['bye', 'see you later'],
    'appereciation': ['thank you', 'thanks']
}

response = {
    'salutation': ["Hello! How can I help you?', 'Hi there! What's good?', 'Hey! How are you?"],
    'depature': ['See you later!', 'Do take care', 'Have a good one'],
    'appereciation': ["'You're welcome!', 'sure thing,always here to help','Glad i could assist you'"]
}


def possible_inputs_identifier(entry):
    for possible_inputs, patterns in possible_inputs.items():
        for pattern in patterns:
            if re.search(pattern, entry, re.IGNORECASE):
                return possible_inputs
    return None

def response(possible_inputs):
    return random.choice(response[possible_inputs])

def chatbot(entry):
   possible_inputs = possible_inputs_identifier(entry)
   if possible_inputs:
       return response(possible_inputs)
   else:
       return "I didn't understand that. Can you please rephrase?"


while True:
    entry = input("You: ")
    if entry.lower() == "quit":
        break
    print("Chatbot: ", chatbot(entry))




















# import nltk
# import io
# import random
# import string
# import warnings
# import numpy as np
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import warnings
# warnings.filterwarnings('ignore')
# from nltk.stem import WordNetLemmatizer
# nltk.download('popular')
# # nltk.download('punkt', download_dir='/nltk.org/nltk_data')