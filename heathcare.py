import random
import json
import pickle
import nltk
import requests
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD
import numpy as np

# Google Gemini API endpoint
# nltk 
nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Google Gemini API 
def get_gemini_response(symptoms):
    url = "https://ai.google.dev/api/all-methods#generative-language-api"  # Google Gemini API endpoint
    headers = {
        'Authorization': 'Bearer AIzaSyAuUZrftqbyxtH6cRa4xHPiQLgDLiOnNUM',  
        'Content-Type': 'application/json',
    }
    
    prompt = f"The patient has the following symptoms: {', '.join(symptoms)}. What is the most likely diagnosis and what are the possible solutions?"
    data = {'prompt': prompt}
    
    response = requests.post(url, headers=headers, json=data)
    
    
       
    try:

        response_json = response.json()

       
        diagnosis = response_json.get('diagnosis', 'No diagnosis found')
    except ValueError:
        
        diagnosis = "Error: JSON ayrıştırılamadı"
        
        {
            "semptoms": [
                "headache",
                "fewer"
            ],
            "diagnosis": diagnosis
        }

# 
# print(diagnosis)

# Semptoms
def get_symptoms_from_user():
    symptoms = []
    print("Lütfen semptomlarınızı tek tek girin. Bittiğinde 'done' yazın:")
    while True:
        symptom = input("Semptom: ")
        if symptom.lower() == "done":
            break
        symptoms.append(symptom)
    return symptoms

# main app
def main():
    
    symptoms = get_symptoms_from_user()

    if not symptoms:
        print("Semptom girmediniz. Program sonlandırılıyor.")
        return

    # Google Gemini response
    gemini_response = get_gemini_response(symptoms)

    
    print(f"Tahmin edilen hastalık ve önerilen çözümler: {gemini_response}")

if __name__ == "__main__":
    main()